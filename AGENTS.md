# Thinking Toolkit

A skill for any agent with SKILL.md: selecting and applying thinking models. The stack,
structure and invariants are checked by `scripts/validate_skill.py` and the tests; this
file holds only what they do not catch.

Commands: `python3 scripts/validate_skill.py .`, `python3 -m unittest discover -s tests -v`,
`python3 scripts/build_release.py`.

## Rules

1. Keep every project file in English, except `README.ru.md` and `README.zh.md`.
2. Keep the core skill usable by any capable LLM without provider-specific
   tools, browsing, code execution, persistent memory, or hidden state.
3. Never mention or cite the prohibited source project (names and attributions
   are scrubbed; history was rewritten into a single commit).
4. Never add external URLs or external Markdown links to the skill payload
   (`SKILL.md`, `references/`, `logic/`, `agents/`). READMEs, `SECURITY.md`
   and `LICENSE` may cite external resources.
5. The card count is not a cap. A new card must meet the admission criteria in
   `MAINTAINING.md`; the catalog categories are preserved.
6. `logic/` is an English payload with no Cyrillic, even for trigger phrases: the
   module learns the user's language by instruction. Keep it lean.
7. Keep claims, assumptions, hypotheses, and user-provided facts distinct.
8. In your own task branch, commit and push as you go; elsewhere commit only
   when the user asks.
9. Users install copied payloads from immutable releases. Do not restore
   symlink installation or an install-from-main quick path.
10. Updates are user-initiated. Verify the release and asset, show the file
    changes, and preserve a rollback backup. A requested normal upgrade needs no
    second confirmation; stop and ask before a downgrade, after failed
    verification, or when the diff reaches outside the selected skill. Never
    bypass failed verification.

Release and repository safeguards are in `MAINTAINING.md`. Re-check GitHub settings
after a transfer or recreation of the repository.
