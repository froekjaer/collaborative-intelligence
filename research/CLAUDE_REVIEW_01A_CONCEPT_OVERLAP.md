# Claude review 01A: Overlap with existing Mission Framework concepts

**Status:** Advisory peer review (Claude, 2026-11-15). Not canonical.
**Baseline:** mission-framework `9a1a45435ed0781f987760b00722d4a7700d5052` (`GLOSSARY.md`, `docs/ARCHITECTURE.md`); collaborative-intelligence `52eb8c9`.
**Question reviewed:** Does the five-check model in [Cross-corpus synthesis 01 §B](./CROSS_CORPUS_SYNTHESIS_01_BENEFICIAL_AUTONOMY.md) add anything beyond existing framework semantics and established engineering practice?

## Finding

Most of the model is a **relabelling**. Only a small residue is a genuine gap.

| Synthesis check | Already in Mission Framework | Established external concept | Residual gap? |
|---|---|---|---|
| Purpose | GLOSSARY *Mission* (accountable authority, objectives, scope) | Purpose limitation (GDPR Art. 5(1)(b)) | Small. Purpose cannot be machine-verified, so it has to be operationalised as scope, not as inferred intent |
| Provenance | GLOSSARY *Evidence* and *Claim* (provenance, status, time) | Information-flow control, taint tracking | Applying provenance to *instructions*, not only to evidence |
| Authority | GLOSSARY *Delegated Authority* (scope, permitted actions, validity period, conditions, oversight, revocation, accountability path); *Actor does not confer authority*; ARCHITECTURE "AI is evidence, not authority" | Least privilege, capability security | **Re-delegation:** may a delegate delegate further, and must bounds be narrowed at each hop? The glossary is silent on this |
| Composition | Not explicit | Reference monitor holding cumulative state; confused-deputy problem | **Yes**, especially across organisations where no shared enforcement point exists |
| Evidence | GLOSSARY *Evidence* (append-only), Decision ≠ Action | Audit, non-repudiation | Little. The question is whether audit *coverage* extends to spawned or delegated work |

## Strongest argument that the model adds nothing new

Every check maps to an existing primitive or a well-known security principle. Publishing it as a "causal model" would breach preamble principle 6 (search before creating) and could fragment the vocabulary.

## What is worth keeping

The model is useful as a **review checklist** that ties security controls to the framework's existing *Decision* and *Delegated Authority* semantics. That cross-disciplinary bridge is valuable. A new primitive is not needed.

## Candidate Framework Findings (do not admit yet; for evaluation only)

1. **Re-delegation semantics.** Does *Delegated Authority* permit onward delegation, and must the bounds narrow monotonically at each hop?
2. **Cumulative constraints.** How does a *Mission* express limits that apply to the sum of several delegated actions, such as total spend or total data released?
3. **Coverage of derived work.** Do oversight and evidence obligations follow work that a delegate spawns or hands on?

Each of these should be phrased as a gap in the existing terms, not as a new concept.

## Recommended edits to research memos

- **Synthesis §B:** Rename it from "minimal causal model" to "review checklist mapped to existing framework terms", and add this mapping table. Confidence: high.
- **ISC memo §5 and Devoteam intake:** Before proposing "agreements as versioned objects", test whether *Delegated Authority* plus *Decision* records already express it. Confidence: medium.
