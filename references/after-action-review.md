# After Action Review

**Category:** Problem solving
**Also known as:** AAR, after-action review, lessons learned review

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

Turn one completed episode into a small, testable update by comparing what was
supposed to happen with what actually happened, explaining the difference, and
deciding what to sustain and what to improve.

## Use When

- An attempt, project, event, or decision has finished or reached a milestone.
- The outcome can be compared with an intent, plan, standard, or expectation.
- The episode succeeded, failed, or was mixed, and success is worth learning
  from as much as failure.
- The people involved want an update to their practice, not a verdict.

## Avoid When

- The situation is still unfolding and needs action now; use OODA Loop.
- A defect or incident needs its causal chain traced to a process fix; use
  Five Whys or Ishikawa Diagram.
- The same kind of event keeps recurring across episodes; use Iceberg Model.
- The purpose is to assign blame, discipline, or legal responsibility.
- No intent or expectation existed and none can be reconstructed honestly.

## Inputs

- The original intent: goal, plan, standard, or prediction, ideally as recorded
  before the episode.
- A factual account of what happened, with sources and timing.
- Perspectives of the people who acted, observed, or were affected.
- The decision or practice that the review should be able to change.

## Procedure

1. **Intended:** state what was supposed to happen. Prefer the record made
   before the episode; label any reconstruction as reconstructed.
2. **Actual:** describe what happened as observations, without causes or
   judgments. Keep interpretations in a separate list.
3. **Gap:** mark where the actual result was better than, worse than, or equal
   to the intent. Include gaps in the favorable direction.
4. **Why:** explain each material gap with competing explanations and the
   evidence for each. Separate conditions under the team's control from luck
   and outside events.
5. **Sustain:** name what worked for a reason that will recur, so it should be
   repeated deliberately. When the explanation is still uncertain, name a
   provisional sustain item labeled as a hypothesis rather than leaving the step
   empty.
6. **Improve:** name what should change next time. Reduce all findings to one
   to three lessons phrased as changes in practice, not as observations.
7. Convert the most important lesson into one next action or experiment with
   an owner, and define the event or date that triggers the next review.

## Guiding Questions

- What exactly did we intend, and where is that recorded?
- What happened, stated so that every participant would accept it as fact?
- Where did the result beat the plan, and was that skill or luck?
- Which explanation for the gap has evidence, and which is only a story?
- What did we do well that we would lose if nobody named it?
- Which lesson would change a concrete decision next time?
- What will we check, and when, to know the lesson was applied?

## Output Format

| Step | Content | Basis |
|---|---|---|
| Intended | Goal, plan, or prediction | Record or reconstruction |
| Actual | Observed result and key events | Source |
| Gap | Better, worse, or equal, per item | Comparison |
| Why | Explanations with evidence and confidence | Evidence |
| Sustain | Practices to repeat deliberately | Gap analysis |
| Improve | Practices to change | Gap analysis |

End with one to three lessons, one next action or experiment with an owner, and
a review trigger.

## Worked Example

A team shipped a feature two weeks late but with half the expected support
tickets. Intended: ship by the release date with a normal ticket volume. Actual:
the date slipped after a late security review; tickets were low. Gap: worse on
time, better on quality. Why: the security review was requested only at code
freeze; the low ticket count followed an extra usability test that the delay
made possible, although a quiet sales month may also explain part of it.
Sustain: a usability test before release. Improve: request the security review
at design time. Next action: add the review request to the design template, and
revisit after the next two releases.

## Common Pitfalls

- Reviewing only failures, so what caused success is never made repeatable.
- Mixing observations with interpretations, so the facts are never agreed on.
- Rewriting the original intent after seeing the outcome (hindsight bias).
- Crediting skill for a result that luck or outside events produced.
- Producing a long list of lessons with no owner or next action.
- Letting the review become a hunt for someone to blame, which stops people
  from reporting what actually happened.

## Useful Combinations

- **Ladder of Inference** — check an explanation of the gap that outruns the
  evidence.
- **Five Whys** — trace one unfavorable gap to a process-level cause.
- **Iceberg Model** — connect lessons from several reviews to recurring
  structures.
- **OODA Loop** — run the next action as a small, observable experiment.
- **Situation-Behavior-Impact** — give individual feedback that arises from the
  review.
