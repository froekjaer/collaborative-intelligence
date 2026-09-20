# Baseline v0.1 Conflicting Observations

## Purpose

This document records material disagreements among reviewers. The objective is not to choose a winner by preference, but to identify the evidence needed for a responsible architectural disposition.

## Conflict 1 — Preserve, freeze or archive Mission Platform

### Reviewer positions

- **Codex:** Preserve the federated model and formalize Framework-to-Platform compatibility before broad implementation.
- **Claude:** Update or freeze Platform because it contains stale semantics, while retaining useful architecture tests and meta-model assets.
- **Z.ai:** Archive Platform or build a schema immediately; archive is preferred.
- **Mistral:** Treat Platform as a sound reference model with insufficient implementation and establish a minimum viable implementation.

### Synthesis

The reviewers agree on the problem but differ on remedy. Platform is not yet an operational platform, and stale duplicated semantics create risk. However, immediate archival would remove useful architecture assets and pre-empt the intended product-to-platform path before it has been tested.

### Disposition

**Freeze and repair, do not archive.**

1. Add a clear status banner and canonical-authority notice.
2. Remove or map duplicated definitions to versioned Framework terms.
3. Produce one minimal machine-readable schema plus conformance fixture.
4. Reassess repository viability after the first vertical slice.

## Conflict 2 — Continue conceptual development or impose a freeze

### Reviewer positions

- **Z.ai:** Freeze all new conceptual development until the Solar Eclipse mission returns at least three operational Framework Findings.
- **Claude:** Apply a consolidation freeze until boundary, platform, review and baseline defects are corrected.
- **Codex:** Avoid broad platform commitments; continue only controlled vertical-slice experimentation and proposition management.
- **Mistral:** Proceed with cautious optimism and accelerate implementation while continuing the programme.

### Synthesis

A complete halt could block necessary corrections and operational guidance. Unrestricted growth would increase validation debt.

### Disposition

**Adopt a stabilization window, not a total freeze.** During the window, allow only:

- correction of contradictions and defects;
- baseline/release anchoring;
- governance and conformance mechanisms;
- operational artefacts required for Solar Eclipse;
- synthesis and disposition of existing findings.

Defer new universal principles, new repositories and broad conceptual taxonomies until empirical findings are available.

## Conflict 3 — Documentation is excellent or excessive

### Reviewer positions

- **Mistral:** Documentation is comprehensive, philosophically coherent and largely exemplary.
- **Codex:** Documentation is rich but distributed and difficult to reconstruct as one baseline.
- **Claude:** Documentation quality is high, but the semantic core is growing too rapidly and contains legacy contradictions.
- **Z.ai:** Framework is over-documented, repetitive and at risk of conceptual inflation.

### Synthesis

These positions are compatible at different levels. Quality of individual prose can be high while the total information architecture is burdensome.

### Disposition

**Preserve content until authority and uniqueness are mapped.** Create:

- a canonical document map;
- lifecycle metadata for normative, explanatory, operational and historical documents;
- mappings from variant diagrams to the canonical loop;
- audience-specific reading views.

Do not delete documents solely to reduce file count.

## Conflict 4 — Repository separation is working or eroding

### Reviewer positions

- **Mistral:** Separation creates clean, non-overlapping authority boundaries.
- **Codex:** Separation is justified and should be retained, but requires executable compatibility.
- **Z.ai:** Authority design is sound but weakly enforced.
- **Claude:** Boundary erosion has already begun inside mission-framework through publication and operational tooling.

### Synthesis

The declared architecture is coherent, but declarations and repository contents are no longer fully aligned.

### Disposition

**Preserve the federated architecture and correct the implementation of its boundaries.** The authority map remains the target architecture. Current placement defects require ADR-backed resolution.

## Conflict 5 — Priority of repository renaming

### Reviewer positions

- **Z.ai:** Treat the Publication Pipeline rename as critical because it is a known defect.
- **Claude:** Treat slug correction as medium priority.
- **Codex:** Treat it as medium priority with controlled migration.
- **Mistral:** Treat it as low priority.

### Synthesis

The defect is real, but it does not block empirical validation. Renaming can break automation and references if done without a baseline manifest and link checks.

### Disposition

**Medium priority.** First establish the baseline manifest and automated link validation, then perform controlled renames with redirects and compatibility checks.

## Conflict 6 — Version 1.0 is misleading or acceptable as a foundation label

### Reviewer positions

- **Z.ai:** Foundation v1.0 is misleading and should be replaced by scoped repository versions below 1.0.
- **Claude:** The baseline is irreproducible because it is not tagged and maturity differs by repository.
- **Codex:** Version and maturity labels are uneven and need a compatibility contract.
- **Mistral:** Different maturity labels create confusion, but the semantic foundation itself is high maturity.

### Synthesis

Two issues are mixed:

1. whether “Foundation v1.0” means operational maturity;
2. whether the exact foundation baseline can be reconstructed.

The second is an objective defect. The first is a communication problem.

### Disposition

**Retain historical labels but clarify scope.** Add coordinated immutable tags, a programme baseline manifest and explicit maturity dimensions. Do not rewrite history by pretending the release was never named.

## Conflict 7 — Framework Findings process is tested or untested

### Reviewer positions

- **Claude:** The findings/disposition machinery demonstrably works and has already driven semantic changes.
- **Codex:** The process provides a healthy route for implementation evidence to challenge theory.
- **Z.ai:** The process is well-designed but no finding has completed the full lifecycle.
- **Mistral:** The process is a mature governance strength but remains manual.

### Synthesis

The discrepancy likely reflects different reviewed snapshots and differing definitions of “complete lifecycle.” Review synthesis and disposition have occurred, but a full operational mission finding propagated across all affected repositories may still be absent.

### Disposition

**Classify as partially demonstrated.** The governance mechanism works in review-driven semantic evolution. It still requires an end-to-end operational finding from observation through disposition and propagated implementation change.

## Conflict 8 — Build one canonical loop or preserve multiple views

### Reviewer positions

- **Z.ai:** Retain one canonical Mission Loop and remove or explicitly map every variant.
- **Mistral:** Values visual aids and recommends more diagrams for accessibility.
- **Claude:** Notes multiple principle and document sets but does not call for one universal diagram.
- **Codex:** Emphasizes a versioned semantic anchor and generated ecosystem views.

### Synthesis

The conflict is not between one diagram and many diagrams. It is between governed views and uncontrolled variants.

### Disposition

**Keep one canonical semantic loop and permit multiple declared views.** Every non-canonical view must state what it expands, omits, aggregates or specializes.

## Conflict 9 — Immediate broad tooling or minimal conformance slice

### Reviewer positions

- **Mistral:** Recommends coordination tooling, dashboards, interactive examples and knowledge-management tooling.
- **Z.ai:** Recommends cross-repo CI and semantic tests, while warning against abstraction growth.
- **Codex:** Recommends a small baseline manifest and compatibility contract before broad implementation.
- **Claude:** Recommends lightweight governance automation and a first machine-readable schema.

### Synthesis

Broad tooling would risk reproducing the conceptual expansion problem in software. The high-value common denominator is small and testable.

### Disposition

**Implement the minimum conformance spine first:** baseline manifest, link checks, schema validation, glossary compatibility and one publication build. Defer dashboards and knowledge graphs.

## Overall Conflict Resolution Principle

Where reviewers disagree on scale, this synthesis prefers the smallest reversible intervention that:

- restores declared architectural boundaries;
- creates empirical evidence;
- improves reproducibility;
- avoids premature universalization;
- preserves useful work unless evidence supports removal.