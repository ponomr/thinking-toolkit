from __future__ import annotations

import importlib.util
import io
import os
import re
import shutil
import subprocess
import tarfile
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BUILDER = load_module("build_release", PROJECT_ROOT / "scripts" / "build_release.py")
UPDATER = load_module("update_skill", PROJECT_ROOT / "update.py")


class ReleaseBuilderTests(unittest.TestCase):
    def test_archive_is_reproducible_and_contains_only_payload(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first, _ = BUILDER.build_archive(root / "first")
            second, _ = BUILDER.build_archive(root / "second")
            self.assertEqual(first.read_bytes(), second.read_bytes())

            with tarfile.open(first, "r:gz") as bundle:
                names = set(bundle.getnames())
            expected = {
                f"thinking-toolkit/{path.relative_to(PROJECT_ROOT).as_posix()}"
                for path in BUILDER.payload_files(PROJECT_ROOT)
            }
            self.assertEqual(names, expected)
            self.assertFalse(any("tests/" in name for name in names))
            self.assertFalse(any("scripts/" in name for name in names))

    def test_checksum_matches_archive(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive, checksums = BUILDER.build_archive(Path(temporary))
            digest, filename = checksums.read_text(encoding="utf-8").split()
            self.assertEqual(filename, archive.name)
            self.assertEqual(digest, BUILDER.hashlib.sha256(archive.read_bytes()).hexdigest())


class UpdaterTests(unittest.TestCase):
    def test_invalid_installed_version_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            (target / "VERSION").write_text("../../escape\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "installed VERSION"):
                UPDATER.current_version(target)

    def test_safe_extract_rejects_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            archive = root / "unsafe.tar.gz"
            with tarfile.open(archive, "w:gz") as bundle:
                link = tarfile.TarInfo("thinking-toolkit/SKILL.md")
                link.type = tarfile.SYMTYPE
                link.linkname = "/tmp/escape"
                bundle.addfile(link)
            with self.assertRaisesRegex(ValueError, "links and special files"):
                UPDATER.safe_extract(archive, root / "output")

    def test_backup_swap_is_reversible(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            parent = Path(temporary)
            target = parent / "thinking-toolkit"
            backup = parent / ".thinking-toolkit.backup-v1.0.0"
            target.mkdir()
            backup.mkdir()
            (target / "VERSION").write_text("2.0.0\n", encoding="utf-8")
            (backup / "VERSION").write_text("1.0.0\n", encoding="utf-8")
            UPDATER.swap_with_backup(target, backup)
            self.assertEqual(UPDATER.current_version(target), "1.0.0")
            self.assertEqual(UPDATER.current_version(backup), "2.0.0")

    def test_verified_update_and_rollback_end_to_end(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            payload_version = (PROJECT_ROOT / "VERSION").read_text().strip()
            release_dir = root / "release"
            archive, _ = BUILDER.build_archive(release_dir)
            target = root / "thinking-toolkit"
            target.mkdir()
            (target / "VERSION").write_text("0.9.0\n", encoding="utf-8")
            (target / "SKILL.md").write_text("old\n", encoding="utf-8")
            shutil.copy2(PROJECT_ROOT / "update.py", target / "update.py")

            binary_dir = root / "bin"
            binary_dir.mkdir()
            fake_gh = binary_dir / "gh"
            fake_gh.write_text(
                "#!/bin/sh\n"
                "if [ \"$1 $2\" = \"release download\" ]; then\n"
                "  while [ \"$1\" != \"--dir\" ]; do shift; done\n"
                "  cp \"$FAKE_RELEASE_ARCHIVE\" \"$2/\"\n"
                "fi\n",
                encoding="utf-8",
            )
            fake_gh.chmod(0o755)
            environment = os.environ.copy()
            environment["PATH"] = f"{binary_dir}{os.pathsep}{environment['PATH']}"
            environment["FAKE_RELEASE_ARCHIVE"] = str(archive)

            updated = subprocess.run(
                [
                    "python3",
                    str(target / "update.py"),
                    "--target",
                    str(target),
                    "--to",
                    f"v{payload_version}",
                    "--yes",
                ],
                check=True,
                capture_output=True,
                text=True,
                env=environment,
            )
            self.assertEqual(UPDATER.current_version(target), payload_version)
            installer = (PROJECT_ROOT / "install.sh").read_text(encoding="utf-8")
            installed_payload = re.search(
                r"^PAYLOAD=\((.*)\)$", installer, re.MULTILINE
            ).group(1).split()
            self.assertEqual(
                {path.name for path in target.iterdir()}, set(installed_payload)
            )
            backup_line = next(
                line for line in updated.stdout.splitlines() if line.startswith("backup: ")
            )
            backup = Path(backup_line.removeprefix("backup: "))
            self.assertEqual(UPDATER.current_version(backup), "0.9.0")

            subprocess.run(
                [
                    "python3",
                    str(target / "update.py"),
                    "--target",
                    str(target),
                    "--rollback",
                    str(backup),
                    "--yes",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertEqual(UPDATER.current_version(target), "0.9.0")


if __name__ == "__main__":
    unittest.main()
