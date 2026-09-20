# Collaborative Intelligence — Programme Current State

> Draft programme control view. This document records the declared state proposed by ARCH-001 and must be reconciled with repository evidence before release.

## Current programme baseline

- Programme: Collaborative Intelligence
- Declared programme release: Foundation v1.0
- Programme authority: `froekjaer/collaborative-intelligence`
- Canonical semantic authority: `froekjaer/mission-framework`
- Reusable implementation authority: `froekjaer/Mission-Platform`
- Publication and derived programme-intelligence authority: `froekjaer/-Publication-Pipeline`

## Active validation paths

### Greenfield

`froekjaer/mission-solar-eclipse` tests whether Mission Framework can support a new, bounded and observable mission without inherited software constraints.

### Brownfield

`froekjaer/timelapse-pro` is the pinned, read-only source system for REVIEW-001. New architecture, implementation, tests and migration work belong in isolated reviewer branches of `froekjaer/Mission-Platform`.

The intended brownfield outcome is Mission Timelapse as a payload and reference mission on Mission Platform, not an in-place rewrite of TimeLapse Pro.

## Active initiatives

| Initiative | Owning repository | State | Purpose |
|---|---|---|---|
| Foundation v1.1 validation candidate | mission-framework | Draft PR | Move from conceptual foundation toward empirical validation |
| REVIEW-001 | mission-framework / Mission-Platform | Preparation | Independent brownfield architecture-and-build exercise |
| Solar Eclipse vertical slice | mission-solar-eclipse | Planned | First greenfield empirical challenge |
| Programme 360 | collaborative-intelligence / Publication Pipeline | Draft implementation | Dynamic cross-repository map, status and consistency report |

## Programme control rules

1. A repository owns only the concerns explicitly assigned to it.
2. Generated publications and Programme 360 reports are derived views, not new semantic authority.
3. Mission-specific findings remain local unless accepted through the Framework Findings process.
4. Canonical semantic changes are made only in Mission Framework.
5. Platform implementation choices must remain traceable to framework concepts and mission needs.
6. Brownfield source repositories remain unchanged when a review or migration exercise declares them read-only.
7. Declared state, observed evidence and accountable disposition must remain distinguishable.

## Immediate consolidation sequence

1. Review and approve the programme architecture and ownership boundaries.
2. Review the programme manifest schema and repository manifests.
3. Reconcile version and lifecycle declarations across repository READMEs, roadmaps and changelogs.
4. Classify and close superseded pull requests and branches without deleting review evidence.
5. Run Programme 360 against pinned repository revisions.
6. Publish the first generated programme map and consistency report.
7. Begin the Solar Eclipse greenfield slice and REVIEW-001 brownfield work under the agreed boundaries.

## Open decisions

- Whether Foundation v1.1 is a programme release, a Mission Framework release or both.
- How programme release compatibility is expressed across independently versioned repositories.
- Whether Mission Timelapse receives a separate repository or initially lives as a payload workspace in Mission Platform.
- Which repository owns the authoritative catalogue of pinned programme revisions.
- Which Programme 360 findings should block a release versus remain advisory.

## Status interpretation

This page is intentionally concise. Detailed rationale and findings are recorded in `PROGRAMME-ARCHITECTURE.md` and `PROGRAMME-360-REVIEW.md`. Once the generator is accepted, most of this page should be generated from repository manifests and observed evidence rather than maintained manually.
