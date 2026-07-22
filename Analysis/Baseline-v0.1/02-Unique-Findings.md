# Baseline v0.1 Unique Findings

## Purpose

This document records materially useful findings raised by only one reviewer, or developed with substantially greater specificity by one reviewer than by the others.

A unique finding is not weaker merely because it is unique. It requires separate evidence assessment because uniqueness may indicate either insight or overreach.

## Claude-Specific Findings

### U-C-01 — Boundary erosion inside `mission-framework`

**Finding:** Publication implementation, publication CI and AI operational integration material have accumulated inside the repository declared to own canonical semantics.

**Evidence quality:** High. Claude cites concrete paths, including `mission-framework/publication/build.py`, the publication workflow and `docs/operational/`.

**Assessment:** Accepted. This is more specific than the other reviewers' general drift concern and identifies a present architectural contradiction rather than only a future risk.

**Action implication:** Decide repository ownership by ADR. Do not move content mechanically until dependencies and publication implementation overlap have been mapped.

### U-C-02 — Two parallel publication implementations

**Finding:** `mission-framework/publication/build.py` and `-Publication-Pipeline` implement overlapping publication/provenance behaviour without a declared relationship.

**Evidence quality:** High for structural duplication; unverified for behavioural equivalence because neither implementation was executed side by side.

**Assessment:** Accepted as a structural finding. Functional duplication remains to be measured.

### U-C-03 — Mission Platform contains stale pre-v1.0 semantics

**Finding:** Platform documents retain definitions that conflict with the canonical glossary, including the accountable-authority treatment of Decision.

**Evidence quality:** High if the quoted files and reviewed commits are accurate.

**Assessment:** Accepted pending a targeted glossary-to-platform diff before modification.

### U-C-04 — Canonical change control is not following its own ADR requirement

**Finding:** The glossary requires ADRs for Core definition changes, while `mission-framework` lacks an ADR store and recent normative additions were not accompanied by ADRs.

**Evidence quality:** High.

**Assessment:** Accepted. This is a direct self-conformance defect.

### U-C-05 — Missing Delegated Authority instrument for the Mission Director

**Finding:** Mission records identify delegated authority, but no explicit instrument records scope, duration, revocation and accountability path.

**Evidence quality:** High for artefact absence in reviewed content; settings or private records were not visible.

**Assessment:** Accepted for the public programme record. This should be corrected before further consequential delegated decisions.

### U-C-06 — Duplicate review paths and near-duplicate names already exist

**Finding:** `review/`, `reviews/`, `Review/`, `REVIEW-SYNTHESIS.md`, `REVIEW_SYNTHESIS.md`, `z-ai/` and `zai/` create governance ambiguity.

**Evidence quality:** High.

**Assessment:** Accepted. This is realised structural drift, not a hypothetical scalability concern.

## Codex-Specific Findings

### U-X-01 — Common-cause provenance failure

**Finding:** Multiple generated or copied artefacts may all cite the same wrong source revision and appear mutually consistent.

**Evidence quality:** Conceptually strong but not demonstrated by a current incident.

**Assessment:** Accepted as a risk model. It adds an important distinction: internal consistency across derived artefacts is not independent corroboration.

### U-X-02 — Governance bypass under mission urgency

**Finding:** A real mission may require action before the formal finding/ADR cycle completes.

**Evidence quality:** Strong as an operational design concern; not yet observed as a failure.

**Assessment:** Accepted. The framework needs an expedited decision path that preserves retrospective traceability rather than pretending urgency will not occur.

### U-X-03 — Independent conformance implementations

**Finding:** A second independent validator should eventually test whether semantics are implementation-neutral.

**Evidence quality:** Sound architectural testing idea, but premature as immediate work.

**Assessment:** Retain as future validation after the first schema and conformance fixtures stabilize.

## Z.ai-Specific Findings

### U-Z-01 — Diagram proliferation violates the framework's own views rule

**Finding:** Numerous loops and diagrams use different steps and terminology without stating what they expand, omit or aggregate from the canonical Mission Loop.

**Evidence quality:** High if the listed diagrams remain current.

**Assessment:** Accepted. This is a concrete documentation-governance issue and should be addressed through mapping, not necessarily deletion.

### U-Z-02 — Programme governance authority is under-specified

**Finding:** Mission governance is defined more clearly than governance of the framework programme itself, including who makes final admission and dispute decisions.

**Evidence quality:** Moderate-high. Human approval is mentioned, but decision authority and escalation are not consistently formalized.

**Assessment:** Accepted. A programme governance charter is warranted.

### U-Z-03 — Mission Platform should be archived or immediately implemented

**Finding:** The repository's present form damages credibility and should either be archived or receive a schema quickly.

**Evidence quality:** High for implementation absence; the recommended binary remedy is opinionated.

**Assessment:** Partially accepted. The problem is valid; archiving is not yet accepted. A status freeze plus a minimal compatibility/schema deliverable is lower-risk and preserves useful architecture assets.

### U-Z-04 — Documentation should be aggressively consolidated

**Finding:** Several named framework documents should be merged or retired.

**Evidence quality:** Moderate. Repetition is real, but the proposed file-level mergers were not supported by a complete information-loss analysis.

**Assessment:** Do not accept the prescribed deletions yet. Accept the need for a canonical-document map and audience-specific views.

### U-Z-05 — The programme's continuity principle should be applied to itself as a Framework Finding

**Finding:** The programme should formally record its own bus-factor exposure as evidence challenging its continuity proposition.

**Evidence quality:** High as a governance observation.

**Assessment:** Accepted. This is an exemplary use of the framework against itself.

## Mistral Vibe Code-Specific Findings

### U-M-01 — Trust is consistently treated as a first-class architectural concern

**Finding:** Trust, provenance and uncertainty are applied coherently across repositories.

**Evidence quality:** Moderate-high. The cited documents support the theme, though the review is more affirmative than the others.

**Assessment:** Accepted as a positive characteristic, while keeping empirical claims about improved trust unproven.

### U-M-02 — Technology independence is a major positive property

**Finding:** The absence of a mandated stack supports replaceability and future evolution.

**Evidence quality:** High for documented intent; operational portability is untested.

**Assessment:** Accepted as a design objective, not yet as a validated outcome.

### U-M-03 — Accessibility and visual learning support are insufficient

**Finding:** Documentation is text-heavy and lacks explicit accessibility standards.

**Evidence quality:** Moderate. Text heaviness is observable; the ecosystem also contains multiple diagrams, so “limited use of diagrams” is less convincing.

**Assessment:** Partially accepted. Add accessibility requirements to publication profiles and documentation standards, but do not respond by adding more uncontrolled diagrams.

### U-M-04 — Community-building mechanisms are absent

**Finding:** External participation beyond reviews is limited.

**Evidence quality:** Moderate; repository content cannot reveal all private engagement.

**Assessment:** Retain as future programme development, not immediate architectural remediation.

## Unique Findings Rejected or Deferred

### Rejected as currently unsupported

- Claims that any specific terminology is circular without a current term-by-term semantic analysis.
- Claims that a test suite passes when the reviewer did not execute it and only inferred CI behaviour.
- Claims that current repository separation fully prevents conceptual drift; evidence shows separation is explicit but not mechanically enforced.

### Deferred pending empirical work

- Knowledge graph implementation.
- Second independent platform implementation.
- Broad community governance.
- Academic publication strategy.
- Claims that Computational Trust Engineering is or is not a distinct discipline.

## Synthesis Value of Unique Findings

The most important unique contributions are:

1. Claude's evidence of actual boundary erosion and stale Platform semantics.
2. Codex's common-cause provenance and urgency-bypass risk models.
3. Z.ai's identification of unmapped diagram variants and under-specified programme authority.
4. Mistral's explicit separation between strong conceptual properties and unvalidated operational outcomes.

These findings materially improve the synthesis beyond a simple majority summary.