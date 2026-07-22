# Recommendations — Independent Architectural Review

---

## Critical

### REC-C1: Complete the Mission Solar Eclipse vertical slice before adding any new conceptual material

**Problem:** The programme has invested heavily in conceptual architecture (28+ framework documents, 40+ glossary terms, a proposed new discipline) while its first and only reference mission is still in the planning phase. Every new concept added before empirical validation increases the risk of building an internally consistent but practically useless framework.

**Evidence:** Mission Solar Eclipse repo was an empty README at v0.2 review time. It now contains mission plans, equipment profiles, and astronomical data — but zero operational results. The eclipse is August 12, 2026 (T-21 days). After that date, either the framework will have its first empirical evidence, or it will have lost its primary validation opportunity.

**Recommendation:** Freeze all new conceptual development in `mission-framework` until Mission Solar Eclipse returns at least 3 Framework Findings based on operational experience (not planning). This includes: no new glossary terms, no new principles, no new trust concepts, no new diagrams.

**Expected Benefit:** Forces the programme to test its ideas against reality — exactly what the framework's own Reality Principle demands. Either the framework survives contact with reality, or it identifies where it needs to change. Both outcomes are more valuable than another document.

**Priority:** Critical

---

### REC-C2: Resolve the Mission-Platform identity crisis

**Problem:** `Mission-Platform` is a repository that claims to be a "reference implementation" containing "schemas, APIs, tools and examples" — but contains none of these things. It is a collection of vision documents that restate framework concepts. A serious reviewer encountering this repo will conclude the entire programme is vapourware.

**Evidence:** README.md says "Reference implementations, schemas, APIs, tools and examples will follow." Not a single schema, API definition, or line of working code exists. ADR-0001 describes what the platform should do, not what it does.

**Recommendation:** Choose one:

A. **Archive the repository** and move its vision content into `mission-framework/docs/` as "Implementation Guidance." Recreate `Mission-Platform` only when schemas and code exist.
B. **Build the first schema within 7 days.** A JSON Schema for a Mission record, or a YAML model for Evidence, or anything machine-readable. If the repo has even one working schema, it has a reason to exist.

Option A is preferred — it reduces the programme's repository count from 5 to 4, eliminates the weakest repo, and concentrates effort where it belongs.

**Expected Benefit:** Removes the single biggest credibility liability in the ecosystem. Prevents future reviewers from dismissing the entire programme based on one empty repository.

**Priority:** Critical

---

### REC-C3: Fix cross-repo naming and establish a consistent convention

**Problem:** Five repositories use three different naming conventions. One has a known defect (leading hyphen). The programme proposes rigorous governance and consistency but does not demonstrate it in its own repository names.

**Evidence:** `collaborative-intelligence` (kebab), `mission-framework` (kebab), `Mission-Platform` (PascalCase), `mission-solar-eclipse` (kebab), `-Publication-Pipeline` (PascalCase with leading hyphen). AI_CONTEXT.md acknowledges the leading hyphen as "a repository naming defect."

**Recommendation:**
1. Rename `-Publication-Pipeline` to `publication-pipeline` (kebab-case, no leading hyphen)
2. Rename `Mission-Platform` to `mission-platform` (if REC-C2 option B is chosen; irrelevant if option A)
3. Document the naming convention in AI_CONTEXT.md

**Expected Benefit:** Eliminates a visible inconsistency. Demonstrates that the programme practices the governance discipline it preaches. Low effort, high symbolic value.

**Priority:** Critical (for the Publication Pipeline rename — it's a known defect)

---

## High

### REC-H1: Create a cross-repo CI integration

**Problem:** The programme's architecture describes integration between repositories (framework → platform → eclipse → publication) but no automated integration exists. A change in `mission-framework` doesn't trigger a Publication Pipeline build. There is no CI check that `mission-solar-eclipse` references valid framework terms.

**Evidence:** Each repo has its own CI (GitHub Pages workflows), but none communicate with each other. There is no integration test that verifies the cross-repo claims in AI_CONTEXT.md.

**Recommendation:** Create a simple GitHub Actions workflow in `collaborative-intelligence` that:
1. Clones all repos
2. Runs Publication Pipeline against mission-framework docs
3. Verifies that all cross-repo links resolve
4. Runs at least one conformance test (e.g., "mission-solar-eclipse uses only terms defined in GLOSSARY.md")

**Expected Benefit:** Catches cross-repo breakage early. Makes the "programme" real rather than aspirational. Relatively low effort — the Publication Pipeline already works locally.

**Priority:** High

---

### REC-H2: Consolidate the canonical Mission Loop and retire variants

**Problem:** At least nine different flow diagrams exist across the ecosystem with different terminology, steps, and no formal mapping to each other. The GLOSSARY.md requires variant diagrams to "state what they expand, omit or aggregate" — none do.

**Evidence:** See Finding A2 for the complete list.

**Recommendation:**
1. Retain ONE canonical Mission Loop in GLOSSARY.md.
2. For each variant diagram: either (a) remove it and link to the canonical loop, or (b) add an explicit mapping table: "This diagram expands steps X, Y, Z of the canonical loop. It omits A and B. It adds C, which is not in the canonical loop and should be read as domain-specific."
3. Add a CI check (REC-H1) that verifies no unlabelled loop variants exist.

**Expected Benefit:** Eliminates a major source of ambiguity. Makes the framework internally consistent with its own stated rules.

**Priority:** High

---

### REC-H3: Add a conformance test suite for the semantic model

**Problem:** The framework defines normative semantics (GLOSSARY.md) but has no way to verify that implementations conform. "Every mission must be recoverable by an independent participant from authoritative artefacts alone" — how would you test whether `mission-solar-eclipse` satisfies this?

**Evidence:** No test directory in `mission-framework`. Mission-Platform's "architecture-tests.md" is a markdown checklist, not executable tests.

**Recommendation:** Create a `mission-framework/tests/` directory with:
1. **Recovery test:** A script that reads the authoritative artefacts from a mission repo and asserts that core fields (purpose, objectives, evidence, decisions) are present and linked.
2. **Terminology test:** A script that scans reference mission repos for framework terms and flags usage that contradicts GLOSSARY.md definitions.
3. **Link test:** A script that verifies all cross-repo links in the ecosystem resolve to existing files.

Start with simple checks. Increase sophistication as the model stabilises.

**Expected Benefit:** Makes the framework's normative claims testable. Provides automated enforcement of the authority model. Demonstrates that the programme's principles apply to its own code.

**Priority:** High

---

### REC-H4: Address the programme's own continuity gap

**Problem:** ENGINEERING_CONTINUITY.md states "No human... shall be the sole carrier of mission-critical knowledge." The programme has a bus factor of 1. Peter is the sole repository owner and contributor.

**Evidence:** GitHub metadata. No other collaborators with write access.

**Recommendation:**
1. Add at least one other person with repository access (collaborator, not just reviewer).
2. Document the programme's own continuity plan: where are credentials stored? Who has access? What is the recovery procedure if the primary contributor becomes unavailable?
3. Treat this as a Framework Finding on the programme itself: does the framework's continuity principle apply to its own development?

**Expected Benefit:** Protects the programme from single-point-of-failure. Demonstrates that the programme's principles are not theoretical — they apply to the programme itself.

**Priority:** High

---

## Medium

### REC-M1: Reduce documentation redundancy in mission-framework

**Problem:** Extensive repetition across documents: the Reality Principle appears in 5+ files, the Mission Loop appears in 9+ variants, "Create what is needed" appears 8+ times.

**Evidence:** Previous z.ai review (RESPONSE-TEMPLATE.md §1, §4) documented specific overlaps.

**Recommendation:**
1. Merge TRUST.md into COMPUTATIONAL_TRUST_ENGINEERING.md (keep the latter).
2. Merge MISSION_THEORY.md's unique content into README.md; retire MISSION_THEORY.md.
3. Remove MISSION.md (root) — redundant with README.md.
4. Merge PURPOSE_VALUES_PHILOSOPHY.md's unique values into PRINCIPIA_MISSIONIS.md.
5. For each remaining document: state at the top what it covers that other documents do not.

**Expected Benefit:** Reduces the reading burden from ~28 to ~20 documents. Makes maintenance easier. Reduces version skew risk.

**Priority:** Medium

---

### REC-M2: Centralise review content in collaborative-intelligence

**Problem:** Review content is scattered across three repositories (`collaborative-intelligence/reviews/`, `mission-framework/reviews/`, `mission-solar-eclipse/reviews/`). A reader cannot see all programme-level reviews from one location.

**Evidence:** z.ai has reviews in `mission-framework/reviews/z-ai/` and `mission-solar-eclipse/reviews/z-ai/`. Mistral's review is in `publication-pipeline/reviews/mistral/`.

**Recommendation:** The `collaborative-intelligence/reviews/` directory should be the canonical location for ALL programme-level reviews. Repo-specific reviews (e.g., platform-only, pipeline-only) can stay in their repos. But any review that spans multiple repos should be centralised. Add a cross-repo review index that links to repo-specific reviews.

**Expected Benefit:** Single point of discovery for all review content. Makes the Independent Examination Board concept real rather than aspirational.

**Priority:** Medium

---

### REC-M3: Publish Mission Solar Eclipse as a living document via Publication Pipeline

**Problem:** The Publication Pipeline exists and works, but is not being used to publish the programme's own documentation.

**Evidence:** `mission-solar-eclipse` has content, but no `publication.yml`. The pipeline's `examples/minimal-mission` demonstrates the format but has no relationship to the actual missions.

**Recommendation:** Add a `publication.yml` to `mission-solar-eclipse` and configure a CI workflow that builds and deploys it via the Publication Pipeline. This would:
1. Test the pipeline against real (not example) content
2. Give the mission public documentation
3. Provide a working demonstration of the programme's own tooling

**Expected Benefit:** Dogfooding. The programme's own principles demand that it tests its tools against its own content.

**Priority:** Medium

---

## Low

### REC-L1: Add a "What Mission Framework Is Not" document

**Problem:** Reviewers and potential adopters may misinterpret the framework as an enterprise architecture framework, a project management methodology, or a software platform. The README addresses this in one section but not in enough detail.

**Evidence:** My own initial review noted the tension between claiming universality while using software-specific vocabulary.

**Recommendation:** Add a short document clarifying what Mission Framework is not: not a replacement for TOGAF, not a replacement for COBIT, not a software platform, not a project management methodology. Explain when to use it alongside existing frameworks vs. when it's not the right tool.

**Expected Benefit:** Reduces adoption confusion. Prevents the framework from being dismissed for not solving problems it never claimed to solve.

**Priority:** Low

---

### REC-L2: Version each repo independently with a scoped label

**Problem:** "Foundation Release v1.0" is applied across the ecosystem despite vastly different maturity levels. The programme's own VERSIONING.md warns against ambiguous labels.

**Evidence:** VERSIONING.md recommends "Mission Framework Semantics v0.3" etc. This guidance is not followed.

**Recommendation:** Apply scoped version labels per VERSIONING.md:
- `mission-framework`: "Mission Framework Semantics v0.3" (reviewed baseline, not validated)
- `mission-solar-eclipse`: "Mission Baseline v0.2" (planning phase)
- `-Publication-Pipeline`: "Publication Pipeline Tooling v0.1" (working code, limited scope)
- `collaborative-intelligence`: "Programme Architecture v0.1" (initial programme structure)

Reserve "v1.0" for when each repo has earned it independently.

**Expected Benefit:** Eliminates misleading version inflation. Provides accurate maturity signals to external readers.

**Priority:** Low

---

## Future Ideas

### REC-F1: Programme dashboard

Consider a simple static site (built by Publication Pipeline, deployed via GitHub Pages) that shows:
- Current mission status (Solar Eclipse: T-X days, planning phase)
- Latest Framework Findings
- Review submissions and disposition status
- Cross-repo CI status

This would make the programme visible and navigable from a single entry point.

---

### REC-F2: Blind reconstruction exercise

The framework claims missions should be recoverable from authoritative artefacts alone. Test this: give an AI that has never seen the programme only the authoritative artefacts from `mission-solar-eclipse`. Ask it to reconstruct the mission state. Compare its reconstruction to the actual state. Publish the result as a Framework Finding.

---

### REC-F3: Cross-framework comparison study

Commission independent comparison between Mission Framework's Reality-Evidence-Trust model and:
- TOGAF's Architecture Development Method
- SRE's Service Level Objectives and error budgets
- ISO 15288's technical processes
- The OODA loop (military decision-making)

Publish objective comparison. Identify where Mission Framework adds value and where existing frameworks are already sufficient.

---

### REC-F4: Publish the review synthesis as a publication

Once multiple independent reviews are collected and synthesised, use the Publication Pipeline to produce a "Review Synthesis" publication (PDF + web). This would demonstrate the pipeline's multi-format capability and provide a concrete output from the review process.
