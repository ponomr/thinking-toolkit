---
name: thinking-toolkit
description: "Apply a named Thinking Toolkit model or audit an argument with /logic. Use only when the user explicitly invokes the toolkit, names an included model or alias, or invokes /logic."
---

# Thinking Toolkit

Use only on explicit toolkit, included-model, alias, or `/logic` requests.
Ordinary planning, analysis, and writing requests do not activate this skill.

## Contract

Reply in the user's language; keep model names recognizable. Preserve user
agency: outputs support decisions, not automatic truth. Distinguish observed
facts, user-provided claims, assumptions, hypotheses, estimates, preferences,
and recommendations. Mark missing evidence and resolve only unknowns that could
change the result. Give conclusions and their support, not private deliberation.
No provider-specific tools, browsing, code execution, or persistent memory are
required. Without file access, ask for the files named by the applicable route;
never claim to have read unavailable instructions.

## Route

- **Named model or alias:** use the [model index](references/catalog.md), then
  read that card. Add another model only with user permission and a distinct,
  material gap left by the first.
- **Toolkit asked to choose:** read [selection](references/selection.md), then
  only the relevant selection group and chosen card. This permission does not
  extend to ordinary requests outside the toolkit.
- **`/logic`:** go directly to [logic overview](logic/overview.md). It owns
  **review** (default), **fix**, and **solve**, and directs reference loading.
  Skip the model index and selection guides.

## Apply

1. Frame the outcome, owner or audience, scope, constraints, horizon, evidence,
   prior actions, affected people, and stakes. Ask up to three focused questions
   only when missing information could change framing, method, or recommendation;
   otherwise proceed with labeled assumptions.
2. Match depth to stakes, reversibility, uncertainty, and intent: quick for
   low-stakes reversible work, standard otherwise, deep for consequential,
   contested, systemic, or hard-to-reverse work. Deep work includes sensitivity,
   disconfirming evidence, and an exit or review condition.
3. Follow the selected procedure in order and deliver its required artifact.
   Use one model by default. For a sequence, read [combinations](references/combinations.md)
   and pass each artifact to the next method. Use at most three models unless
   the user requests a broader workshop; each must fill a separate role.
4. Check unsupported causation, hidden assumptions, omitted stakeholders,
   double-counting, false precision, missing alternatives, and relevant
   sensitivity to plausible assumptions.
5. Return the requested decision, insight, draft, estimate, experiment, or action.
   Explain selection briefly when useful; adapt formatting and detail to the
   request. Preserve required outputs, material uncertainty, next action, and
   evidence or events that should trigger review. No fixed response headings
   or narration of internal steps are required.
