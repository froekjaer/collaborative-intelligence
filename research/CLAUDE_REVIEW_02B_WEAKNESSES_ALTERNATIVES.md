# Claude review 02B: Weaknesses, alternatives and falsification

**Status:** Advisory peer review (Claude, 2026-11-15). Not canonical. Labels: V / S / I / H / U, as in [02A](./CLAUDE_REVIEW_02A_CONCEPTUAL_INTEGRITY.md).

## 1. Severity-ranked weaknesses and contradictions

| # | Severity | Weakness | Location | Label |
|---|---|---|---|---|
| W1 | High | **Central ledger as the architecture by default.** The fixture keeps one in-memory `spent` counter. Synthesis 02 says distributed and central designs "must be compared", but no distributed variant exists, so C3 is in practice the central option | `experiment01_v2_policy.py`; Synthesis 02 §Research architecture | V |
| W2 | High | **Approval, clock and consequence are supplied by the requester** (02A §3, P2–P4). Until fixed, results for H3 and S9 would not be valid | `experiment01_v2_policy.py` | V |
| W3 | High | **Delegate bounds are per action** (P1). S2 and S7 can pass while delegates overspend their intended share | same | V |
| W4 | Medium | **C2 and C2b are not yet implemented.** The smoke fixture's C2-like comparator deliberately leaves out shared budget state, so it cannot test H0. The handover says so | `experiment01_v2_smoke.py`; `HANDOVER_LOG.md` | V |
| W5 | Medium | **No cross-organisation case.** All delegation stays in one ledger owned by one party, but the programme's motivating cases (Devoteam value chains) involve several parties with no shared enforcement point | Protocol, scenarios S1–S12 | V, I |
| W6 | Medium | **Evidence completeness versus privacy.** Synthesis 02 records this conflict, but no endpoint measures privacy cost, such as the amount of personal data retained per action | Protocol, endpoints | V |
| W7 | Medium | **Revocation is evaluated only at request time.** Actions already committed under a later-revoked grant are not addressed: no compensation or rollback semantics | Fixture; S12 | V, I |
| W8 | Low | **The handover reports 27 tests including an atomic fixture that is not in the repository.** It cannot be reviewed here | `HANDOVER_LOG.md` top entry | V (file absent), U (contents) |

## 2. When established controls are probably sufficient (I, H)

- **A single organisation with a single budget owner.** A shared budget counter in the existing payment or approval system, plus least privilege, probably achieves what C3 does. Testing H0 should start here.
- **Low-consequence, reversible actions.** Audit and after-the-fact correction can be cheaper than prevention. The GLOSSARY *Consequential* qualifier already gives a basis for treating them differently.
- **Short delegation chains with human principals.** Ordinary role-based access control and four-eyes approval are mature, legally understood and auditable.
- **OT.** Here the existing safety engineering (safety functions, segmentation, one-way data paths) should take precedence over any agent-level orchestration ([01D](./CLAUDE_REVIEW_01D_OT_RESILIENCE_AND_PEOPLE.md)).

## 3. Costs of mission-level orchestration (I, H)

| Risk | Mechanism | Mitigation to evaluate |
|---|---|---|
| Single point of failure | If the cumulative ledger is down, work stops, or it fails open | Fail-closed default, with explicit degraded modes (pre-allocated local budgets) |
| Latency | Every consequential action needs a round trip to the ledger | Measure it, and compare with pre-allocated budgets |
| Surveillance | One component sees all actions by all actors | Data minimisation; aggregate-only accounting |
| Power concentration | Whoever runs the ledger controls everyone's autonomy | Separate accounting from decision authority; make governance of the ledger explicit |
| Cross-organisation infeasibility | No party accepts another party's ledger | **Pre-allocated, attenuated budgets** that each party enforces locally (H) |

**H-ALT (alternative architecture to test):** *Allocate, don't centralise.* The accountable authority splits a mission Constraint into non-overlapping per-delegate allocations when it delegates. Each delegate then enforces its allocation locally, and onward delegation can only subdivide it. This needs no central round trip and may be enough for S2, S7 and S11. It is weaker where allocations must be rebalanced at runtime. Add it as condition **C3-alloc** alongside the central C3.

## 4. Falsification: evidence that v2 is unnecessary, ineffective or harmful

| v2 is shown to be… | …if (preregistered) | Label |
|---|---|---|
| Unnecessary | C2 or C2b with a shared budget counter matches C3 on violations, completion and false refusals, within the noninferiority margin | H |
| Unnecessary | C3-alloc matches central C3 at lower latency and with no single point of failure | H |
| Ineffective | Mission-level violations under C3 are not significantly lower than under C2b on held-out scenarios written by independent designers | H |
| Ineffective | Under seeded invalid proposals (S9), approval error in C4 is not lower than in C3 without approval | H |
| Harmful | C3 or C4 raises false refusals or abandonment above a preregistered threshold, or shifts burden onto employees or third parties | H |
| Harmful | The evidence coverage required for S8 needs retention of personal data that fails a privacy review | H |

**I:** A negative result on any "unnecessary" row should lead to **recommending established controls**, not to refining v2 until it wins.

*Next:* [02C collaboration and governance](./CLAUDE_REVIEW_02C_COLLABORATION_GOVERNANCE.md).
