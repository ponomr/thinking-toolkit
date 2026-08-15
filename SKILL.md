---
name: thinking-toolkit
description: "A toolkit of 30 decision-making, problem-solving, systems-thinking, and communication models, plus a /logic mode that audits an argument's validity. This skill should be used when a user names a specific model, or describes a situation that calls for one: framing or reframing a problem, comparing options, setting priorities, tracing consequences, finding root causes, estimating an unknown quantity, planning toward a distant goal, mapping or stress-testing a system, resolving a conflict, giving feedback, or structuring a message. It should also be used to check reasoning for logical validity and fallacies. When the method is left open, the skill selects the smallest useful set of models automatically."
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

Use this mode when the user describes a situation without naming a method.

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

## Fast Selection Map

| User need | Primary model |
|---|---|
| Examine a choice from distinct perspectives | Six Thinking Hats |
| Sort work by urgency and importance | Eisenhower Matrix |
| Trace downstream consequences | Second-Order Thinking |
| Compare options across weighted criteria | Decision Matrix |
| Prioritize by benefit and required work | Impact-Effort Matrix |
| Check a conclusion for inferential leaps | Ladder of Inference |
| Match decision effort to stakes and comparability | Hard Choice Model |
| Decide and adapt under time pressure | OODA Loop |
| Match action to the nature of a situation | Cynefin Framework |
| Balance product speed and quality using confidence | Confidence Determines Speed vs. Quality |
| Focus effort on the few contributors that drive most of an effect | Pareto Analysis |
| Plan backward from a defined desirable future | Backcasting |
| Organize possible causes of a defined effect | Ishikawa Diagram |
| Trace one incident to a process-level fix | Five Whys |
| Estimate an unknown quantity without direct data | Fermi Estimation |
| Challenge a plan from an adversary's perspective | Red Teaming |
| Reframe a problem at broader or narrower levels | Abstraction Laddering |
| Resolve opposing positions through shared needs | Conflict Resolution Diagram |
| Generate combinations across independent dimensions | Zwicky Box |
| Run an end-to-end creative problem-solving process | Productive Thinking Model |
| Prevent failure by reasoning backward | Inversion |
| Decompose a problem or solution space | Issue Trees |
| Rebuild from fundamental constraints and truths | First Principles |
| Move from events to patterns, structures, and beliefs | Iceberg Model |
| Map causal relationships and feedback loops | Connection Circles |
| Map concepts and explicit propositions | Concept Map |
| Explain goal-seeking or stabilizing behavior | Balancing Feedback Loop |
| Explain compounding growth or decline | Reinforcing Feedback Loop |
| Give specific, behavior-based feedback | Situation-Behavior-Impact |
| Lead a message with its conclusion | Minto Pyramid |

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

## Response Shape

Adapt the headings to the request, but include these elements when useful:

1. **Frame** — outcome, scope, constraints, and known evidence.
2. **Selected model(s)** — name and concise selection rationale.
3. **Inputs and assumptions** — clearly labeled.
4. **Model artifact** — matrix, tree, map, sequence, draft, or structured notes.
5. **Interpretation** — insights, trade-offs, uncertainty, and sensitivity.
6. **Action** — decision, next step, owner, experiment, or review trigger.

## Model References

Read only the cards needed for the current request.

### Decision making

- [Six Thinking Hats](references/six-thinking-hats.md)
- [Eisenhower Matrix](references/eisenhower-matrix.md)
- [Second-Order Thinking](references/second-order-thinking.md)
- [Decision Matrix](references/decision-matrix.md)
- [Impact-Effort Matrix](references/impact-effort-matrix.md)
- [Ladder of Inference](references/ladder-of-inference.md)
- [Hard Choice Model](references/hard-choice-model.md)
- [OODA Loop](references/ooda-loop.md)
- [Cynefin Framework](references/cynefin-framework.md)
- [Confidence Determines Speed vs. Quality](references/confidence-speed-quality.md)
- [Pareto Analysis](references/pareto-analysis.md)
- [Backcasting](references/backcasting.md)

### Problem solving

- [Ishikawa Diagram](references/ishikawa-diagram.md)
- [Five Whys](references/five-whys.md)
- [Abstraction Laddering](references/abstraction-laddering.md)
- [Conflict Resolution Diagram](references/conflict-resolution-diagram.md)
- [Zwicky Box](references/zwicky-box.md)
- [Productive Thinking Model](references/productive-thinking-model.md)
- [Inversion](references/inversion.md)
- [Red Teaming](references/red-teaming.md)
- [Issue Trees](references/issue-trees.md)
- [First Principles](references/first-principles.md)
- [Fermi Estimation](references/fermi-estimation.md)

### Systems thinking

- [Iceberg Model](references/iceberg-model.md)
- [Connection Circles](references/connection-circles.md)
- [Concept Map](references/concept-map.md)
- [Balancing Feedback Loop](references/balancing-feedback-loop.md)
- [Reinforcing Feedback Loop](references/reinforcing-feedback-loop.md)

### Communication

- [Situation-Behavior-Impact](references/situation-behavior-impact.md)
- [Minto Pyramid](references/minto-pyramid.md)

## Logic Analysis (`/logic`)

The model cards above help the user *choose how to think*. The `/logic` mode does
something different: it *audits reasoning that already exists* — a claim, an
argument, or a draft — and returns a verdict on its validity.

Route to `/logic` when the user asks to "check the logic", "find the logical
errors", "is this argument valid", "spot the fallacies", or gives a textbook
logic task — in any language. It has three modes:

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
