#!/usr/bin/env python3
"""Validate the Thinking Toolkit project without third-party dependencies."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


EXPECTED_MODELS = {
    "six-thinking-hats.md": ("Six Thinking Hats", "Decision making"),
    "eisenhower-matrix.md": ("Eisenhower Matrix", "Decision making"),
    "second-order-thinking.md": ("Second-Order Thinking", "Decision making"),
    "decision-matrix.md": ("Decision Matrix", "Decision making"),
    "impact-effort-matrix.md": ("Impact-Effort Matrix", "Decision making"),
    "ladder-of-inference.md": ("Ladder of Inference", "Decision making"),
    "hard-choice-model.md": ("Hard Choice Model", "Decision making"),
    "ooda-loop.md": ("OODA Loop", "Decision making"),
    "cynefin-framework.md": ("Cynefin Framework", "Decision making"),
    "confidence-speed-quality.md": (
        "Confidence Determines Speed vs. Quality",
        "Decision making",
    ),
    "pareto-analysis.md": ("Pareto Analysis", "Decision making"),
    "backcasting.md": ("Backcasting", "Decision making"),
    "ishikawa-diagram.md": ("Ishikawa Diagram", "Problem solving"),
    "five-whys.md": ("Five Whys", "Problem solving"),
    "fermi-estimation.md": ("Fermi Estimation", "Problem solving"),
    "red-teaming.md": ("Red Teaming", "Problem solving"),
    "abstraction-laddering.md": ("Abstraction Laddering", "Problem solving"),
    "conflict-resolution-diagram.md": (
        "Conflict Resolution Diagram",
        "Problem solving",
    ),
    "zwicky-box.md": ("Zwicky Box", "Problem solving"),
    "productive-thinking-model.md": (
        "Productive Thinking Model",
        "Problem solving",
    ),
    "inversion.md": ("Inversion", "Problem solving"),
    "issue-trees.md": ("Issue Trees", "Problem solving"),
    "first-principles.md": ("First Principles", "Problem solving"),
    "iceberg-model.md": ("Iceberg Model", "Systems thinking"),
    "connection-circles.md": ("Connection Circles", "Systems thinking"),
    "concept-map.md": ("Concept Map", "Systems thinking"),
    "balancing-feedback-loop.md": (
        "Balancing Feedback Loop",
        "Systems thinking",
    ),
    "reinforcing-feedback-loop.md": (
        "Reinforcing Feedback Loop",
        "Systems thinking",
    ),
    "situation-behavior-impact.md": (
        "Situation-Behavior-Impact",
        "Communication",
    ),
    "minto-pyramid.md": ("Minto Pyramid", "Communication"),
}

REQUIRED_SECTIONS = (
    "Purpose",
    "Use When",
    "Avoid When",
    "Inputs",
    "Procedure",
    "Guiding Questions",
    "Output Format",
    "Worked Example",
    "Common Pitfalls",
    "Useful Combinations",
)

# The /logic analysis module: a lean, English payload that ships discipline
# (procedure + taxonomy + verdict format), not a logic textbook. overview.md is
# the entry point; the other files are progressively loaded references.
LOGIC_FILES = (
    "overview.md",
    "fallacies.md",
    "formal-validity.md",
    "induction.md",
)
LOGIC_MODES = ("review", "fix", "solve")

TEXT_SUFFIXES = {".md", ".py", ".txt", ".yaml", ".yml"}


def project_text_files(root: Path) -> list[Path]:
    """Return stable, relevant text files while ignoring generated caches."""
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file()
        and path.suffix in TEXT_SUFFIXES
        and "__pycache__" not in path.parts
    )


def validate_frontmatter(skill_path: Path) -> list[str]:
    errors: list[str] = []
    text = skill_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return ["SKILL.md has invalid frontmatter delimiters"]

    keys = []
    for line in match.group(1).splitlines():
        if line and not line.startswith((" ", "\t")) and ":" in line:
            keys.append(line.split(":", 1)[0].strip())
    if keys != ["name", "description"]:
        errors.append("SKILL.md frontmatter must contain only name and description")
    if "name: thinking-toolkit" not in match.group(1):
        errors.append("SKILL.md has an unexpected skill name")
    return errors


def validate_agent_metadata(metadata_path: Path) -> list[str]:
    errors: list[str] = []
    text = metadata_path.read_text(encoding="utf-8")
    expected_keys = ["display_name", "short_description", "default_prompt"]
    found_keys = re.findall(r"^  ([a-z_]+):", text, re.MULTILINE)
    if found_keys != expected_keys:
        errors.append(
            "agents/openai.yaml interface must contain display_name, "
            "short_description, and default_prompt in that order"
        )

    values = dict(
        re.findall(r'^  ([a-z_]+):\s+"([^"]*)"\s*$', text, re.MULTILINE)
    )
    if values.get("display_name") != "Thinking Toolkit":
        errors.append("agents/openai.yaml has an unexpected display_name")
    short_description = values.get("short_description", "")
    if not 25 <= len(short_description) <= 64:
        errors.append(
            "agents/openai.yaml short_description must contain 25 to 64 characters"
        )
    if "$thinking-toolkit" not in values.get("default_prompt", ""):
        errors.append(
            "agents/openai.yaml default_prompt must mention $thinking-toolkit"
        )
    return errors


def validate_model_cards(root: Path) -> list[str]:
    errors: list[str] = []
    references = root / "references"
    actual_cards = {
        path.name for path in references.glob("*.md") if path.name != "catalog.md"
    }
    expected_cards = set(EXPECTED_MODELS)

    for missing in sorted(expected_cards - actual_cards):
        errors.append(f"missing model card: references/{missing}")
    for extra in sorted(actual_cards - expected_cards):
        errors.append(f"unexpected model card: references/{extra}")

    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    catalog_text = (references / "catalog.md").read_text(encoding="utf-8")

    if "(references/catalog.md)" not in skill_text:
        errors.append("SKILL.md does not route model selection through catalog.md")

    for filename, (title, category) in EXPECTED_MODELS.items():
        path = references / filename
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith(f"# {title}\n"):
            errors.append(f"{path.relative_to(root)} has an unexpected title")
        if f"**Category:** {category}" not in text:
            errors.append(f"{path.relative_to(root)} has an unexpected category")
        if len(text.splitlines()) > 100 and "## Contents\n" not in text:
            errors.append(
                f"{path.relative_to(root)} exceeds 100 lines without a contents section"
            )
        for section in REQUIRED_SECTIONS:
            if f"## {section}\n" not in text:
                errors.append(
                    f"{path.relative_to(root)} is missing section: {section}"
                )
        if f"({filename})" not in catalog_text:
            errors.append(f"references/catalog.md does not link to {filename}")
        if f"(references/{filename})" in skill_text:
            errors.append(
                f"SKILL.md duplicates the catalog link to references/{filename}"
            )

    categories = [category for _, category in EXPECTED_MODELS.values()]
    if (
        len(catalog_text.splitlines()) > 100
        and "## Contents\n" not in catalog_text
    ):
        errors.append("references/catalog.md exceeds 100 lines without a contents section")
    expected_counts = {
        "Decision making": 12,
        "Problem solving": 11,
        "Systems thinking": 5,
        "Communication": 2,
    }
    for category, expected_count in expected_counts.items():
        count = categories.count(category)
        if count != expected_count:
            errors.append(
                f"manifest category {category!r} has {count} cards; "
                f"expected {expected_count}"
            )
    return errors


# Repository documentation may cite external resources; the skill payload
# itself must stay fully self-contained and offline-safe.
REPO_DOC_FILES = {
    "README.md",
    "README.ru.md",
    "README.zh.md",
    "SECURITY.md",
    "MAINTAINING.md",
    "LICENSE",
}
# Localized READMEs are intentionally non-English; the main README carries
# native-language names in its language switcher.
LOCALIZED_DOC_FILES = {"README.md", "README.ru.md", "README.zh.md"}


def validate_links(root: Path) -> list[str]:
    errors: list[str] = []
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in project_text_files(root):
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip()
            if target.startswith("#"):
                continue
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                if path.name not in REPO_DOC_FILES:
                    errors.append(
                        f"{path.relative_to(root)} contains an external link"
                    )
                continue
            file_part = target.split("#", 1)[0]
            resolved = (path.parent / file_part).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(
                    f"{path.relative_to(root)} has an unresolved link: {target}"
                )
    return errors


def validate_project_text(root: Path, forbidden_terms: list[str]) -> list[str]:
    errors: list[str] = []
    url_pattern = re.compile(r"\b(?:https?://|www\.)", re.IGNORECASE)
    cyrillic_pattern = re.compile(r"[\u0400-\u04ff]")
    placeholder_pattern = re.compile(r"\bT" + r"ODO\b|\[T" + r"ODO", re.IGNORECASE)

    for path in project_text_files(root):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root)
        if url_pattern.search(text) and path.name not in REPO_DOC_FILES:
            errors.append(f"{relative} contains an external URL")
        if (
            cyrillic_pattern.search(text)
            and path.name not in LOCALIZED_DOC_FILES
        ):
            errors.append(f"{relative} contains Cyrillic text")
        if placeholder_pattern.search(text):
            errors.append(f"{relative} contains a placeholder marker")
        lowered = text.casefold()
        for term in forbidden_terms:
            if term.casefold() in lowered:
                errors.append(f"{relative} contains a forbidden term")
    return errors


def validate_logic_module(root: Path) -> list[str]:
    """Validate the /logic analysis module.

    The generic passes (validate_links, validate_project_text) already enforce
    internal-links-only, no external URLs, no Cyrillic, and no placeholders on
    logic/*.md via rglob. This function adds the module-specific invariants:
    the expected files exist and are non-empty, SKILL.md links each of them, and
    SKILL.md documents the three modes.
    """
    errors: list[str] = []
    logic_dir = root / "logic"
    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")

    for filename in LOGIC_FILES:
        path = logic_dir / filename
        if not path.exists():
            errors.append(f"missing logic file: logic/{filename}")
            continue
        if not path.read_text(encoding="utf-8").strip():
            errors.append(f"logic/{filename} is empty")
        if f"logic/{filename}" not in skill_text:
            errors.append(f"SKILL.md does not link to logic/{filename}")

    # Reject stray files so the module stays lean and the manifest stays honest.
    if logic_dir.exists():
        actual = {p.name for p in logic_dir.glob("*.md")}
        for extra in sorted(actual - set(LOGIC_FILES)):
            errors.append(f"unexpected logic file: logic/{extra}")

    for mode in LOGIC_MODES:
        if f"**{mode}**" not in skill_text:
            errors.append(f"SKILL.md does not document the /logic mode: {mode}")
    return errors


def validate_distribution(root: Path) -> list[str]:
    """Validate versioning and the copy-only installation boundary."""
    errors: list[str] = []
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        errors.append("VERSION must use semantic x.y.z format")

    installer = (root / "install.sh").read_text(encoding="utf-8")
    if "--symlink" in installer:
        errors.append("install.sh must not offer symlink installation")
    for item in ("SKILL.md", "references", "logic", "agents", "LICENSE", "VERSION", "update.py"):
        if item not in installer:
            errors.append(f"install.sh payload does not mention: {item}")

    updater = (root / "update.py").read_text(encoding="utf-8")
    verification_calls = {
        'run_gh("release", "verify",': "gh release verify",
        'run_gh("release", "verify-asset",': "gh release verify-asset",
    }
    for code, command in verification_calls.items():
        if code not in updater:
            errors.append(f"update.py is missing verification command: {command}")
    return errors


def validate_project(root: Path, forbidden_terms: list[str] | None = None) -> list[str]:
    """Return all validation errors for a project root."""
    forbidden_terms = forbidden_terms or []
    required = [
        root / "AGENTS.md",
        root / "SKILL.md",
        root / "agents" / "openai.yaml",
        root / "references" / "catalog.md",
        root / "logic" / "overview.md",
        root / "VERSION",
        root / "install.sh",
        root / "update.py",
        root / "SECURITY.md",
        root / "MAINTAINING.md",
        root / ".github" / "workflows" / "validate.yml",
        root / ".github" / "workflows" / "release.yml",
    ]
    errors = [
        f"missing required file: {path.relative_to(root)}"
        for path in required
        if not path.exists()
    ]
    if errors:
        return errors
    errors.extend(validate_frontmatter(root / "SKILL.md"))
    errors.extend(validate_agent_metadata(root / "agents" / "openai.yaml"))
    errors.extend(validate_model_cards(root))
    errors.extend(validate_logic_module(root))
    errors.extend(validate_distribution(root))
    errors.extend(validate_links(root))
    errors.extend(validate_project_text(root, forbidden_terms))
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="project directory to validate")
    parser.add_argument(
        "--forbid",
        action="append",
        default=[],
        help="case-insensitive term that must not appear; repeat as needed",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.path.resolve()
    errors = validate_project(root, args.forbid)
    if errors:
        print(f"Validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validation passed: {len(EXPECTED_MODELS)} complete model cards")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
