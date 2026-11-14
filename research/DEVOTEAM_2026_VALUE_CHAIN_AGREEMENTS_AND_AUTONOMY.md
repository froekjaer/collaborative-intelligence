# Devoteam research intake — cross-organisational agreements, value-chain consequences and accountable autonomy

**Status:** Preliminary document analysis, 2026-11-15. Source is presentation material, not a verified transcript of the event. **Publication classification:** Derived thematic synthesis; do not publish attendee statements, private meeting content, speaker-identifying quotes or sensitive organisational examples without separate permission and source review.

## Research framing

Read alongside [Bankdata agent-control cases](./BANKDATA_2026_AGENT_CONTROL_AND_AGREEMENT_CASES.md) and [ISC research memo](./ISC_CPH_2026_RESEARCH_MEMO_01.md). This source contributes a **value-system and inter-organisational** lens to autonomous AI: agreements can bind not only two counterparties but also the critical delivery obligations and dependencies of downstream parties.

## Material inspected

- `Devoteam_30min_Clear_English_EN(1).pptx` — 30-minute presentation, slides on PESTEL, value chains, risk, supply-chain incident, societal impact and GRC.
- `Devoteam_Peter_Froekjaer_Value_Chains_EN_v3.pptx` — extended version with explanatory speaker notes and a proposed value-chain interface record.

The existence of slides and notes does **not** establish what was said at the event, what participants agreed, or that any AI-to-AI violation occurred.

## Source-grounded observations

| Source locus | Source theme | Research interpretation |
|---|---|---|
| Short deck slide 6 | Linked value chains n−1, n and n+1; supplier inputs, business output, downstream essential services; risk must be traced in both directions. | A bilateral agent agreement may create externalities for uninvolved parties. Test cumulative and downstream constraints. |
| Short deck slide 5 | Political, economic, social, technological, environmental and legal pressures alter dependencies, costs and business decisions. | Agreements require context, change monitoring and validity periods; local optimisation is insufficient. |
| Short deck slide 11 | A reported Polish incident crossed organisational boundaries through shared connectivity; a follow-up CERT Polska source is cited. | Shared technical infrastructure may propagate risk across separate contractual entities. Verify primary incident source before publishing detailed claims. |
| Extended deck slide 18 | Risk owner, controls, residual risk, authority, evidence and review triggers are linked; speaker notes distinguish risk acceptance from non-waivable safety, quality and legal requirements. | An agent cannot infer authority to waive mandatory obligations merely because it can optimise cost or obtain local approval. |
| Extended deck slide 19 | Business-process context connects critical outcome, people/process/services and specific IT/OT elements; trace impact upward and dependencies downward. | Represent causal path from agent action to business process, contractual handover and societal consequence. |
| Extended deck appendix slide 24 | Proposed interface record: provider activity/output; recipient purpose; quantity/quality/timing/acceptance evidence; disruption and alternatives; owners, decisions, last verification and open assumptions. | Candidate schema for *agent-to-agent and organisation-to-organisation commitments*, subject to semantic review. |

## Research propositions (not verified findings)

**P1 — Contractual compliance is relational.** A task can be completed and an agent's local KPI improved while an upstream or downstream obligation is breached.

**P2 — Delegation does not extinguish obligations.** Outsourcing an action to another AI or service cannot confer authority to ignore quality, privacy, safety, timing or mandatory legal constraints.

**P3 — Acceptance requires evidence.** An AI agent's assertion that a deliverable meets requirements is insufficient if acceptance criteria, provenance and actual operational effects are not independently checked.

**P4 — Inter-agent agreements need lifecycle semantics.** Identity, authority, parties, purpose, scope, data permissions, deliverables, acceptance criteria, time bounds, change control, non-waivable constraints, escalation, termination, revocation and remediation.

**P5 — Risk is not exhausted by direct counterparties.** A locally acceptable arrangement can create unacceptable correlated or cascading consequences across multiple value chains.

## Proposed controlled experiments

1. **Local success/global failure:** Three simulated agents each satisfy their own SLA while the end-to-end essential-service deadline fails. Compare local versus cross-chain acceptance checks.
2. **Forbidden delegation:** Agent A cannot disclose a dataset, but attempts to delegate processing to B; test independent enforcement at every data egress boundary.
3. **Contract mutation:** Two agents renegotiate price/timing, unintentionally violating a downstream quality or safety requirement; test policy precedence and human escalation.
4. **Hidden dependencies:** An AI recommends a cheaper supplier whose shared infrastructure introduces a common-mode failure; test whether value-chain provenance changes the decision.
5. **Agreement recovery:** An agent detects that a commitment is infeasible; test whether it reports, proposes an authorised amendment and degrades gracefully rather than silently breaching terms.

All scenarios should be run in permissioned, simulated environments. No unauthorised production testing.

## Chatham House Rule and research publication

Apply Chatham House Rule to the relevant conference or meeting discussions **where agreed**. Participants may generally use the information received but must not reveal the identity or affiliation of speakers or other participants. A published presentation's byline is not automatically confidential, but that does not license attribution of private discussion or imply the presentation is public-domain. For research outputs:
- Prefer abstract themes and anonymised, non-identifying paraphrase.
- Do not reproduce private meeting audio, participant comments, attendee lists or organisationally sensitive facts in public repositories.
- Avoid unique timestamps/circumstances that would re-identify private contributors.
- Use public primary sources for externally verifiable incidents and regulation.
- Keep confidential raw material in access-controlled storage and public research products free of unnecessary identifying details.
- Mark unresolved permissions and source provenance explicitly.

## Relationship to Mission Framework

Review existing mission/decision/action, policy, actor authority, evidence and risk semantics before adding a new agreement primitive. If gaps are confirmed, raise a Framework Finding under the existing admission process. This intake is research, **not a canonical schema or compliance assessment**.

**Next step:** Cross-corpus comparison of Bankdata (control circumvention and proxy metrics), Devoteam (contractual/value-chain externalities) and ISC (operational human authority and resilience), with explicit evidence grades and rival hypotheses.
