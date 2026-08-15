# Pareto Analysis

**Category:** Decision making
**Also known as:** 80/20 analysis, vital-few analysis

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

Concentrate limited effort where it changes the outcome most by measuring how
much each contributor adds to a total effect and separating the vital few
contributors from the trivial many.

## Use When

- One measurable effect has many contributors: defects, costs, delays,
  complaints, revenue, load.
- Contribution data exists or can be collected quickly.
- Capacity is limited and effort must be allocated, not spread evenly.
- A team suspects a small subset drives most of the problem but has not
  verified it.

## Avoid When

- Contributions cannot be measured on one comparable scale.
- Every contributor carries an obligation that must be handled regardless of
  size, such as legal or safety requirements.
- The distribution is roughly uniform, so ranking would create false focus.
- The effect itself is not yet defined precisely enough to attribute.

## Inputs

- A single, clearly defined effect metric with scope and time period.
- A categorization of contributors at consistent granularity.
- Measured or reliably estimated contribution per category.
- Cost and feasibility of addressing each top contributor.

## Procedure

1. Define the effect metric precisely: what is being counted or summed, over
   what period, for whom.
2. Choose contributor categories before looking at results, at a granularity
   coarse enough to act on and fine enough to differentiate.
3. Measure each category's contribution. Verify totals add up to the whole.
4. Sort categories by contribution and compute cumulative percentages,
   verifying the arithmetic with a tool rather than mentally.
5. Identify the vital few: the smallest set of categories covering the
   majority of the effect. Treat any specific split such as 80/20 as an
   empirical result, not a law the data must obey.
6. Before acting, check stability: would a different period, segment, or
   categorization produce a different ranking?
7. For each vital-few category, compare expected reduction against the cost
   and risk of addressing it, then choose interventions.
8. Re-measure after intervening; the ranking shifts as top contributors
   shrink, so the analysis is a cycle, not a one-time cut.

## Guiding Questions

- What single metric defines the effect, and does everyone measure it the
  same way?
- Were the categories chosen before seeing which ranking they produce?
- Do the top categories reflect frequency alone, or also severity and cost?
- Would weighting by impact instead of count reorder the list?
- Is the concentration stable across periods and segments?
- What in the long tail cannot be ignored despite its small size?
- What is the cheapest intervention with the largest expected reduction?

## Output Format

| Rank | Category | Contribution | Share | Cumulative share | Proposed action |
|---:|---|---:|---:|---:|---|
|  |  |  |  |  |  |

Conclude with the vital few, the chosen interventions and owners, obligations
retained from the long tail, and the re-measurement date.

## Worked Example

A support team classifies 1,200 monthly tickets by cause. Password resets
account for 34 percent, one confusing billing screen for 22 percent, and a
missing export feature for 15 percent; eleven remaining categories share the
rest. Three categories thus drive 71 percent of volume. Weighting by handling
time keeps the same top three, so the ranking is stable. The team ships
self-service resets and a billing-screen fix, leaves the export request to the
product backlog with data attached, and re-measures after two months, when a
new top contributor emerges.

## Common Pitfalls

- Treating 80/20 as a universal law and forcing the data to fit it.
- Choosing or merging categories after seeing results to favor a preferred
  conclusion.
- Ranking by raw frequency when severity or cost per event differs sharply.
- Ignoring long-tail items that carry obligations or early signals of new
  problems.
- Acting on an unstable ranking produced by one unusual period.
- Running the analysis once and never re-measuring after interventions.

## Useful Combinations

- **Ishikawa Diagram** — investigate why a vital-few category is so large.
- **Five Whys** — trace a dominant category to its process-level cause.
- **Impact-Effort Matrix** — prioritize interventions across the vital few.
- **Second-Order Thinking** — check what the fix displaces or induces before
  committing.
