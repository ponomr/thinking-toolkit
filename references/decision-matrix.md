# Decision Matrix

**Category:** Decision making
**Also known as:** Weighted decision matrix, weighted scoring model

## Purpose

Compare several options across explicit criteria and make value judgments,
trade-offs, and scoring assumptions visible.

## Use When

- There are multiple viable options and several relevant criteria.
- Options are comparable enough to use a common scoring scale.
- Stakeholders need a transparent record of why an option leads.
- Weights and scores can be grounded in evidence or explicit preference.

## Avoid When

- A hard constraint already disqualifies an option.
- The options are fundamentally incommensurable and values are still unclear.
- Cause and effect are too uncertain for scores to be meaningful.
- A small, reversible experiment would be cheaper than prolonged scoring.

## Inputs

- A precise decision statement and a complete-enough option set.
- Must-have constraints separated from preferences.
- Distinct criteria with clear definitions and direction of preference.
- A consistent scoring scale, criterion weights, evidence, and uncertainty.

## Procedure

1. State the decision, decision owner, deadline, and baseline option.
2. Remove options that violate verified non-negotiable constraints.
3. Define criteria before scoring options. Avoid overlap and double-counting.
4. Define what each score means for every criterion. Convert measures so a
   higher score consistently means a better result.
5. Assign weights that express relative importance. Explain the value judgment
   behind each weight.
6. Score each option using evidence. Mark estimates and unknowns explicitly.
7. Multiply each score by its weight and sum the weighted values. Verify every
   calculation rather than relying on mental arithmetic.
8. Run sensitivity checks: vary uncertain scores and the most influential
   weights within plausible bounds.
9. Review non-quantifiable concerns and decide whether the numerical leader is
   robust, conditional, or misleading.

## Guiding Questions

- What decision are we actually making, and what is the baseline?
- Which criteria reflect outcomes rather than convenient proxies?
- Are any criteria counting the same benefit or cost twice?
- What evidence supports each score?
- Which weight represents a contested value judgment?
- What plausible change would reverse the ranking?
- Does the leading score hide a fatal downside or weak confidence?

## Output Format

| Criterion | Definition | Weight | Option A | Option B | Option C | Evidence or uncertainty |
|---|---|---:|---:|---:|---:|---|
|  |  |  |  |  |  |  |
| **Weighted total** |  |  |  |  |  |  |

Add hard constraints, sensitivity scenarios, qualitative caveats, the selected
option, and the condition under which the choice should be revisited.

## Worked Example

A team compares three support platforms on reliability, migration effort,
workflow fit, total cost, and vendor risk. Reliability and workflow fit receive
the highest weights. The first scoring pass favors Platform B, but the migration
score is based on a rough estimate. A sensitivity check shows B still leads even
if migration effort is one category worse, while Platform C leads only under a
much lower reliability weight. The team selects B subject to a technical proof
of concept that validates the uncertain migration assumption.

## Common Pitfalls

- Choosing criteria or weights after seeing which option they favor.
- Treating ordinal scores as precise measurements.
- Double-counting correlated criteria.
- Hiding uncertainty inside a single confident number.
- Failing to compare against doing nothing or delaying.
- Selecting the highest total without sensitivity or constraint checks.

## Useful Combinations

- **Hard Choice Model** — decide whether a matrix is appropriate and how much
  effort to invest.
- **Second-Order Thinking** — add delayed consequences to the criteria set.
- **Six Thinking Hats** — generate criteria and alternatives before scoring.
- **Inversion** — identify disqualifying risks and stress-test the leader.
