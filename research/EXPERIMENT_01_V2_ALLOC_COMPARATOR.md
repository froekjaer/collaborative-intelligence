# Experiment 01 v2 — C3-alloc comparator and evaluation gate

**Status:** Synthetic, unvalidated design candidate. 2026-11-15. No live agent or operational authorization.

## What is compared

- **C2:** Mature conventional enforcement, including a shared stateful budget counter, RBAC, allowlists and independently enforced policy.
- **C2b:** Capability/provenance enforcement **with equally strong cumulative-state controls where appropriate**. Do not intentionally weaken C2b by removing counters.
- **C3-central:** Same foundation plus mission-wide accounting, delegation inheritance and derived-work audit.
- **C3-alloc:** An accountable issuer partitions a fixed mission budget into disjoint allocations, which delegates may subdivide but never exceed. Spending uses local transactional state, with no central per-action round trip.
- **C4:** Human decision interface layered on the best eligible technical condition; compare independently.

The new `experiment01_v2_alloc.py` is **one-file SQLite bookkeeping**, not a genuine distributed implementation. Its root issuer and all accounts currently reside in the same database. It tests conservation and subdivision semantics, **not** network partitions, cross-organizational trust, secure issuance or offline synchronization.

## Core invariant

For every account, `spent + delegated <= allocated`. For a tree rooted in a fixed mission cap, each child allocation reduces the parent's available amount. Assuming non-clonable allocations, authenticated issuers and atomic persistent writes, aggregate spending cannot exceed the root cap. These assumptions are **not** guaranteed by this fixture.

### Counterexamples to test before making claims

1. **Allocation cloning / DB rollback:** Copy a delegate's local ledger, spend on both copies, and exceed the original allocation. Without anti-rollback hardware, online reconciliation, one-time vouchers or equivalent, offline allocation does not prevent this.
2. **Revocation while disconnected:** A revoked parent cannot immediately stop a disconnected child. Model bounded lease expiry and residual exposure explicitly.
3. **Crash after external action before local commit:** A tool action succeeds but the local ledger transaction fails. Requires action idempotency, transactional outbox or compensation.
4. **Unused budget stranded:** One delegate exhausts allocation while another has unused capacity; compare authorized reallocation protocols and recovery time.
5. **Issuer split-brain:** Two issuers allocate the same parent balance concurrently. A local SQLite lock only protects one shared file, not independently operating issuers.
6. **Compromised child identity:** Local accounting does not establish actor authenticity or the legitimacy of approval.
7. **Privacy:** Central ledger can reveal full activity; allocation receipts can reveal delegation relationships. Measure information exposure for both.

## Fair experimental sequence

**Gate A — contract correctness:** all reference implementations pass common tests for budget conservation, replay, delegation, expiry, revocation and crash recovery. Compare same requirements; explicitly mark unavailable guarantees.

**Gate B — baseline parity:** independent reviewer confirms that C2/C2b receive comparable engineering effort and controls; measure maintenance complexity and local repair alternatives.

**Gate C — synthetic workloads:** fixed scenarios with both benign edge cases and cumulative abuse; independent deterministic environment-state scoring. No actual attacks or real infrastructure.

**Gate D — distributed simulation:** controlled partitions, delayed revocations, issuer failures and rollback attempts. Distinguish *fail-closed safety* from *availability*.

**Gate E — preregistration:** pilot-derived effect sizes, power analysis accounting for task clustering, sealed held-out cases and precommitted stopping rules.

**Gate F — human factors:** qualified participants, meaningful consent, independent assessment of seeded-error detection and delayed unassisted skills. Human studies require separate ethics/privacy assessment.

## Research decision

C3-alloc is a comparator, **not the preferred architecture**. If C2b or a simpler conventional shared counter matches C3 on violations and valid task completion with lower burden, the Mission Framework-specific architectural superiority hypothesis fails. A negative result must remain publishable.

## Dependencies and propagation

- Research protocol: `EXPERIMENT_01_V2_PROTOCOL.md` should incorporate C3-alloc only after a reviewer confirms comparison conditions.
- `CROSS_MODEL_REVIEW_01.md`: evidence register is advisory and may need updated statuses after tests.
- Claude PR #12 remains separate and open.
- No changes to `froekjaer/mission-framework`, Mission-Platform, Publication-Pipeline, Timelapse Pro, mission-resilience or waterworks-pro are justified yet.
- **Unresolved cross-repository propagation:** canonical glossary/Framework Findings review is deferred pending empirical results; track in research handover and later create an authorized Finding if a generic principle is validated.

## Reproduction

```sh
cd research
python -m unittest -v test_experiment01_v2_alloc
python -m unittest -v test_experiment01_v2_atomic
```

The C3-alloc code and tests were added to GitHub through the connector; **the new tests have not been executed in the local container in this session** because GitHub raw-file retrieval from that container was unavailable. The previous 29 atomic/in-memory tests were executed successfully. The draft PR must not be represented as fully verified until the new tests run in CI or an independent environment.
