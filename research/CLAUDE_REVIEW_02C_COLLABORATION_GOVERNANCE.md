# Claude review 02C: Human–AI and AI–AI collaboration

**Status:** Advisory peer review (Claude, 2026-11-15). Not canonical. Labels: V / S / I / H / U.

## 1. Human–AI collaboration

**Opportunities (H).**
- AI as a *challenger*: it generates counterarguments and missing alternatives (preamble principle 7) rather than verdicts.
- AI preparing evidence so that human judgement is spent on the material choices.
- AI making expertise accessible across languages and disciplines.

**Risks (S, I).**
- **Automation bias.** People tend to over-accept recommendations. "Human oversight" requirements often fail in practice ([Green 2022](https://arxiv.org/abs/2109.05067), S).
- **Deskilling.** Immediate throughput can rise while delayed unassisted skill falls. The ISC material raised this, and Protocol H5 tests it.
- **Manipulation by framing.** A system that explains persuasively can *increase* deference, so a better explanation is not automatically better oversight (I).
- **Responsibility gaps.** A human approves something they could not evaluate, and accountability becomes nominal.

**Design implications (H).**
1. Measure oversight by **detection of seeded errors** (S9), not by whether approval took place.
2. Treat **disagreement rate** as a health signal: a human who never overrides is not overseeing.
3. Schedule **unassisted practice** in high-consequence roles; this is the OT parallel in 01D.
4. The **human contributes purpose, context and legitimacy**; the AI contributes breadth and challenge. This is already the preamble's collaboration model (V), so no new term is needed.

**Missing perspectives (I).**
- **Labour.** Monitoring of AI use is also monitoring of employees; in Denmark, cooperation committees (samarbejdsudvalg) and GDPR Art. 88 apply.
- **Small organisations.** Many controls assume specialist staff.
- **Accessibility.** Safeguards that depend on user vigilance burden people with impairments.
- **Language.** Protection may be weaker in Danish than in English (S, recording 5; untested).
- **International.** Accountability norms differ between jurisdictions.

## 2. AI–AI collaboration: what counts as an "agreement"?

| Interaction | What it is | GLOSSARY mapping | Is it an agreement? |
|---|---|---|---|
| API call or tool execution | One component invokes a capability | *Service*, *Action* | No |
| Workflow orchestration | A planner sequences steps that others execute | *Workflow* | No. Authority stays with the orchestrator's principal |
| Delegation | A hands bounded authority to B | *Delegated Authority* | No. It is a grant, not a mutual commitment |
| **Agreement** | Two or more parties, **each with its own accountable authority**, make reciprocal commitments with acceptance criteria and remedies | *Decision* by each party + *Relationship* (typed, temporal, with provenance) + *Constraint* | **Yes**, and only when both sides have independent principals |

**I:** Most "agent agreements" in current discourse are orchestration or delegation within a single principal's authority. A genuine **inter-organisational agreement** requires each side's commitment to resolve to its own accountable role (the GLOSSARY requirement for *Delegated Authority*).

**Candidate semantic gap (H):** A *Relationship* whose type is "commitment". It would need parties, reciprocal obligations, acceptance evidence, validity interval and termination. First test whether the existing *Relationship* definition (identity, provenance, status, validity interval) already covers it. If it does, the gap is only a typing convention, not a primitive.

## 3. Coordination across organisations (H)

- **Evidence exchange.** Each party keeps its own append-only *Evidence*. What is exchanged are references and integrity proofs, not raw data.
- **Change negotiation.** An agent may *propose* an amendment. Adopting it is a *Decision* by each party's accountable authority, or by a delegate whose grant explicitly includes amendment authority with bounds.
- **Obligation management.** Cumulative constraints are allocated to each party in advance (C3-alloc, [02B](./CLAUDE_REVIEW_02B_WEAKNESSES_ALTERNATIVES.md)), so that no party has to trust another party's ledger.
- **Failure mode to test.** Agents coordinating through channels that no one designed as communication channels, such as shared storage. The declared agreement then misses the actual coordination. Monitoring should therefore cover shared resources, not only declared interfaces (I).

## 4. Falsifiable hypotheses

- **HC1.** In a two-organisation synthetic task, pre-allocated attenuated budgets (C3-alloc) achieve the same constraint satisfaction as a shared ledger, without either party running the other's infrastructure.
- **HC2.** A human rejection rate of seeded errors at or below the human-only baseline indicates rubber-stamping. Reject C4's oversight claim if this holds.
- **HC3.** Typed *Relationship* records are enough to represent amendments and terminations of multi-party commitments without a new primitive. Falsified if a preregistered set of contract-lifecycle events cannot be represented.

*Next:* [02D high-consequence governance and the minimum change set](./CLAUDE_REVIEW_02D_HIGH_CONSEQUENCE_AND_CHANGES.md).
