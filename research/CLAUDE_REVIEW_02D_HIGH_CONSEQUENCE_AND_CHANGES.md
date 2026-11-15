# Claude review 02D: High-consequence autonomy, minimum changes and open disagreements

**Status:** Advisory peer review (Claude, 2026-11-15). Not canonical. Governance-level only. Labels: V / S / I / H / U.

## 1. Governance of high-consequence autonomy (I, H)

Each line below is a requirement on the governance arrangement, mapped to existing terms.

| Requirement | Existing term | What to add or test |
|---|---|---|
| Legitimate authority | *Delegated Authority* resolving to an identifiable role | For dual-use and defensive testing, the mandate must be a **verifiable record** (scope, validity, issuer), not merely an assertion by the requester |
| Proportionality | *Consequential*, *Material* | Autonomy granted in proportion to consequence and reversibility. Irreversible actions need a separate *Decision* |
| Independent enforcement | ARCHITECTURE: "AI is evidence, not authority" | Enforcement, clock and approval must sit **outside the acting agent** ([02A](./CLAUDE_REVIEW_02A_CONCEPTUAL_INTEGRITY.md) P2–P4) |
| Oversight | *Delegated Authority* (oversight) | Measured by error detection (S9), not by approval counts |
| Revocation | *Delegated Authority* (revocation criteria) | Must propagate to derived work. Committed effects need compensation semantics (02B W7) |
| Interruption | Not explicit | A **stop path** that works independently of the agent and is rehearsed. Graceful stop and recovery (S12) |
| Emergency boundaries | *Constraint* | Define in advance which constraints may never be relaxed, even in an emergency. Safety functions are an example (01D) |
| Controlled evaluation | Protocol boundaries | **Isolation is a claim that needs evidence**: verify egress restrictions and independent monitoring before evaluating, and account for third parties who would bear the risk if isolation failed |

**Dual-use (I).** Refusal policies set by a model provider differ from the authorisation of an action. The first is the provider's risk choice; the second is the mandate holder's legitimate *Decision*. Neither substitutes for the other, and both should be recorded separately as *Evidence*.

## 2. Recommended minimum change set before v2 (research documents only, no canonical change)

| # | Change | Where | Priority |
|---|---|---|---|
| M1 | Decide and document per-action versus cumulative delegate limits; default to cumulative | Protocol; fixture | High |
| M2 | Move clock, approval issuance and the consequence classification outside the requester | Fixture; Protocol §Conditions | High |
| M3 | Add C3-alloc (pre-allocated, attenuated budgets) as a decentralised comparator | Protocol §Conditions | High |
| M4 | Implement C2 and C2b with shared budget state before any H0 claim | Fixture | High |
| M5 | Add a two-organisation scenario with no shared ledger | Protocol §Scenarios | Medium |
| M6 | Add endpoints for privacy cost and burden on employees | Protocol §Endpoints | Medium |
| M7 | Specify revocation of committed effects (compensation) | Protocol S12 | Medium |
| M8 | Add the atomic fixture to the repository before referring to its 27 tests | Handover | Low |
| M9 | Phrase the three candidate Framework Findings as gaps in *Delegated Authority* and *Constraint*, not as new primitives | Synthesis 02 | Medium |

## 3. Unresolved disagreements and evidence gaps

1. **Central versus allocated** cumulative control. Synthesis 02 leaves it open; I expect allocation to be sufficient in most cases (H). There is no data either way (U).
2. **Whether "agreements" need a new primitive.** I hold that typed *Relationship* is probably sufficient (H, HC3); the Devoteam intake implies otherwise.
3. **Value of human approval (C4)** in practice. It may fail through rubber-stamping (S, literature). Untested here (U).
4. **Bankdata slide 03 / vendor incidents.** The primary source was still not read by either reviewer (U).
5. **Transcript fidelity.** One shared machine transcript; no audio check yet (U).
6. **The atomic fixture** was not available for review (U).
7. **External equivalents** (capability attenuation, token exchange) are cited from reviewer knowledge and were not re-verified this session (S/I).

## 4. What reality would need to show for v2 to be justified

C3 or C3-alloc beats a hygiene-hardened C2 and a capability-based C2b on held-out, independently designed scenarios:
- with fewer mission-level violations;
- at a noninferior completion rate and acceptable false refusals;
- without a privacy or labour burden that fails review.

Short of that, the evidence justifies **refinements to *Delegated Authority* and *Constraint*** and not a new architecture.
