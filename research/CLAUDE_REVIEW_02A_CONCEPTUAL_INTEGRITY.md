# Claude review 02A: Conceptual integrity of the v2 candidate

**Status:** Advisory peer review (Claude, 2026-11-15), issue [#9](https://github.com/froekjaer/collaborative-intelligence/issues/9). Not canonical.
**Baseline:** collaborative-intelligence `fab97b5`; mission-framework `9a1a454` (`GLOSSARY.md`).
**Evidence labels:** **V** verified (by reading the repository or running code) · **S** source-reported claim · **I** inference · **H** hypothesis · **U** unknown.

## 1. Executive assessment of v2 readiness

- **V.** [Synthesis 02](./CROSS_CORPUS_SYNTHESIS_02_V2_READINESS.md) and [Experiment 01 v2](./EXPERIMENT_01_V2_PROTOCOL.md) have absorbed review 01: there are strong baselines (C2, C2b), held-out scenario design, seeded invalid approvals (S9), false refusals (S10) and an explicit null hypothesis (H0).
- **I.** The v2 candidate is **ready for architecture discussion, not for normative admission.** That is the documents' own assessment, and I agree with it.
- **V, I.** The candidate's only genuinely new claims are three semantic refinements to existing terms: delegation inheritance, cumulative Constraint accounting, and coverage of derived work. All three are **under-specified** in the reference fixture (§3).
- **I.** The largest readiness risk is not novelty. It is that **the fixture's semantics may be read as the intended semantics** before anyone has decided them.

## 2. Concept-by-concept comparison

| v2 candidate notion | Existing GLOSSARY term (V) | Established external equivalent (I) | Genuine gap? |
|---|---|---|---|
| "Authority" check | *Delegated Authority*: scope, permitted actions, validity period, conditions, oversight, revocation criteria, accountability path | Least privilege; capability security | No. Use the existing term |
| Delegation inheritance (A→B→C) | Not stated. *Delegated Authority* does not say whether a delegate may delegate further | Capability attenuation (object-capability systems); OAuth token exchange with narrowing scopes (RFC 8693) | **Yes, narrow:** whether onward delegation is allowed, and whether bounds must narrow monotonically |
| Cumulative constraint | *Constraint* (a limit on permitted states or actions) and *Mission* | A reference monitor holding cumulative state; quotas and budgets | **Partly.** The Constraint concept covers it; what is missing is how its consumption is *attributed* across actors |
| Derived-work coverage | *Action* ("under direct or delegated authority"); *Evidence* (append-only) | Distributed tracing; audit coverage | **Partly:** whether evidence obligations follow spawned work |
| Provenance check | *Provenance* (origin, producer, method, version, custody) | Information-flow control; taint tracking | No. The term exists. Applying it to *instructions* is a use of the term, not a new concept |
| Purpose check | *Mission*, *Objective* | GDPR purpose limitation | No. It is not machine-checkable, so operationalise it as scope |
| Evidence check | *Evidence*, *Verification status*, *Consequential* | Audit, non-repudiation | No |
| "Agreement" between agents (Devoteam intake) | *Decision* plus *Delegated Authority*; *Relationship* (typed, temporal, with its own provenance) | Contracts; SLAs; service-level objectives | **U.** First test whether a *Relationship* carrying a *Delegated Authority* already expresses it (see 02C) |

**Conclusion (I):** No new primitive is justified at present. Three candidate **Framework Findings** remain, framed as gaps in *Delegated Authority* and *Constraint*: re-delegation, attribution of cumulative consumption, and evidence coverage of derived work.

## 3. Semantic ambiguities shown by the reference fixture (V: code executed)

Each probe was run against `research/experiment01_v2_policy.py` at `fab97b5`. All 22 existing tests pass.

| # | Probe | Observed | Why it matters for semantics |
|---|---|---|---|
| P1 | Delegate B has `limit=10`; it makes ten requests of 10 | All 10 allowed; total spent 100 | `limit` is **per request**, not cumulative per delegate. Is a delegate's bound per action or per lifetime? The GLOSSARY does not say. **This is the central cumulative-constraint question** |
| P2 | B's grant expires at t=500; B supplies `timestamp=1` | Allowed | The **requester supplies the time**. Expiry is only meaningful if an independent clock decides it |
| P3 | `approval=True` is set by the requester itself | Allowed | Approval is **self-asserted**. S9 (seeded invalid approvals) cannot be measured validly until approval is issued by an independent party |
| P4 | Approval is needed only when the caller passes `require_approval=True` | Allowed without approval | **Whether approval is needed is decided by the caller**, not by policy bound to the action's consequence. In GLOSSARY terms, *Consequential* should decide it |

**I:** These are not bugs in a toy. They are the **exact open semantic decisions** v2 must make explicitly:
- who holds the clock;
- who issues approval;
- whether delegate bounds are per action or cumulative;
- whether policy, rather than the caller, classifies an action as consequential.

The handover already acknowledges that approval is a placeholder (V). It does not acknowledge P1, P2 or P4.

## 4. Recommended semantic decisions before v2 (H: to be tested)

1. Delegate limits carry an explicit `scope_of_limit: per_action | cumulative`. The default is **cumulative**, because a per-action bound is not a meaningful delegation bound.
2. Time and approval are **inputs from independent parties** (clock, approver), never fields supplied by the requester.
3. Whether approval is needed derives from policy plus the existing **Consequential** qualifier, not from the caller.
4. Onward delegation is **forbidden unless explicitly granted**, and any onward grant must narrow or equal its parent. The fixture already rejects widening (V), but it checks this only when a request is made, not when the grant is created.

*Next:* [02B weaknesses and alternatives](./CLAUDE_REVIEW_02B_WEAKNESSES_ALTERNATIVES.md).
