# Executive Summary

**Reviewer:** Claude (Anthropic) · **Date:** 2026-07-22 · Commits per `Metadata.md`. Statements are labelled **[Fact]**, **[Assumption]**, **[Opinion]**, **[Recommendation]** per the call's working rules.

## Overall assessment

The ecosystem is an unusually disciplined documentation-first architecture programme with one real reference mission, one real implementation component, and a working multi-reviewer governance loop. Its declared architecture — five repositories with separated responsibilities (semantic core / programme / reference mission / publication tooling / platform) — is sound and clearly documented. **[Opinion, grounded in facts below]**

Its actual state has begun to diverge from its declared architecture. In the days following Foundation v1.0, the semantic-core repository (`mission-framework`) absorbed publication tooling, CI build code, per-AI operational integration guides and a new assurance programme (MIAR), while the repository designated to own tooling (`Mission-Platform`) has received no commits since before the v1.0 semantic changes and still contains definitions the project's own review synthesis agreed to remove. The single greatest architectural risk is therefore not design — it is boundary erosion under high solo-steward velocity, unchecked by any automation. **[Opinion, grounded in facts below]**

## Overall strengths

1. **Separation of concerns is explicitly designed and documented.** The authority map in `collaborative-intelligence/AI_CONTEXT.md` states per-concern ownership and the rule that no repository is authoritative for everything. **[Fact]** This is better architectural hygiene than most documentation programmes achieve. **[Opinion]**
2. **The governance loop demonstrably works.** External review findings from three AI reviewers were synthesised, dispositioned and implemented with traceability (`mission-framework/reviews/REVIEW-SYNTHESIS.md`; glossary, Core admission procedure, versioning policy all exist as a result). **[Fact]**
3. **The reference mission is real.** `mission-solar-eclipse` contains a charter with assessable objectives, decision records with alternatives and supersession (DEC-0001/DEC-0002), and the first genuine Framework Findings (FF-0001, FF-0002) — including a hard deadline (2026-08-12) that the project cannot negotiate with. **[Fact]**
4. **One component has crossed from prose to engineering.** `-Publication-Pipeline` contains an installable Python package (`mission-docgen`, pinned dependencies, pytest suite, ruff, CI on Python 3.11) and implements the provenance manifest its own finding FF-PUB-001 called for. **[Fact]**
5. **Institutional honesty.** `HISTORY.md` was rewritten to distinguish intentions from achievements; `review/KNOWN_LIMITATIONS.md` and `KNOWN_OPEN_QUESTIONS.md` are frank. **[Fact]**

## Overall weaknesses

1. **Boundary erosion.** `mission-framework` now contains `publication/build.py`, a publication CI workflow, `docs/operational/` per-AI loaders and `docs/publication/` — implementation and operational tooling inside the repository whose declared role is canonical semantics, duplicating the Publication Pipeline repository's declared responsibility. **[Fact]**
2. **Platform drift.** `Mission-Platform` (last commit `48e1cfc`) predates the v1.0 semantic corrections. It still defines Decision as made by "an authorised actor or mechanism", retains a loose Evidence definition and its own 12-principle set — all items the review synthesis marked as required work. **[Fact]**
3. **Structural duplication under velocity.** `reviews/REVIEW-SYNTHESIS.md` and `reviews/REVIEW_SYNTHESIS.md` coexist as different files; directories `z-ai/` and `zai/` coexist; `review/` and `reviews/` coexist; the deliverable location mandated by this call (`Review/`) collides with the existing `reviews/` in `collaborative-intelligence`. **[Fact]**
4. **Governance is prose-only.** No repository has CONTRIBUTING, CODEOWNERS, SECURITY.md, issue/PR templates, git tags or releases; no CI enforces links, naming, glossary conformance or finding-record formats. The glossary requires an ADR for Core definition changes, yet `mission-framework` has no ADR directory, and Principles 16–17 entered `PRINCIPIA_MISSIONIS.md` without one. **[Fact]**
5. **Bus factor of one.** All 114 commits to `mission-framework` are by a single human identity. The programme's own Engineering Continuity principle ("no single carrier of mission-critical knowledge") is satisfied for artefacts but not for stewardship. **[Fact]**

## Major risks

- **R1 — Semantic-core repository becomes a monorepo by accretion**, dissolving the ecosystem's central architectural claim. Likelihood: high at current velocity; already begun. **[Opinion]**
- **R2 — Platform becomes a semantic fork.** Stale canonical-sounding definitions in `Mission-Platform` will be quoted as authoritative. **[Opinion]**
- **R3 — Review-programme proliferation** (v0.2 `review/` package, `reviews/` board, MIAR, this architecture call) exceeds one steward's triage capacity, causing findings to be lost — the precise failure the Findings process exists to prevent. **[Opinion]**
- **R4 — Irreproducible baseline.** "Foundation Release v1.0" exists only as prose labels; without tags, the baseline cannot be checked out, cited or diffed. **[Fact as to absence; Opinion as to consequence]**
- **R5 — Steward unavailability halts the programme.** No second maintainer, no CODEOWNERS, no succession mechanics in repository form. **[Fact as to absence]**

## Overall architectural maturity

Using a conventional five-level lens: **conceptual architecture and governance design: level 3–4 (defined and partially managed); implementation: level 1–2 (initial, one component); enforcement/automation: level 1 (ad hoc); operational validation: level 1 (first mission in progress).** The programme is markedly mature in vocabulary and process design for its size, and immature in everything that requires either code or a second person. **[Opinion]**

## Overall recommendation

**Proceed — with a consolidation freeze.** Do not add new concepts, programmes or repositories until: (1) publication tooling is relocated or its placement re-scoped by an explicit ADR; (2) Mission-Platform is updated to v1.0 semantics or clearly frozen with a status banner; (3) the four review structures are consolidated under one index; (4) Foundation v1.0 is tagged in all five repositories; and (5) minimal governance automation (link check, naming lint, glossary-drift check) runs in CI. Detail and priorities in `Recommendations.md`. **[Recommendation]**
