# Baseline v0.1 Mission Framework Backlog

## Purpose

This backlog converts accepted synthesis recommendations into implementable work. It is intentionally limited to actions required to stabilize, validate and make the ecosystem reproducible.

## Backlog Conventions

- **P0:** Must be completed before claiming a reproducible baseline or proceeding with broad conceptual expansion.
- **P1:** Should be completed during the stabilization window.
- **P2:** Should follow the first empirical vertical slice.
- **Evidence of completion:** observable artefact or executable result, not a statement of intent.

## P0 — Baseline and Authority

### BL-001 — Create programme baseline manifest

- **Repository:** `collaborative-intelligence`
- **Deliverable:** machine-readable manifest listing all five repositories, exact commit SHAs, canonical role, Framework compatibility, entry-point documents and review version.
- **Acceptance evidence:** CI resolves every listed commit and verifies required entry points.
- **Depends on:** none.

### BL-002 — Tag the coordinated baseline

- **Repositories:** all five.
- **Deliverable:** immutable coordinated tags corresponding to the manifest.
- **Acceptance evidence:** each tag resolves to the SHA declared in the manifest.
- **Depends on:** BL-001.

### BL-003 — Publish programme authority and compatibility matrix

- **Repository:** `collaborative-intelligence`
- **Deliverable:** versioned matrix identifying authoritative concern, permitted derived representations and compatibility expectations.
- **Acceptance evidence:** every repository README links to the same versioned matrix.
- **Depends on:** BL-001.

### BL-004 — ADR: publication and operational content ownership

- **Repository:** `mission-framework`, with references from affected repositories.
- **Deliverable:** decision on ownership of publication implementation, publication CI and AI operational integration documents.
- **Acceptance evidence:** one primary implementation is identified; duplicate or consumer roles are documented.
- **Depends on:** BL-003.

### BL-005 — Create ADR mechanism in Mission Framework

- **Repository:** `mission-framework`
- **Deliverable:** ADR directory, template, index and governance rule.
- **Acceptance evidence:** BL-004 and future Core changes use the mechanism.
- **Depends on:** none.

## P0 — Review and Governance Consolidation

### BL-006 — Create canonical review index

- **Repository:** `collaborative-intelligence`
- **Deliverable:** index of all programme-level and repository-specific reviews, locations, reviewers, versions, status and dispositions.
- **Acceptance evidence:** no active review track is discoverable only through an unindexed directory.
- **Depends on:** none.

### BL-007 — Standardize review directory convention

- **Repositories:** all affected repositories.
- **Deliverable:** one documented convention; legacy paths retained through links or migration notes where needed.
- **Acceptance evidence:** duplicate `review`/`reviews`/`Review` authority ambiguity is removed.
- **Depends on:** BL-006.

### BL-008 — Programme governance charter

- **Repository:** `collaborative-intelligence`
- **Deliverable:** named decision authority, admission authority, escalation/dispute process, delegated authority rules and change approval classes.
- **Acceptance evidence:** consequential programme decisions can be traced to an authorized role and record type.
- **Depends on:** BL-003.

## P0 — Platform Safety

### BL-009 — Freeze and label Mission Platform state

- **Repository:** `Mission-Platform`
- **Deliverable:** status banner stating maturity and canonical authority precedence.
- **Acceptance evidence:** every entry-point document warns against treating duplicated definitions as normative.
- **Depends on:** BL-003.

### BL-010 — Framework-to-Platform semantic diff

- **Repository:** `Mission-Platform`
- **Deliverable:** term-by-term compatibility table for overlapping concepts.
- **Acceptance evidence:** stale or conflicting definitions are identified with disposition.
- **Depends on:** BL-009.

### BL-011 — First machine-readable compatibility schema

- **Repository:** `Mission-Platform`
- **Deliverable:** one minimal schema for a bounded record type, linked to Framework terms and version.
- **Acceptance evidence:** valid and invalid fixtures pass/fail in CI.
- **Depends on:** BL-010.

## P1 — Conformance Spine

### BL-012 — Ecosystem CI workflow

- **Repository:** `collaborative-intelligence`
- **Deliverable:** workflow that checks out manifest commits, validates entry points, checks links and executes conformance checks.
- **Acceptance evidence:** intentionally broken fixture causes a failed run.
- **Depends on:** BL-001, BL-011.

### BL-013 — Naming and structure lint

- **Repositories:** all five or centrally through BL-012.
- **Deliverable:** checks for forbidden duplicate naming patterns and directory conventions.
- **Acceptance evidence:** near-duplicate review file/directory fixtures are detected.
- **Depends on:** BL-007, BL-012.

### BL-014 — Glossary compatibility check

- **Repository:** `mission-framework` or central conformance tooling.
- **Deliverable:** initial rule set that flags probable redefinitions of canonical terms outside approved locations.
- **Acceptance evidence:** known stale Platform definition is detected.
- **Depends on:** BL-010, BL-012.

### BL-015 — Cross-repository publication build

- **Repository:** `collaborative-intelligence` CI using Publication Pipeline.
- **Deliverable:** build one selected profile from pinned mission/framework inputs.
- **Acceptance evidence:** generated manifest records exact source revisions.
- **Depends on:** BL-001, BL-004, BL-012.

## P1 — Solar Eclipse Validation

### BL-016 — Define bounded end-to-end evidence exercise

- **Repository:** `mission-solar-eclipse`
- **Deliverable:** one decision selected for full trace from external observation through evidence, decision, action, outcome and learning.
- **Acceptance evidence:** approved mission decision record names required artefacts and success criteria.
- **Depends on:** BL-001.

### BL-017 — Create Delegated Authority instrument

- **Repository:** `mission-solar-eclipse`
- **Deliverable:** delegation record for Mission Director scope, validity, oversight, revocation and accountability.
- **Acceptance evidence:** consequential decision records reference it.
- **Depends on:** BL-008.

### BL-018 — Execute and publish vertical slice

- **Repository:** `mission-solar-eclipse`
- **Deliverable:** complete evidence trace and resulting Framework Findings.
- **Acceptance evidence:** at least one finding completes observation, review, disposition and propagation or explicit deferral.
- **Depends on:** BL-016, BL-017.

### BL-019 — Recovery drill

- **Repository:** `mission-solar-eclipse` with report in `collaborative-intelligence`.
- **Deliverable:** independent cold-start reconstruction from authoritative artefacts.
- **Acceptance evidence:** measured completeness, errors, assumptions and recovery time.
- **Depends on:** BL-018.

## P1 — Knowledge and Documentation Control

### BL-020 — Canonical document map

- **Repository:** `mission-framework`
- **Deliverable:** map of normative, explanatory, operational and historical documents with authority and audience.
- **Acceptance evidence:** every framework document is classified and linked.
- **Depends on:** none.

### BL-021 — Mission Loop view registry

- **Repository:** `mission-framework`
- **Deliverable:** canonical loop plus registry mapping each variant's expansions, omissions, aggregations and specializations.
- **Acceptance evidence:** no active loop diagram remains unclassified.
- **Depends on:** BL-020.

### BL-022 — Standard document metadata

- **Repositories:** initially Mission Framework and Mission Platform.
- **Deliverable:** status, version, owner, authority class and last-reviewed header convention.
- **Acceptance evidence:** CI validates metadata for normative documents.
- **Depends on:** BL-020, BL-012.

### BL-023 — Structured finding and decision schemas

- **Repository:** `Mission-Platform` or dedicated conformance area by ADR.
- **Deliverable:** canonical schemas and fixtures for findings and decisions.
- **Acceptance evidence:** existing records can be validated or have documented migration gaps.
- **Depends on:** BL-011, BL-018.

## P1 — Continuity and Operational Governance

### BL-024 — Programme continuity Framework Finding

- **Repository:** `collaborative-intelligence`
- **Deliverable:** finding recording stewardship concentration and continuity exposure.
- **Acceptance evidence:** formal disposition and mitigation owner.
- **Depends on:** BL-008.

### BL-025 — Recovery and succession plan

- **Repository:** `collaborative-intelligence`
- **Deliverable:** non-secret recovery procedure, stewardship succession roles and dependency register.
- **Acceptance evidence:** second authorized participant can complete a defined recovery task.
- **Depends on:** BL-024.

### BL-026 — Expedited decision path

- **Repository:** `mission-framework` and mission template.
- **Deliverable:** process for urgent decisions with bounded authority, minimum evidence and mandatory retrospective review.
- **Acceptance evidence:** Solar Eclipse exercise tests or simulates the path.
- **Depends on:** BL-008, BL-017.

## P2 — After First Empirical Findings

### BL-027 — Brown-field adoption guide

- **Deliverable:** staged inventory-to-first-finding method for existing systems.
- **Acceptance evidence:** applied to one bounded existing system.

### BL-028 — Documentation consolidation based on usage evidence

- **Deliverable:** merge/retire decisions supported by document map, overlap analysis and recovery/onboarding evidence.
- **Acceptance evidence:** no authoritative content is lost and links remain valid.

### BL-029 — Controlled repository rename

- **Deliverable:** rename defective slugs after link and baseline automation exists.
- **Acceptance evidence:** redirects, manifests, CI and documentation all resolve.

### BL-030 — Baseline v0.2 controlled review

- **Deliverable:** repeatable review package using an immutable manifest and improved evidence rules.
- **Acceptance evidence:** reviewers demonstrably assess the same repository commits.

## Stabilization Exit Criteria

The stabilization window can end when:

1. one coordinated baseline is immutable and reproducible;
2. repository authority boundaries are aligned with actual content or explicitly redefined;
3. Mission Platform cannot silently contradict canonical semantics;
4. review governance has one discoverable index;
5. minimum conformance CI is running;
6. one Solar Eclipse evidence trace has produced dispositioned learning;
7. the programme has recorded and addressed its own continuity exposure.

Until these criteria are met, new universal concepts and new repositories should require explicit exceptional approval.