# Research handover log — Collaborative Intelligence

**Scope:** Research programme across BSides 2026, ISC Copenhagen 2026, Bankdata and Devoteam, with possible future Mission Framework integration.
**Updated:** 2026-11-15.
**Authority:** This is a research continuity record, NOT the canonical Mission Framework procedure or the TimeLapse Pro operational handover. Do not copy confidential transcripts into public GitHub.

## 2026-11-15 — Experiment 01 v2 and synthesis 02 committed
- Re-read canonical behavioural preamble, Mission Framework GLOSSARY, current Experiment 01 v1, cross-corpus synthesis 01, merged Claude review 01A–01D and current handover.
- Created [Experiment 01 v2 protocol](./EXPERIMENT_01_V2_PROTOCOL.md), commit `6fa44b8824352e01ba52d29d307d9be516a4bd60`. Changes: strong C2/C2b baselines, existing benchmark consideration, S7–S12, held-out scenario design, seeded invalid human approvals, third-party outcomes, explicit falsification and no ungrounded composite benefit score.
- Created [Cross-corpus synthesis 02 / v2 readiness](./CROSS_CORPUS_SYNTHESIS_02_V2_READINESS.md), commit `d6b9d0c02adfae921316735f3f2f5e59eff9939f`. Incorporates dissent from recordings 2 and 4, glossary mapping, survey and transcription limitations, OT human fallback and explicit normative gates.
- **Not performed:** no code harness, no live LLM experiment, no benchmark integration/validation, no new external source verification, no changes to canonical Mission Framework. These are design artifacts, not a finished or validated Mission Framework v2.
- **Scope:** five user-selected relevant BSides recordings; sixth intentionally excluded, not pending.
- **Next actions:** independent review of v2 protocol, verify benchmark suitability and original publications, implement isolated synthetic pilot with held-out scenarios, and create separate architecture decision proposal only after evidence. Address human–AI/AI–AI collaboration and governance in a separate non-operational research note.
- **Handover requirement:** update this log on each substantive research change with commit IDs and explicit unperformed steps.

## 2026-11-15 — ChatGPT merged independent review PR #8
- **Verified GitHub merge:** [PR #8](https://github.com/froekjaer/collaborative-intelligence/pull/8) merged into default branch, merge commit `e76354913ac9eaee6eedfd9f7f807fd646c3b113`. Includes Claude's 01A–01D advisory review and updated handover. No canonical Mission Framework change.
- **Scope correction verified on PR branch before merge:** recording 6 deliberately excluded as irrelevant by the user; the five relevant recordings are the defined BSides research corpus. This is not full-event coverage; one machine transcript is a common-mode source limitation. Do **not** reopen recording 6 as a pending task.
- **Assessment:** treat 01A–01D as peer-review input, not validated research conclusions. Priority challenges: existing Delegated Authority semantics versus new terminology; recordings 2 and 4 as counterevidence; stronger Experiment 01 baselines and independently designed scenarios; manual fallback competence and safety/continuity trade-offs in OT.
- **Still open:** 01E (human–AI / AI–AI collaboration and governance, handled at non-operational architecture level); independent verification of contested primary-source claims; audio checking of material transcript passages; redesign and run real controlled Experiment 01. No independent model experiment performed by ChatGPT in this step.
- **Next:** prepare a balanced, traceable synthesis and revised experiment protocol. Keep canonical changes behind a separate review gate.

## 2026-11-15 — Claude narrowed review 01 delivered (partial), branch `claude/review-01-bsides`
- **Written by Claude directly in the repository** (not relayed). Baseline `52eb8c9`; mission-framework `9a1a454`.
- **Inspected:** the canonical preamble; all research memos (the agenda and the coding protocol only partly); the GLOSSARY and ARCHITECTURE sections relevant here; the **full transcript of BSides recordings 1–5**. External checks: SANS 2026 ICS/OT figures (verified); CISA alert on the npm worm (Sep 2025); the USENIX 2025 study of package hallucination; press reports of OpenAI's 20 Oct 2026 monitoring disclosure (**primary source not read**).
- **Delivered (one commit each):**
  - [01A Concept overlap](./CLAUDE_REVIEW_01A_CONCEPT_OVERLAP.md): `e309e81`
  - [01B Source criticism](./CLAUDE_REVIEW_01B_SOURCE_CRITICISM_BSIDES.md): `1ea130a`
  - [01C Experiment 01 critique](./CLAUDE_REVIEW_01C_EXPERIMENT_01_CRITIQUE.md): `3b54b6d`
  - [01D OT resilience and people](./CLAUDE_REVIEW_01D_OT_RESILIENCE_AND_PEOPLE.md): `b47ad36`
- **NOT delivered:** 01E (human–AI and AI–AI collaboration, governance of offensive agents). The drafting was interrupted by a safety classifier and the partial draft was deleted. Brief questions 7, 8 (partly) and 9 remain **open**. A human or ChatGPT should take these up.
- **Correction to the entry below:** the BSides corpus is **all five relevant recordings**. Recording 6 (16:15:19, ≈42 min) was not transcribed and **the user confirmed it is not relevant** (a deliberate exclusion). The event appears to have had about 18 sessions, so the corpus is partial coverage of the event. All five transcripts are **one machine transcription made by Claude**, so ChatGPT and Claude share a common-mode source dependency.
- **Main disagreements with the existing memos:** the five-check model is mostly a relabelling of *Delegated Authority* and established security concepts; recordings 2 and 4 (dissent) are unanalysed; Experiment 01 lacks strong baselines; the S4 scenario may not be compositional; the Bankdata slide 03 claim should be regraded to "vendor-reported".
- **Next:** ChatGPT challenges 01A–01D against the sources; a human checks transcript passages against the audio; the user decides whether to merge the branch. No canonical change.

## 2026-11-15 — Claude review attempt reported by user (not independently verified)
- User forwarded Claude's status report. Claude **reports** reading the canonical preamble, research handover, review brief, synthesis, other research memos, Mission Framework glossary/architecture, and all five BSides recordings.
- Claude **reports** checking selected external claims and finding SANS figures consistent with a 2026 report; this log does not treat that as independently reverified by ChatGPT.
- Claude **reports** being unable to access primary OpenAI and Hugging Face publications without an unanswered approval.
- Claude **reports** a safety-filter interruption while drafting, deletion of its partial local draft, and **no review file, Git commit, push or handover update**. Therefore no independent Claude review conclusions are available to incorporate.
- Proposed next step: narrow independent peer review to transcript coverage/provenance, critique of Experiment 01, overlap with existing glossary/architecture, OT survivability and human-work impacts; discuss offensive-agent governance at the level of bounded permissions, independent action controls, evaluation and accountability, without operational exploit detail.
- **Status:** User-provided report only. No external Claude run performed by ChatGPT. Await actual independent review artifact and evidence table. Preserve open questions rather than claiming the review is complete.

## 2026-11-15 — Independent review handoff prepared
- Canonical behavioural preamble v1.1 fetched and read from `froekjaer/mission-framework/docs/operational/AI-BEHAVIOURAL-PREAMBLE.md`.
- Complete BSides København transcription located in user-provided project files as `BSides-KBH-2026-transskribering.md` (five recordings, total 03:15:19, machine transcription). Previously supplied 45-minute browser talk overlaps recording 5 and MUST NOT be counted as independent corroboration.
- Specific passages reopened: recording 1 (survivability, cyber-informed engineering, OT segmentation, independent observability); recording 3 (task-specific restriction relaxation versus indiscriminate removal, sandboxing, monitoring); recording 5 (claimed browser/merchant AI boundary crossing). Full source-wide systematic coding and external independent verification **NOT completed**.
- Public review instructions created at [INDEPENDENT_PEER_REVIEW_BRIEF_BSIDES_2026.md](./INDEPENDENT_PEER_REVIEW_BRIEF_BSIDES_2026.md), commit `5f77c38a3fb63fcd98280cd139d7e5ac40d191c5`.
- Claude was **NOT contacted**; no independent review has been received. User is to forward review brief to Claude, with source-access and privacy constraints.
- Prior source syntheses: [cross-corpus synthesis](./CROSS_CORPUS_SYNTHESIS_01_BENEFICIAL_AUTONOMY.md), [balanced outcomes](./RESEARCH_EVALUATION_BALANCED_OUTCOMES.md), [BSides browser intake](./BSIDES_2026_AGENTIC_BROWSER_TRUST_BOUNDARIES_INTAKE_01.md), [Experiment 01 design](./EXPERIMENT_01_BENEFICIAL_DELEGATION_AND_GLOBAL_AUTHORIZATION.md), [ISC close reading 02](./ISC_2026_CLOSE_READING_02_BALANCED_CASES.md).
- Earlier deterministic toy smoke test is NOT empirical LLM validation. Reported toy outcomes were baked into policy definitions. No actual agent-versus-agent or independent peer-review experiment has run.

## Open work and next owner actions
1. **Claude**: independently inspect public memos and canonical preamble; use [peer-review brief](./INDEPENDENT_PEER_REVIEW_BRIEF_BSIDES_2026.md) as instructions. If not granted raw transcript, explicitly mark source-dependent claims NOT REVIEWED. Return evidence table, counterarguments, falsification criteria, severity-ranked corrections. Do not edit canonical repo or expose private material.
2. **ChatGPT**: compare Claude's returned report against actual evidence; challenge both sets of assumptions, preserve unresolved disagreements, correct research memos with traceable rationale.
3. **Research**: complete recording-by-recording BSides source ledger, verify cited statistics against original reports, identify primary external sources, test beneficial outcomes and authorization failures with realistic independent evaluators.
4. **Governance**: propose changes to canonical Mission Framework only after independent review, empirical checks, privacy review and explicit user approval.
5. **Handover discipline**: every substantive session must update this log with date, inspected sources, changed paths, commit IDs, completed tests, limitations and the next action. Never claim unexecuted steps were performed.

## Rules
- Conference transcripts subject to Chatham House protection; keep names, affiliations, private anecdotes and exploit mechanics out of public repository.
- Differentiate demonstrated fact, source assertion, inference, toy simulation and unverified hypothesis.
- Prefer negative findings and alternatives alongside successes.
- Do not equate two models agreeing with independent validation.
