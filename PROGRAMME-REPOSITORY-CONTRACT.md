# Programme Repository Contract

## Purpose

This contract defines the minimum relationship expected between repositories in the Collaborative Intelligence programme. It is a programme-governance proposal, not a replacement for repository-specific governance.

## Required declaration

Each participating repository SHOULD provide a versioned `programme.yml` compatible with the Programme 360 schema. A repository that must remain read-only MAY be represented by an external pinned declaration whose provenance and authority limitations are explicit.

The declaration should identify:

- programme and repository identity;
- repository role, lifecycle, status and version;
- concise purpose;
- concerns owned and explicitly not owned;
- capabilities consumed from and provided to other repositories;
- current baseline and initiative;
- greenfield, brownfield-source or brownfield-target status where applicable;
- publication sources and authority boundaries.

## Authority rules

### Collaborative Intelligence

Owns programme purpose, research questions, portfolio structure and cross-repository governance context.

### Mission Framework

Owns canonical Mission Core semantics, the Mission Loop, evidence and trust semantics, governance semantics and Framework Finding dispositions.

### Mission Platform

Owns reusable technical contracts, schemas, validators, services, runtime architecture and implementation evidence. It does not silently redefine framework semantics.

### Reference missions

Own mission-specific purpose, evidence, decisions, outcomes and local domain extensions. They return semantic findings to Mission Framework instead of changing canonical meaning locally.

### Publication Pipeline

Owns publication manifests, transformations, rendering, build provenance, output validation and derived Programme 360 generation. Generated output does not become source authority.

## Dependency direction

The preferred direction is:

```text
Programme purpose and research governance
                  ↓
Canonical semantics and governance
                  ↓
Reusable platform contracts and implementation
                  ↓
Mission-specific operation and evidence
                  ↓
Framework findings and programme learning
                  ↓
Traceable publication and external challenge
```

Feedback is expected, but authority must not become circular. Evidence may challenge an upstream model; it does not silently replace it.

## Change propagation

A material cross-repository change should record:

1. the owning repository and accountable decision-maker;
2. the changed version or pinned revision;
3. affected downstream repositories;
4. compatibility and migration consequences;
5. required validation or evidence;
6. publication consequences;
7. unresolved disagreement or residual risk.

## Declared and observed state

Programme 360 must distinguish:

- **Declared state** — the approved repository declaration.
- **Observed state** — versions, files, commits, pull requests, workflows and other evidence collected from repositories.
- **Finding** — a traceable difference, absence, conflict or uncertainty.
- **Disposition** — an accountable decision to correct, accept, defer, reject or investigate the finding.

The generator may report findings. It must not make the disposition on behalf of an accountable owner.

## Greenfield and brownfield

Greenfield and brownfield missions are complementary validation strategies.

- Greenfield tests whether programme semantics and platform capabilities help construct a new mission coherently.
- Brownfield tests whether the programme can understand, preserve and transform valuable existing behaviour, evidence and operating knowledge.

A brownfield source may be declared read-only. In that case, all target architecture and implementation work must occur in an explicitly designated target repository or branch.

## Publication

A publication must identify its source repositories and revisions. Editorial restructuring may improve accessibility, but semantic corrections must return to the owning repository. Programme 360 output should include its catalogue, manifests, revisions, generator version and build identity.

## Non-conformance

A repository does not become invalid merely because its declaration and observed state differ. The difference becomes a finding requiring proportionate investigation. Blocking severity should depend on impact, including semantic ambiguity, loss of evidence, broken compatibility, unsafe implementation or misleading publication.
