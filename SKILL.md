---
name: thinking-toolkit
description: "Apply a named Thinking Toolkit model or audit an argument with /logic. Use only when the user explicitly invokes the toolkit, names an included model or alias, or invokes /logic."
---

# Thinking Toolkit

Apply structured thinking without assuming access to tools, browsing, code,
memory, or a particular LLM provider. Use plain language and produce artifacts
that remain useful outside the conversation.

## Core Contract

1. Reply in the user's language. Keep standard model names recognizable.
2. Preserve user agency. Treat model outputs as decision support, not automatic
   truth or authority.
3. Separate observed facts, user-provided claims, assumptions, hypotheses,
   estimates, preferences, and recommendations.
4. Never invent missing evidence. Mark unknowns and propose a way to resolve
   only the unknowns that could change the outcome.
5. Give a concise selection rationale and the resulting artifact. Do not expose
   private hidden reasoning or produce a diary of internal deliberation.
6. Match depth to stakes, reversibility, uncertainty, and user intent.

## Choose the Mode

### Explicit-model mode

Use the requested model when the user names it or an unambiguous alias. Read
[the catalog](references/catalog.md), then read only that model's card. Add a
second model only when the user permits it and the first model leaves a distinct
gap that materially affects the result.

### Automatic-selection mode

Use this mode only when the user explicitly asks Thinking Toolkit or a
structured thinking toolkit to choose a method but does not name one. Do not
select a model merely because an ordinary request could be approached with a
framework.

1. Identify the job: decide, prioritize, diagnose, reframe, generate, map a
   system, resolve conflict, give feedback, or communicate.
2. Identify the dominant uncertainty: missing evidence, unclear values,
   multiple criteria, causal ambiguity, dynamics, time pressure, or audience.
3. Read [the catalog](references/catalog.md) and shortlist the models whose
   selection cues match.
4. Choose one primary model. Add at most two complementary models only when each
   has a separate role in a clear sequence.
5. State the selected model or sequence and explain the choice in one or two
   sentences.

## Use the Adaptive Workflow

### 1. Frame the situation

Capture only what matters:

- the desired outcome and decision owner or audience;
- scope, constraints, time horizon, and deadline;
- available options, evidence, and prior actions;
- stakes, reversibility, uncertainty, and affected people.

Ask up to three focused questions when missing information could materially
change the model, framing, or recommendation. Otherwise proceed and label
reasonable assumptions.

### 2. Set the working depth

- Use a quick pass for low-stakes, reversible, time-sensitive situations.
- Use a standard pass for ordinary planning, analysis, and communication.
- Use a deep pass for consequential, hard-to-reverse, contested, or systemic
  situations. Include sensitivity checks, disconfirming evidence, and an exit or
  review condition.

### 3. Apply the model faithfully

Read the selected card before using it. Follow its procedure in order, adapt the
questions to the user's context, and create the specified output. Do not reduce
a model to a label or generic advice.

### 4. Test the result

Check for unsupported causal claims, hidden assumptions, omitted stakeholders,
double-counted criteria, false precision, and missing alternatives. Where
relevant, test how the result changes under a plausible alternative assumption.

### 5. Close with action

End with the decision, insight, draft, experiment, or next step the user asked
for. State unresolved uncertainties and define what evidence or event should
trigger a review.

## Catalog Routing

[The catalog](references/catalog.md) is the single index for model names,
aliases, selection cues, category counts, and combination recipes. Read it to
resolve an explicit alias or make an authorized automatic selection, then load
only the selected model card or cards.

## Combine Models Deliberately

- Use one model by default.
- Use a sequence only when models perform different phases, such as classify,
  analyze, choose, stress-test, or communicate.
- Use no more than three models unless the user explicitly asks for a broader
  workshop.
- Do not combine near-duplicates merely to appear thorough.
- Preserve each model's artifact and show how one output becomes the next
  model's input.
- Read the combination recipes in [the catalog](references/catalog.md) before
  constructing a sequence.

## Shape the Response

Match the output to the user's requested format and level of detail; no fixed
set of headings is required. Include the selected model and a brief rationale
when that helps the user follow the artifact. Label material assumptions and
uncertainties, preserve the model's required artifact, and end with the
decision, draft, insight, experiment, or next step the user requested.

## Logic Analysis (`/logic`)

The model cards above help the user *choose how to think*. The `/logic` mode does
something different: it *audits reasoning that already exists* — a claim, an
argument, or a draft — and returns a verdict on its validity.

Route here when the user explicitly invokes `/logic`, including with an
argument, draft, or textbook logic task in any language. It has three modes:

- **review** (default) — diagnose the argument and deliver a verdict; no rewrite.
- **fix** — repair the reasoning with minimal intervention, preserving voice.
- **solve** — work a specific task (validate a syllogism, build a truth table,
  apply a Mill's method, reconstruct an enthymeme).

Read [the logic overview](logic/overview.md) first — it carries the core
contract, the analysis procedure, and the verdict format. Then read only the
reference needed:

- [Logic overview](logic/overview.md) — modes, argument reconstruction, laws of
  thought, verdict format.
- [Fallacy taxonomy](logic/fallacies.md) — named errors (English + Latin) with
  modern examples.
- [Formal validity](logic/formal-validity.md) — syllogism rules and
  propositional/truth-functional tests.
- [Induction](logic/induction.md) — generalization, Mill's methods, analogy,
  hypothesis strength.
