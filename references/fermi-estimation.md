# Fermi Estimation

**Category:** Problem solving
**Also known as:** Order-of-magnitude estimation, back-of-the-envelope calculation

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

Produce a defensible rough estimate of an unknown quantity by decomposing it
into factors that can each be bounded from everyday knowledge, then combining
the factors while tracking how uncertain the result is.

## Use When

- A decision needs a number and no direct data is available in time.
- A claim, plan, or metric needs a plausibility check.
- Knowing the order of magnitude would already change the decision.
- A large unknown can be expressed as a product or sum of smaller knowns.

## Avoid When

- Accurate data is cheaply available and the stakes justify getting it.
- The decision hinges on a difference smaller than the estimate's error range.
- The quantity depends on a mechanism nobody can bound, so factor guesses
  would be fiction rather than estimation.
- The estimate would be quoted as a measured fact outside its context.

## Inputs

- A precisely defined target quantity with units, scope, and time period.
- Reference values the estimator actually knows or can bound confidently.
- A decision threshold: what answer would change the choice.
- A way to perform arithmetic reliably rather than mentally.

## Procedure

1. Define the quantity exactly, including units and boundaries.
2. Decompose it into factors whose product or sum equals the target. Prefer
   factors that can be anchored to known reference values.
3. Estimate each factor as a range: a plausible lower and upper bound. When a
   factor spans orders of magnitude, choose the geometric middle of the bounds
   rather than the arithmetic average.
4. Combine the factors. Compute a low, central, and high scenario, and verify
   the arithmetic with a calculator or tool rather than mental math.
5. Check units end to end; unit mismatch is the most common silent error.
6. Sanity-check the result against an independent anchor: a known total it
   cannot exceed, a per-person or per-day rate, or a second decomposition.
7. Identify the factor contributing the most uncertainty. If the decision is
   sensitive to it, refine only that factor with better evidence.
8. Report the estimate as a range with its assumptions, not as a point fact.

## Guiding Questions

- What exactly is being estimated, in what units, over what period?
- What decomposition uses quantities I can actually bound?
- What do I know that anchors each factor: populations, rates, sizes, prices?
- Is each bound honest, or narrowed by overconfidence?
- Does an independent cross-check land within the same order of magnitude?
- Which single factor would change the conclusion if it were wrong?
- Is the range tight enough for the decision, or is real data now required?

## Output Format

| Factor | Low | Central | High | Basis or anchor |
|---|---:|---:|---:|---|
|  |  |  |  |  |
| **Combined** |  |  |  |  |

Conclude with the range, the dominant uncertainty, the cross-check used, and
whether the decision needs real data before proceeding.

## Worked Example

A founder asks whether a support team can handle launching in a new market.
Expected new users are decomposed into reachable audience, realistic signup
rate, and support-contact rate per user per month. Bounds give 400 to 2,500
extra tickets monthly, with a central estimate near 1,000. An agent handles
roughly 300 tickets monthly, so the range implies one to eight additional
agents, most likely around three. The cross-check against the current market's
tickets-per-user rate falls in the same range. The decision is robust: hiring
two agents now with a contractor on standby covers the plausible range, so no
expensive market study is needed.

## Common Pitfalls

- Estimating the whole quantity in one intuitive leap instead of decomposing.
- Using arithmetic means across order-of-magnitude ranges, which biases high.
- Compounding several "safe" pessimistic factors into an absurd total.
- Dropping or mismatching units midway through the calculation.
- Presenting the central value as a fact and omitting the range.
- Refining comfortable factors while the decision hinges on an uncomfortable
  one.

## Useful Combinations

- **Issue Trees** — structure the decomposition when factors branch.
- **Decision Matrix** — feed estimated quantities into criteria scoring with
  their uncertainty attached.
- **Second-Order Thinking** — estimate the size of downstream effects.
- **Inversion** — ask what the number would have to be for the plan to fail,
  then check whether that value is plausible.
