#!/usr/bin/env python3
"""Explicitly update an installed Thinking Toolkit from a verified release."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path, PurePosixPath


REPOSITORY = "ponomr/thinking-toolkit"
BUNDLE_ROOT = "thinking-toolkit"
TAG_PATTERN = re.compile(r"^v[0-9]+\.[0-9]+\.[0-9]+$")
VERSION_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
# Bootstrap files ship in the release archive but are not part of an installed
# copy; install.sh leaves them out, so an update must too.
ARCHIVE_ONLY = ("install.sh",)


def run_gh(*arguments: str, capture: bool = False) -> str:
    command = ["gh", *arguments]
    try:
        result = subprocess.run(
            command,
            check=True,
            text=True,
            capture_output=capture,
        )
    except FileNotFoundError as error:
        raise RuntimeError("GitHub CLI (gh) is required for verified updates") from error
    except subprocess.CalledProcessError as error:
        detail = (error.stderr or error.stdout or "").strip()
        raise RuntimeError(f"gh command failed: {detail or error.returncode}") from error
    return result.stdout.strip() if capture else ""


def current_version(target: Path) -> str:
    version = (target / "VERSION").read_text(encoding="utf-8").strip()
    if not VERSION_PATTERN.fullmatch(version):
        raise ValueError(f"installed VERSION must look like 1.2.3, got {version!r}")
    return version


def latest_tag() -> str:
    return run_gh(
        "release",
        "view",
        "--repo",
        REPOSITORY,
        "--json",
        "tagName",
        "--jq",
        ".tagName",
        capture=True,
    )


def safe_extract(archive: Path, destination: Path) -> Path:
    destination = destination.resolve()
    with tarfile.open(archive, mode="r:gz") as bundle:
        members = bundle.getmembers()
        names = [member.name for member in members]
        if len(names) != len(set(names)):
            raise ValueError("release archive contains duplicate paths")
        for member in members:
            path = PurePosixPath(member.name)
            if (
                path.is_absolute()
                or ".." in path.parts
                or not path.parts
                or path.parts[0] != BUNDLE_ROOT
            ):
                raise ValueError(f"unsafe archive path: {member.name}")
            if not (member.isfile() or member.isdir()):
                raise ValueError(f"archive links and special files are forbidden: {member.name}")

        for member in members:
            output = destination.joinpath(*PurePosixPath(member.name).parts)
            if member.isdir():
                output.mkdir(parents=True, exist_ok=True)
                continue
            output.parent.mkdir(parents=True, exist_ok=True)
            source = bundle.extractfile(member)
            if source is None:
                raise ValueError(f"could not read archive member: {member.name}")
            with source, output.open("wb") as handle:
                shutil.copyfileobj(source, handle)
            os.chmod(output, member.mode & 0o777)

    extracted = destination / BUNDLE_ROOT
    if not (extracted / "SKILL.md").is_file() or not (extracted / "VERSION").is_file():
        raise ValueError("release archive is missing SKILL.md or VERSION")
    return extracted


def file_digests(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def describe_changes(old: Path, new: Path) -> list[str]:
    old_files = file_digests(old)
    new_files = file_digests(new)
    lines: list[str] = []
    for name in sorted(new_files.keys() - old_files.keys()):
        lines.append(f"added:   {name}")
    for name in sorted(old_files.keys() - new_files.keys()):
        lines.append(f"removed: {name}")
    for name in sorted(old_files.keys() & new_files.keys()):
        if old_files[name] != new_files[name]:
            lines.append(f"changed: {name}")
    return lines


def confirm(prompt: str, assume_yes: bool) -> None:
    if assume_yes:
        return
    if not sys.stdin.isatty():
        raise RuntimeError("confirmation requires a terminal; pass --yes to proceed")
    if input(f"{prompt} [y/N] ").strip().lower() not in {"y", "yes"}:
        raise RuntimeError("cancelled")


def unique_backup(target: Path, version: str) -> Path:
    candidate = target.parent / f".{target.name}.backup-v{version}"
    counter = 1
    while candidate.exists():
        candidate = target.parent / f".{target.name}.backup-v{version}-{counter}"
        counter += 1
    return candidate


def replace_with_backup(target: Path, replacement: Path, version: str) -> Path:
    backup = unique_backup(target, version)
    target.rename(backup)
    try:
        replacement.rename(target)
    except Exception:
        backup.rename(target)
        raise
    return backup


def swap_with_backup(target: Path, backup: Path) -> None:
    expected_prefix = f".{target.name}.backup-"
    if (
        backup.parent.resolve() != target.parent.resolve()
        or not backup.is_dir()
        or not backup.name.startswith(expected_prefix)
    ):
        raise ValueError("rollback target must be a generated sibling backup")
    swap = target.parent / f".{target.name}.rollback-swap"
    if swap.exists():
        raise ValueError(f"rollback staging path already exists: {swap}")
    target.rename(swap)
    try:
        backup.rename(target)
        swap.rename(backup)
    except Exception:
        if not target.exists() and swap.exists():
            swap.rename(target)
        raise


def update(target: Path, tag: str, assume_yes: bool, dry_run: bool) -> int:
    if not TAG_PATTERN.fullmatch(tag):
        raise ValueError(f"release tag must look like v1.2.3, got {tag!r}")
    if (target / ".git").exists():
        raise ValueError("this is a Git checkout; update it with git instead")

    installed = current_version(target)
    if tag == f"v{installed}":
        print(f"already current: {tag}")
        return 0

    asset_name = f"thinking-toolkit-{tag}.tar.gz"
    with tempfile.TemporaryDirectory(prefix=".thinking-toolkit-update-", dir=target.parent) as raw:
        temporary = Path(raw)
        run_gh("release", "verify", tag, "--repo", REPOSITORY)
        run_gh(
            "release",
            "download",
            tag,
            "--repo",
            REPOSITORY,
            "--pattern",
            asset_name,
            "--dir",
            str(temporary),
        )
        archive = temporary / asset_name
        run_gh("release", "verify-asset", tag, str(archive), "--repo", REPOSITORY)
        replacement = safe_extract(archive, temporary / "unpacked")
        release_version = current_version(replacement)
        if tag != f"v{release_version}":
            raise ValueError(
                f"release tag {tag} does not match archive VERSION {release_version}"
            )
        for name in ARCHIVE_ONLY:
            (replacement / name).unlink(missing_ok=True)

        changes = describe_changes(target, replacement)
        print(f"installed: v{installed}")
        print(f"verified release: {tag}")
        for line in changes or ["no file changes"]:
            print(line)
        if dry_run:
            return 0
        confirm("install this verified release?", assume_yes)
        backup = replace_with_backup(target, replacement, installed)

    print(f"updated: {target} -> {tag}")
    print(f"backup: {backup}")
    print(f"rollback: python3 {target / 'update.py'} --rollback {backup}")
    return 0


def rollback(target: Path, backup: Path, assume_yes: bool, dry_run: bool) -> int:
    changes = describe_changes(target, backup)
    print(f"current: v{current_version(target)}")
    print(f"rollback target: v{current_version(backup)}")
    for line in changes or ["no file changes"]:
        print(line)
    if dry_run:
        return 0
    confirm("swap the installation with this backup?", assume_yes)
    swap_with_backup(target, backup)
    print(f"rolled back: {target}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--to", help="version tag to install; defaults to latest")
    parser.add_argument("--target", type=Path, help="installed skill directory")
    parser.add_argument("--yes", action="store_true", help="skip confirmation")
    parser.add_argument("--dry-run", action="store_true", help="show changes only")
    parser.add_argument("--rollback", type=Path, help="swap with a prior backup")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = (args.target or Path(__file__).resolve().parent).resolve()
    try:
        if args.rollback:
            return rollback(target, args.rollback.resolve(), args.yes, args.dry_run)
        tag = args.to or latest_tag()
        return update(target, tag, args.yes, args.dry_run)
    except (OSError, RuntimeError, ValueError) as error:
        print(f"update failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
