# Ishikawa Diagram

**Category:** Problem solving
**Also known as:** Fishbone diagram, cause-and-effect diagram

## Purpose

Organize many plausible causes of a defined effect into categories and deeper
subcauses so investigation is broad, visible, and less vulnerable to the first
available explanation.

## Use When

- A recurring or consequential effect may have multiple contributing causes.
- A knowledgeable group needs a structured root-cause brainstorming session.
- The problem statement is specific enough to investigate.
- Candidate causes must be organized before evidence gathering.

## Avoid When

- The effect is vague, compound, or not yet measurable.
- Immediate containment must occur before diagnosis.
- A brainstorming diagram would be mistaken for proof of causation.
- The primary need is mapping feedback among variables rather than tracing causes
  toward one effect.

## Inputs

- A neutral, observable effect statement with scope and timeframe.
- People with relevant process knowledge and available data.
- Context-appropriate cause categories.
- A way to test, compare, or gather evidence for candidate causes.

## Procedure

1. Write the effect precisely at the head of the diagram. Include what, where,
   when, and magnitude when known; do not embed a presumed cause.
2. Choose broad categories. For operational processes, possible prompts include
   people, equipment or technology, methods, measurement, materials or inputs,
   and environment. Adapt or replace them for the domain.
3. Ask what could contribute to the effect and place each candidate on a branch.
4. For every candidate, ask why it could occur and add deeper subcauses. Continue
   until a cause is specific enough to test or act on.
5. Permit a candidate to appear in more than one branch when the categorization
   genuinely overlaps; the diagram is a thinking aid, not a taxonomy contest.
6. Mark whether each item is observed, inferred, or merely possible.
7. Prioritize candidates by evidence, plausible mechanism, frequency, control,
   and potential contribution.
8. Define a verification step for the most decision-relevant candidates.
9. Update the diagram as tests eliminate, refine, or confirm causes.

## Guiding Questions

- Is the effect written as an observation rather than a diagnosis?
- Which process categories could contribute?
- Why might this candidate cause occur?
- What evidence supports or contradicts this branch?
- Could several causes interact or be necessary together?
- Is this a root cause, an intermediate mechanism, or another symptom?
- What test would distinguish this candidate from alternatives?

## Output Format

- **Effect statement:** observable and bounded.
- **Category branches:** hierarchical candidate causes and subcauses.
- **Evidence labels:** observed, inferred, possible, contradicted.
- **Priority table:** candidate, mechanism, evidence, confidence, verification.
- **Next investigation:** test, owner, expected signal, and review point.

## Worked Example

A service team investigates a rise in failed account activations. The effect is
bounded to a release date and one region. Branches cover user inputs, email
delivery, application logic, monitoring, support process, and environment.
Several hypotheses emerge, but logs support only a delayed-email branch while a
browser-compatibility branch lacks evidence. The team tests delivery latency by
provider before declaring root cause and discovers that a retry policy interacts
with one provider's rate limit.

## Common Pitfalls

- Writing the suspected cause into the effect statement.
- Using generic categories as mandatory or complete.
- Stopping at broad labels such as "people" or "process."
- Voting for a root cause without verification.
- Assuming there can be only one cause.
- Treating correlation, sequence, or diagram position as causal proof.

## Useful Combinations

- **Iceberg Model** — identify patterns and structures before detailing causes.
- **First Principles** — probe a branch until assumptions and mechanisms are
  explicit.
- **Issue Trees** — structure a broader diagnostic question before the fishbone.
- **OODA Loop** — test a prioritized causal hypothesis through bounded action.
