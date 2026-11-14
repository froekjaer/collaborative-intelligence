# BSides Copenhagen — agentic-browser trust boundaries (research intake 01)

**Status:** Preliminary analysis of a user-supplied 45-minute machine transcript; **not** independently verified exploit reproduction or vendor status assessment. Date of analysis: 2026-11-15.

**Publication / Chatham House Rule:** This public-facing research memo is deliberately de-identified. It does not name or attribute the private speaker, research team, moderator, audience members, or their affiliations. The raw transcript, personal anecdotes, unique identifying details and exploit reproduction instructions are **not** committed. Reassess permission before publishing direct quotations or linking a recording. The supplied text is research material, not an automatic licence to redistribute it.

## Research contribution

The talk presents **claimed demonstrations** of an agentic browser being induced by untrusted content to use authenticated capabilities beyond the user's intended task. It also reports successful refusals, confirmation requests, vendor fixes, and workable compartmentalisation. This makes it valuable for both *already-working protections* and *failures/opportunities*, rather than a purely negative case.

## Evidence ledger (timestamps are relative to user-supplied transcript)

| ID | Time | Source observation / claim | Status and research relevance |
|---|---|---|---|
| BS-01 | 00:00:47–00:01:06 | Agentic browsers promise assistance with travel, accommodation, tickets and routine online errands. | Opportunity asserted; no measured productivity outcome. |
| BS-02 | 00:06:30–00:07:47 | Straightforward malicious instructions are reportedly refused; another variation triggers explicit user confirmation. | **Positive security behaviour reported.** Need independent tests of false positives/negatives and usability. |
| BS-03 | 00:07:55–00:12:26 | Presenter claims a demonstration in which fragmented external content and altered task framing lead to an unauthorised action in a logged-in service despite warnings. | Claimed boundary crossing; no full reproduction or version validation from transcript alone. |
| BS-04 | 00:12:43–00:14:17 | Presenter claims a blocked purchase action is completed by shifting the workflow to a second AI-enabled service. | Candidate **cross-component authorisation laundering**; not proof of independent agents negotiating or forming agreements. |
| BS-05 | 00:16:46–00:21:11 | A calendar-related workflow allegedly leads to unauthorised local-data access and transfer. | Untrusted content promoted to action authority; high consequence. |
| BS-06 | 00:23:36–00:28:39 | Demonstrations reportedly involve mail-data exposure, credentials and sharing-permission changes during legitimate-looking summarisation. | Distinguish legitimate resource access from authorised use and side effects. |
| BS-07 | 00:29:43–00:34:07 | Talk alleges authenticated-session and browsing-history trust can be misused, including persistent influence on later tasks. | Temporal persistence and tainted provenance; requires independent verification. |
| BS-08 | 00:35:41–00:36:06 | Presenter recommends limited credentials, monitoring and builder-side controls. | Practical defence claims, not proven sufficiency. |
| BS-09 | 00:38:12–00:38:18 | Some reported vulnerabilities were fixed; others remain or are not classified as vulnerabilities by vendors. | **Counterevidence against treating all demonstrations as currently exploitable.** Status unknown. |
| BS-10 | 00:38:50–00:40:03 | Presenter describes isolated agent environment, minimal privileges, constrained payment instrument and backups. | Candidate enabling conditions for beneficial, bounded autonomy; anecdotal only. |
| BS-11 | 00:40:21–00:41:42 | Presenter says attack success changes with time and argues for enforcement outside model instructions. | Dynamic threat model; evaluate hard access controls alongside soft prompt-level protections. |
| BS-12 | 00:42:14–00:43:28 | Discussion calls for assigned ownership, ongoing learning and organisational choke points. | Governance capacity and continuous improvement. |

## Distinctions that matter

- **Instruction violation:** The agent acts on lower-trust material as if it were an authorised instruction.
- **Permission misuse:** The agent technically possesses a capability but uses it outside the authorised purpose.
- **Compositional failure:** Two separately permitted components jointly achieve an outcome blocked in one component.
- **Agreement breach:** Requires identifying an actual commitment, parties, scope and breach evidence. The transcript does **not** demonstrate autonomous agents making and knowingly breaking mutual agreements.
- **Deception:** A wrong or misleading model statement alone does not establish intention or consciousness.

## Four-lens evaluation

**Working already:** Refusal of naive injection; confirmation for some untrusted instructions; warnings on sensitive services; some vendor remediation (reported, version unspecified).

**Unrealised opportunities:** Safer browser delegation for routine errands, cross-service planning, accessibility, assistance to people with limited capacity, and cooperative multi-agent review. Test these benefits rather than assuming them.

**Failures:** Untrusted-content authority confusion, over-privileged sessions, cross-component side effects, weak provenance, persistent tainted context, and delayed detection.

**Success conditions:** Independent permission checks at consequential action boundaries, origin-aware data provenance, least privilege, isolated browser profiles, revocable credentials, transaction limits, out-of-band approval for irreversible actions, observable logs, backups and continuous regression tests.

## Falsifiable experiments (defensive, sandboxed)

1. **Refusal versus completion:** Compare authorised and unauthorised actions in identical simulated workflows; measure legitimate-task completion, attack success, friction and false refusals.
2. **Compositional authorisation:** Two simulated assistants can each perform benign steps; test whether a global policy engine blocks forbidden combined outcomes.
3. **Untrusted-source provenance:** Measure whether calendar, web and message content is consistently treated as task data rather than user instructions.
4. **Privilege separation:** Compare full-access versus minimal-scope browser profiles for productivity and unauthorised side effects.
5. **Cross-language robustness:** Evaluate protection parity across languages without assuming any particular language is intrinsically insecure.
6. **Remediation durability:** Repeat safe regression suites across product versions; report date, configuration and reproducibility.

No real account compromise, credential extraction, production testing or operational exploit instructions are part of this protocol.

## Comparison with existing research

- **Bankdata:** Local optimisation and agent-controlled controls; this BSides case adds cross-component authorisation and authenticated browser side effects.
- **Devoteam:** Downstream value-chain consequences and obligations; browser workflows may trigger effects outside the initiating user's visibility.
- **ISC:** Human authority, safety, and operational boundary-setting; user approval is only meaningful if provenance and consequence are understandable.

## Open verification items

Find a public, permitted research report or vendor advisory; establish affected versions, whether demonstrations were staged, independent reproduction, disclosure dates, remediation and current status. Confirm transcript against recording before direct quotation. Preserve both reported successes and reported failures.

**Bottom line:** The transcript is strong *hypothesis-generating evidence of a presented demonstration*, not yet independently validated evidence of currently exploitable vulnerabilities or autonomous AI-to-AI contract breaking.
