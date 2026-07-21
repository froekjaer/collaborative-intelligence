# AI Context — Collaborative Intelligence

**Status:** Foundation Release v1.0  
**Purpose:** Authoritative onboarding context for a new AI or human contributor

## Start here

Collaborative Intelligence is the programme-level repository for an open research programme examining how people, artificial intelligence and governed systems may improve understanding and action together while preserving transparency, provenance, uncertainty, contestability and accountability.

A new contributor should read the repositories in this order:

1. [`collaborative-intelligence`](https://github.com/froekjaer/collaborative-intelligence) — programme vision, architecture and research posture
2. [`mission-framework`](https://github.com/froekjaer/mission-framework) — canonical semantics and governance of semantic change
3. [`mission-solar-eclipse`](https://github.com/froekjaer/mission-solar-eclipse) — first operational reference implementation
4. [`-Publication-Pipeline`](https://github.com/froekjaer/-Publication-Pipeline) — reproducible transformation of reviewed sources into publications

The leading hyphen in the current Publication Pipeline repository slug is a repository naming defect, not part of the project name.

## Authority map

| Concern | Authoritative repository | Rule |
|---|---|---|
| Programme vision and research architecture | `collaborative-intelligence` | Defines programme scope and relationships; does not own framework semantics |
| Canonical terminology and Mission Loop | `mission-framework` | Normative definitions belong here |
| Framework change process | `mission-framework` | Findings and Mission Core admission govern semantic change |
| Solar eclipse mission facts, plans and observations | `mission-solar-eclipse` | Operational truth and mission-specific decisions belong here |
| Publication transformations and output profiles | `-Publication-Pipeline` | Generated publications must remain traceable to reviewed sources |

No repository is authoritative for all concerns.

## Non-negotiable distinctions

A contributor must keep the following distinctions explicit:

- reality is not the same as an observation of reality
- observation is not automatically evidence
- evidence is not automatically knowledge
- a recommendation is not a decision
- a decision is not an action
- an output is not automatically an outcome or value
- AI-generated analysis is not empirical evidence merely because it is fluent
- a reference implementation may challenge canonical semantics but may not silently redefine them
- a publication may explain canonical material but does not become canonical by publication

## Reality rule

**Reality wins.** More precisely: when credible evidence contradicts a model, plan, claim or prior decision, the model must be revised or the contradiction must remain explicitly unresolved. Evidence must not be suppressed to preserve coherence.

## Version interpretation

Foundation Release v1.0 is a coordinated programme baseline across repositories. It does not mean that every theory, schema, implementation or publication tool has reached independent semantic or software maturity 1.0.

Repository-specific versions and review candidates must be interpreted within their own scope. See the versioning guidance in `mission-framework`.

## Expected AI behaviour

An AI working in this programme should:

1. identify which repository owns the concern before editing
2. read existing files before proposing changes
3. preserve source provenance and uncertainty
4. distinguish observed facts from assumptions and generated analysis
5. prefer improving existing structures over replacing them
6. submit semantic concerns as Framework Findings
7. avoid creating platform abstractions before the Solar Eclipse vertical slice demonstrates a real need
8. record exact source files and commit SHAs when producing derived material

## Current programme objective

The immediate objective is to build a small, traceable vertical slice in Mission Solar Eclipse that exercises the Mission Framework from mission purpose through observation, evidence, decision, action, outcome and learning, and then returns concrete Framework Findings.

The Foundation Release should therefore be treated as a stable starting contract for experimentation, not as proof that the framework has already been validated.
