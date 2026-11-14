# ISC-CPH 2026 — Research memo 01: Human–AI reciprocal intelligence and accountable autonomy

**Status:** Preliminary, source-grounded qualitative research memo — **not** a completed comprehensive psychological analysis, systematic literature review or validated finding.  
**Date:** 2026-11-15  
**Corpus:** ISC-CPH 2026 Danish Track day 1; Main Track days 1, 2 and 3 (four machine-transcribed Markdown files; approximately 196,500 words).  
**Method:** Initial session inventory and cross-track targeted reading of timestamped passages. All four files were directly reopened. Coverage is **selective**, not exhaustive: every talk has been indexed, but not every utterance has been interpreted. No claims about individual psychology, intent or the population beyond this conference are warranted.

## 1. Research question and epistemic stance

How can humans and multiple AI systems learn, disagree, coordinate, negotiate, decide and act together without eroding agency, expertise, diversity, accountability or mission integrity?

Conference statements are **data about participants' models, assumptions and professional concerns**, not independent proof that those assumptions are true. The memo records observations separately from interpretation, rival explanations and experiments. Time codes are relative to each recording, not wall-clock time. Automated transcription can be inaccurate; quotes below are paraphrased rather than represented as verbatim human-verified quotations.

The research deliberately includes **Human→AI, AI→Human, AI→AI and AI-mediated Human↔Human** relations. For AI→AI, distinguish hypothetical future agency from demonstrated autonomous interactions in the corpus.

## 2. Initial evidence ledger — four source files

| ID | Recording and time | What is observable in the transcript | Interpretive hypothesis, not fact |
|---|---|---|---|
| DK-01 | Danish Track, 00:22:21 | Opening explicitly urges participants to listen, ask questions and meet people with different skills and views. | Epistemic diversity is an articulated social norm; test whether it is practised under conflict. |
| DK-02 | Danish Track, 00:39:06 | A story about creative technical workarounds connects benign efficiency-seeking with actions outside intended system design. | Optimisation can bypass assumed boundaries without malicious intent; analogy to agent specification gaming, **not evidence of AI doing so**. |
| DK-03 | Danish Track, 05:19:33 | Supplier discussion contrasts IT security KPIs with OT continuity and uptime priorities. | Different local objectives can generate system-level conflict even among well-intentioned actors. |
| DK-04 | Danish Track, 06:12:20 | Discussion questions whether methods and frameworks help without appropriate organisational intent and capacity. | Governance artefacts may be performative if not connected to operational incentives and ability to act. |
| DK-05 | Danish Track, 07:44:00 | A speaker explicitly distinguishes meanings of control and links quality, security and resilience. | Shared vocabulary may hide incompatible mental models; develop a semantic disambiguation test. |
| M1-01 | Main day 1, 00:08:34 | CTF introduction expects AI use but encourages people to engage their own brains and learn. | Performance and learning are distinct objectives; AI-assisted success need not imply skill acquisition. |
| M1-02 | Main day 1, 05:37:09 | Workforce panel warns that AI-generated output can create the appearance of expertise without fundamentals. | Possible automation bias and expertise illusion; alternative: AI may enable genuine accelerated learning. |
| M1-03 | Main day 1, 05:40:26 | Panel describes faster CTF completion with AI and debate about AI-restricted competitions. | Compare task performance, retained knowledge and transfer to novel problems. The anecdote is not a controlled study. |
| M1-04 | Main day 1, 06:47:29 | Speaker argues AI shifts governance boundaries and reiterates human-in-the-loop. | 'Human in the loop' is a proposed safeguard, not proof of effective human authority. |
| M1-05 | Main day 1, 07:40:15 | AI-in-industrial-operations talk calls for data integrity, granular read/write governance and independently verifiable commands. | Technical enforcement at action boundaries is a plausible complement to normative instructions. |
| M2-01 | Main day 2, 00:09:06–00:10:39 | Moderator explicitly raises workforce uncertainty, welcomes newcomers and solicits mentors. | Professional identity, mentoring and intergenerational transmission matter to AI adoption. |
| M2-02 | Main day 2, 01:33:42 | Presenter says engineering decisions should remain human and rejects autonomous operation in a safety-critical setting. | Domain-specific autonomy boundaries may be justified by irreversibility and safety consequence. |
| M2-03 | Main day 2, 03:34:01 | Audience question warns that local models and their weights can be altered, potentially influencing decisions. | Sovereignty/local hosting trades some external dependencies for local integrity and maintenance obligations. |
| M2-04 | Main day 2, 05:39:21 | Session explicitly stages disagreement about whether AI belongs inside an OT environment. | Disagreement is substantive, not simply ignorance or resistance; test differing risk models. |
| M2-05 | Main day 2, 07:50:37 | Presenter describes developing a protocol-focused ML tool with another person and mentions explainability. | Collaborative learning involves human guidance, tooling and interpretability; no evidence of independent AI-to-AI agreements here. |
| M3-01 | Main day 3, 00:10:00 and 00:38:05 | Speaker challenges assumptions about the value/timing of OT detection and invites disagreement. | An explicit counter-model can improve collective reasoning if challenged with operational counterexamples. |
| M3-02 | Main day 3, 01:09:27 | Speaker raises risks of compromised model/training data affecting operational decisions. | Model supply-chain integrity is a dependency of trustworthy autonomy; specific claims need external verification. |
| M3-03 | Main day 3, 04:20:01 | Discussion questions whether live OT penetration tests are justified given operational safety risk. | Knowledge acquisition has physical costs; experimental ethics and safe test environments are essential. |
| M3-04 | Main day 3, 06:10:31 | Speaker questions governance, education and leadership when AI influences decisions. | Human agency may be diminished by institutional incentives, not merely model behaviour. |
| M3-05 | Main day 3, 06:15:18 | Speaker distinguishes levels including autonomous decisions across ecosystems and asks when autonomy should be allowed. | Cross-system decision authority is an explicit professional concern; **not proof that such autonomy was demonstrated**. |

## 3. Cross-cutting tensions (early analytic coding)

### A. Efficiency versus learning
CTF comments (M1-01–03) make it possible to ask whether AI is making practitioners more capable or simply more productive. Competing hypotheses: (H1) AI assistance improves learning by feedback and scaffolding; (H2) it masks lack of fundamentals; (H3) effects depend on pedagogy and task design. Test with delayed, AI-free transfer tasks.

### B. Human control as aspiration versus effective control
Speakers endorse human-in-the-loop (M1-04, M2-02) while discussing autonomous operations (M3-05). A person nominally approving an AI recommendation may not have time, evidence or practical ability to dissent. Test with decision latency, override rates, explanation quality and simulated high-pressure scenarios.

### C. Local optimisation versus global constraints
IT/OT KPI tension (DK-03) and human technical workarounds (DK-02) provide **human analogues** for multi-agent failures. They motivate, but do not empirically establish, AI-to-AI compositional policy violations. Test agents with independently permitted subtasks whose combined result breaches privacy, safety or contractual constraints.

### D. Trust as social practice versus enforceable property
Open disagreement (DK-01, M3-01) and independent command verification (M1-05) suggest two complementary requirements: deliberative challenge and external technical enforcement. Neither alone guarantees correctness or legitimacy.

### E. Sovereignty versus responsibility
Local models may support data control, yet integrity and operations shift to the operator (M2-03). Compare cloud/local/hybrid configurations under matched threat and governance models rather than assuming one is intrinsically safer.

### F. Safety and reversibility
M2-02 and M3-03 distinguish high-consequence physical operations from low-impact experimentation. An autonomy framework should separate discovery, communication, nonbinding negotiation, delegation, decision and execution rather than use a single 'autonomous/not autonomous' switch.

## 4. AI-to-AI research gap

The sampled conference passages raise autonomy, AI-enabled decisions and governance. They **do not yet demonstrate** agents independently finding one another, forming agreements, colluding, breaching agreements or concealing rule-breaking. Those are research hypotheses from the programme discussion and require separately sourced literature and controlled experiments.

Proposed scenarios:
1. **Discovery and counterpart trust:** Can agents authenticate an unknown peer and identify its authority before exchanging data?
2. **Delegation boundary:** Can an agent obtain a forbidden capability indirectly by assigning a task to a peer?
3. **Compositional violation:** Can locally compliant actions jointly breach a global confidentiality, budget or safety rule?
4. **Agreement breach:** What observable event constitutes a broken inter-agent commitment, and which entity is accountable?
5. **Correction and dissent:** Can an agent challenge an invalid policy or unsafe request without unilaterally violating it?
6. **Emergent coordination:** Does repeated interaction create norms or correlated failures not present in isolated runs?

Use externally enforced permissions, isolated simulated environments, independent monitoring, and counterfactual baselines. Distinguish apparent deception from stochastic failure, ambiguity and specification error.

## 5. Provisional architecture mapping

Before inventing new framework primitives, map hypotheses to the existing Mission Framework: mission constraints; actor identity; policy engine; decision/action distinction; evidence provenance; audit; human accountability. Potential gaps to investigate: **agent discovery and peer authentication; agreements as versioned objects; delegation chain and revocation; cumulative cross-agent constraints; observable violation and remediation; system-wide authority attribution**. This is a gap hypothesis, not a completed architecture audit.

## 6. Scientific protocol for the next pass

1. Segment and index **every substantive session** of all four recordings, including discussion and audience questions.
2. Code each segment using a published codebook: speaker claim, metaphor, underlying assumption, counterclaim, psychological construct, social context, consequence, and epistemic status.
3. Sample disconfirming material deliberately. Preserve quotations and exact timestamps, check ambiguous transcription against audio/slides before publication.
4. Use at least two independently reasoned coding passes and document disagreements; no invented inter-rater reliability.
5. Compare constructs against peer-reviewed psychology, HCI, multi-agent systems, safety engineering and governance literature; do not confuse literature claims with conference claims.
6. Pre-register falsifiable experiments and test human-only, AI-only, human–AI and multi-agent conditions.
7. When BSides transcripts arrive, treat them as a **new corpus**: code initially without forcing the ISC categories, then compare convergence, contradictions and new categories.
8. Respect Chatham House Rule and confidential audience contributions; avoid personal psychological diagnosis.

## 7. What can and cannot be concluded now

**Supported by direct transcript inspection:** The conference includes substantive, sometimes conflicting concerns about human competence, AI-assisted performance, operational safety, governance, trust, AI data integrity, human authority and cross-ecosystem autonomy.

**Interpretive, not established:** These tensions may illuminate reciprocal intelligence and accountable autonomy; a cross-disciplinary psychological theory is not yet demonstrated.

**Not yet established:** The full corpus has been read and coded exhaustively; all speaker attributions are error-free; AI-to-AI autonomous agreement violations occurred; any specific proposed governance mechanism is sufficient; conference views generalise to society.

**Next deliverables:** Complete session-by-session evidence ledger, explicit codebook, contradiction matrix, independently checked literature review, and sandbox experiment specifications.

## Links

- [Collaborative Intelligence research agenda](./RECIPROCAL_INTELLIGENCE_AND_ACCOUNTABLE_AUTONOMY.md)
- [Mission Framework issue #15](https://github.com/froekjaer/mission-framework/issues/15)
- [Canonical AI behavioural preamble](https://github.com/froekjaer/mission-framework/blob/main/docs/operational/AI-BEHAVIOURAL-PREAMBLE.md)

**Research rule:** Reality outranks agreement; contradictory observations remain visible.
