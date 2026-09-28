# Maintaining Thinking Toolkit

This document records the release and trust decisions that are easy to lose
between maintenance sessions. It applies to repository maintainers; agents do
not load it as part of the skill.

## Trust boundary

Thinking Toolkit is instruction code. A change to `SKILL.md`, `references/`,
`logic/`, or `agents/` can change an agent's behavior even though the project
has no executable runtime. Stable users therefore receive copied, versioned
payloads rather than a live checkout.

The distribution rules are:

- Never restore symlink installation or recommend installing from `main`.
- Never check for or apply updates during an agent session.
- Keep installation and update explicit: verify, show changes, confirm, back
  up, then replace.
- Keep `scripts/`, `tests/`, repository documentation, and Git metadata out of
  the release archive.
- Treat `VERSION` as the identity of the installed payload. Repository-only
  documentation may change without a version bump when the payload is
  unchanged.

## Repository safeguards

The public repository is configured with these controls:

- `main` accepts changes through pull requests and requires the `validate`
  check, including for administrators.
- Linear history and resolved review conversations are required.
- Force-push and branch deletion are disabled for `main`.
- Private vulnerability reporting is enabled.
- Immutable releases are enabled. Once published, a release tag and its assets
  cannot be replaced.

If the repository is transferred, recreated, or its rules are edited, verify
these settings before publishing another release. Workflow files alone do not
enforce repository settings.

## What ships

`scripts/build_release.py` creates a deterministic archive named
`thinking-toolkit-v<VERSION>.tar.gz` and a `SHA256SUMS` manifest. The archive
contains only:

- `SKILL.md`, `LICENSE`, `VERSION`, `install.sh`, and `update.py`
- `agents/`, `references/`, and `logic/`

The builder rejects symlinks, normalizes archive metadata, and runs validation
and tests unless `--skip-checks` is explicitly supplied. The release workflow
does not use that escape hatch.

## Adding a model card

The number of cards is not a cap, but every card adds a routing decision. Admit
a new card only when all of the following hold:

1. It produces an artifact that no existing card produces, and the difference
   from each close neighbor is written as a selection rule in
   `references/catalog.md`.
2. Its aliases do not collide with the name or aliases of an existing model.
3. On a small set of realistic requests, including at least one control request
   that should route elsewhere, the skill with the card selects it where
   intended, avoids it on the control, and returns a better or leaner artifact
   than the current catalog.

An admitted card also updates `EXPECTED_MODELS` and the category counts in
`scripts/validate_skill.py`, the card count in `AGENTS.md`, the counts and
catalog tables in all three READMEs, and the minor version.

## Release procedure

1. Change the payload and update all three READMEs when user-visible behavior
   changes.
2. Set `VERSION` to the intended semantic version in the same pull request.
3. Run the complete local gate:

   ```bash
   python3 scripts/validate_skill.py .
   python3 -m unittest discover -s tests -v
   python3 scripts/build_release.py
   bash -n install.sh
   git diff --check
   ```

4. Merge through the protected `main` branch and confirm that `validate`
   succeeded on the merged commit.
5. From an up-to-date, clean `main`, create and push an annotated version tag:

   ```bash
   release_version=1.1.0
   test "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)"
   git tag -a "v${release_version}" -m "Thinking Toolkit v${release_version}"
   git push origin "v${release_version}"
   ```

6. Wait for `.github/workflows/release.yml`. It verifies that the tag matches
   `VERSION`, rebuilds the payload, and publishes the archive and manifest.
7. Verify the result from a fresh directory:

   ```bash
   gh release download "v${release_version}" --repo ponomr/thinking-toolkit \
     --pattern "thinking-toolkit-v${release_version}.tar.gz" --pattern SHA256SUMS
   gh release verify "v${release_version}" --repo ponomr/thinking-toolkit
   gh release verify-asset "v${release_version}" \
     "thinking-toolkit-v${release_version}.tar.gz" \
     --repo ponomr/thinking-toolkit
   shasum -a 256 -c SHA256SUMS
   ```

Do not reuse a version or tag. Immutable releases make correction-by-replacement
impossible; fix a bad release with a new version.

## Update and rollback behavior

`update.py` runs only when a user invokes it. It verifies the release and
archive through GitHub CLI, rejects unsafe archive paths and links, compares
file hashes, and asks for confirmation. Replacement happens in the target's
parent directory so the previous installation can be renamed into a sibling
backup. The updater prints the exact rollback command after a successful
replacement.

When changing the updater, preserve this order:

1. Verify the release and asset.
2. Validate the archive and its `VERSION`.
3. Display added, removed, and changed files.
4. Ask for confirmation.
5. Replace while preserving a recoverable backup.

## Current baseline

The first hardened release is `v1.0.0`. Its release and asset attestations,
SHA-256 manifest, clean installation, update path, and rollback path were all
verified after publication. Future claims should refer to a named release and
its verification result rather than to the current contents of `main`.

`v1.1.0` adds the After Action Review card. After publication, the release was
confirmed immutable; `gh release verify` and `verify-asset` succeeded; the
archive matched `SHA256SUMS` and a local build byte for byte; a clean
installation succeeded; and an installed `v1.0.0` was updated to `v1.1.0` and
rolled back through `update.py`. Release verification needs a GitHub CLI
recent enough to provide `gh release verify`.
