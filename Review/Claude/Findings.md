# Findings

Each finding states **Observation** (fact unless marked otherwise), **Evidence** (file/commit-verifiable), and **Impact** (engineering judgement). Commits per `Metadata.md`.

---

## Architecture

### A1 — The declared five-repository separation of concerns is coherent and well documented
- **Observation:** The ecosystem declares explicit per-repository responsibilities and an authority map, including the rule "No repository is authoritative for all concerns."
- **Evidence:** `collaborative-intelligence/AI_CONTEXT.md` (authority map table); `collaborative-intelligence/README.md` (programme architecture diagram); `mission-framework/README.md` ("Role in the research programme").
- **Impact:** Positive. The design gives each concern an owner, a change process and a feedback path — the structural precondition for everything else the programme claims.

### A2 — The semantic-core repository has begun absorbing implementation and operational concerns
- **Observation:** `mission-framework` now contains a publication build system (`publication/build.py`, `publication/book.yml`, `publication/profiles/`), a publication CI workflow (`.github/workflows/publication-pipeline.yml`), per-AI operational integration material (`docs/operational/` with loaders and integration guides for ChatGPT, Claude, Codex, Mistral, z.ai) and publication design documents (`docs/publication/`). The declared owner of publication transformation is the Publication Pipeline repository; the declared owner of tooling and implementation is Mission-Platform.
- **Evidence:** Directory listing of `mission-framework` at `e9644ba`; authority map in `collaborative-intelligence/AI_CONTEXT.md` ("Publication transformations and output profiles → `-Publication-Pipeline`"); `Mission-Platform` role statements in `mission-framework/reviews/*/INVITATION.md` ("Mission-Platform owns schemas, tooling, architecture and reference implementation").
- **Impact:** The ecosystem's central architectural claim — separation of semantics from implementation — is being dissolved from inside its most authoritative repository. Two publication implementations now exist (`mission-framework/publication/build.py` and `-Publication-Pipeline`'s `mission-docgen`), with no document stating their relationship, precedence or migration intent. Every future reviewer and AI agent following the authority map will be misdirected.

### A3 — Two parallel publication implementations with no declared relationship
- **Observation:** `-Publication-Pipeline` implements `mission-docgen` (Python ≥3.11, pinned deps, tests, provenance manifest). `mission-framework/publication/build.py` independently implements a publication builder (hashing, manifests, GENERATOR_VERSION "1.1.0"). Neither references the other.
- **Evidence:** `pubpipe/pyproject.toml`, `pubpipe/src`, `pubpipe/tests`; `mission-framework/publication/build.py` (imports hashlib, writes dist manifests).
- **Impact:** Duplicate effort, divergent provenance formats, and a contradiction of FF-PUB-001's own recommendation of a single "reusable, implementation-neutral minimum publication-provenance profile."

### A4 — Platform strategy remains aspirational and now stale
- **Observation:** `Mission-Platform` contains vision, reference model, meta model, architecture tests and one ADR; no schemas, validators, APIs or code. It has received no commits since before the Foundation v1.0 semantic changes.
- **Evidence:** Repository tree at `48e1cfc` (12 markdown files, 580 lines, no source directories); framework commit history shows all v1.0 work post-dates `48e1cfc`.
- **Impact:** Acceptable as strategy-before-implementation — but see G2/T2: its texts now conflict with canonical semantics, which is worse than absence.

## Documentation

### D1 — Documentation quality and voice are consistently high
- **Observation:** Documents are well structured, consistently voiced, and most carry status headers (e.g., "Foundation Draft", version fields).
- **Evidence:** `Mission-Platform/docs/*` (Version/Status headers); `mission-framework/docs/VERSIONING.md`; `mission-solar-eclipse/MISSION.md`.
- **Impact:** Positive; lowers onboarding cost for both humans and AI agents.

### D2 — Documentation mass is heavily concentrated in the semantic core and growing fast
- **Observation:** mission-framework: 95 markdown files / ~12,470 lines; Mission-Platform: 12 / ~580; mission-solar-eclipse: 24 / ~2,100; collaborative-intelligence: 11 / ~240; -Publication-Pipeline: 24 / ~710. Approximately 60 commits were added to mission-framework within roughly one day after Foundation v1.0.
- **Evidence:** File counts at the reviewed commits; `git log` between `e82fb32` and `e9644ba`.
- **Impact:** The canonical repository is the fastest-moving repository in the ecosystem. Canonical semantics should be the *slowest*-moving layer; the current inversion undermines the meaning of "stable semantic baseline" days after it was declared.

### D3 — Legacy documents contradict the current foundation
- **Observation:** `MISSION.md` still presents the pre-v0.2 voice and the motto "Build once. Reuse forever.", unreconciled with "Everything Evolves" (`PROJECT_PRINCIPLES.md` §10) and Principle 11 ("no mission architecture is ever complete"). Three overlapping principle sets remain unmapped (11 Project Principles; Principia 0–17; Platform's 12 Guiding Principles).
- **Evidence:** `mission-framework/MISSION.md`; `mission-framework/PROJECT_PRINCIPLES.md`; `mission-framework/docs/PRINCIPIA_MISSIONIS.md`; `Mission-Platform/docs/principles/guiding-principles.md`. The reconciliation task appears as open "Required next work" in `reviews/REVIEW-SYNTHESIS.md`.
- **Impact:** New readers cannot determine which principle set governs; the glossary solved this for terms but not for principles.

### D4 — Untranslated Danish passages in an English corpus
- **Observation:** Operative content exists only in Danish in at least one governing artefact (the meta-instruction in `mission-solar-eclipse/docs/decisions/MDN-0001-meta-instruction.md`); the Reality Principle documents preserve "Remtræk til Virkeligheden" (intentionally, with attribution — not a defect).
- **Evidence:** MDN-0001 quotes the owner's instruction in Danish without translation.
- **Impact:** Minor. Conflicts with the framework's own requirement that language be "understandable without prior access to the project conversation" for non-Danish participants.

## Knowledge Architecture

### K1 — The canonical glossary is a genuine knowledge-architecture asset
- **Observation:** `GLOSSARY.md` is declared the single normative source; it defines normative language (must/should/may), core concepts, load-bearing qualifiers and the canonical Mission Loop with a views rule.
- **Evidence:** `mission-framework/GLOSSARY.md`.
- **Impact:** Resolves the v0.2 drift problem in design. (Disclosure: this reviewer recommended it; see Metadata bias note.)

### K2 — No machine-readable knowledge representation exists anywhere
- **Observation:** All semantics are prose. There is no YAML/JSON/RDF export of the glossary, no schema for finding records, decision records or evidence records, despite three different finding formats already in use.
- **Evidence:** Finding formats differ across `mission-solar-eclipse/docs/findings/FF-0001…` (markdown header fields), `-Publication-Pipeline/docs/framework-findings.md` (embedded YAML blocks) and `mission-framework/docs/FRAMEWORK_FINDINGS.md` (field table specification); no schema files exist in any repository.
- **Impact:** For a programme explicitly designed for AI collaboration, the absence of machine-readable contracts forces every AI agent to re-parse prose and guarantees format drift — already observable.

### K3 — Cross-repository references are unpinned
- **Observation:** Inter-repo links point to `main` (or bare repository URLs), not to tags or commits; `AI_CONTEXT.md` rule 8 instructs contributors to "record exact source files and commit SHAs when producing derived material," which repository practice only partially follows (good: DEC-0002's timestamped directive; z.ai reviews citing "main HEAD" only).
- **Evidence:** Links in `mission-framework/README.md`, `mission-solar-eclipse/MISSION.md`, `collaborative-intelligence/AI_CONTEXT.md`; absence of tags in all five repositories (`git tag` empty).
- **Impact:** Derived material cannot be reliably re-derived; the ecosystem's traceability claim stops at repository granularity.

## Governance

### G1 — The findings/disposition machinery works and is the programme's best governance asset
- **Observation:** External findings were consolidated, dispositioned on a five-value scale, and implemented with visible traceability; reference-mission findings (FF-0001/FF-0002) were triaged with restraint (defer/clarify) rather than reflexive ontology growth; SP-0002 proposes a deferral heuristic.
- **Evidence:** `mission-framework/reviews/REVIEW-SYNTHESIS.md`; `mission-solar-eclipse/docs/findings/`; `docs/decisions/SP-0002-defer-finding-guidance.md`.
- **Impact:** Positive and unusual at this scale.

### G2 — The glossary's own change-control rule is not being followed
- **Observation:** `GLOSSARY.md` Governance states: "Changes to a Core definition require an Architecture Decision Record." `mission-framework` contains no ADR directory or ADR files. Principles 16–17 and five Experimental Core candidates were added after that rule was written, without ADRs.
- **Evidence:** `GLOSSARY.md` (Governance section); repository tree at `e9644ba` (no ADR path; ADR directories exist only in `Mission-Platform/docs/adr` and `-Publication-Pipeline/docs/adr`); `git log e82fb32..e9644ba` for the additions.
- **Impact:** The strongest governance rule in the ecosystem is currently aspirational in its own home repository. If the canonical repo does not follow its own change control, downstream repositories have no reason to.

### G3 — Four review programmes now coexist without an index
- **Observation:** (1) `mission-framework/review/` — the v0.2 review package; (2) `mission-framework/reviews/` — per-reviewer board workspaces plus synthesis; (3) `mission-framework/reviews/MIAR/` plus per-reviewer MIAR invitations and per-organisation introductions — a new assurance programme; (4) this architectural review, deliverable to `collaborative-intelligence/Review/`. No document lists all active review tracks, their status or their relationship.
- **Evidence:** Directory trees at `e9644ba` and `4ed96fc`; the call for review (received from the owner) mandating `Review/` while `collaborative-intelligence/reviews/` already exists.
- **Impact:** Review findings — the programme's declared lifeblood — risk being scattered across parallel structures faster than one steward can triage them. Duplicate artefacts have already appeared (see R-S1).

### G4 — No repository-mechanical governance exists
- **Observation:** No CONTRIBUTING.md, CODEOWNERS, SECURITY.md, issue templates or PR templates in any of the five repositories; no tags or releases; branch protection unverifiable (see Metadata limitations).
- **Evidence:** File-presence scan across all five repositories at the reviewed commits.
- **Impact:** Governance depends entirely on the steward's personal discipline. It has held so far (observable in HISTORY.md corrections), but it does not scale to the multi-reviewer, multi-organisation participation the MIAR programme invites.

## Mission Framework

### MF1 — Semantic quality is high and self-correcting
- **Observation:** The v0.2 → v1.0 delta implemented nearly all converged review findings (glossary, canonical loop, verification/fitness split, Delegated Authority, procedural Core admission, Principle-15-compliant history).
- **Evidence:** `git diff 9b78a23..e82fb32` file list; `reviews/REVIEW-SYNTHESIS.md` disposition table.
- **Impact:** Positive. The semantic core deserves its "canonical" designation on quality grounds.

### MF2 — Normative growth has resumed faster than validation
- **Observation:** After declaring semantic stabilisation, the repository added Principles 16–17, a 268-line continuity/verification discipline, the MIAR assurance programme, audience-adaptive publication theory and operational onboarding models — before the first reference mission has reached its validation event (2026-08-12).
- **Evidence:** `git log e82fb32..e9644ba` (≈60 commits, one day); `docs/ENGINEERING_CONTINUITY_AND_INDEPENDENT_VERIFICATION.md` §6 (proposition "admitted for empirical challenge" — not yet tested).
- **Impact:** The ratio of normative text to measured outcomes grows; each addition enlarges the surface the Solar Eclipse mission is supposed to validate, making the validation weaker per concept. This is the project's own "trust debt" pattern applied to itself.

## Mission Platform

### MP1 — Platform contradicts canonical semantics agreed for removal
- **Observation:** `Mission-Platform` still defines Decision as "a selection among alternatives made by an authorised actor **or mechanism**" (contradicting the glossary's accountable-authority definition and Delegated Authority), retains an Evidence definition without provenance/integrity conditions, and presents its own principle set — items the synthesis marked "Required next work: Remove or clearly mark duplicated semantic definitions."
- **Evidence:** `Mission-Platform/docs/architecture/mission-reference-model.md` at `48e1cfc`; `mission-framework/GLOSSARY.md` (Decision, Evidence, Delegated Authority); `reviews/REVIEW-SYNTHESIS.md` (Platform work items).
- **Impact:** The ecosystem's second-most-authoritative-sounding repository actively contradicts its first. Any implementer starting from Platform docs will build the pre-correction semantics — including the exact accountability hole ("or mechanism") the v1.0 round fixed.

### MP2 — Useful Platform assets are ready for extraction
- **Observation:** The Architecture Tests (12 reflective checks) and the meta-model's relationship-property requirements (identity, provenance, validity interval) remain valuable and are consistent with v1.0 semantics.
- **Evidence:** `Mission-Platform/docs/architecture/architecture-tests.md`; `mission-meta-model.md`.
- **Impact:** Positive: the update path is mostly deletion and linking, not redesign.

## Repository Structure

### R-S1 — Naming and structure drift is now observable inside single directories
- **Observation:** `mission-framework/reviews/` contains both `REVIEW-SYNTHESIS.md` (92 lines, the substantive synthesis) and `REVIEW_SYNTHESIS.md` (5 lines, a newer index stub) — two files whose names differ only by hyphen/underscore, with different content; directories `z-ai/` and `zai/` coexist; top level has both `review/` and `reviews/`.
- **Evidence:** Directory listing and `diff` at `e9644ba`.
- **Impact:** Concrete, already-realised instance of continuity regression risk: a reader (or AI) has no way to know which synthesis file is authoritative. The framework's own §1.6 ("silent change of meaning… broken links") describes precisely this failure class.
- **Note:** This call itself continues the pattern by mandating `Review/` in a repository that has `reviews/`. **[Fact as to the collision]**

### R-S2 — Repository slugs are inconsistent and one is defective
- **Observation:** Slugs mix conventions: `mission-framework`, `Mission-Platform`, `mission-solar-eclipse`, `collaborative-intelligence`, `-Publication-Pipeline` (leading hyphen, acknowledged in `AI_CONTEXT.md` as "a repository naming defect"). The call for review lists `mission-platform` and `publication-pipeline`, which do not match the actual slugs (GitHub tolerates case differences but `publication-pipeline` ≠ `-Publication-Pipeline`).
- **Evidence:** Actual clone URLs; `collaborative-intelligence/AI_CONTEXT.md`; the call text.
- **Impact:** Link rot, broken automation, and avoidable confusion for every external participant the programme is currently inviting.

## Traceability

### T1 — Decision and finding traceability within repositories is good
- **Observation:** DEC-0001/DEC-0002 record alternatives, rationale, supersession, and the owner's directive with timestamp; findings link decisions to canonical references; publication builders emit hash manifests.
- **Evidence:** `mission-solar-eclipse/docs/decisions/`; `-Publication-Pipeline/docs/framework-findings.md` (FF-PUB-001); `mission-framework/publication/build.py` (hash manifest code).
- **Impact:** Positive; within-repo provenance practice matches the theory.

### T2 — Cross-repository traceability lacks anchors
- **Observation:** No tags or releases exist in any repository; "Foundation Release v1.0" is not checkoutable; cross-repo links are unpinned (K3); the Delegated Authority instrument for the Mission Director role asserted in solar-eclipse headers ("z.ai (Mission Director, delegated authority from Peter)") exists nowhere as a record with scope/validity/revocation as the glossary requires.
- **Evidence:** `git tag` empty ×5; `mission-solar-eclipse/docs/README.md` and `DEC-0001` headers; `GLOSSARY.md` (Delegated Authority requirements).
- **Impact:** The ecosystem cannot currently prove which versions of its own parts constituted "Foundation v1.0" — a reproducibility gap directly counter to Principle 15 and the versioning policy's intent.

## Strengths

1. Explicit authority map and separation-of-concerns design (A1).
2. Working, restrained findings governance (G1).
3. Real reference mission with unmovable deadline and honest decision records (MF1, T1).
4. First real engineering component with tests, pinned deps and CI (`mission-docgen`).
5. Institutional willingness to correct its own record under its own rules (HISTORY.md rewrite).
6. AI-collaboration onboarding pattern (`AI_CONTEXT.md`, expected-behaviour rules) — ahead of common practice. **[Opinion]**

## Weaknesses

1. Boundary erosion into the semantic core (A2, A3).
2. Stale, contradicting Platform (MP1).
3. Prose-only governance without repository mechanics or automation (G2, G4).
4. No machine-readable semantics or record schemas (K2).
5. Unanchored releases and unpinned references (T2, K3).
6. Review-programme proliferation and structure drift (G3, R-S1).

## Risks

1. **Monorepo-by-accretion** in mission-framework; the declared architecture becomes fiction while remaining documented as fact (A2). Severity: high; horizon: months. **[Opinion]**
2. **Semantic fork via Platform** (MP1). Severity: high if any implementer starts now; mitigation cost currently low. **[Opinion]**
3. **Findings loss under review-programme sprawl** (G3). Severity: medium-high; the failure would be silent. **[Opinion]**
4. **Steward single-point-of-failure** — 114/114 mission-framework commits by one identity; no CODEOWNERS/succession mechanics in-repo; SUSTAINABILITY.md acknowledges but does not mitigate. Severity: high impact, unknown likelihood. **[Fact as to commits; Opinion as to severity]**
5. **Baseline irreproducibility** (T2) — undermines every future "we validated against v1.0" claim. Severity: medium; fix trivial. **[Opinion]**
6. **Validation debt** — normative surface growing ahead of the single validation event (MF2). Severity: medium-high. **[Opinion]**

## Technical Debt

1. Two publication implementations with no declared relationship (A3).
2. `REVIEW-SYNTHESIS.md` vs `REVIEW_SYNTHESIS.md`; `z-ai/` vs `zai/`; `review/` vs `reviews/` (R-S1).
3. Platform's pre-v1.0 definitions (MP1).
4. `MISSION.md` legacy document and three unmapped principle sets (D3).
5. `-Publication-Pipeline` slug defect and slug-convention inconsistency (R-S2).
6. Missing ADR store in mission-framework versus glossary's ADR requirement (G2).
7. Divergent finding-record formats across three repositories (K2).
8. Missing Delegated Authority instrument for the Mission Director role (T2).
