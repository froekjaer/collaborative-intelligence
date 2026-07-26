# Collaborative Intelligence Programme Architecture

## Purpose

This document defines the intended relationship between the repositories that form the Collaborative Intelligence research programme. It is a programme-level map, not a replacement for repository-specific architecture.

## Programme structure

```text
Collaborative Intelligence
        │
        ├── Mission Framework
        │     Canonical semantics, principles and governance
        │
        ├── Mission Platform
        │     Reusable technical implementation of framework semantics
        │
        ├── Reference missions
        │     ├── Mission Solar Eclipse — greenfield reference implementation
        │     └── TimeLapse Pro / Mission Timelapse — brownfield transformation case
        │
        └── Publication Pipeline
              Reproducible discovery, validation and publication
```

## Repository responsibilities

### Collaborative Intelligence

**Primary question:** Why does the programme exist, and how is it researched?

Owns:

- programme vision and research questions;
- programme architecture and repository roles;
- shared research posture and scientific method;
- cross-repository roadmap and programme-level findings;
- rules for programme-wide coherence.

Must not silently redefine canonical Mission Framework semantics or implementation contracts.

### Mission Framework

**Primary question:** What canonical concepts, principles and governance rules describe a governed mission?

Owns:

- canonical vocabulary and Mission Core;
- Mission Loop and normative semantic relationships;
- evidence, trust, authority and governance semantics;
- admission and change rules for canonical meaning;
- Framework Findings dispositions.

Must remain implementation-independent. Implementations may challenge it through evidence but may not redefine it locally.

### Mission Platform

**Primary question:** How can the framework be implemented as reusable technical capability?

Owns:

- schemas, contracts and validators implementing framework semantics;
- reusable runtime services, APIs and tooling;
- platform/payload boundaries;
- control-plane and data-plane architecture;
- reference implementation patterns for deployment, operation and evidence capture.

Must trace material platform concepts to Mission Framework and must return semantic ambiguity through Framework Findings rather than inventing canonical meaning.

### Mission Solar Eclipse

**Role:** Greenfield reference implementation.

Tests whether the programme can create a new, bounded and observable mission from purpose through outcome without legacy constraints. It should expose unclear, missing or unnecessary framework and platform concepts through operational evidence.

### TimeLapse Pro and Mission Timelapse

**Role:** Brownfield source system and transformation reference case.

TimeLapse Pro is the existing operational and engineering evidence base. During REVIEW-001 it is strictly read-only. Mission Timelapse is the future payload and migration target implemented through Mission Platform.

This case tests whether the programme can:

- understand an existing system without erasing its history;
- preserve critical behaviour, knowledge and evidence;
- distinguish platform capability from domain payload;
- migrate reversibly;
- demonstrate source-to-target traceability;
- improve architecture without losing necessary value.

### Publication Pipeline

**Primary question:** How is reviewed programme material discovered, checked, assembled and published reproducibly?

Owns:

- publication manifests and source maps;
- generators for programme maps and current-state reports;
- provenance records for generated artefacts;
- transformation and rendering logic;
- consistency checks between declared and observed programme state.

It does not own programme truth. It publishes declared state from owning repositories and reports discrepancies found through observable repository evidence.

## Dependency direction

```text
Programme vision
      ↓
Canonical semantics
      ↓
Platform contracts and services
      ↓
Mission implementations
      ↓
Observation and evidence
      ↓
Framework and programme findings
      ↓
Reviewed disposition
      ↓
Publication and external challenge
```

Dependencies should be explicit and predominantly flow downward for definitions and upward for evidence. Circular code dependencies between repositories are prohibited. Feedback loops occur through governed findings, not implicit coupling.

## Greenfield and brownfield validation

The two reference strategies are complementary:

| Strategy | Repository or case | Programme question |
|---|---|---|
| Greenfield | Mission Solar Eclipse | Can the framework and platform help create a new mission coherently from the beginning? |
| Brownfield | TimeLapse Pro → Mission Timelapse | Can they understand, preserve and transform an existing system without losing necessary capability or evidence? |

Neither case alone is sufficient evidence of general validity.

## Canonical ownership rules

1. Every material concept has one declared owning repository.
2. A consumer may specialise a concept but may not silently change its canonical meaning.
3. Runtime contracts belong to Mission Platform, even when they encode Mission Framework concepts.
4. Domain-specific facts and operating evidence belong to the mission that observed them.
5. Generated publications are derived artefacts and never become canonical by generation alone.
6. Cross-repository disagreements are recorded as findings, not hidden through local interpretation.

## Required programme metadata

Every participating repository should provide a machine-readable `programme.yml` containing:

- repository identity and role;
- lifecycle and current status;
- declared version or baseline;
- canonical ownership;
- dependencies and provided interfaces;
- current initiative and roadmap pointers;
- reference implementation type where applicable;
- publication sources and evidence outputs.

The schema and generator belong in Publication Pipeline.

## Programme control view

Publication Pipeline should generate a current programme view that distinguishes:

- **Declared state** — what each owning repository says is current;
- **Observed state** — what branches, documents, pull requests and releases show;
- **Discrepancies** — contradictions, stale pointers, missing manifests or unclear ownership;
- **Decisions required** — matters needing accountable human disposition.

This separation applies the programme's own Reality Principle to the programme itself.
