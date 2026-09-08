# Thinking Toolkit — Standalone Context

A provider-neutral agent skill for selecting and applying practical thinking
models. Works in any agent that supports the SKILL.md convention.

## Critical Rules

1. Keep every project file in English, except the localized READMEs
   (`README.ru.md`, `README.zh.md`), which mirror `README.md`.
2. Keep the core skill usable by any capable LLM without provider-specific
   tools, browsing, code execution, persistent memory, or hidden state.
3. Never mention or cite the prohibited source project.
4. Never add external URLs or external Markdown links to the skill payload
   (`SKILL.md`, `references/`, `logic/`, `agents/`). READMEs, `SECURITY.md`,
   and `LICENSE` are repository documentation and may cite external resources.
5. Preserve all 30 model cards and all four catalog categories.
6. The `/logic` module (`logic/`) is an English payload — no Cyrillic, even for
   trigger phrases; `/logic` recognizes and replies in the user's language by
   instruction, not by hardcoded examples. Keep it lean (4 files); it ships
   discipline, not a logic textbook.
7. Keep claims, assumptions, hypotheses, and user-provided facts distinct.
8. Do not commit changes unless the user explicitly requests a new commit.
9. Stable users install copied payloads from immutable releases. Do not restore
   symlink installation or an install-from-main quick path.
10. Updates are user-initiated and must verify the release and asset, show the
    file changes, request confirmation, and preserve a rollback backup.

## Architecture

| Path | Role |
|---|---|
| `SKILL.md` | Core adaptive workflow and direct reference routing |
| `references/catalog.md` | Complete model index, aliases, selection cues, and combinations |
| `references/*.md` | One detailed, progressively loaded card per model |
| `logic/*.md` | `/logic` argument-analysis module (overview + 3 references) |
| `scripts/validate_skill.py` | Deterministic structure and content validation |
| `scripts/build_release.py` | Deterministic payload archive and SHA-256 manifest |
| `tests/test_validate_skill.py` | Validator regression tests and project checks |
| `agents/openai.yaml` | Optional host-specific discovery metadata; not required by the core skill |
| `install.sh` | Copies a release payload and preserves replaced installations |
| `update.py` | Verifies a release, displays changes, confirms, updates, and supports rollback |
| `VERSION` | Semantic version shared by package names and installed copies |
| `README.md` | Public repository documentation |
| `MAINTAINING.md` | Trust decisions, repository safeguards, and release procedure |

## Development Commands

```bash
python3 scripts/validate_skill.py .
python3 -m unittest discover -s tests -v
python3 scripts/build_release.py
```

## Validation Invariants

- The catalog contains exactly 30 model cards: 12 decision-making, 11
  problem-solving, 5 systems-thinking, and 2 communication models.
- Every card contains the required operational sections.
- Every Markdown link in the skill payload is internal and resolves to an
  existing file.
- No skill-payload text contains external URLs, non-English Cyrillic text,
  placeholders, or a caller-supplied forbidden term.
- `SKILL.md` frontmatter contains only `name` and `description`.
- The `/logic` module contains exactly 4 files (overview, fallacies,
  formal-validity, induction); each is linked from `SKILL.md`, which documents
  all three modes (review, fix, solve).
- `VERSION` uses semantic `x.y.z` format; the installer contains no symlink mode
  and ships the license, version marker, and explicit updater.
- Release archives contain only the allowlisted payload, contain no links, and
  build byte-for-byte reproducibly.
- Repository safeguards and the release process stay synchronized with
  `MAINTAINING.md`; re-check GitHub settings after a transfer or recreation.

## Dependencies

The skill itself has no runtime dependencies. Repository validation and release
building use only the Python standard library. Verified installation and update
use GitHub CLI; these maintenance actions are outside agent runtime.
