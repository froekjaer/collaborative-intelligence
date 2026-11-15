# Cross-model review 01 — Experiment 01 v2

**Status:** Advisory research integration; NOT canonical, NOT efficacy evidence. 2026-11-15.  
**Baseline:** main branch; Claude review 02 in open PR #12 (not merged).  
**Reviewers:** Claude (repository/code inspection + four executed probes, reviewer-reported); Gemini (methodological proposal, explicitly no live source/repository access); DeepSeek (inspection of locally supplied atomic Python files, explicitly no execution); ChatGPT (independent local execution of baseline tests and F-05 reproduction, 2026-11-15).

## Evidence discipline

- **EXEC:** Executed in local Python runtime, with test command/result described below.
- **CODE:** Verified by reading the supplied fixture source; no execution implied.
- **REVIEW:** External reviewer claim, not independently established.
- **DESIGN:** Documented limitation or unresolved semantic choice.
- **UNVERIFIED:** Literature, sample-size, performance or security claims not source-checked.

Agreement among AI reviewers is **not** independent empirical replication. No live agents, real payments, external systems or production targets were tested. Do not merge normative changes based on this report.

## Evidence and findings register

| ID | Claim | Status | Decision / next test |
|---|---|---|---|
| D-01 / DeepSeek F-05 | `setup()` is partially committed on duplicate grant when `isolation_level=None`; `with connection:` does not open a transaction | **EXEC confirmed** | Fix with explicit `BEGIN IMMEDIATE` and rollback; add failure-injection regression |
| D-02 / Claude P1 | In-memory policy delegate `limit` is per-request, not cumulative per delegate | **REVIEW** (Claude reports executed probe) | Define per-action vs cumulative grant semantics; test on both fixtures |
| D-03 / Claude P2 | Requester-provided timestamp controls expiry | **CODE** (atomic `submit(timestamp)`) | Introduce trusted clock/decision time outside acting agent |
| D-04 / Claude P3/P4 | Approval is requester-supplied, and old policy caller chooses whether approval required | **REVIEW/CODE** | Policy-owned approval requirement and independent issuer; test invalid, stale and unauthorized approvals |
| D-05 / DeepSeek F-09–12 | Shared HMAC proves knowledge of a test secret, not approver identity, mandate, expiry or rotation | **CODE / DESIGN** | Maintain fixture-only warning; design authenticated issuer, approval scope/expiry and recovery before production |
| D-06 / DeepSeek F-13–15 | `requests` lacks full request payload, authorization snapshot, ordered events and setup/revocation events | **CODE / DESIGN** | Define minimal privacy-preserving, reconstructable audit event schema |
| D-07 / DeepSeek F-01 | Pairwise delegation attenuation allegedly fails to enforce transitivity | **NOT SUBSTANTIATED** | Pairwise `child <= parent` at every traversed link implies transitive `descendant <= ancestor`; equality is allowed unless policy says otherwise. Test actual counterexample, not equality alone |
| D-08 / DeepSeek F-03 | Revocation allegedly bypassable by descendant | **NOT SUBSTANTIATED** | Traversal checks revoked ancestors; distinguish logical propagation from materialized flags; add tests for B and C and broken chains |
| D-09 / DeepSeek F-02 | `setup()` accepts invalid/cyclic grants and fails late | **CODE** | Validate graph at setup; decide whether deliberate malformed-graph tests require separate fixture API |
| D-10 / DeepSeek F-06–08 | Rollback masking, lock contention and unbounded request growth | **DESIGN / PARTLY CODE** | Test rollback behavior, define retry/retention for any operational design |
| D-11 / Gemini | Six-arm study, 180 tasks, 48 humans and statistical power numbers | **UNVERIFIED** | Treat as candidate design only; pilot, clustering and independent power calculation before preregistration |
| D-12 / Gemini | External benchmark and literature claims (AgentDojo, CaMeL, etc.) | **UNVERIFIED in Gemini review** | Check primary papers, benchmark versions, license and fidelity before comparison |
| D-13 / Claude | Central ledger vs C3-alloc pre-allocated, attenuated budgets | **DESIGN** | Add distributed/offline comparator with partition, double-spend, revocation and reallocation tests |
| D-14 / Claude/Gemini | Human approval may rubber-stamp; delayed skill retention matters | **HYPOTHESIS** | Measure seeded-error detection, false approvals, burden, and unassisted delayed performance |
| D-15 / Gemini | k>=15 suffices for privacy-preserving declassification | **UNSUPPORTED** | A cell-size threshold alone does not rule out differencing or linkage attacks |
| D-16 / Gemini | Publication of all raw telemetry | **UNSAFE AS GENERAL RULE** | Publish synthetic/minimized data only after privacy, confidentiality and security review |

## Independent execution record (ChatGPT)

Environment: Python stdlib `unittest`, local copies of `experiment01_v2_policy.py`, `test_experiment01_v2_policy.py`, `experiment01_v2_atomic.py`, `test_experiment01_v2_atomic.py`. Executed:

```sh
cd /mnt/data/mf_v2
python -m unittest -q
# Ran 27 tests ... OK
```

Reproduced F-05 by opening a fresh SQLite database and calling:
```python
p.setup('m', 100, [('A', None, 100, 100), ('A', 'B', 50, 50)])
```
Second grant raised `IntegrityError`, while `missions` retained `('m',100,0)` and `grants` retained the first A row. This establishes partial setup, not general production exploitability. The existing 27 tests do not cover this failure.

## Minimum change sequence and gates

1. Fix atomic setup; add regression and trusted state transitions; publish code and tests for external reproduction.
2. Resolve grant limit scope, approval authority, trusted clock, and consequence classification **before** efficacy claims.
3. Implement strong C2 and C2b comparators with equivalent stateful budgets; add C3-alloc and cross-organization scenarios.
4. Define audit/event privacy, revocation of committed effects, offline/degraded modes, and third-party impacts.
5. Verify literature and benchmarks; run pilot and independent power calculation; preregister held-out evaluation.
6. Compare empirical results against the ordinary-controls null. Reject new primitives/architecture if established controls suffice.

**Governance:** Keep Claude PR #12 open until its findings and this register are reconciled. No automatic merge of PR #12, no canonical Mission Framework changes, and no claim that Experiment 01 v2 has been empirically validated.
