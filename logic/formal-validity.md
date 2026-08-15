# Formal Validity

Tests for whether a deductive form is *truth-preserving*: if the premises are
true, must the conclusion be true? Validity is about form only. A valid argument
can still have false premises — check truth separately (see
[overview](overview.md)).

Two families cover almost every deductive argument you will audit: categorical
(term) logic and propositional (truth-functional) logic.

## Categorical logic

### The four proposition types

| Type | Form | Name | Subject | Predicate |
|------|------|------|---------|-----------|
| A | All S are P | universal affirmative | distributed | undistributed |
| E | No S are P | universal negative | distributed | distributed |
| I | Some S are P | particular affirmative | undistributed | undistributed |
| O | Some S are not P | particular negative | undistributed | distributed |

A term is **distributed** when the proposition says something about every member
of its class. Rule of thumb: subjects are distributed in universals (A, E);
predicates are distributed in negatives (E, O).

### The eight rules of the syllogism

A categorical syllogism has exactly three terms across three propositions (two
premises, one conclusion). It is valid only if all eight hold:

1. **Three terms only.** Exactly three; a fourth (often via
   [equivocation](fallacies.md)) is the *four-term fallacy*.
2. **Middle term distributed at least once.** Otherwise the premises never
   connect — the *undistributed middle*.
3. **No term distributed in the conclusion unless distributed in its premise.**
   Violations: *illicit major* / *illicit minor*.
4. **No conclusion from two negative premises.**
5. **A negative premise requires a negative conclusion, and vice versa.**
6. **No conclusion from two particular premises.**
7. **If either premise is particular, the conclusion must be particular.**
8. **If either premise is negative, the conclusion must be negative** (restates
   the negative-handling of rules 4–5 as a quick check).

Fast audit: check three-terms, then the middle (rule 2), then distribution in the
conclusion (rule 3), then the negative/particular quantity rules (4–8). Most
invalid real-world syllogisms fail rule 2 or rule 3.

*Example (invalid):* "All auditors are careful; she is careful; so she is an
auditor." Middle term "careful" is the predicate of two affirmatives, never
distributed → undistributed middle.

### Conditional and disjunctive syllogisms

- **Conditional (hypothetical):** "If P then Q." See the valid and invalid forms
  under Propositional logic below.
- **Disjunctive:** "Either P or Q; not P; therefore Q" is valid (*modus tollendo
  ponens*) when the "or" is genuinely exclusive or at least one disjunct holds.
  Affirming one disjunct to deny the other is invalid for an inclusive "or".

### Enthymemes

An argument with a premise or the conclusion left unstated. Reconstruct the
missing part before testing validity, and mark it as supplied — the hidden
premise is often exactly where the argument is weakest.

## Propositional (truth-functional) logic

Here the units are whole statements joined by connectives; validity is decided by
truth values, not by terms.

### Connectives

| Connective | Symbol form | True when |
|------------|-------------|-----------|
| not | ¬P | P is false |
| and | P ∧ Q | both true |
| or (inclusive) | P ∨ Q | at least one true |
| if–then | P → Q | false only when P true and Q false |
| iff | P ↔ Q | both sides share a truth value |

### The truth-table test

An argument form is **valid** iff no row makes all premises true and the
conclusion false. Build a row per combination of the atomic statements, mark the
premise and conclusion columns, and look for a counterexample row.

*Modus ponens* (P → Q, P ⊢ Q) has no such row — valid. Affirming the consequent
(P → Q, Q ⊢ P) has a row where P is false, Q true, premises true, conclusion
false — invalid.

### Valid forms (memorize these)

| Name | From | Conclude |
|------|------|----------|
| Modus ponens | P → Q ; P | Q |
| Modus tollens | P → Q ; ¬Q | ¬P |
| Hypothetical syllogism | P → Q ; Q → R | P → R |
| Disjunctive syllogism | P ∨ Q ; ¬P | Q |
| Constructive dilemma | (P → Q) ∧ (R → S) ; P ∨ R | Q ∨ S |

### Invalid forms (the formal fallacies)

| Name | From | Wrongly concludes | Why |
|------|------|-------------------|-----|
| Affirming the consequent | P → Q ; Q | P | Q may hold for another reason |
| Denying the antecedent | P → Q ; ¬P | ¬Q | Q may hold without P |

*Example:* "If the deploy broke it, the page is down; the page is down; so the
deploy broke it." Affirming the consequent — a database outage fits the same
evidence. See [fallacies](fallacies.md).

### A note on quantifiers

Statements about "all" and "some" that interact across terms ("every reviewer
missed some bug") exceed propositional logic and need quantifier logic. For an
audit, reduce them to categorical form (the eight rules) where possible, and flag
when an argument's validity genuinely turns on nested quantifiers rather than
guessing.

## Connects to

- Name each violation against the [fallacy taxonomy](fallacies.md).
- For generalizations, causes, and analogies — which are not deductive — use
  [induction](induction.md) instead; validity is the wrong test there.
