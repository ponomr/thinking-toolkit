# Security model

Thinking Toolkit is instruction code: an agent reads its Markdown and may
change its behavior accordingly. Treat updates with the same care as executable
software updates.

## Installation boundary

- Stable installations use a copied, versioned release payload.
- Releases are immutable: their tag and attached assets cannot be replaced
  after publication.
- The release archive contains the skill payload, license, version marker,
  installer, and explicit updater. Repository tests and release tooling stay out.
- The skill never checks for updates while an agent is using it.
- Symlink installation is intentionally unsupported because it couples every
  installed agent to a mutable working tree.

## Verify before installing

With GitHub CLI installed, verify both the release and the downloaded asset:

```bash
gh release verify v1.0.0 --repo ponomr/thinking-toolkit
gh release verify-asset v1.0.0 thinking-toolkit-v1.0.0.tar.gz \
  --repo ponomr/thinking-toolkit
```

The release archive also ships with `SHA256SUMS` for environments that record
or compare checksums. A checksum detects changed bytes; release verification
also checks that the asset belongs to the published repository release.

## Updates

Updates are always initiated by the user. `update.py` verifies the target
release and asset, displays added, removed, and changed files, asks for
confirmation, and preserves the previous installation as a rollback backup.

## Repository safeguards

The protected `main` branch requires pull requests, linear history, resolved
review conversations, and the `validate` status check. These rules also apply
to administrators; force-push and branch deletion are disabled. Private
vulnerability reporting and immutable releases are enabled at repository
level. See [MAINTAINING.md](MAINTAINING.md) for the release checklist and the
settings that must be re-verified after a repository transfer or recreation.

## Reporting a vulnerability

Use [GitHub private vulnerability reporting](https://github.com/ponomr/thinking-toolkit/security/advisories/new)
for this repository. Do not publish exploit details in a public issue before a
fix is available.
