from __future__ import annotations

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = PROJECT_ROOT / "scripts" / "validate_skill.py"
SPEC = importlib.util.spec_from_file_location("validate_skill", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load validator module")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ValidatorTests(unittest.TestCase):
    def copy_project(self, destination: Path) -> Path:
        copied = destination / "thinking-toolkit"
        shutil.copytree(
            PROJECT_ROOT,
            copied,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )
        return copied

    def test_current_project_is_valid(self) -> None:
        self.assertEqual(VALIDATOR.validate_project(PROJECT_ROOT), [])

    def test_invalid_version_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            (copied / "VERSION").write_text("latest\n", encoding="utf-8")
            errors = VALIDATOR.validate_project(copied)
            self.assertTrue(any("VERSION must use semantic" in error for error in errors))

    def test_symlink_install_option_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            installer = copied / "install.sh"
            installer.write_text(installer.read_text() + "\n# --symlink\n", encoding="utf-8")
            errors = VALIDATOR.validate_project(copied)
            self.assertTrue(any("must not offer symlink" in error for error in errors))

    def test_missing_model_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            (copied / "references" / "inversion.md").unlink()
            errors = VALIDATOR.validate_project(copied)
            self.assertTrue(any("missing model card" in error for error in errors))

    def test_model_missing_from_catalog_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            catalog = copied / "references" / "catalog.md"
            text = catalog.read_text().replace(
                "[Inversion](inversion.md)", "Inversion"
            )
            catalog.write_text(text, encoding="utf-8")
            errors = VALIDATOR.validate_project(copied)
            self.assertTrue(
                any("catalog.md does not link to inversion.md" in e for e in errors)
            )

    def test_direct_model_link_in_skill_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            skill = copied / "SKILL.md"
            skill.write_text(
                skill.read_text()
                + "\n[Inversion](references/inversion.md)\n",
                encoding="utf-8",
            )
            errors = VALIDATOR.validate_project(copied)
            self.assertTrue(any("duplicates the catalog link" in e for e in errors))

    def test_missing_logic_file_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            (copied / "logic" / "fallacies.md").unlink()
            errors = VALIDATOR.validate_project(copied)
            self.assertTrue(any("missing logic file" in error for error in errors))

    def test_logic_file_cyrillic_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            path = copied / "logic" / "overview.md"
            path.write_text(path.read_text() + "\n" + chr(0x041f), encoding="utf-8")
            errors = VALIDATOR.validate_project(copied)
            self.assertTrue(any("Cyrillic" in error for error in errors))

    def test_unexpected_logic_file_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            (copied / "logic" / "stray.md").write_text("# stray\n", encoding="utf-8")
            errors = VALIDATOR.validate_project(copied)
            self.assertTrue(any("unexpected logic file" in error for error in errors))

    def test_non_english_cyrillic_text_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            path = copied / "references" / "catalog.md"
            path.write_text(path.read_text() + "\n" + chr(0x041f), encoding="utf-8")
            errors = VALIDATOR.validate_project(copied)
            self.assertTrue(any("Cyrillic" in error for error in errors))

    def test_external_url_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            path = copied / "references" / "catalog.md"
            sample = "https" + "://" + "example.invalid"
            path.write_text(path.read_text() + "\n" + sample, encoding="utf-8")
            errors = VALIDATOR.validate_project(copied)
            self.assertTrue(any("external URL" in error for error in errors))

    def test_unresolved_internal_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            path = copied / "references" / "catalog.md"
            path.write_text(
                path.read_text() + "\n[Missing](missing-card.md)",
                encoding="utf-8",
            )
            errors = VALIDATOR.validate_project(copied)
            self.assertTrue(any("unresolved link" in error for error in errors))

    def test_invalid_agent_metadata_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            path = copied / "agents" / "openai.yaml"
            path.write_text(
                path.read_text().replace("$thinking-toolkit", "$other-skill"),
                encoding="utf-8",
            )
            errors = VALIDATOR.validate_project(copied)
            self.assertTrue(any("default_prompt" in error for error in errors))

    def test_long_reference_without_contents_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            path = copied / "references" / "minto-pyramid.md"
            path.write_text(
                path.read_text().replace("## Contents", "## Navigation", 1),
                encoding="utf-8",
            )
            errors = VALIDATOR.validate_project(copied)
            self.assertTrue(any("without a contents section" in error for error in errors))

    def test_localized_readme_cyrillic_is_not_reported(self) -> None:
        errors = VALIDATOR.validate_project(PROJECT_ROOT)
        self.assertFalse(any("Cyrillic" in error for error in errors))
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            path = copied / "SKILL.md"
            path.write_text(path.read_text() + "\n" + chr(0x041F), encoding="utf-8")
            errors = VALIDATOR.validate_project(copied)
            self.assertTrue(any("Cyrillic" in error for error in errors))

    def test_caller_supplied_forbidden_term_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copy_project(Path(temporary))
            term = "blocked-brand"
            path = copied / "references" / "catalog.md"
            path.write_text(path.read_text() + "\n" + term, encoding="utf-8")
            errors = VALIDATOR.validate_project(copied, [term])
            self.assertTrue(any("forbidden term" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
