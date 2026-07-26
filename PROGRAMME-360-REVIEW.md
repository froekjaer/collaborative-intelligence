# Collaborative Intelligence Programme 360 Review

**Review status:** Initial architecture and coherence review  
**Scope:** Collaborative Intelligence, Mission Framework, Mission Platform, Mission Solar Eclipse, TimeLapse Pro and Publication Pipeline  
**Purpose:** Establish a shared current-state picture and a controlled path toward dynamic programme documentation.

## Executive assessment

The programme has a strong conceptual foundation and a credible separation between programme vision, canonical semantics, implementation and publication. The strongest elements are Mission Framework's semantic ownership, the Framework Findings feedback mechanism, the explicit research posture and the complementary use of greenfield and brownfield reference cases.

The principal weakness is not lack of content. It is that programme growth has outpaced cross-repository status management. Repository descriptions, versions, roadmaps, reviews and active initiatives are not yet represented through one authoritative, machine-readable programme view. A new contributor must reconstruct the current state from several README files, open pull requests and historical documents.

**Overall condition:** sound architecture, incomplete programme control plane.

## Current repository map

| Repository | Intended role | Current visible condition | Main coherence risk |
|---|---|---|---|
| `collaborative-intelligence` | Programme vision, research architecture and shared method | Foundation v1.0; documents four concerns | Programme map omits Mission Platform and the brownfield validation track |
| `mission-framework` | Canonical semantics, principles and governance | Foundation v1.0 with substantial review and validation work | Roadmap, changelog and open PRs represent several generations simultaneously |
| `Mission-Platform` | Reusable technical implementation | Foundation 0.1 draft, documentation-first | Existing architectural material may predate the clarified semantic ownership and REVIEW-001 boundary |
| `mission-solar-eclipse` | Greenfield reference implementation | Foundation v1.0; first vertical slice pending | Must be clearly distinguished from platform development and from brownfield migration |
| `timelapse-pro` | Brownfield source system and evidence base | LAB/pre-production with extensive code and operational documentation | Its mature internal architecture may accidentally become the target platform architecture rather than evidence to be evaluated |
| `-Publication-Pipeline` | Reproducible publication and derived artefacts | Foundation v1.0 with working documentation generator | Programme-wide discovery and consistency reporting are not yet implemented |

## Confirmed strengths

### 1. Clear semantic ownership

Mission Framework is explicitly positioned as the canonical owner of normative terms, the Mission Loop, evidence semantics and governance rules. This is the correct boundary and should remain stable.

### 2. Evidence can challenge the framework

Mission Solar Eclipse is designed to evaluate the framework rather than demonstrate it uncritically. Framework Findings provide a legitimate return path from implementation evidence to canonical review.

### 3. Complementary validation strategies

The programme now has two distinct and necessary implementation tests:

- **Greenfield:** Mission Solar Eclipse tests creation from a clean starting point.
- **Brownfield:** TimeLapse Pro to Mission Timelapse tests understanding, preservation and reversible transformation of an existing system.

This distinction should be made explicit in every programme-level map and release plan.

### 4. Publication is separated from authority

Publication Pipeline correctly treats generated products as derived artefacts. This enables dynamic programme reporting without turning the generator into a semantic authority.

### 5. Human accountability is retained

Governance permits AI-assisted drafting, analysis and review while reserving consequential approval for identifiable accountable humans.

## Material findings

### F-001 — Programme map is incomplete

**Severity:** Major  
**Observation:** The Collaborative Intelligence README names Mission Framework, Mission Solar Eclipse and Publication Pipeline, but not Mission Platform or the brownfield TimeLapse transformation path.  
**Consequence:** New contributors receive an incomplete mental model of the programme.  
**Disposition proposed:** Update the programme architecture after review of this document.

### F-002 — No machine-readable programme state

**Severity:** Major  
**Observation:** Repository roles, versions, dependencies, active initiatives and canonical ownership are expressed only in prose.  
**Consequence:** The programme cannot generate a reliable current-state view or automatically detect contradictions.  
**Disposition proposed:** Introduce a versioned `programme.yml` schema owned by Publication Pipeline.

### F-003 — Version and roadmap drift

**Severity:** Major  
**Observation:** Mission Framework presents Foundation v1.0 while active roadmap, changelog and pull requests include v0.2, v0.9 and v1.1 narratives.  
**Consequence:** Released, proposed, historical and superseded states are difficult to distinguish.  
**Disposition proposed:** Establish one current-state document and classify open PRs as active, evidence-only, superseded or merge candidates.

### F-004 — Mission Platform baseline requires reconciliation

**Severity:** Major  
**Observation:** Mission Platform describes a Foundation 0.1 conceptual architecture, while Mission Framework has since clarified canonical semantic ownership and REVIEW-001 establishes a new platform/payload transformation exercise.  
**Consequence:** Existing platform documents may contain useful proposals, but their authority and compatibility are unclear.  
**Disposition proposed:** Treat existing Mission Platform main as a proposal/evidence baseline. REVIEW-001 reviewer branches should independently evaluate it, and accepted target architecture should be synthesised separately.

### F-005 — Greenfield and brownfield cases are not yet represented as one validation strategy

**Severity:** Moderate  
**Observation:** The repositories individually describe their roles, but the programme does not yet state why both implementation types are required.  
**Consequence:** Work may be prioritised as competing projects instead of complementary tests.  
**Disposition proposed:** Add a validation matrix to the programme map and generated 360 report.

### F-006 — Review material has overlapping locations

**Severity:** Moderate  
**Observation:** Mission Framework contains `review/`, `review-kit/`, `reviews/` and `pilot-reviews/`.  
**Consequence:** Binding templates, historical responses and active exercises are difficult to distinguish.  
**Disposition proposed:** Publish an explicit review hierarchy and classify each directory by authority and lifecycle.

### F-007 — AI provenance is inconsistently visible

**Severity:** Moderate  
**Observation:** AI systems have produced material, but commits generally identify the repository owner rather than the contributing system and validation state.  
**Consequence:** Attribution and review provenance can be reconstructed only from conversation history.  
**Disposition proposed:** Add optional `assisted_by`, `reviewed_by` and `decision_owner` metadata to programme artefacts and PR templates.

### F-008 — Dynamic reporting must not infer authority from prose alone

**Severity:** Critical design constraint  
**Observation:** A generator that guesses current state from README text, commit messages or AI interpretation would be fragile.  
**Consequence:** It could publish a convincing but incorrect programme picture.  
**Disposition proposed:** Separate declared manifest state from observed repository evidence and report discrepancies without silently resolving them.

## Target operating model

### Declared state

Each repository maintains a reviewed `programme.yml`. The owning repository is accountable for its declared role, version, lifecycle, dependencies and active initiative.

### Observed state

Publication Pipeline collects available repository metadata such as default branch, referenced documents, pull requests, tags and build status.

### Reconciliation

The generator compares declared and observed state and produces findings such as:

- declared version differs from primary README;
- roadmap points to an older lifecycle;
- dependency points to a missing repository or file;
- two repositories claim ownership of the same canonical concern;
- an active initiative has no current decision owner;
- generated publication sources do not record commit SHAs.

### Accountable disposition

The generator may identify and classify discrepancies. It must not decide semantic ownership, close work or alter declared state automatically.

## Recommended implementation sequence

1. Approve the programme architecture and repository ownership model.
2. Establish schema version 1 for `programme.yml` in Publication Pipeline.
3. Create pilot manifests for the six repositories in scope.
4. Generate a Markdown current-state report from a local source catalogue.
5. Add JSON Schema validation and deterministic tests.
6. Add optional GitHub collection with pinned revisions and graceful offline operation.
7. Generate diagrams, HTML and PDF through the existing publication process.
8. Add CI that reports drift but does not automatically rewrite owning repositories.
9. Update repository README files only after the generated view demonstrates the intended model.

## Immediate decisions proposed to the Mission Owner

These decisions are sufficiently supported to proceed as working assumptions, subject to pull-request review:

1. Collaborative Intelligence owns programme architecture and research direction.
2. Mission Framework owns canonical mission semantics and governance meaning.
3. Mission Platform owns reusable technical contracts and runtime implementation.
4. Mission Solar Eclipse is the primary greenfield reference implementation.
5. TimeLapse Pro is a read-only brownfield evidence source during REVIEW-001.
6. Mission Timelapse is the brownfield transformation target and a payload on Mission Platform.
7. Publication Pipeline owns the dynamic programme generator and manifest schema, but not the truth it publishes.

## Definition of done for the first 360 capability

The first release is complete when:

- all in-scope repositories have validated manifests;
- one command produces a deterministic Markdown programme report;
- the report identifies source repositories and revisions;
- declared and observed state are shown separately;
- the programme map includes both greenfield and brownfield validation;
- ownership conflicts and stale version pointers are reported;
- generated output contains no silently invented status or decision;
- a new contributor can identify programme purpose, repository roles, current baseline and next actions from one entry point.
