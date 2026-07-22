# Recommendations

Cross-references (A2, G3, …) point to `Findings.md`. Every recommendation lists Problem, Evidence, Recommendation, Expected Benefit and Priority as required by the call.

---

## Critical

### C1 — Restore the repository responsibility boundaries
- **Problem:** The semantic-core repository has absorbed publication tooling, CI build code and operational integration material, duplicating responsibilities declared to belong to `-Publication-Pipeline` and `Mission-Platform` (A2, A3).
- **Evidence:** `mission-framework/publication/build.py`; `.github/workflows/publication-pipeline.yml`; `docs/operational/`; authority map in `collaborative-intelligence/AI_CONTEXT.md`.
- **Recommendation:** Decide explicitly, in an ADR, where publication implementation lives. Either (a) move `publication/` and the workflow into `-Publication-Pipeline` and have mission-framework consume it, or (b) re-scope the authority map to match reality. Do the same for `docs/operational/` (candidate new home: `collaborative-intelligence`, which owns programme-level participant onboarding). One implementation must be designated primary; the other archived or made a thin consumer.
- **Expected Benefit:** The ecosystem's central architectural claim becomes true again; AI agents following the authority map stop being misdirected; duplicate maintenance ends.
- **Priority:** Critical

### C2 — Consolidate the review architecture under a single index
- **Problem:** Four review programmes coexist (`review/`, `reviews/` board, MIAR, this call's `Review/`), with duplicate synthesis files and duplicate reviewer directories already present (G3, R-S1).
- **Evidence:** `reviews/REVIEW-SYNTHESIS.md` vs `reviews/REVIEW_SYNTHESIS.md`; `z-ai/` vs `zai/`; `review/` vs `reviews/`; `collaborative-intelligence/reviews/` vs this call's `Review/`.
- **Recommendation:** Create one `REVIEW_INDEX.md` (in mission-framework or collaborative-intelligence) listing every active and historical review track, its purpose, location, status and owner. Merge or delete the duplicate synthesis file and `zai/` directory. Choose one directory convention (`reviews/`, lower case, plural — matching the majority) and apply it in all repositories, including for this review's deliverables.
- **Expected Benefit:** Findings stop scattering; reviewers and the steward regain a single triage surface; the continuity-regression pattern (§1.6) stops manifesting in the governance layer itself.
- **Priority:** Critical

## High

### H1 — Update or freeze Mission-Platform
- **Problem:** Platform still carries pre-v1.0 semantics that the synthesis agreed to remove, including the "or mechanism" Decision definition (MP1).
- **Evidence:** `Mission-Platform/docs/architecture/mission-reference-model.md` @ `48e1cfc`; `GLOSSARY.md`; `reviews/REVIEW-SYNTHESIS.md` "Required next work — Platform".
- **Recommendation:** Minimum viable fix within hours: add a status banner to the Platform README and each doc — "Pre-Foundation-v1.0 draft; where definitions conflict with mission-framework/GLOSSARY.md, the glossary governs." Full fix: replace duplicated definitions with glossary links, keep the Architecture Tests and meta-model rules (MP2), and re-issue as Platform Foundation 0.2.
- **Expected Benefit:** Eliminates the semantic-fork risk before any implementer builds on stale semantics.
- **Priority:** High

### H2 — Create the ADR store in mission-framework and use it retroactively
- **Problem:** The glossary requires ADRs for Core changes; no ADR mechanism exists in the canonical repo; Principles 16–17 and five Experimental Core candidates entered without one (G2).
- **Evidence:** `GLOSSARY.md` Governance; repository tree at `e9644ba`; `git log e82fb32..e9644ba`.
- **Recommendation:** Add `docs/adr/` using Platform's existing ADR template. Write retroactive ADRs for: Principles 16–17, the Experimental Core candidate list, the MIAR programme, and the publication-tooling placement (C1). Retroactive ADRs should say so honestly.
- **Expected Benefit:** The canonical repository obeys its own change control; future semantic archaeology becomes possible; the Principle 15 standard is met for the framework's own decisions.
- **Priority:** High

### H3 — Tag the baseline; pin cross-repo references
- **Problem:** "Foundation Release v1.0" is not checkoutable; no tags exist anywhere; cross-repo links point to `main` (T2, K3).
- **Evidence:** `git tag` empty in all five repositories; links in README/AI_CONTEXT/MISSION.md.
- **Recommendation:** Tag the commits that constituted the coordinated baseline (e.g., `foundation-v1.0`) in all five repositories, plus scoped tags per `VERSIONING.md`'s own recommended forms. Pin normative cross-repo references to tags; keep `main` links only for "latest" navigation. Add tagging to the release rule in `docs/VERSIONING.md`.
- **Expected Benefit:** Reproducible baselines; citable reviews; the versioning policy becomes mechanically real. Cost: minutes.
- **Priority:** High

### H4 — Add governance automation to CI
- **Problem:** All governance is manual prose; structure drift already occurs (G4, R-S1).
- **Evidence:** Only Pages/publication/ci workflows exist; duplicate files and directories at `e9644ba`.
- **Recommendation:** Add a lightweight `governance.yml` workflow to each repository: markdown link check (internal + cross-repo), filename/directory naming lint (would have caught `REVIEW_SYNTHESIS.md` and `zai/`), and — in mission-framework — a glossary-drift check (grep-level: flag any file that redefines a glossary headword with "is defined as"/"means" outside GLOSSARY.md). Fail PRs, warn on main.
- **Expected Benefit:** The continuity-regression principle (§1.6) gets mechanical teeth; the steward stops being the only defence.
- **Priority:** High

### H5 — Record the missing Delegated Authority instrument
- **Problem:** The Mission Director role (z.ai) makes consequential decisions under a delegation that exists only in document headers, contradicting the glossary's Delegated Authority requirements (T2).
- **Evidence:** `mission-solar-eclipse/docs/decisions/DEC-0001` header; `GLOSSARY.md` (scope, validity period, revocation, accountability path required).
- **Recommendation:** Write `DEL-0001` in mission-solar-eclipse defining the Mission Director delegation (scope, permitted decision classes, oversight = owner confirmation, validity through mission close, revocation). Reference it from decision-record headers.
- **Expected Benefit:** The mission complies with its own governance at its most sensitive point; FF-0001 (delegation chains) gains its first real evidence artefact.
- **Priority:** High (before the next consequential mission decision; eclipse is 2026-08-12)

## Medium

### M1 — Fix repository slugs and the call's repository list
- **Problem:** `-Publication-Pipeline` leading-hyphen defect; mixed slug conventions; the call lists slugs that do not resolve (R-S2).
- **Evidence:** Clone URLs; `AI_CONTEXT.md`; call text.
- **Recommendation:** Rename `-Publication-Pipeline` → `publication-pipeline` and `Mission-Platform` → `mission-platform` (GitHub preserves redirects for renames); update all references; correct the call document.
- **Expected Benefit:** Working links for every future participant; convention consistency. GitHub's automatic redirects make this low-risk.
- **Priority:** Medium

### M2 — Add repository community/governance files
- **Problem:** No CONTRIBUTING, CODEOWNERS, SECURITY.md, or issue/PR templates anywhere (G4).
- **Evidence:** File scan across all five repositories.
- **Recommendation:** Add per repository: CONTRIBUTING.md (how to submit findings/reviews — largely links to existing process docs), CODEOWNERS (even with one owner today; it makes succession a one-line change), SECURITY.md, and a Framework Finding issue template matching the field table in `docs/FRAMEWORK_FINDINGS.md`.
- **Expected Benefit:** External participation (which MIAR actively solicits) gets a mechanical front door; finding submissions arrive pre-structured.
- **Priority:** Medium

### M3 — Publish machine-readable semantics and record schemas
- **Problem:** Prose-only semantics; three divergent finding formats (K2).
- **Evidence:** FF-0001 (header fields) vs FF-PUB-001 (YAML) vs FRAMEWORK_FINDINGS.md (table spec).
- **Recommendation:** Export `glossary.yaml` generated from GLOSSARY.md (term, definition, normative level, version); define one YAML schema each for finding records and decision records; validate in CI (H4). This is a legitimate first Mission-Platform deliverable — assign it there.
- **Expected Benefit:** AI agents consume semantics reliably; finding formats converge; Platform gets a real, small, boundary-respecting first implementation.
- **Priority:** Medium

### M4 — Reconcile the principle sets and retire legacy documents
- **Problem:** Three overlapping principle sets and a contradicting legacy MISSION.md (D3).
- **Evidence:** PROJECT_PRINCIPLES.md, PRINCIPIA_MISSIONIS.md, Platform guiding-principles.md, MISSION.md.
- **Recommendation:** Declare Principia canonical for principles; convert the other sets into mapped views or fold them in; mark MISSION.md as historical or rewrite it against the glossary.
- **Expected Benefit:** Completes the stabilisation the glossary began; removes the last v0.2-era contradictions.
- **Priority:** Medium

### M5 — Add a brown-field application guide
- **Problem:** The framework targets organisations and existing systems ("Brown-field Transformation Readiness" is a review objective in this call) but contains zero migration guidance and no worked example applying Dependency Descent or the Architecture Tests to an existing system. **[Fact as to absence]**
- **Evidence:** No brown-field content in any repository; Solar Eclipse is a green-field mission.
- **Recommendation:** After the eclipse mission closes, run one small brown-field pilot (e.g., apply Dependency Descent and the 12 Architecture Tests to one existing real system — the Publication Pipeline itself is a candidate) and publish the walkthrough as the second reference case.
- **Expected Benefit:** Evidence for the framework's largest untested applicability claim; a template for organisational adopters.
- **Priority:** Medium

## Low

### L1 — Translate operative Danish passages
- **Problem/Evidence:** MDN-0001's governing instruction is Danish-only (D4).
- **Recommendation:** Add English translations inline for any operative (non-attributional) non-English content.
- **Expected Benefit:** Meets the framework's own accessibility requirement.
- **Priority:** Low

### L2 — Standardise document metadata headers
- **Problem/Evidence:** Version/Status headers are present in Platform and mission docs but absent from most framework docs.
- **Recommendation:** Adopt one metadata header (Status, Version, Owner, Last-reviewed) across all normative documents; lint in CI.
- **Expected Benefit:** Readers can distinguish stable, draft and historical documents without reading git history.
- **Priority:** Low

### L3 — Add a tacit-dependency register to the mission template
- **Problem/Evidence:** Engineering Continuity §1.2's recovery claim silently excludes tacit/personal dependencies (bookings, skills, relationships) that artefacts cannot carry.
- **Recommendation:** Require missions to list dependencies that are *not* recoverable from artefacts, so a replacement participant knows what must be re-established rather than read.
- **Expected Benefit:** Makes the continuity principle honest and operational at its boundary.
- **Priority:** Low

## Future Ideas

1. **Cross-repository findings registry** — a single machine-readable registry (per FRAMEWORK_FINDINGS.md's own "until a dedicated cross-repository registry is established"), fed by the M3 schemas, rendered by the Publication Pipeline.
2. **Conformance test suite in Mission-Platform** — executable tests for the synthesis's listed invariants (unsupported claims, evidence mutation, contradiction preservation, authority transitions, extension isolation); Platform's first substantial code deliverable.
3. **Second steward** — the highest-leverage single mitigation available for R4/R5; CODEOWNERS plus one committed co-maintainer converts SUSTAINABILITY.md from aspiration to mechanism.
4. **MIAR admission criteria** — before expanding the Independent Examination Board further, define what an examiner organisation must provide (independence declaration, method statement, response SLA) and cap concurrent review tracks to triage capacity (C2).
5. **Recovery drill as a release gate** — before each future Foundation release, hand the tagged baseline to a fresh participant (human or AI) and measure reconstruction fidelity; adopt as the release's acceptance evidence (connects to Principia 16 and the Foundation examination's experiment proposals).

---

# Final Reflection

**What additional information would have enabled a better review?**

GitHub settings and history that repository contents cannot show: branch protection rules, PR review history (which changes were reviewed by whom before merge), issue traffic, and Pages deployment configuration — most governance claims are only verifiable there. Second: a runnable Python ≥3.11 environment to execute the Publication Pipeline test suite and reproduce a build manifest end-to-end. Third: the intent behind the post-v1.0 additions (MIAR, operational loaders, publication hub) — ADRs would have answered whether these are deliberate scope changes or velocity artefacts; their absence forced me to treat placement as a finding rather than a decision. Fourth: any record of the delegation instruments and of which AI produced which commit (commits are uniformly authored by the owner's identity, which hides the human/AI provenance the framework itself says should be visible).

**If I had one additional week, what would I investigate further?**

(1) Execute the full publication chain in both implementations (`mission-docgen` and `publication/build.py`) against the same sources, diff the outputs and manifests, and turn A3 from a structural finding into a measured one. (2) Run the replacement-participant recovery drill on mission-solar-eclipse per Principia 16 — reconstruct mission state from artefacts alone, score the reconstruction against the steward's account, and time it; this would be the first empirical test of Engineering Continuity. (3) Trace every cross-repository link and produce a link-integrity and pinning report (input to H3/H4 automation). (4) Perform a glossary-conformance sweep: every use of Mission, Evidence, Claim, Decision, Trust across all five repositories checked against the canonical definitions, quantifying residual drift after the v1.0 stabilisation. (5) Review the MIAR programme's content in depth — it was added mid-review and this assessment covers its existence and placement, not its design quality.
