# Baseline v0.1 Consensus Matrix

## Purpose

This matrix identifies findings that recur across the four independent reviews. Consensus is graded by reviewer coverage, but acceptance depends on evidence quality and architectural relevance rather than vote count.

## Matrix

| ID | Consolidated finding | Claude | Codex | Z.ai | Mistral | Consensus | Evidence assessment | Synthesis disposition |
|---|---|---:|---:|---:|---:|---|---|---|
| C-01 | The five-repository authority model is coherent and valuable | Yes | Yes | Yes | Yes | Strong | Directly supported by authority maps and repository role documents | **Accept and preserve** |
| C-02 | The ecosystem is conceptually mature but operationally immature | Yes | Yes | Yes | Yes | Strong | Direct repository-content evidence; only Publication Pipeline has meaningful executable code | **Accept** |
| C-03 | Mission Solar Eclipse must provide the first end-to-end empirical validation | Yes | Yes | Yes | Yes | Strong | All reviewers identify planning artefacts but no completed operational trace | **Accept as top programme objective** |
| C-04 | Cross-repository governance and traceability are documented but not mechanically enforced | Yes | Yes | Yes | Yes | Strong | No shared baseline manifest, semantic conformance suite or ecosystem CI | **Accept** |
| C-05 | Mission Platform is documentation-only and cannot yet be treated as an implemented platform | Yes | Yes | Yes | Yes | Strong | Repository contains architecture prose but no schema, API or runtime implementation | **Accept** |
| C-06 | Machine-readable semantics and record schemas are missing | Yes | Yes | Yes | Yes | Strong | No canonical schemas for glossary terms, findings, decisions or evidence records | **Accept** |
| C-07 | Semantic drift between Framework and Platform is a material risk | Yes | Yes | Yes | Yes | Strong | Overlapping definitions plus no executable compatibility boundary | **Accept; verify exact stale definitions before change** |
| C-08 | Repository naming and slug inconsistency are real defects | Yes | Yes | Yes | Yes | Strong | Actual slugs visibly differ from the invitation and from one another | **Accept; correct in controlled change** |
| C-09 | Programme maturity/version labels are uneven or potentially misleading | Yes | Yes | Yes | Yes | Strong | Different repositories use Foundation v1.0, 0.1 Draft and Sprint labels | **Accept; clarify scoped versioning** |
| C-10 | Governance automation and conformance tests are insufficient | Yes | Yes | Yes | Yes | Strong | Only Publication Pipeline has conventional tests; governance remains prose/manual elsewhere | **Accept** |
| C-11 | Documentation is strong but creates navigation and cognitive-load problems | Yes | Yes | Yes | Yes | Strong | Reviewers independently report distributed navigation, conceptual density and uneven maturity | **Accept; address through views and consolidation, not indiscriminate deletion** |
| C-12 | The Framework Findings process is one of the strongest governance mechanisms | Yes | Yes | Yes | Yes | Strong | Directly documented lifecycle and existing finding artefacts | **Accept and operationalize end to end** |
| C-13 | Cross-repository references are insufficiently pinned to immutable baselines | Yes | Yes | Yes | Yes | Strong | References use `main`, names or HEAD rather than coordinated tags/SHAs | **Accept** |
| C-14 | Brown-field adoption guidance is missing or insufficient | Yes | Yes | Yes | Yes | Strong | No staged migration guide or complete brown-field reference case | **Accept, but schedule after current consolidation and first validation slice** |
| C-15 | Practical onboarding and operational examples are insufficient relative to theory | Yes | Yes | Yes | Yes | Strong | Strong start-here material exists, but limited executable examples and runbooks | **Accept** |
| C-16 | Programme continuity depends too heavily on one steward | Yes | Partial | Yes | Partial | Broad | Git history and repository ownership show concentrated stewardship; exact collaborator settings were not fully visible | **Accept as governance risk with evidence caveat** |
| C-17 | Review material and review governance are becoming fragmented | Yes | Partial | Yes | Partial | Broad | Multiple `review`/`reviews` locations and duplicate reviewer structures are observable | **Accept and consolidate** |
| C-18 | Mission Framework's conceptual surface is growing faster than empirical validation | Yes | Yes | Yes | Yes | Strong | All reviewers identify conceptual load and validation gap, though tone differs | **Accept; institute a validation-first stabilization window** |
| C-19 | Publication Pipeline is the strongest current example of implementation discipline | Yes | Yes | Yes | Yes | Strong | Executable CLI, tests, CI, provenance intent and deliberately limited scope | **Accept as reference engineering pattern** |
| C-20 | The programme needs one reproducible cross-repository baseline definition | Yes | Yes | Yes | Yes | Strong | Review metadata itself demonstrates snapshot mismatch; multiple reviewers explicitly request a manifest or version contract | **Accept as immediate foundational action** |

## Strongest Positive Consensus

The reviewers agree that the project is not architecturally incoherent. Its principal strength is the explicit distribution of authority:

- Mission Framework owns canonical semantics.
- Mission-specific repositories own operational facts.
- Publication Pipeline owns derived publication behaviour.
- Collaborative Intelligence owns programme-level coordination.
- Mission Platform is intended to operationalize semantics without becoming a competing authority.

This separation should be preserved. The reviewers do not support collapsing the ecosystem into a single undifferentiated repository merely because implementation maturity is uneven.

## Strongest Negative Consensus

The central gap is not lack of ideas. It is the absence of a reproducible, executable bridge between the repositories.

The programme currently has:

- documented authority without a baseline manifest;
- normative semantics without schemas;
- traceability requirements without pinned cross-repository anchors;
- governance rules without consistent repository mechanics;
- a platform vision without executable conformance;
- a reference mission without a completed operational evidence loop.

## Consensus Interpretation

The reviews converge on a consistent architectural diagnosis:

> The ecosystem has a credible semantic and governance foundation, but its claims remain vulnerable until a small end-to-end mission slice, a cross-repository baseline contract and basic conformance automation demonstrate that the documented architecture works as a system.

This is not a recommendation to abandon the conceptual foundation. It is a recommendation to stop increasing its surface temporarily and convert selected concepts into evidence-producing mechanisms.