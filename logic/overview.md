# Logic Analysis (`/logic`)

Run a concrete argument, claim, or request through logic and return a verdict:
is the reasoning valid, what does it assume, and where does it break.

This is a distinct capability from the thinking-model cards. A model card helps
you *choose how to think*; `/logic` *audits reasoning that already exists* —
yours, another person's, or a draft the agent is about to ship.

The module ships **discipline, not a textbook**: a fixed procedure, a consistent
fallacy taxonomy, and a repeatable verdict format. It assumes the reader already
commands the underlying logic; it enforces that the logic gets applied in order
and reported the same way every time.

## Core contract

1. Reply in the user's language. Keep standard term names (Latin fallacy names,
   English logic terms) recognizable.
2. **Separate formal validity from material truth.** A valid form can carry
   false premises to a false conclusion; true premises can sit in an invalid
   form. Judge the two independently and say which failed.
3. Never invent evidence. Mark a premise as unstated, unsupported, or false —
   do not supply facts the text does not contain.
4. Attack the strongest reading of the argument, not a straw version.
5. Give the verdict and the reasoning that supports it, not a diary of every
   step considered.

## Modes

Route by the user's phrasing. Default to **review**.

| Mode | Triggers | Does |
|------|----------|------|
| **review** (default) | "check the logic", "find the logical errors", "is this valid" | Diagnose only. Reconstruct the argument, test validity, name errors, deliver a verdict. No rewrite. |
| **fix** | "fix the logic", "make the argument sound", "improve the reasoning" | Review, then rewrite with **minimal intervention** — repair the reasoning, preserve the author's voice, weaken overreaching claims ("all" → "some") rather than delete them. Add a changelog. |
| **solve** | a textbook task: "is this syllogism valid", "build the truth table", "which Mill's method", "reconstruct the enthymeme" | Apply the specific procedure and show the work. |

## Step 1 — Reconstruct the argument

Before judging anything, extract the skeleton:

- **Thesis** — the one conclusion the text is trying to establish.
- **Premises** — the stated reasons offered for it.
- **Hidden premises** — the unstated assumptions the inference needs to work.
  An argument stated without a premise it depends on is an *enthymeme*; surface
  the missing piece and mark it as supplied.
- **Inference form** — how the premises are meant to reach the thesis:
  - **categorical / term** ("all S are P") → deductive, test with
    [formal validity](formal-validity.md).
  - **propositional** (if–then, and, or, not) → deductive, test with
    [formal validity](formal-validity.md).
  - **inductive** (generalize from cases, infer a cause, argue by analogy) →
    non-deductive, test *strength* with [induction](induction.md).

State the reconstruction plainly. If the text is too vague to reconstruct, say
so and ask for the claim and its support rather than guessing.

## Step 2 — Check the laws of thought

The floor any reasoning stands on. Apply these before the form-specific tests:

- **Identity** — a term keeps one meaning throughout. A term that shifts sense
  mid-argument is *equivocation* (see [fallacies](fallacies.md)).
- **Non-contradiction** — the argument does not assert and deny the same thing
  in the same respect at the same time.
- **Excluded middle** — for a strict either/or, one side holds. Beware its abuse:
  presenting two options as exhaustive when more exist is a *false dilemma*.
- **Sufficient reason** — a claim advanced as established needs a ground. A thesis
  resting on itself is *petitio principii*.

## Step 3 — Test the inference

Run the form-specific test from Step 1's classification:

- deductive → [formal validity](formal-validity.md): is the form truth-preserving?
- inductive → [induction](induction.md): how strong is the support, and what
  would weaken it?

Then name every defect against the taxonomy in [fallacies](fallacies.md), giving
the English and Latin name and the mechanism.

## Step 4 — Separate validity from truth, then deliver the verdict

State, independently: (a) whether the form is valid, and (b) whether the premises
are true, unsupported, or false. A verdict conflating the two is itself an error.

### Verdict format

Adapt headings to the request; output in the user's language.

```
Verdict: <valid | N errors (K critical, M contestable)>
Argument structure: <thesis; premises; inference form>

| # | Location | Error (English + Latin) | Why it fails | Fix |
|---|----------|-------------------------|--------------|-----|

Hidden premises: <unstated assumptions the argument needs>
Formal validity vs material truth: <which holds, which fails>
Inductive / analogical strength: <if the inference is non-deductive>
```

In **fix** mode, follow the verdict with the rewritten text and a short
changelog of what changed and why. In **solve** mode, show the procedure and
the answer.

## Severity

- **Critical** — the error breaks the conclusion: an invalid form, a false or
  question-begging premise, an equivocated key term.
- **Contestable** — a weakness a reader could reasonably dispute: a thin
  induction, an unstated but plausible premise, an imprecise term.

Do not force a fixed quota of findings. A sound argument gets a clean verdict.

## Connects to the thinking-model cards

Logic analysis pairs with the toolkit's cards, and the boundary is clean: the
cards help you *think*; `/logic` *audits finished reasoning*.

- A fallacy about an unsupported leap is the defect the
  [Ladder of Inference](../references/ladder-of-inference.md) traces rung by rung.
- To stress-test the argument you just repaired, use
  [Inversion](../references/inversion.md) or
  [Red Teaming](../references/red-teaming.md).
- To challenge a premise instead of accepting it, use
  [First Principles](../references/first-principles.md).
- To restructure a repaired argument for a reader, use the
  [Minto Pyramid](../references/minto-pyramid.md).

## Sources

The methods here are distilled from classical and modern logic: term logic and
the eight syllogism rules; the laws of thought; the methods of inductive
inference; and truth-functional logic. All text is original prose written for
this module.
