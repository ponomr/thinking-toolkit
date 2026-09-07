![Thinking Toolkit — best battle-tested thinking models, one field manual for agents](assets/banner.png)

# 🧠 Thinking Toolkit

**English** · [Русский](README.ru.md) · [中文](README.zh.md)

**30 battle-tested thinking models, packaged as one portable skill for any AI agent.**

Thinking Toolkit teaches an agent *how to think about thinking*: given a messy
real-world request — a decision to make, a problem to diagnose, a system to
understand, a message to deliver — it selects the smallest useful set of
structured thinking models, applies them faithfully step by step, and returns a
concrete artifact: a weighted matrix, a causal map, a premortem table, a
backward plan, a draft message.

It is plain Markdown with zero runtime dependencies. If your agent can read
files, it can use this skill.

## Why

Left to itself, an LLM agent reasons in prose that sounds convincing and skips
steps. Meanwhile engineering, strategy, intelligence analysis, and
organizational learning have spent decades turning the situations agents face
daily — comparing options, finding root causes, estimating without data,
stress-testing plans — into named, tested procedures. This skill turns those
procedures into instructions an agent can execute, with the pitfalls
practitioners documented along the way.

Three commitments shape the design:

1. **Selection.** Knowing what a decision matrix is costs nothing; the
   expensive mistake is reaching for one at the wrong moment. The catalog
   encodes selection cues, contrast rules ("Five Whys for one causal chain,
   Ishikawa for breadth, Connection Circles for feedback"), and anti-patterns
   for every model.
2. **Procedure.** Each model ships as a full operational card: inputs,
   numbered steps, guiding questions, output format, a worked example, and
   documented pitfalls. The agent follows the card instead of improvising
   around a label.
3. **Honesty.** The core contract separates observed facts from assumptions,
   marks unknowns instead of inventing evidence, runs sensitivity checks on
   consequential results, and ends every artifact with an action and a review
   trigger.

## How It Works

When a model is named explicitly, the agent loads that card and follows it.
When the request is open, it identifies the job (decide, diagnose, estimate,
map, resolve, communicate), routes through the catalog's selection cues and
contrast rules, and picks one primary model with at most two complements. It
then frames the situation — stakes, reversibility, evidence — applies the
card's procedure at quick, standard, or deep depth, tests the result for
hidden assumptions and sensitivity, and closes with an artifact, an action,
and a review trigger.

The skill uses **progressive disclosure** to stay context-efficient: the agent
first reads only `SKILL.md` (~180 lines), consults the routing catalog when
selection is unclear, and loads *only* the model cards it actually needs.
Thirty models cost nothing until one is used.

## The Catalog

### Decision making — 12 models

| Model | Use when |
|---|---|
| Six Thinking Hats | A choice needs balanced perspectives instead of debate |
| Eisenhower Matrix | Tasks differ by urgency and importance |
| Second-Order Thinking | Immediate benefits may hide later effects |
| Decision Matrix | Several options must be compared across weighted criteria |
| Impact-Effort Matrix | A backlog needs rough portfolio prioritization |
| Ladder of Inference | A conclusion may have outrun its evidence |
| Hard Choice Model | The right amount of decision effort is unclear |
| OODA Loop | Conditions change while action is underway |
| Cynefin Framework | The response must fit the situation's causal nature |
| Confidence → Speed vs. Quality | Product work must trade speed against polish |
| Pareto Analysis | A few contributors may drive most of a measured effect |
| Backcasting | A distant goal needs a path from the endpoint to today |

### Problem solving — 11 models

| Model | Use when |
|---|---|
| Ishikawa Diagram | A defined effect has many possible causes |
| Five Whys | One incident needs its causal chain traced to a process fix |
| Abstraction Laddering | The problem statement may be too narrow or vague |
| Conflict Resolution Diagram | Opposing demands appear mutually exclusive |
| Zwicky Box | A solution can be assembled from independent dimensions |
| Productive Thinking Model | A defined problem needs a complete creative process |
| Inversion | Failure modes reveal the path to success |
| Red Teaming | A confident plan needs an independent adversarial challenge |
| Issue Trees | A large problem needs non-overlapping decomposition |
| First Principles | Conventions and analogies constrain solution quality |
| Fermi Estimation | A quantity must be estimated without direct data |

### Systems thinking — 5 models

| Model | Use when |
|---|---|
| Iceberg Model | Repeated events point to deeper structures and beliefs |
| Connection Circles | Variables and feedback relationships need mapping |
| Concept Map | Concepts and their semantic relationships need clarity |
| Balancing Feedback Loop | A system resists change or seeks a target |
| Reinforcing Feedback Loop | Growth or decline feeds further growth or decline |

### Communication — 2 models

| Model | Use when |
|---|---|
| Situation-Behavior-Impact | Feedback must be specific and non-judgmental |
| Minto Pyramid | A busy audience needs the conclusion first |

Beyond single models, the catalog ships **combination recipes** — proven
sequences such as *Consequential choice* (Hard Choice Model → Decision Matrix →
Red Teaming) or *Root-cause investigation* (Pareto → Iceberg → Ishikawa → Five
Whys → OODA) — plus guardrails against the classic failure of stacking models
to appear thorough.

## Logic analysis (`/logic`)

The 30 cards help you *choose how to think*. `/logic` does the opposite job: it
*audits reasoning that already exists* — a claim, an argument, or a draft — and
returns a verdict on its validity.

It ships **discipline, not a textbook**. The model already knows what modus
tollens is; what `/logic` adds is a fixed procedure (reconstruct → test validity
→ separate form from truth → verdict), a consistent fallacy taxonomy with stable
English + Latin names, and a repeatable verdict format. Three modes, routed by
phrasing, in any language:

- **review** (default) — diagnose and deliver a verdict; no rewrite.
- **fix** — repair the reasoning with minimal intervention, preserving voice.
- **solve** — work a textbook task (validate a syllogism, build a truth table,
  apply a Mill's method, reconstruct an enthymeme).

> *"Check the logic: we shipped the redesign and signups rose, so the redesign
> worked."*
> → **1 critical error.** *Post hoc ergo propter hoc* — a marketing campaign
> launched the same week is an unruled-out cause. Formally invalid; the premise
> may still be true, but the argument doesn't establish it.

Four lean reference files back it: [overview](logic/overview.md) (procedure +
verdict format), [fallacy taxonomy](logic/fallacies.md),
[formal validity](logic/formal-validity.md) (syllogism + propositional), and
[induction](logic/induction.md) (Mill's methods, analogy, hypothesis).

## Installation

The skill follows the [Agent Skills](https://simonwillison.net/2025/Dec/12/openai-skills/)
convention (`SKILL.md` + resource files), supported by Claude Code, OpenAI
Codex CLI, OpenClaw, and other SKILL.md runtimes. Stable installation uses a
copied payload from a fixed, immutable release.

### Recommended: verified release

```bash
gh release download v1.0.0 --repo ponomr/thinking-toolkit \
  --pattern 'thinking-toolkit-v1.0.0.tar.gz' --pattern SHA256SUMS
gh release verify v1.0.0 --repo ponomr/thinking-toolkit
gh release verify-asset v1.0.0 thinking-toolkit-v1.0.0.tar.gz \
  --repo ponomr/thinking-toolkit
tar -xzf thinking-toolkit-v1.0.0.tar.gz
./thinking-toolkit/install.sh
```

This requires [GitHub CLI](https://cli.github.com/). It verifies that the
downloaded bytes belong to the published release before running the installer.
The installer copies the payload into every detected agent, prints each path,
and preserves any replaced installation as a sibling backup.

Options:

- Pick a host: `./install.sh claude`, `codex`, `openclaw`, or a custom path.
- `--force` replaces an existing install without asking; it still keeps a backup.

### Updating

Updates never run inside an agent session. Start them explicitly from an
installed copy:

```bash
python3 ~/.claude/skills/thinking-toolkit/update.py --dry-run
python3 ~/.claude/skills/thinking-toolkit/update.py
```

The updater verifies the immutable release and its archive, displays every
added, removed, and changed file, and asks before replacing anything. It prints
the path to the preserved backup and the exact rollback command. Use the
corresponding Codex or OpenClaw path if that is the copy you want to update.

### Manual install

| Agent | Personal skills directory | Project-scoped |
|---|---|---|
| Claude Code | `~/.claude/skills/thinking-toolkit/` | `.claude/skills/thinking-toolkit/` |
| OpenAI Codex CLI | `~/.codex/skills/thinking-toolkit/` | `.codex/skills/thinking-toolkit/` |
| OpenClaw | `~/.openclaw/skills/thinking-toolkit/` | `.openclaw/skills/thinking-toolkit/` |
| Anything else | Wherever your runtime discovers `SKILL.md` | — |

From the unpacked release, copy the `thinking-toolkit/` directory to the chosen
skills directory. The repository's `scripts/` and `tests/` directories are
development tooling and are deliberately absent from the release archive.
Using the skill requires no API keys, network access, or code execution;
network access is used only when you explicitly install or update it.

For self-hosted gateways and custom harnesses: inject `SKILL.md` into the
system context and make `references/` readable; the skill assumes nothing
beyond file reading.

### Development checkout

Contributors can clone `main` and run `./install.sh`, but `main` is a development
line rather than an audited release. Stable users should install a versioned
release. Symlink installation is intentionally unsupported because it would
couple every agent to changes in a mutable working tree.

## Security model

Thinking Toolkit is instruction code. Treat a change to its Markdown as you
would treat a software update. Published releases are immutable, CI validates
the skill and reproducibility of its archive, and updates always require a
user action and confirmation. See [SECURITY.md](SECURITY.md) for the trust
boundary, verification commands, and vulnerability reporting.

## Usage

Ask for a model by name:

> *"Run a premortem on this launch plan."*
> *"Compare these three vendors with a weighted matrix."*
> *"Backcast from where we want the newsletter to be in three years."*

Or just describe the situation and let the routing work:

> *"Support tickets keep growing and I don't know where to start."*
> → Pareto Analysis to find the vital few, then Five Whys on the top category.

> *"We keep arguing about whether to rewrite the billing service."*
> → Six Thinking Hats to structure the debate, Decision Matrix if options
> stabilize, Red Teaming before committing.

The agent states which model it chose and why, applies the card's procedure,
and returns the artifact with its assumptions and a review trigger.

## Repository Layout

```
thinking-toolkit/
├── SKILL.md                  # entry point: contract, routing, workflow
├── VERSION                   # installed and release version
├── references/
│   ├── catalog.md            # index, aliases, selection cues, recipes
│   └── <model>.md            # 30 operational cards, one per model
├── logic/                    # /logic procedure and focused references
├── agents/openai.yaml        # optional host discovery metadata
├── scripts/                  # validation and deterministic release build
├── tests/                    # regression and supply-chain tests
├── install.sh                # copy payload into agent skill dirs
└── update.py                 # verified updates and rollback
```

### Development

```bash
python3 scripts/validate_skill.py .        # structure + content invariants
python3 -m unittest discover -s tests -v   # validator regression tests
python3 scripts/build_release.py           # reproducible payload + SHA256SUMS
```

The validator enforces the invariants that make the skill reliable: every card
carries all ten operational sections, every link resolves internally, the skill
payload contains no external URLs (it must work fully offline), and the catalog
matches the card set exactly.

## Design Principles

- **Provider-neutral by construction.** No tool calls, no browsing, no code
  execution, no memory assumptions. Any capable LLM with file access qualifies.
- **The smallest useful model set.** One model by default, three at most, and
  explicit permission to use none: a communication model is chosen only after
  the underlying analysis is adequate.
- **User agency preserved.** Model outputs support a decision that stays with
  the user. The skill never manufactures certainty the evidence does not
  contain.
- **Depth matched to stakes.** Quick pass for reversible low-stakes calls; deep
  pass — with sensitivity checks and disconfirming evidence — for consequential
  or irreversible ones.
- **Deterministic quality gates.** A stdlib-only validator keeps all 30 cards
  structurally complete and the routing tables in sync with the card set.

## License

MIT — see [LICENSE](LICENSE).
