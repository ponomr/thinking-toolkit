# Induction and Non-Deductive Strength

Deductive validity is binary: the form preserves truth or it does not. Inductive
reasoning is different — it generalizes, infers causes, and argues by analogy, and
its conclusions are only ever *strong* or *weak*, never guaranteed. Audit
inductive arguments for **strength and what would weaken them**, not validity.

The distinction matters: calling a strong induction "invalid" because it isn't
deductive is itself an error. Judge each inference by the right standard.

## Generalization

Inferring a rule about a class from observed members.

- **Full (complete) induction** enumerates every member — certain, but rare and
  usually trivial.
- **Partial (incomplete) induction** infers from a sample. This is the ordinary,
  fallible kind. Its strength depends on:
  - **sample size** — enough cases to rule out coincidence;
  - **representativeness** — the sample resembles the class on the relevant
    dimensions, not just the convenient ones;
  - **absence of known counterexamples** — and an active search for them.

The failure mode is **hasty generalization**: a sweeping claim from too few or
biased cases (see [fallacies](fallacies.md)). *Example:* "Two beta users loved it,
so the market wants it."

## Causal inference — Mill's methods

Five methods for isolating a cause from observed circumstances. Each is a probe,
not a proof; each is defeated by an unexamined third factor.

| Method | Test | Finds |
|--------|------|-------|
| **Agreement** | Cases with the effect share only one prior circumstance | A candidate cause common to all occurrences |
| **Difference** | Two cases identical except one factor; effect present only with it | The factor that makes the difference |
| **Joint agreement and difference** | Combine both — present with, absent without | A stronger candidate than either alone |
| **Residues** | Subtract known causes of parts of an effect | The cause of the remaining part |
| **Concomitant variation** | The effect varies as a factor varies | A cause that scales with the effect (or a shared driver) |

**Guardrails.** Mill's methods find *candidate* causes, not certainties. Every one
is vulnerable to a hidden common cause, a reversed direction of causation, or a
confounder that rides along with the factor under test. Correlation surfaced by
concomitant variation is not causation — see *post hoc* and *false cause* in the
[fallacy taxonomy](fallacies.md).

*Example (Difference):* two identical deploys, one adds a caching layer, latency
drops only in that one → caching is the difference-maker, provided nothing else
changed between them.

## Analogy

Inferring that because two things share known features, they share a further one.
Strength depends on:

- the **number and variety** of relevant shared features;
- the **relevance** of the shared features to the inferred one (surface
  similarity is worthless);
- the **absence of relevant disanalogies** — differences that bear on the
  conclusion.

Weak analogy is a common dressed-up fallacy: "Running a company is like commanding
an army, so the CEO should never be questioned" — the shared feature (hierarchy)
is irrelevant to the inferred one (immunity from challenge).

## Hypothesis

A conjectured explanation, tested by its consequences. A hypothesis earns
confidence when it:

- **explains** the known facts without special pleading;
- makes a **testable prediction** that could fail;
- **survives** attempts to falsify it;
- is **simpler** than rivals of equal explanatory reach (do not multiply
  assumptions past necessity).

Confirming a prediction *raises* confidence but never proves the hypothesis —
another explanation may fit the same evidence (this is affirming the consequent
at the level of theory; see [formal validity](formal-validity.md)). A hypothesis
that forbids nothing explains nothing.

## Connects to

- **[Second-Order Thinking](../references/second-order-thinking.md)** — trace the
  downstream consequences a causal claim implies, then check whether they occur.
- **[Connection Circles](../references/connection-circles.md)** — map the feedback
  and confounders a single Mill's-method probe cannot capture.
- **[Fermi Estimation](../references/fermi-estimation.md)** — sanity-check whether
  a generalization's implied magnitudes are even plausible.
