#!/usr/bin/env python3
"""Build a deterministic, versioned Thinking Toolkit release archive."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import re
import subprocess
import sys
import tarfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUNDLE_ROOT = "thinking-toolkit"
TOP_LEVEL_FILES = (
    "SKILL.md",
    "LICENSE",
    "VERSION",
    "install.sh",
    "update.py",
)
PAYLOAD_DIRS = ("agents", "references", "logic")
VERSION_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


def read_version(root: Path = ROOT) -> str:
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    if not VERSION_PATTERN.fullmatch(version):
        raise ValueError(f"VERSION must be semantic x.y.z, got {version!r}")
    return version


def payload_files(root: Path = ROOT) -> list[Path]:
    files = [root / name for name in TOP_LEVEL_FILES]
    for directory in PAYLOAD_DIRS:
        files.extend(path for path in (root / directory).rglob("*") if path.is_file())

    missing = [path for path in files if not path.exists()]
    if missing:
        raise FileNotFoundError(f"missing payload file: {missing[0].relative_to(root)}")

    for path in files:
        if path.is_symlink():
            raise ValueError(f"payload must not contain symlinks: {path.relative_to(root)}")
    return sorted(files, key=lambda path: path.relative_to(root).as_posix())


def run_checks(root: Path = ROOT) -> None:
    commands = (
        [sys.executable, "scripts/validate_skill.py", "."],
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
    )
    for command in commands:
        subprocess.run(command, cwd=root, check=True)


def build_archive(output_dir: Path, root: Path = ROOT) -> tuple[Path, Path]:
    version = read_version(root)
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f"thinking-toolkit-v{version}.tar.gz"

    tar_buffer = io.BytesIO()
    with tarfile.open(fileobj=tar_buffer, mode="w", format=tarfile.GNU_FORMAT) as tar:
        for path in payload_files(root):
            relative = path.relative_to(root).as_posix()
            data = path.read_bytes()
            info = tarfile.TarInfo(f"{BUNDLE_ROOT}/{relative}")
            info.size = len(data)
            info.mode = 0o755 if relative in {"install.sh", "update.py"} else 0o644
            info.mtime = 0
            info.uid = 0
            info.gid = 0
            info.uname = ""
            info.gname = ""
            tar.addfile(info, io.BytesIO(data))

    with archive.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as compressed:
            compressed.write(tar_buffer.getvalue())

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksums = output_dir / "SHA256SUMS"
    checksums.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    return archive, checksums


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "dist",
        help="directory for the archive and SHA256SUMS",
    )
    parser.add_argument(
        "--skip-checks",
        action="store_true",
        help="skip validator and tests (intended only for release-tool tests)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.skip_checks:
        run_checks()
    archive, checksums = build_archive(args.output_dir.resolve())
    print(f"built: {archive}")
    print(f"checksums: {checksums}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
