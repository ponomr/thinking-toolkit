# Five Whys

**Category:** Problem solving
**Also known as:** 5 Whys, why chain

## Contents

- [Purpose](#purpose)
- [Use When](#use-when)
- [Avoid When](#avoid-when)
- [Inputs](#inputs)
- [Procedure](#procedure)
- [Guiding Questions](#guiding-questions)
- [Output Format](#output-format)
- [Worked Example](#worked-example)
- [Common Pitfalls](#common-pitfalls)
- [Useful Combinations](#useful-combinations)

## Purpose

Trace one observed problem to an actionable process-level cause by repeatedly
asking why the previous answer occurred, then fix the condition that allowed
the problem rather than only its symptom.

## Use When

- A specific, bounded incident or defect has already occurred.
- The causal chain is likely short and mostly within one process.
- A quick, low-ceremony root-cause pass is more useful than a full diagram.
- The team can verify each answer against evidence rather than opinion.

## Avoid When

- The effect plausibly has many independent contributing causes; use an
  Ishikawa Diagram to enumerate them first.
- Causes interact through feedback rather than a linear chain.
- The chain would cross into blame for individuals instead of conditions.
- Answers cannot be checked against observations, logs, or records.

## Inputs

- A precise problem statement: what happened, where, when, and magnitude.
- Access to evidence for each proposed causal step.
- People who know the process well enough to verify answers.
- A stopping rule: a cause the team can change at the process level.

## Procedure

1. Write the problem as an observable event without an embedded cause.
2. Ask why the event occurred. Record the answer as a checkable claim.
3. Verify the answer with evidence before asking the next why.
4. Repeat the why question against each verified answer. Five is a guideline,
   not a rule; stop when the answer is a process or system condition the team
   can change and test.
5. Branch when a why has more than one verified contributing answer. Follow
   each branch that could change the countermeasure.
6. Check the chain backward: each cause, if removed, should have prevented the
   next effect. Repair or discard links that fail this test.
7. Define a countermeasure at the deepest actionable cause, and consider
   smaller safeguards at intermediate links.
8. Assign an owner, implement, and verify that recurrence actually stops.

## Guiding Questions

- Is the starting statement an observation or already a diagnosis?
- What evidence shows this answer is true, not merely plausible?
- Would removing this cause have prevented the effect above it?
- Does this why have a second independent answer worth a branch?
- Have we reached a condition of the process rather than a person's mistake?
- What countermeasure changes the condition, and how will we verify it?
- What early signal would show the problem returning?

## Output Format

| Level | Why answer | Evidence | Verified | Branch |
|---|---|---|---|---|
| Problem |  |  |  |  |
| Why 1 |  |  |  |  |
| Why 2 |  |  |  |  |
| Why n |  |  |  |  |

Conclude with the actionable root condition, countermeasure, owner, and a
recurrence check with its review date.

## Worked Example

A weekly report was sent with stale numbers. Why? The export job failed the
night before. Why? Its API token had expired. Why? Tokens expire quarterly and
renewal relies on one person remembering. Why? There is no expiry monitoring or
renewal procedure. The team stops here: the actionable condition is a missing
renewal process, not the individual's memory. Countermeasures are automated
expiry alerts and a documented renewal step, verified at the next quarter
boundary.

## Common Pitfalls

- Stopping at "human error" and retraining instead of changing the condition.
- Accepting plausible answers without verification, so different people produce
  different chains from the same facts.
- Forcing exactly five levels when the actionable cause appears earlier or
  later.
- Following a single chain when the effect required several causes together.
- Fixing the deepest cause while leaving cheap intermediate safeguards unbuilt.
- Declaring success without checking that recurrence actually stopped.

## Useful Combinations

- **Ishikawa Diagram** — enumerate candidate causes first, then drill into the
  strongest branch with why questions.
- **Iceberg Model** — continue from a process cause to structures and beliefs
  when the same problem recurs across processes.
- **OODA Loop** — implement the countermeasure and observe recurrence.
- **Situation-Behavior-Impact** — discuss a behavior-related link without
  assigning blame.
