# Issue Trees

**Category:** Problem solving
**Also known as:** Logic trees, problem trees, why trees, how trees

## Purpose

Break a broad problem or solution question into smaller branches that are
distinct, collectively cover the decision-relevant space, and can be analyzed or
assigned independently.

## Use When

- A problem is too large or ambiguous to analyze as one block.
- A team needs a shared map of subquestions and workstreams.
- Root causes or solution categories must be explored systematically.
- Prioritization requires seeing the whole decision-relevant space.

## Avoid When

- Strong feedback loops make a strict hierarchy misleading.
- The question is primarily semantic and needs a concept map.
- The effect is already narrow and candidate causes fit an Ishikawa Diagram.
- A familiar template would be imposed without adapting it to the actual issue.

## Inputs

- A precise root question with scope, metric, stakeholder, and timeframe.
- Known constraints, definitions, and baseline evidence.
- A chosen tree type: diagnostic "why" or solution "how."
- A stopping rule for leaves that are specific and actionable enough.

## Procedure

1. Write the root as one answerable question.
2. Choose a decomposition logic appropriate to the question: equation, process,
   stakeholder, segment, category, time, geography, or another principled split.
3. Create first-level branches that are as mutually exclusive and collectively
   exhaustive as practical. Treat MECE as a quality test, not a guarantee.
4. State every branch at the same logical level and in parallel language.
5. Repeat the split for branches that remain too broad.
6. For a diagnostic tree, ask why the parent outcome occurs. For a solution
   tree, ask how the parent outcome could be achieved.
7. Check for overlaps, gaps, hidden assumptions, and branches that cannot be
   tested or acted upon.
8. Attach evidence, hypotheses, and an owner to relevant leaves.
9. Prioritize leaves by impact, evidence, and cost of analysis rather than
   expanding every branch equally.

## Guiding Questions

- Is the root question specific and answerable?
- What decomposition logic makes the branches coherent?
- Do branches overlap? What relevant case falls into none of them?
- Are siblings at the same level of abstraction?
- Does each leaf produce a test, analysis, or action?
- Which branch could explain the largest share of the problem?
- What evidence would prune or elevate a branch?

## Output Format

```text
Root question
├── Branch A
│   ├── Leaf A1 — hypothesis, evidence, owner
│   └── Leaf A2 — hypothesis, evidence, owner
└── Branch B
    ├── Leaf B1 — hypothesis, evidence, owner
    └── Leaf B2 — hypothesis, evidence, owner
```

Add decomposition logic, gap and overlap check, prioritized leaves, and next
analysis.

## Worked Example

A service asks why trial users are not becoming paying customers. The first split
separates users who never reach the purchase decision from users who reach it but
do not buy. The first branch divides into activation and sustained-use issues;
the second into value, price, trust, and procurement barriers. Evidence shows a
large drop before activation, so the team prioritizes that branch rather than
investigating every leaf at equal depth.

## Common Pitfalls

- Using memorized categories that do not fit the question.
- Mixing causes, solutions, and symptoms within one sibling set.
- Claiming perfect completeness without testing edge cases.
- Decomposing indefinitely without prioritizing evidence.
- Making branches so generic that no analysis follows.
- Ignoring cross-branch interactions that need a causal map.

## Useful Combinations

- **Abstraction Laddering** — improve the root question before decomposition.
- **Ishikawa Diagram** — expand candidate causes within a prioritized leaf.
- **Impact-Effort Matrix** — prioritize solution-tree leaves.
- **Minto Pyramid** — convert the completed logic into a clear message.
