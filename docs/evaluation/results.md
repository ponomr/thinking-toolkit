# Routing optimization observations

Baseline: f90c7748c70ca17639467e95c1255a141521a0c6 (1.1.1).
Candidate: this branch's 1.2.0 development payload; no release or installation
into user agents is implied.

## Instruction footprint

Run `python3 scripts/measure_context.py` from the repository. Counts include
entry, required routing files and the applied card or logic references. Words
are whitespace-delimited; reads are logical file reads, not physical I/O.
They exclude output, reasoning, retries, cache behavior and provider overhead.
These numbers do not measure total tokens, money or latency.

| Route | Before words | After words | Reduction | Logical reads |
| --- | ---: | ---: | ---: | --- |
| Issue Trees (named) | 3162 | 1424 | 55.0% | 3 -> 3 |
| Issue Trees (automatic) | 3162 | 1506 | 52.4% | 3 -> 4 |
| Connection Circles (automatic) | 3179 | 1403 | 55.9% | 3 -> 4 |
| Minto Pyramid (automatic) | 3186 | 1348 | 57.7% | 3 -> 4 |
| /logic with formal-validity.md (logic) | 3761 | 3242 | 13.8% | 4 -> 4 |

All 31 cards and all four logic files match the frozen baseline SHA-256 hashes.
The entry is smaller and automatic selection reads one category instead of the
entire catalog. Automatic selection adds a file read; the two-method scenario
used six candidate reads versus four baseline reads. A workload dominated by
read overhead may therefore behave differently. No tokenizer or paid model API
was used. Full route counts are in [footprint.json](footprint.json), with frozen
file counts and hashes in [baseline-files.json](baseline-files.json).

## Behavioral smoke comparison

The same 12 [cases and acceptance criteria](routing-cases.json) were supplied to
two separate worker contexts using the inherited primary model. One read only
the frozen old payload; the other read only the candidate. Each generated actual
answers and recorded selected models and files read. A third context saw only
randomized A/B answer pairs, prompts and acceptance criteria. It did not receive
the mapping or the source payloads. This is a same-family blinded smoke check,
not a cross-provider experiment or an independently replicated benchmark.

Both arms passed the acceptance criteria on all 12 cases. The judge preferred
the old answer in three cases, the new answer in one, and tied eight. The old
answers had more explicit Issue Trees leaf tests, a closer minimal logic rewrite,
and a more usable incomplete vendor matrix. The new prioritization answer was
clearer about the optional meeting's urgency. The judge classified these as
preferences without material defects. This does not establish equivalent quality
across unseen tasks. Card compression and additional model cards were deferred.

Artifacts: [old answers](old-answers.json), [new answers](new-answers.json),
[blind packets](blind-packets.json), [mapping](blind-key.json),
[scores](blind-scores.json), [old limitations](old-limitations.txt), and
[new limitations](new-limitations.txt).

Three additional manual-use requests supplied only SKILL.md. All requested the
exact next file (index, selector, or logic overview), with no claim of applying
unread instructions: [packet](manual-packet.txt), [answers](manual-answers.json).

Limitations: one answer per scenario; cases within each worker shared context;
no independent fresh model invocation per case; same-family judge; no provider
usage counters, cache measurements, wall-clock model latency, statistical power
or cross-provider replication. The next evidence needed for a total-spend claim
is repeated isolated old/new runs with usage and latency recorded by the owner
on their chosen provider. No fixed savings target is claimed.

## Distribution and verification

A new clean-install test exposed an existing shell exit-status bug: copying
succeeded but a missing rollback-backup message left the function returning 1.
An explicit successful return fixes that case. The test executes the real
installer and compares copied payload bytes, including nested routing guides.
The update test uses a local release-service double and checks installed bytes
and rollback; it does not attest a published release's verification.

Final repository checks are recorded in the PR after the complete local gate.
The preservation map is [contract-preservation.md](contract-preservation.md).
