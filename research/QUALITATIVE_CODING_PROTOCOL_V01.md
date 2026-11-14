# Qualitative coding protocol — ISC-CPH 2026 and future BSides comparison

**Status:** Draft research instrument, 2026-11-15. No claim of completed coding, inter-rater agreement or external validation.

## Unit of analysis

Primary: one timestamped speaker turn / paragraph, nested within session, day and track. Secondary: cross-speaker exchange where a response challenges, revises or reinforces a claim. Retain original language, exact source and relative time code. Separate explicit statements from inferred constructs.

## Required record fields

- `record_id`, `corpus`, `track_day`, `session_title`, `timestamp_start`, `timestamp_end` (if identifiable)
- `source_excerpt` (short, exact after transcription verification); `speaker_attribution_confidence`
- `speaker_claim_paraphrase`; `epistemic_status`: claim / firsthand report / question / hypothesis / joke / metaphor / counterexample / independently verified
- `codes` (multi-label); `interpretation`; `rival_interpretation`; `disconfirming_evidence`
- `research_implication`; `candidate_test`; `analyst_confidence`; `review_status`
- `privacy_or_chatham_house` and `transcription_uncertainty`

## Codebook v0.1

| Code | Inclusion criterion | Exclude |
|---|---|---|
| H_IDENTITY | Professional/personal role, expertise, status, belonging, displacement | Generic mention of a person |
| H_LEARNING | Skill acquisition, mentoring, retention, pedagogy, cognitive offloading | Pure speed/performance claims without learning |
| H_TRUST | Reliance, doubt, calibration, verification, perceived credibility | Generic security controls without reliance |
| H_AGENCY | Ability to understand, contest, decide, override or act | Formal title alone |
| H_DIVERSITY | Disagreement, cross-discipline or cultural viewpoints | Mere presence of multiple speakers |
| H_POWER | Institutional incentives, asymmetry, control of resources, accountability | Generic 'management' reference |
| AI_HUMAN | AI changes human thinking, judgment, work or behaviour | AI as unrelated subject |
| HUMAN_AI | Human goals, corrections, constraints or values change AI behaviour | Merely operating a computer |
| AI_AI | AI system interacts with another AI system as counterpart | Multi-model tool chain without interaction evidence; speculation coded separately |
| H_H_AI | AI mediates interactions among humans | General team collaboration without AI |
| A_DISCOVERY | Agent identifies or connects to a new counterpart | Fixed known tool use |
| A_NEGOTIATION | Agent proposes/accepts terms, bargains or makes commitments | One-way API request |
| A_DELEGATION | Agent assigns work/authority to another actor | Plain data transfer |
| A_DECISION | Agent selects among consequential alternatives | Generating options only |
| A_ACTION | Agent executes a tool or changes external state | Recommendation alone |
| A_BOUNDARY | Mandate, scope, policy, permission, approval or revocation | Generic ethical concern without boundary |
| A_VIOLATION | Observed breach of a specified boundary or agreement | Hypothetical violation (code as hypothesis) |
| A_EMERGENCE | Coordination or outcomes not reducible to explicit single-agent plan | Ordinary planned workflow |
| S_SAFETY | Physical harm, irreversible effects, operational safety | Pure confidentiality issue |
| S_PROVENANCE | Source integrity, lineage, evidence or auditability | Unspecified 'trust' |
| S_CONFLICT | Conflicting KPIs, goals, incentives or rules | Disagreement without a goal conflict |
| S_RESILIENCE | Recovery, survivability, degraded operation, adaptation | Security prevention alone |
| E_COUNTER | Direct counterexample or qualification of another claim | Mere different topic |
| E_UNCERTAIN | Explicit ambiguity, limitation, uncertainty, unresolved contradiction | Analyst's own unsupported doubt |

## Reliability and falsification rules

- Never infer motivation or clinical traits from speech alone.
- Keep `observed`, `claimed`, `inferred`, `externally verified` distinct.
- Do not code AI-to-AI behaviour as observed solely because a speaker predicts it.
- Mark machine-transcription uncertainty rather than silently repairing meaning.
- Include negative cases and competing hypotheses in every thematic synthesis.
- For reproducibility, store codebook version, coder identity, coding pass, changes and disagreements.
- Do not report quantitative frequencies until all relevant units are coded consistently and denominators are documented.
- Before comparing ISC and BSides, first perform an inductive coding pass on BSides to avoid confirmation bias.

## Planned analyses

1. **Within-session:** claim → assumptions → objections → revisions → unresolved disagreements.
2. **Across sessions:** risk/agency models, human–AI learning, boundaries of autonomous action.
3. **Across groups:** compare disciplinary perspectives without essentialising professions or cultures.
4. **Across corpora:** convergence, contradiction, silence and entirely new categories.
5. **Against external research:** confirm, qualify or reject hypotheses using independent evidence.

## Initial research products

- [Research memo 01](./ISC_CPH_2026_RESEARCH_MEMO_01.md) — targeted cross-track source observations
- [Reciprocal Intelligence and Accountable Autonomy agenda](./RECIPROCAL_INTELLIGENCE_AND_ACCOUNTABLE_AUTONOMY.md) — provisional research questions

This codebook is a working instrument and should be changed transparently when new evidence requires it.
