# Model Catalog and Selection Guide

Use this file to route a request before loading a detailed model card.

## Contents

- [Argument analysis vs model selection](#argument-analysis-vs-model-selection)
- [Explicit selection](#explicit-selection)
- [Complete catalog](#complete-catalog)
- [Selection rules](#selection-rules)
- [Combination recipes](#combination-recipes)
- [Combination guardrails](#combination-guardrails)

## Argument Analysis vs Model Selection

This catalog routes to a thinking model — a way to *approach* a problem. When
the request is instead to *audit reasoning that already exists* ("check the
logic", "is this argument valid", "find the fallacy"), in any language, that
is not a model-selection task: route to the `/logic` module at
[logic/overview.md](../logic/overview.md) and do not pick a card from the table
below.

## Explicit Selection

Treat a standard name, common alias, or unmistakable description as an explicit
request. For example, "apply a weighted scoring table" selects Decision Matrix,
and "run a premortem" selects Inversion. When a phrase could mean two models,
ask one short question or state the interpretation before proceeding.

## Complete Catalog

| Category | Model | Common aliases or phrases | Best signal |
|---|---|---|---|
| Decision making | [Six Thinking Hats](six-thinking-hats.md) | six hats, parallel thinking | A choice needs balanced perspectives |
| Decision making | [Eisenhower Matrix](eisenhower-matrix.md) | urgent-important matrix, priority quadrants | Tasks differ by urgency and importance |
| Decision making | [Second-Order Thinking](second-order-thinking.md) | downstream effects, and then what, time horizons | Immediate benefits may hide later effects |
| Decision making | [Decision Matrix](decision-matrix.md) | weighted matrix, criteria scoring, weighted choice | Several options and criteria must be compared |
| Decision making | [Impact-Effort Matrix](impact-effort-matrix.md) | impact-work matrix, quick wins | Initiatives need rough portfolio prioritization |
| Decision making | [Ladder of Inference](ladder-of-inference.md) | inference ladder, check assumptions | A conclusion may outrun the evidence |
| Decision making | [Hard Choice Model](hard-choice-model.md) | impact-comparability matrix, decision type | The right amount of decision effort is unclear |
| Decision making | [OODA Loop](ooda-loop.md) | observe-orient-decide-act, rapid decision loop | Conditions change while action is underway |
| Decision making | [Cynefin Framework](cynefin-framework.md) | sense-making domains | The response must fit the situation's causal structure |
| Decision making | [Confidence Determines Speed vs. Quality](confidence-speed-quality.md) | speed-quality confidence model | Product work must trade speed against polish |
| Decision making | [Pareto Analysis](pareto-analysis.md) | 80/20, vital few | A few contributors may drive most of a measured effect |
| Decision making | [Backcasting](backcasting.md) | future-back planning, work backward from the future | A distant goal needs a path from the endpoint to today |
| Problem solving | [Ishikawa Diagram](ishikawa-diagram.md) | fishbone, cause-and-effect diagram | A defined effect has multiple possible causes |
| Problem solving | [Five Whys](five-whys.md) | 5 whys, why chain | One incident needs its causal chain traced to a process fix |
| Problem solving | [Fermi Estimation](fermi-estimation.md) | order-of-magnitude estimate, back-of-the-envelope | A quantity must be estimated without direct data |
| Problem solving | [Red Teaming](red-teaming.md) | adversarial review, devil's advocacy, challenge session | A confident plan needs an independent adversarial challenge |
| Problem solving | [Abstraction Laddering](abstraction-laddering.md) | why-how ladder, problem framing ladder | The initial problem statement may be too narrow or vague |
| Problem solving | [Conflict Resolution Diagram](conflict-resolution-diagram.md) | evaporating cloud, conflict cloud | Opposing demands appear mutually exclusive |
| Problem solving | [Zwicky Box](zwicky-box.md) | morphological box, morphological analysis | A solution can be assembled from independent dimensions |
| Problem solving | [Productive Thinking Model](productive-thinking-model.md) | productive thinking, target future, DRIVE | A defined problem needs a complete creative process |
| Problem solving | [Inversion](inversion.md) | premortem, reverse thinking, avoid failure | Failure modes or opposite conditions reveal the solution |
| Problem solving | [Issue Trees](issue-trees.md) | logic tree, why tree, how tree | A large problem needs non-overlapping decomposition |
| Problem solving | [First Principles](first-principles.md) | fundamental truths, reasoning from basics | Conventions or analogies constrain solution quality |
| Systems thinking | [Iceberg Model](iceberg-model.md) | event-pattern-structure-mental model | Repeated events point to deeper system causes |
| Systems thinking | [Connection Circles](connection-circles.md) | causal circle, relationship circle | Variables and feedback relationships need mapping |
| Systems thinking | [Concept Map](concept-map.md) | knowledge map, proposition map | Concepts and their semantic relationships need clarity |
| Systems thinking | [Balancing Feedback Loop](balancing-feedback-loop.md) | stabilizing loop, goal-seeking loop | A system resists change or seeks a target |
| Systems thinking | [Reinforcing Feedback Loop](reinforcing-feedback-loop.md) | amplifying loop, compounding loop | Growth or decline feeds further growth or decline |
| Communication | [Situation-Behavior-Impact](situation-behavior-impact.md) | SBI, behavior-based feedback | Feedback must be specific and non-judgmental |
| Communication | [Minto Pyramid](minto-pyramid.md) | pyramid principle, answer first, BLUF | A busy audience needs the conclusion first |

## Selection Rules

1. Select by the user's desired output, not by superficial vocabulary.
2. Prefer the narrowest model that can complete the job.
3. Distinguish prioritization models:
   - Use Eisenhower Matrix for urgency versus importance.
   - Use Impact-Effort Matrix for portfolio value versus work.
   - Use Pareto Analysis when contribution to one effect can be measured.
   - Use Decision Matrix for multiple explicit criteria and comparable options.
4. Distinguish causal models:
   - Use Five Whys to trace one incident's causal chain to a process fix.
   - Use Ishikawa Diagram to enumerate possible causes of a defined effect.
   - Use Issue Trees to decompose the full question space.
   - Use Iceberg Model to connect events to recurring patterns and structures.
   - Use Connection Circles to map mutual causation and feedback.
5. Distinguish relationship maps:
   - Use Concept Map for semantic propositions between concepts.
   - Use Connection Circles for directional causal influence between variables.
6. Distinguish uncertainty responses:
   - Use OODA Loop when rapid iteration and fresh feedback matter.
   - Use Cynefin Framework when the nature of cause and effect is itself unclear.
   - Use Hard Choice Model when stakes and option comparability determine effort.
   - Use Fermi Estimation when the missing piece is a bounded quantity.
7. Distinguish stress tests and forward views:
   - Use Inversion to imagine failure conditions from within the team.
   - Use Red Teaming when an independent challenger or a responsive adversary
     must attack the plan.
   - Use Second-Order Thinking to trace consequences forward from a decision.
   - Use Backcasting to reason backward from a defined desirable future.
8. Use a communication model only after the underlying analysis is adequate.

## Combination Recipes

Use these as patterns, not mandatory bundles. Keep the actual sequence to the
smallest set that addresses the request.

### Consequential choice

1. Use Hard Choice Model to calibrate effort.
2. Use Decision Matrix when options share meaningful criteria.
3. Use Second-Order Thinking or Inversion to stress-test the leading option,
   and Red Teaming when the stakes justify an independent challenge.

### Ambiguous or novel problem

1. Use Cynefin Framework to identify the operating domain.
2. Use Abstraction Laddering to improve the problem frame.
3. Use First Principles or Productive Thinking Model to develop a response.

### Root-cause investigation

1. Use Pareto Analysis to find which contributors deserve investigation first.
2. Use Iceberg Model to distinguish event, pattern, structure, and mental model.
3. Use Ishikawa Diagram or Issue Trees to organize candidate causes, then
   Five Whys to drill the strongest branch to a process-level fix.
4. Use OODA Loop to test the most decision-relevant hypothesis through action.

### Innovation portfolio

1. Use First Principles to expose fundamental constraints.
2. Use Zwicky Box to generate novel combinations.
3. Use Impact-Effort Matrix or Decision Matrix to prioritize candidates.

### Dynamic system

1. Use Connection Circles to map variables and causal links.
2. Use Reinforcing and Balancing Feedback Loops to classify closed loops.
3. Use Iceberg Model to connect the map to structures and mental models.

### Difficult feedback

1. Use Ladder of Inference to remove unsupported interpretation.
2. Use Situation-Behavior-Impact to draft the feedback.
3. Use Minto Pyramid when a broader written message needs a clear conclusion.

### Priority overload

1. Use Eisenhower Matrix to separate urgency from importance.
2. Use Pareto Analysis when measured contribution should direct the effort.
3. Use Impact-Effort Matrix within the important work when capacity is limited.
4. Use OODA Loop only if priorities must be repeatedly updated from new signals.

### Long-horizon goal

1. Use Backcasting to define the end state and the backward milestone chain.
2. Use Fermi Estimation to check that milestone magnitudes are plausible.
3. Use Issue Trees to decompose the nearest milestone into workstreams.
4. Use Inversion or Red Teaming to stress-test the weakest links in the path.

### Estimate under missing data

1. Use Fermi Estimation to produce a bounded range for the unknown quantity.
2. Use Second-Order Thinking when the estimate feeds a consequential decision.
3. Use Decision Matrix to carry the range, not a false point value, into the
   comparison.

## Combination Guardrails

- Do not score a situation before the options and criteria are stable enough.
- Do not map causal loops from semantic association alone.
- Do not treat a brainstorming diagram as proof of root cause.
- Do not use a fast iteration loop to bypass irreversible-risk analysis.
- Do not let a communication framework conceal uncertainty or weak evidence.
- Pass an explicit artifact between models: a frame, criteria set, hypothesis
  list, causal map, selected option, or draft message.
