# Recommendations

## Critical

### Establish a cross-repository baseline manifest

- **Problem:** Current authority is documented but not mechanically reconstructed across repositories.
- **Evidence:** `AI_CONTEXT.md` provides an authority map; Publication Pipeline records local source hashes, but no shared programme manifest exists.
- **Recommendation:** Define a small, versioned baseline manifest listing repository URLs, commit SHAs, owning concern, compatible Framework version and entry-point files. Build it in CI without changing canonical source content.
- **Expected Benefit:** Reproducible reviews, recovery and publication; reduced semantic drift.
- **Priority:** Critical.

### Formalise Framework-to-Platform compatibility

- **Problem:** Mission Platform concepts overlap canonical Framework terms without executable conformance.
- **Evidence:** Platform MRM and Framework glossary define overlapping Mission, Objective, Evidence, Actor and Decision concepts.
- **Recommendation:** Before implementing platform services, create a compatibility specification and tests that bind each schema field and relationship to a specific Framework version and term.
- **Expected Benefit:** Prevents Platform from becoming a competing semantic authority.
- **Priority:** Critical.

## High

### Run a Solar Eclipse end-to-end evidence exercise

- **Problem:** The mission has detailed planning records but no completed trace from external observation through outcome and learning.
- **Evidence:** `mission-solar-eclipse/docs/README.md` marks observations and evidence for later population; plan identifies forecast and site-reconnaissance gaps.
- **Recommendation:** Select one bounded decision, preserve source snapshots, record the decision, action and outcome, then publish the resulting Framework Findings.
- **Expected Benefit:** Converts the programme's strongest claim into empirical evidence.
- **Priority:** High.

### Add ecosystem CI checks

- **Problem:** Cross-repository links, required documents and compatible versions can drift silently.
- **Evidence:** Current repositories have local documentation/CI patterns but no visible ecosystem test suite.
- **Recommendation:** Add a non-mutating CI job that resolves the baseline manifest, checks links and IDs, validates declared Framework versions, and builds the selected publication profile.
- **Expected Benefit:** Earlier detection of broken traceability and release mismatch.
- **Priority:** High.

### Define brown-field adoption guidance

- **Problem:** Existing organisations will often begin with fragmented documents, undocumented authority and incompatible toolchains.
- **Evidence:** Current material describes ideal governed artefacts but not an assessed migration path.
- **Recommendation:** Create a staged adoption guide: inventory, authority identification, minimum provenance, first decision record, first recovery drill and only then model extension.
- **Expected Benefit:** Makes the framework testable outside green-field repositories.
- **Priority:** High.

## Medium

### Separate propositions from normative terms

- **Problem:** Continuity and independent verification are useful but not yet empirically established as universal principles.
- **Evidence:** `docs/ENGINEERING_CONTINUITY_AND_INDEPENDENT_VERIFICATION.md` labels an initial proposition, while related language elsewhere is stronger.
- **Recommendation:** Maintain a dedicated proposition register with hypothesis, boundary conditions, measures, contradictory evidence and disposition.
- **Expected Benefit:** Preserves scientific humility and prevents theory from becoming policy by prose.
- **Priority:** Medium.

### Resolve the Publication Pipeline slug

- **Problem:** The leading hyphen is explicitly documented as a naming defect.
- **Evidence:** `AI_CONTEXT.md`.
- **Recommendation:** Plan a controlled repository rename with redirects, baseline-manifest update and link checks; retain compatibility aliases during transition.
- **Expected Benefit:** Less tooling friction and fewer integration errors.
- **Priority:** Medium.

## Low

### Add a visual ecosystem map generated from the baseline manifest

- **Problem:** The authority model is clear in prose but expensive to reconstruct visually.
- **Evidence:** Authority map exists in `AI_CONTEXT.md`.
- **Recommendation:** Generate a read-only graph showing repositories, authority boundaries, version dependencies and active reference missions.
- **Expected Benefit:** Better onboarding and review orientation.
- **Priority:** Low.

## Future Ideas

### Independent conformance implementations

- **Problem:** A single Platform implementation could embed its own interpretations of Framework semantics.
- **Evidence:** Mission Platform remains an unimplemented reference architecture.
- **Recommendation:** After the first schema stabilises, invite a second independent minimal implementation or validator using the same public conformance fixtures.
- **Expected Benefit:** Evidence that semantics are implementation-neutral rather than merely portable prose.
- **Priority:** Future Ideas.
