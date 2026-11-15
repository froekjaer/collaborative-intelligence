# Independent critical review — Collaborative Intelligence v2 foundations

**Reviewer:** Claude (Anthropic), model Claude Opus 5.5, acting as independent critical academic reviewer at the request of the programme lead.
**Review date:** 2026-11-15.
**Object of review:** PR #14, branch `research/collaborative-intelligence-v2-foundations`, head `53811743589457217493d7dafbfc63ec392a8e69`.
**Status:** Advisory external review. Not canonical. Does not modify Mission Framework semantics, the glossary, the operational preamble or any existing research conclusion.
**Independence note:** The programme lead asked that criticisms not be softened to fit the existing framework. None have been. The reviewer is itself an AI system; see §11 on why this review is not independent of the programme's other AI reviews.

---

## Contents

1. Labels used in this review
2. Access record: what was and was not examined
3. Overall assessment
4. What v2 proposes, and how novel it is
5. Evidence by foundation
6. Classification of v2's assumptions
7. Internal inconsistencies
8. Temporal validity
9. Issue and Recommendation Register
10. Recommendations (R-01 to R-20)
11. Limitations of this review
12. References with verified DOIs

---

## 1. Labels used in this review

Two independent label sets are used. Every substantive statement carries a **basis** label; literature claims also carry a **status** label.

### 1.1 Basis: how the reviewer knows

| Label | Meaning |
| --- | --- |
| **[S]** | Supported by **directly examined source material**: repository files read in full at the commits listed in §2, or results of checks run by the reviewer (Crossref, PubMed queries). |
| **[A]** | Based on an **abstract or bibliographic metadata** read in this session (Crossref, PubMed, Semantic Scholar, publisher or proceedings page). Full text not read. |
| **[K]** | Based on the reviewer's **prior knowledge** of a publication, not re-read in this session. **Requires further verification against the full text before citation.** |
| **[I]** | **Interpretation or theoretical argument** by the reviewer. Not an empirical finding. |

Anything labelled [K], and any [A] summary used for a load-bearing decision, belongs to the category *claims requiring further verification*. The register in §9 records this per issue.

### 1.2 Status: what the literature shows

| Label | Meaning |
| --- | --- |
| **E** | Established: systematic review, meta-analysis or replicated finding. |
| **C** | Contested: credible evidence on more than one side, or failed replications. |
| **P** | Philosophical or normative: argued, not empirically testable as stated. |
| **U** | Untested hypothesis: no direct evidence found by the reviewer. |

---

## 2. Access record: what was and was not examined

### 2.1 Examined [S]

| Repository | Branch / ref | Commit | Files read in full |
| --- | --- | --- | --- |
| `froekjaer/collaborative-intelligence` | `research/collaborative-intelligence-v2-foundations` (PR #14) | `5381174` | `research/COLLABORATIVE_INTELLIGENCE_V2_FOUNDATIONS.md`; `research/NEUROINCLUSION_YOUTH_CAPABILITIES_01.md`; `research/CAPACITY_ADAPTED_PARTICIPATION_01.md` |
| `froekjaer/collaborative-intelligence` | `main` | `fab97b5` | `README.md`; `AI_CONTEXT.md`; `index.html` (text extracted from markup); `research/CROSS_CORPUS_SYNTHESIS_02_V2_READINESS.md`; `research/RECIPROCAL_INTELLIGENCE_AND_ACCOUNTABLE_AUTONOMY.md` (first ~120 lines, which is substantially all of it) |
| `froekjaer/collaborative-intelligence` | `claude/review-02-v2-architecture` (PR #12) | `669eb4a` | `research/CLAUDE_REVIEW_02A_CONCEPTUAL_INTEGRITY.md`; `research/CLAUDE_REVIEW_02B_WEAKNESSES_ALTERNATIVES.md` |
| `froekjaer/collaborative-intelligence` | `research/cross-model-review-01` (PR #13) | `7d5f658` | `research/INTERDISCIPLINARY_SOURCE_REGISTER_01.md`; `research/INTERDISCIPLINARY_SOURCES_VERIFIED.csv` |
| `froekjaer/mission-framework` | `main` | `9a1a454` | `GLOSSARY.md`; `docs/MISSION_THEORY.md`; `docs/REALITY_MODEL.md`; `MISSION_INTELLIGENCE.md`; `review/KNOWN_LIMITATIONS.md`; `review/KNOWN_OPEN_QUESTIONS.md` |
| `froekjaer/mission-framework` | `hybrid-intelligence-corpus` (PR #11) | `2a88d5b` | `INTELLECTUAL_CORPUS.md` |

Before committing this file, the reviewer re-verified that the PR #14 head was still `5381174`, that PR #14 was an open draft against `main`, and that it had no issue comments, review comments or reviews (REST API, 2026-11-15).

### 2.2 Examined only by file listing or branch metadata [S, listing only]

- File lists of both repositories on `main`; branch and PR ref lists (`git ls-remote`) for both repositories.
- Diff statistics for PR #12 and PR #13, including the C3-alloc and atomic fixture code in PR #13, which was **not run** in this review.

### 2.3 Not accessed or not read

| Item | Reason |
| --- | --- |
| `froekjaer/mission-solar-eclipse`, `froekjaer/-Publication-Pipeline`, `Mission-Platform`, `timelapse-pro`, `waterworks-pro`, `water-treatment-interface` | Not read. No finding in this review depends on them. |
| GitHub issues (including #9), PR discussions and review comments on PRs #11–#14 | During the review itself the GitHub API refused access (HTTP 403). At commit time PR #14 was confirmed to have no comments; other PRs' discussions remain unread. |
| On `main`: Experiment 01 and its v2 protocol, Bankdata, Devoteam, ISC and BSides intakes, Claude reviews 01A–01D, `HANDOVER_LOG.md`, qualitative coding protocol, `Review/` and `reviews/` folders | Not read; only names seen. Claude reviews 02C–02D on PR #12 also not read. |
| `mission-framework`: remaining docs (`TRUST.md`, `EVIDENCE_MODEL.md`, `PURPOSE_VALUES_PHILOSOPHY.md`, `PRINCIPIA_MISSIONIS.md`, operational preamble files and others) | Not read. The behavioural preamble was available to the reviewer only as the embedded user preference text. |
| 2013 MBA evidence PDFs; conference recordings and transcripts | Not read. |
| Full texts of the cited literature | Not read. See basis labels in §12. |

---

## 3. Overall assessment

v2 is a well-hedged research agenda, not yet a framework that can be tested as a whole [I]. Its epistemic posture is unusually good: it separates value commitments from empirical claims, rejects composite scores, demands strong baselines and commits to publishing negative results [S]. Its main problems are scope, construct definition and its relationship to existing work.

1. **Scope has outrun the core.** v2 moves from a narrow, testable problem (delegation and cumulative constraints for AI agents, Experiment 01) to evolution, religion, ecology, youth neuroinclusion, chronic illness and association boards [S]. No single construct links these. Each research question can be falsified; "Collaborative Intelligence" as a whole cannot [I].
2. **The central term is undefined.** The v2 document states that it is "not yet settled" whether CI is a theory, an integration framework, a design method or a research programme [S]. Mature fields already occupy each option (§4).
3. **The best evidence points against the default optimism behind RQ1 and RQ2.** On average, human–AI combinations perform worse than the best of humans or AI alone (Vaccaro et al., 2024) [A, E]. Demographic diversity has a near-zero average effect on team performance (van Dijk et al., 2012) [K, E]. v2 frames both as open questions, which is correct; its hypotheses and power calculations should start from these baselines, not from neutrality [I].
4. **Inclusion is made partly contingent on performance.** RQ2 asks whether diversity *improves deliberation* [S]. If the answer is no, the instrumental case fails, but the epistemic-justice case does not [I, P]. v2 should state explicitly that inclusion rests on rights and justice and that performance effects are a separate empirical question.
5. **Canonical semantics are in tension with epistemic justice.** The Mission Framework glossary defines Evidence by provenance, integrity information and relevance [S]. Lived testimony from marginalised groups rarely carries such metadata. Applied as written, the Reality rule can systematically downgrade exactly the voices v2 seeks to include [I; grounded in Fricker, 2007; Dotson, 2011, P].
6. **Human oversight is assumed to work.** The public site states "AI proposes; humans approve" [S]. Systematic evidence on automation bias and on human-oversight policies shows that this often fails or turns humans into liability buffers (Goddard et al., 2012 [A, E]; Green, 2022 [A]; Elish, 2019 [K]).
7. **The disability tracks are ethically careful but bypass the strongest evidence base.** Individual Placement and Support (IPS) has robust randomised evidence, including a Danish trial (Suijkerbuijk et al., 2017; Christensen et al., 2019) [A, E]. Autism-specific employment interventions have weak evidence (Hedley et al., 2017) [A]. v2 cites neither and proposes untested mechanisms instead [S, I].
8. **The programme's AI review method has a known flaw.** Several AI systems review the programme; this reviewer is another. LLM errors are substantially correlated across providers (Kim et al., 2025) [A]. AI reviews are not independent replications, including this one [I].

**Bottom line [I]:** keep the evidence contract and the falsification posture. Narrow CI to one defined construct, position it against existing frameworks, and separate the disability and participation tracks into their own studies with domain expertise and ethics approval.

---

## 4. What v2 proposes, and how novel it is

The reviewer found no v2 component without a close, established predecessor [I]. The potential contribution is integration: a traceable evidence contract applied to human–AI work. That is plausible but must be shown against these predecessors.

| v2 element [S] | Closest existing work | Overlap [I] | What v2 would need to add [I] |
| --- | --- | --- | --- |
| Research proposition: complementary human, AI and collective capabilities | Hybrid intelligence (Dellermann et al., 2019; Akata et al., 2020) [K]; AI-enhanced collective intelligence (Cui & Yasseri, 2024; Burton et al., 2024) [K] | High. Akata et al. already set out a research agenda for collaborative, adaptive, responsible and explainable human–AI systems (title verified [A]) | A definition that predicts something these do not |
| Four distinctions (human, AI, collective, environment) | Sociotechnical systems theory; Mission Theory's own Operational Reality Layer [S] | High | Justify why environment is "not an agent" while ecology is a value dimension |
| Six value dimensions | Responsible Research and Innovation: anticipation, reflexivity, inclusion, responsiveness (Stilgoe et al., 2013) [K]; capabilities approach (Sen; Nussbaum) [K]; human-centred AI (Shneiderman, 2020) [K] | High | A method for trade-offs, which v2 explicitly leaves open |
| Reality Belt (two-way feedback) | Double-loop learning (Argyris) [K]; realist evaluation and theory-of-change practice [K]; PDCA; Mission Framework's own Reality Ascent [S] | High | A test showing it reduces false-success claims (RQ5) against these |
| Accountable delegation; AI proposes, humans decide | Meaningful human control (Santoni de Sio & van den Hoven, 2018); responsibility gaps (Matthias, 2004; Santoni de Sio & Mecacci, 2021); accountability (Bovens, 2007) [K] | High | Engage with empirical failures of oversight (§5.2, §5.8) |
| "Mission" as organising unit | Mission-oriented innovation policy (Mazzucato, 2018) [K] and its critiques | Partial; same term, different level | State the relationship to avoid confusion |
| Perspective Challenge, epistemic diversity (PR #11) | Standpoint epistemology (Harding) [K]; epistemic injustice (Fricker, 2007) [K]; participatory AI (Birhane et al., 2022) [K] | High | Operational tests of whether the questions change decisions |
| Two-way capability–environment fit | WHO ICF biopsychosocial model; social model and critiques (Shakespeare & Watson, 2001) [K]; Universal Design for Learning; IPS | Very high | Little beyond application; say so |

**Assessment [I]:** CI is best described at present as an *integration programme* with a distinctive *evidence discipline*. Calling it a framework or theory before a defining construct exists invites the critique that it relabels known ideas. v2's own near-term deliverable 2 ("identify existing academic constructs before coining new terms") [S] should be applied to the name itself.

---

## 5. Evidence by foundation

### 5.1 Collective intelligence

The existence of a general group-intelligence factor is contested; v2 should not assume one [I].

- **Supports.** Woolley et al. (2010) reported a general factor *c*, predicted by social sensitivity, conversational turn-taking and proportion of women [K]. A meta-analysis of 22 studies (5,279 individuals, 1,356 groups) found strong support for *c*; collaboration process was its strongest predictor (Riedl et al., 2021) [A, E within that research programme].
- **Contradicts.** Across three studies with 312 people, individual IQ accounted for about 80% of group-IQ differences; the predicted effects of number of women and turn-taking were not supported (Bates & Gupta, 2017) [A]. A reanalysis questioned the factor structure (Credé & Howardson, 2017) [K]. A study of virtual groups did not find a general factor (Barlow & Dennis, 2016) [K]. Status: **C**.
- **Wisdom of crowds.** Social influence can undermine crowd accuracy (Lorenz et al., 2011) [K] or improve it in decentralised networks (Becker et al., 2017) [K]. Network structure is the moderator. Status: **C**, with a clear mechanism.
- **Implication [I].** Measure collective performance as task outcomes plus process, not infer it from group composition.

### 5.2 Human–AI collaboration

The best-evidenced area, and it cuts against RQ1's implicit optimism.

- **Average synergy is negative.** A preregistered systematic review and meta-analysis of 106 experiments (370 effect sizes, studies published 2020 to mid-2023) found human–AI combinations performed worse than the best of humans or AI alone (Hedges' g = −0.23, 95% CI −0.39 to −0.07). Losses were concentrated in decision tasks; gains appeared in content creation and where humans alone outperformed the AI alone (Vaccaro et al., 2024) [A, E; authors note possible publication bias].
- **Explanations do not fix it.** Explanations increased the chance that people accepted AI recommendations regardless of correctness (Bansal et al., 2021) [A]. Cognitive forcing interventions reduced over-reliance (Buçinca et al., 2021) [K]. Appropriate reliance needs its own measurement (Schemmer et al., 2023) [K].
- **Automation bias is robust.** A systematic review (74 included studies) found it mediated by workload, task complexity, time pressure, trust and experience, and mitigated by training, accountability emphasis and display design (Goddard et al., 2012) [A, E]; see also Parasuraman & Manzey (2010) [K].
- **Deskilling is plausible and now observed.** In a field experiment with nearly 1,000 high-school students, unrestricted GPT-4 access improved practice grades by 48% but reduced grades by 17% once access was removed; a guardrailed tutor largely mitigated the harm (Bastani et al., 2025) [A]. In an observational multicentre study, endoscopists' adenoma detection rate in non-AI colonoscopy fell from 28.4% to 22.4% after AI introduction (Budzyń et al., 2025) [A; observational]. Skill decay increases with non-use (Arthur et al., 1998) [K]. Status: **E** for the mechanism, **C** for effect size.
- **Productivity gains are real but uneven.** Among 5,172 customer-support agents, AI assistance increased issues resolved per hour by 15% on average, mostly for less experienced workers; the most experienced saw small quality declines (Brynjolfsson et al., 2025) [A]. Writing tasks sped up in an experiment (Noy & Zhang, 2023) [K]. In Danish linked survey–register data, chatbots had no significant effect on earnings or recorded hours, with average time savings of about 3% (Humlum & Vestergaard, NBER w33777; working paper, not peer reviewed) [A via abstract quoted in search results]. Status: **C**.
- **AI mediation can homogenise.** Generative AI raised individual creativity but reduced the collective diversity of novel content (Doshi & Hauser, 2024) [K]. An AI mediator helped groups find common ground in deliberation (Tessler et al., 2024) [K]. Both directions matter for v2's diversity claims.
- **Implication [I].** RQ1 is well posed. Preregister Vaccaro et al.'s moderators (task type; relative human vs AI accuracy) and expect null or negative synergy in decision tasks.

### 5.3 Participatory design

Participation is necessary but not self-validating [I].

- Arnstein's (1969) ladder distinguishes tokenism from citizen power [K, P]. Participation in AI often amounts to consultation without power and can launder legitimacy (Sloane et al., 2022; Birhane et al., 2022) [K]. Evidence is mostly conceptual and qualitative; few controlled studies.
- Participatory autism research shows feasible co-production models and their costs to participants (Fletcher-Watson et al., 2019) [K].
- **Implication [I].** v2 lists co-design as a safeguard [S]. It should specify the power participants hold (veto, agenda-setting, data control) and pay for participation; otherwise co-design becomes the "representation without influence" that v2 itself warns about [S].

### 5.4 Epistemic justice

This foundation is philosophical and should be presented as such.

- Testimonial and hermeneutical injustice (Fricker, 2007) and testimonial quieting and smothering (Dotson, 2011) are conceptual frameworks [K, P]. They justify inclusion on grounds of justice, not of performance.
- Applications to generative AI (Kay et al., 2024) are conceptual [K]. As an empirical claim: **U**.
- **Tension with the glossary [S + I].** Evidence requires "sufficient provenance, integrity information and relevance" (GLOSSARY) [S]. The Reality Model's lifecycle places validated recordings before human understanding [S]. Unless testimony is a first-class evidence type with its own validity criteria, the evidence rules risk reproducing testimonial injustice [I].

### 5.5 Diversity and deliberation (RQ2)

- **Demographic diversity:** near-zero average relationship with performance; job-related diversity is weakly positive, especially for innovation (van Dijk et al., 2012; Horwitz & Horwitz, 2007; Bell et al., 2011) [K, E]. Cultural diversity raises creativity but lowers social integration, with little net effect on performance (Stahl et al., 2010) [K].
- **Mechanism:** the categorisation–elaboration model predicts benefits only when diverse information is actually elaborated, and harm when diversity triggers intergroup bias (van Knippenberg et al., 2004) [K, C].
- **"Diversity trumps ability"** (Hong & Page, 2004) rests on a model whose mathematical claim has been sharply criticised (Thompson, 2014) [K, C]. It should not be cited as support.
- **Dissent:** a meta-analysis of 65 hidden-profile studies (3,189 groups) found groups with distributed information about eight times less likely to find the correct solution than fully informed groups (Lu et al., 2012) [A, E]; the original paradigm: Stasser & Titus (1985) [K]. Dissent facilitates decision quality (Schulz-Hardt et al., 2006) [K]; authentic dissent outperforms role-played devil's advocacy (Nemeth et al., 2001) [K].
- **Implication [I].** RQ2's "structured dissent from diverse expertise" is the right test. Treat diversity as a moderator of information elaboration and use authentic rather than assigned dissent.

### 5.6 Autonomy and freedom (RQ7)

v2 mixes three distinct concepts of autonomy and should choose operational definitions [I].

- **Psychological autonomy (self-determination theory).** Basic-need satisfaction relates to wellbeing and motivation at work (Van den Broeck et al., 2016) [K]; leader autonomy support relates to need satisfaction and outcomes (Slemp et al., 2018) [K]. **E** for correlation; causal and cross-cultural claims **C**, given mainly self-report data [K].
- **Job control.** Reviews find additive effects of demands and control on wellbeing, with weaker support for the buffering interaction (Häusser et al., 2010) [K]. Efficiency gains do not automatically become control [I].
- **Substantive freedom** (Sen; Nussbaum) and **relational autonomy** (feminist and disability philosophy) [K, P].
- **Who captures the gains.** Algorithmic management tends to intensify control (Kellogg et al., 2020) [K]. Danish data show little pass-through of time savings to earnings (Humlum & Vestergaard) [A]. Digital systems can manipulate by exploiting decision vulnerabilities (Susser et al., 2019) [K]. These support RQ7 and RQ-P9 as genuine questions.

### 5.7 Disability inclusion

The safeguards are strong; the evidence base is missing or bypassed [S, I].

- **IPS supported employment** is the best-evidenced vocational intervention for severe mental illness: Cochrane network meta-analysis of 48 RCTs (8,743 participants), moderate- to low-quality evidence (Suijkerbuijk et al., 2017) [A, E]. It generalises outside the US (Bond et al., 2012) [K]. A Danish three-arm RCT (n = 720) found IPS and enhanced IPS increased hours in work or education versus usual services, with no added effect from the enhancements and no differences in non-vocational outcomes (Christensen et al., 2019) [A].
- **Autism employment interventions.** A systematic review (50 empirical studies) found poor participant characterisation, small samples and little randomisation or appropriate control (Hedley et al., 2017) [A]. Most specific programmes: **U**.
- **Neurodiversity framing.** Scholarship supports moving from deficit to neurodiversity approaches (Pellicano & den Houting, 2022; Doyle, 2020) [K]. Critiques of the strict social model argue impairment cannot be reduced entirely to barriers (Shakespeare & Watson, 2001) [K, C]. v2's "strengths and support coexist" [S] is consistent with this critique.
- **Universal Design for Learning.** A meta-analysis reports positive effects from a small, heterogeneous base (Capp, 2017) [K, C].
- **Volunteering.** Cohort studies link volunteering to better wellbeing; experimental studies did not confirm these effects (Jenkinson et al., 2013) [A, C]. Selection bias is likely. This bears directly on the capacity-adapted participation hypothesis.
- **Fluctuating capacity.** UK clinical guidance on ME/CFS (NICE NG206, 2021) withdrew graded exercise therapy and recommended energy management within individual limits [K via search results; guideline, not peer-reviewed research]. Any participation model must avoid incremental-load assumptions [I].
- **Conflict with RQ3 [I].** "Delayed unassisted performance" is a sound deskilling measure for students. For many disabled people, assisted performance with tools is legitimate competence, not dependence. Separate success criteria are needed.

### 5.8 Organisational governance

- **Oversight.** Surveying 41 policies that require human oversight of government algorithms, Green (2022) argues that evidence shows people are often unable to perform the oversight functions, so such policies legitimise flawed algorithms and provide a false sense of security [A]. Humans given algorithmic risk assessments showed disparate interactions (Green & Chen, 2019) [K]. Elish (2019) describes humans as "moral crumple zones" [K].
- **Accountability.** The problem of many hands (Thompson, 1980) and responsibility gaps (Matthias, 2004) predict that delegation chains diffuse accountability [K, P with case evidence].
- **Psychological safety** relates to team learning (Edmondson, 1999) and to performance and learning outcomes in meta-analysis (Frazier et al., 2017) [K, E]. It is absent from v2 [S].
- **Commons and polycentricity.** Ostrom (1990) supports distributed, nested governance over central control [K]. This aligns with the C3-alloc alternative proposed in PR #12 [S].
- **Volunteer boards.** Nonprofit governance research has concentrated narrowly on boards (Cornforth, 2012) [K]. AI-supported board work has no evidence base found by the reviewer: **U**.

---

## 6. Classification of v2's assumptions

Most load-bearing assumptions are contested or untested; the few established findings mainly argue for caution [I].

| Assumption (stated or implied in v2) [S] | Status | Key evidence (basis) |
| --- | --- | --- |
| Human–AI combinations can outperform either alone | C; negative on average, positive in some tasks | Vaccaro et al., 2024 [A]; Bansal et al., 2021 [A] |
| Human approval protects against AI error | C; often fails | Goddard et al., 2012 [A]; Green, 2022 [A]; Green & Chen, 2019 [K] |
| AI assistance can erode unassisted skill | E for mechanism | Bainbridge, 1983 [K]; Arthur et al., 1998 [K]; Bastani et al., 2025 [A]; Budzyń et al., 2025 [A] |
| Structured dissent improves error detection | E for authentic dissent | Schulz-Hardt et al., 2006 [K]; Nemeth et al., 2001 [K]; Lu et al., 2012 [A] |
| Meaningful diversity improves deliberation | C; demographic ≈ 0, informational small positive | van Dijk et al., 2012 [K]; van Knippenberg et al., 2004 [K] |
| Groups have a general collective intelligence | C | Riedl et al., 2021 [A] vs Bates & Gupta, 2017 [A] |
| Multiple AI reviewers give independent checks | Contradicted | Kim et al., 2025 [A] |
| Efficiency becomes freedom and free time | U; early evidence says not automatically | Humlum & Vestergaard [A]; Kellogg et al., 2020 [K] |
| Explicit outcome feedback reduces false success (Reality Belt) | U | No direct test found [I] |
| Mission-wide constraints add value beyond capability controls (RQ8) | U | PR #12 falsification table [S] |
| Inclusion of affected people is owed as a matter of justice | P | Fricker, 2007 [K]; Dotson, 2011 [K]; UN CRPD |
| Two-way capability–environment fit beats person-only change | Partly E (IPS), mostly U | Suijkerbuijk et al., 2017 [A]; Christensen et al., 2019 [A] |
| Capacity-adapted participation improves belonging and agency | U; volunteering experiments null | Jenkinson et al., 2013 [A] |
| AI scaffolding reduces coordination burden for boards | U | No studies found [I] |
| Rights, safety and ecology are non-compensatory | P | Normative choice; defensible, needs a decision procedure [I] |
| "Reality has priority over models" | P; operationally contested | Who rules on "credible evidence" is a question of power [I] |

**index.html "Key Findings".** The public site states results such as "Operational incident logs are more predictive of system trust than static trust models" [S]. The reviewer found no study supporting them in the material read (§2.3 lists what was not read). They are **U** and should be labelled as hypotheses.

---

## 7. Internal inconsistencies

The repositories present at least three accounts of what CI is, at three levels of caution [S, I].

| # | Inconsistency [S] | Where | Why it matters [I] |
| --- | --- | --- | --- |
| 1 | The site frames CI as "autonomous AI agents and human operators … in safety-critical industrial systems"; v2 frames it as human–AI–collective flourishing across society | `index.html` vs v2 foundations | Readers and reviewers will evaluate different programmes |
| 2 | The site lists six principles (Human Accountability, Explicit Uncertainty, Empirical Validation, Multi-Agent Divergence, Operational Trust, Continuous Feedback); the README lists eight different shared principles | `index.html` vs `README.md` | No canonical principle set |
| 3 | The site states "Key Findings"; v2 says nothing is validated | `index.html` vs v2 "Explicit unknowns" | Overclaiming in the most-read artefact |
| 4 | "Every autonomous decision is traceable to a human operator. AI proposes; humans approve" vs the glossary, which allows approved policy to classify decisions as non-consequential | `index.html` vs `GLOSSARY.md` (Consequential) | Different accountability rules |
| 5 | Mission Theory proposes a "Grand Unification" of nine disciplines; Known Limitations concedes possible overlap with established disciplines and limited validation | `MISSION_THEORY.md` vs `KNOWN_LIMITATIONS.md` | Rhetoric undercuts the stated research posture |
| 6 | v2 requires religions to be studied "both internally and critically"; the PR #13 register's 14 religion entries are all status C (unverified), and no full text has been read | v2 W1 vs PR #13 register | W1 is aspirational, not yet a workstream |
| 7 | v2 warns not to "silently incorporate" PR #12 and #13 findings, but its workstreams and deliverables depend on both (source register; C3-alloc reconciliation) | v2 header vs body | Acceptable if logged; currently only noted |
| 8 | RQ3 treats unassisted performance as the success criterion; the neuroinclusion track values assisted, adapted participation | v2 RQ3 vs track 01 | Conflicting definitions of competence |

The reviewer did not verify whether the Solar Eclipse vertical slice, named as the "immediate objective" in `AI_CONTEXT.md` [S], has progressed. If it has not, v2's expansion runs ahead of the one empirical test the programme committed to [I].

---

## 8. Temporal validity

The evidence cited was produced under specific technological and social conditions. This section separates those conditions from present capabilities and from hypotheses about the future. **Published study results are reported as published and are not adjusted, reinterpreted or "updated" here.** Where the reviewer thinks a result may not transfer to current systems, that is stated as a hypothesis [H], not as a correction of the study.

### 8.1 Original research conditions

| Study | Conditions under which results were obtained | Basis |
| --- | --- | --- |
| Vaccaro et al., 2024 | Experiments published 1 Jan 2020 – 30 Jun 2023; mostly pre-frontier-LLM systems and lab tasks | [A] |
| Bastani et al., 2025 | Field experiment with GPT-4-based tutors in high-school mathematics (Turkey; dating of fieldwork to be verified) | [A] for design; [K] for setting |
| Brynjolfsson et al., 2025 | Staggered rollout of a generative-AI assistant to 5,172 customer-support agents; assistant predates current models (exact model and dates to be verified) | [A] for design; [K] for model |
| Noy & Zhang, 2023 | Online experiment with early ChatGPT on professional writing tasks | [K] |
| Budzyń et al., 2025 | Colonoscopy with AI computer-aided detection, Poland, Sept 2021 – Mar 2022; observational | [A] |
| Humlum & Vestergaard (w33777) | Danish surveys late 2023 and 2024 linked to registers; working paper revised in 2026 | [A] |
| Kim et al., 2025 | More than 350 LLMs on two leaderboards and a résumé-screening task, as of 2025 | [A] |
| Goddard et al., 2012; Parasuraman & Manzey, 2010; Bainbridge, 1983 | Pre-LLM clinical decision support, aviation and process control | [A]/[K] |
| Diversity and hidden-profile meta-analyses (2004–2012) | Human-only teams, largely Western samples, mostly lab or organisational settings | [K]/[A] |
| Christensen et al., 2019; Suijkerbuijk et al., 2017 | Recruitment 2012–2016 (Danish trial); RCTs to Nov 2016 (Cochrane); no AI component | [A] |

### 8.2 Current capabilities (November 2026)

- AI systems available today are more capable, more agentic and more widely deployed than those in most of the studies above [I]. No systematic review of human–AI synergy covering post-2023 frontier models was identified in this review [I; not searched systematically].
- The mechanisms these studies identify (over-reliance, explanation-driven acceptance, skill decay with disuse, correlated errors, gains captured by employers) are properties of human cognition, organisations and model ecosystems. There is no evidence that they have disappeared with newer models [I].
- Vaccaro et al. found that combinations lost performance when the AI alone outperformed humans alone [A]. As AI systems become stronger relative to humans on more tasks, that finding, if it holds, predicts more such losses, not fewer [I, H].

### 8.3 Future hypotheses [H]

These are hypotheses for the programme to test, not findings.

- H-T1: With current frontier models, average human–AI synergy in decision tasks remains at or below the better single agent unless the interaction is specifically designed (for example, forcing functions, calibrated confidence).
- H-T2: Error correlation across frontier models increases as models converge on similar data and training methods, further reducing the value of multi-model review.
- H-T3: Deskilling effects scale with the share of a task delegated and with time since last unassisted practice, independent of model generation.
- H-T4: Time savings from agentic AI are captured by employers or absorbed by new tasks unless governance allocates them explicitly (RQ7, RQ-P9).

### 8.4 Rules for the programme

1. Cite each study with its period, population and system, as in §8.1.
2. When a newer study disagrees with an older one, record both; do not overwrite the older result.
3. Label any claim that a finding "no longer applies" as [H] until tested with current systems.

---

## 9. Issue and Recommendation Register

**Severity:** High = undermines validity of the programme's central claims or risks harm to participants; Medium = weakens a research question or component; Low = presentation or consistency.
**Verification status:** *Verified (repo)* = confirmed by reading repository files; *Supported (abstract)* = rests on abstract-level reading; *Needs verification* = rests at least partly on [K] sources or unread material; *Interpretation* = reviewer argument.

| ID | Severity | Affected component | Issue | Supporting evidence | Recommended action | Verification status |
| --- | --- | --- | --- | --- | --- | --- |
| CR-01 | High | CI v2 research proposition | CI is undefined: theory, framework, method or programme is "not yet settled" | v2 "Explicit unknowns" [S] | R-01, R-02 | Verified (repo) |
| CR-02 | High | v2 scope; workstreams W1–W5 | Scope extends far beyond the testable core; no unifying construct | v2 workstreams and tracks [S] | R-03 | Verified (repo); severity is interpretation |
| CR-03 | High | RQ1; Experiment 01 | Default expectation of synergy contradicted by meta-analysis | Vaccaro et al., 2024 [A] | R-09, R-10 | Supported (abstract) |
| CR-04 | High | Six value dimensions; RQ2 | Inclusion framed partly as instrumentally justified by performance | v2 RQ2 [S]; Fricker, 2007 [K] | R-04 | Verified (repo); argument is interpretation |
| CR-05 | High | Mission Framework GLOSSARY: Evidence; Reality rule | Evidence criteria risk systematically discounting lived testimony | GLOSSARY, REALITY_MODEL [S]; Fricker; Dotson [K] | R-05, R-06 (via Framework Findings) | Verified (repo); impact is interpretation |
| CR-06 | High | Human accountability principle; index.html | "AI proposes; humans approve" assumed effective | Goddard et al., 2012 [A]; Green, 2022 [A]; Elish, 2019 [K] | R-07 | Supported (abstract) |
| CR-07 | High | Neuroinclusion track 01; capacity track 02 | Strongest evidence base (IPS) not engaged; untested mechanisms proposed | Suijkerbuijk et al., 2017 [A]; Christensen et al., 2019 [A]; Hedley et al., 2017 [A] | R-12 | Supported (abstract) |
| CR-08 | High | Human-subject pilots (tracks 01–02, board pilot) | Pilots involving minors, diagnoses, health or benefits status require approval and data-protection assessment | v2 safeguards [S] | R-16, R-17 | Verified (repo); legal specifics need verification |
| CR-09 | Medium | Programme review method | Multiple AI reviewers are not independent | Kim et al., 2025 [A] | R-19 | Supported (abstract) |
| CR-10 | Medium | RQ2; Perspective Challenge (PR #11) | Demographic diversity has near-zero average effect; mechanism is information elaboration | van Dijk et al., 2012; van Knippenberg et al., 2004 [K] | R-09, R-14 | Needs verification |
| CR-11 | Medium | Collective intelligence concept | General *c* factor contested | Riedl et al., 2021 [A]; Bates & Gupta, 2017 [A]; Credé & Howardson, 2017 [K] | R-01, R-14 | Supported (abstract) / Needs verification |
| CR-12 | Medium | RQ3 vs track 01 | Conflicting competence criteria (unassisted vs assisted) | v2 RQ3, track 01 [S] | R-13 | Verified (repo) |
| CR-13 | Medium | RQ7; RQ-P9 | Efficiency-to-freedom pathway assumed; evidence of low pass-through | Humlum & Vestergaard [A]; Häusser et al., 2010 [K] | R-15 | Supported (abstract) / Needs verification |
| CR-14 | Medium | Six value dimensions | No trade-off or decision procedure for non-compensatory dimensions | v2 [S] | R-08 | Verified (repo) |
| CR-15 | Medium | Participatory safeguards | Co-design without specified power risks tokenism | Arnstein, 1969; Sloane et al., 2022; Birhane et al., 2022 [K] | R-17 | Needs verification |
| CR-16 | Medium | All group studies | Psychological safety and network structure absent as moderators | Frazier et al., 2017; Becker et al., 2017 [K] | R-14 | Needs verification |
| CR-17 | Medium | Research design across RQs | No prior effect sizes, power analysis, primary outcomes or multiplicity control | v2 RQs and evaluation contract [S] | R-09, R-10, R-11 | Verified (repo) |
| CR-18 | Medium | Capacity track 02 | Volunteering benefits likely confounded; incremental-load assumptions risky | Jenkinson et al., 2013 [A]; NICE NG206 [K] | R-12, R-16 | Supported (abstract) / Needs verification |
| CR-19 | Medium | Board pilot (track 02 extension) | Possible conflict of interest if run where the programme lead holds office; n = 1, self-selected | v2 pilot description [S] | R-18 | Verified (repo); applicability not verified |
| CR-20 | Low | index.html | Untested "Key Findings" presented as results | index.html [S] | R-20 | Verified (repo) |
| CR-21 | Low | index.html vs README | Two different principle sets | index.html; README [S] | R-20 | Verified (repo) |
| CR-22 | Low | MISSION_THEORY.md | "Grand Unification" rhetoric conflicts with Known Limitations | MISSION_THEORY; KNOWN_LIMITATIONS [S] | R-20 | Verified (repo) |
| CR-23 | Low | W1; PR #13 register | Religious and civilisational sources unverified and unread | PR #13 register [S] | R-03 | Verified (repo) |
| CR-24 | Low | v2 vs PRs #12, #13 | Dependence on unmerged PRs only noted, not logged | v2 header [S] | R-02, R-03 | Verified (repo) |
| CR-25 | Medium | Novelty claims across v2 | Close predecessors not positioned (hybrid intelligence, RRI, meaningful human control, mission-oriented policy) | §4 sources [K] | R-02 | Needs verification |
| CR-26 | Low | Programme sequencing | v2 expansion may run ahead of the Solar Eclipse vertical slice | AI_CONTEXT.md [S]; Solar Eclipse repo not read | R-03 | Needs verification |

---

## 10. Recommendations (R-01 to R-20)

Ordered by consequence. All canonical changes should go through the Framework Findings / ADR process, not be applied directly.

### Concepts and scope

- **R-01 — Define CI with one construct and one boundary.** For example: "the measured improvement in justified, calibrated decisions when humans, AI and institutions are combined, relative to the strongest single-source baseline." State what would show it does not exist.
- **R-02 — Position against existing work** in a short related-work section covering hybrid intelligence, collective intelligence, meaningful human control, Responsible Research and Innovation, sociotechnical systems and mission-oriented policy. If no distinctive prediction remains, adopt the existing term and frame CI as an application programme.
- **R-03 — Split v2 into independent studies** with their own owners and ethics paths: (a) agent delegation and constraints (Experiment 01, RQ8); (b) human–AI decision quality and dissent (RQ1, RQ2, RQ5); (c) learning and deskilling (RQ3); (d) disability and capacity-adapted participation; (e) voluntary board governance. Park W1 (civilisational foundations) as a background reading programme until a concrete claim needs it.
- **R-04 — Separate justice from performance.** State in the proposition that inclusion is justified by rights and epistemic justice, and treat performance effects of diversity as a separate empirical question whose null result would not remove the obligation.

### Canonical semantics (via Framework Findings, not silently)

- **R-05 — Add testimony as a first-class Evidence type** with its own validity criteria (consistency, situatedness, corroboration where appropriate). Record when testimony was discounted and why.
- **R-06 — Name who adjudicates "credible evidence"** in the Reality rule, and give affected stakeholders a route to contest that adjudication.
- **R-07 — Replace "AI proposes; humans approve"** with oversight designed against automation bias: independent verification for consequential actions, cognitive forcing, reviewer workload limits and measured approval error (the S9 seeded-invalid design already points this way).
- **R-08 — Add a trade-off procedure** for the six dimensions: name the decision authority, the non-compensatory floors and how dissent is recorded.

### Research design

- **R-09 — Use prior effect sizes.** Base RQ1 on Vaccaro et al.'s moderators and RQ2 on hidden-profile and dissent paradigms, which have validated tasks. Power studies accordingly.
- **R-10 — Preregister as Registered Reports** (for example via OSF), with one primary outcome per RQ and correction for multiple outcomes.
- **R-11 — Use validated instruments** rather than bespoke ones: Brier scores for calibration, NASA-TLX for workload, Edmondson's psychological-safety scale, a validated basic-need-satisfaction scale for SDT.
- **R-12 — Make IPS the comparator** in the disability track wherever employment is a participant goal. Do not design a new intervention without first testing against it.
- **R-13 — Define two competence measures:** unassisted retention for deskilling, and participant-chosen assisted task performance for accessibility. Report both.
- **R-14 — Add psychological safety and network structure** as measured moderators in all group studies.
- **R-15 — Treat RQ7 as distributional:** measure who receives time savings (participant, employer, colleagues) with time-use data, not self-report alone.

### Ethics and governance of the programme

- **R-16 — No human-subject pilot without approval** from the relevant Danish research ethics body and a GDPR Article 9 assessment wherever health or diagnosis data could arise. Minors require additional safeguards; v2 already says so. (Which body has jurisdiction depends on study design; the reviewer has not verified this.)
- **R-17 — Give co-designers real power:** agenda-setting, a veto over use of their data, and payment. Document the Arnstein rung each activity reaches.
- **R-18 — Declare conflicts in the board pilot.** If the pilot runs in an association where the programme lead holds office, the dual role is a conflict of interest to declare and manage, for example with an external evaluator.
- **R-19 — Recruit human disciplinary reviewers**, prioritising disability studies, organisational psychology, HCI and philosophy, including disabled reviewers. Treat AI reviews, including this one, as one correlated source.
- **R-20 — Align public pages with the research posture:** relabel the index.html "Key Findings" as hypotheses, unify the principle lists, and remove "Grand Unification" language until evidence supports it.

**Minimum next step [I]:** one preregistered RQ2 study with seeded errors, comparing human-only, human + conventional tool, and human + AI, with authentic dissent as a factor. It is cheap, uses validated paradigms, and its result would constrain much of v2.

---

## 11. Limitations of this review

This is a structured critical review by an AI system, not a systematic review and not independent human peer review.

- **Not systematic.** Studies were selected from the reviewer's knowledge and checked with targeted searches. No protocol-driven database search, screening or risk-of-bias appraisal was done. Selection bias is likely; relevant positive and negative studies are surely missing.
- **Abstract-level reading.** About 20 sources were read at abstract level in this session ([A]). The rest ([K]) rely on prior knowledge and must be checked against the full text before citation.
- **Correlated reviewer.** The reviewer is a language model, like the programme's other reviewers; its errors may correlate with theirs (Kim et al., 2025). An earlier Claude session wrote reviews 02A–02D; reading 02A–02B may have anchored this review.
- **Partial corpus.** See §2.3. Unread repositories and PR discussions could resolve some inconsistencies in §7.
- **Western, English-language skew.** Most cited evidence comes from WEIRD samples and English-language venues, the same limitation v2 identifies in its own register.
- **Working papers and observational designs.** Humlum & Vestergaard is a working paper, not peer reviewed. Budzyń et al. is observational.
- **Delivery format.** This file reproduces a review first delivered as a Claude Docs document on 2026-11-15, extended with the access record (§2), basis labels, temporal-validity section (§8) and register (§9) at the programme lead's request. Findings were not softened in that process.

---

## 12. References with verified DOIs

Every DOI below resolved via the Crossref API on 2026-11-15, and title, first author and year matched the citation [S]. **Read** gives the basis label of the summary in this review. Years are print years; some items appeared online a year earlier.

| Reference | DOI | Read |
| --- | --- | --- |
| Akata, Z. et al. (2020). A research agenda for hybrid intelligence. *Computer* | [10.1109/MC.2020.2996587](https://doi.org/10.1109/MC.2020.2996587) | K |
| Arnstein, S. R. (1969). A ladder of citizen participation. *J. Am. Inst. Planners* | [10.1080/01944366908977225](https://doi.org/10.1080/01944366908977225) | K |
| Arthur, W. Jr. et al. (1998). Factors that influence skill decay and retention. *Human Performance* | [10.1207/s15327043hup1101_3](https://doi.org/10.1207/s15327043hup1101_3) | K |
| Bainbridge, L. (1983). Ironies of automation. *Automatica* | [10.1016/0005-1098(83)90046-8](https://doi.org/10.1016/0005-1098(83)90046-8) | K |
| Bansal, G. et al. (2021). Does the whole exceed its parts? *CHI '21* | [10.1145/3411764.3445717](https://doi.org/10.1145/3411764.3445717) | A |
| Barlow, J. B. & Dennis, A. R. (2016). Not as smart as we think. *J. Management Information Systems* | [10.1080/07421222.2016.1243944](https://doi.org/10.1080/07421222.2016.1243944) | K |
| Bastani, H. et al. (2025). Generative AI without guardrails can harm learning. *PNAS* | [10.1073/pnas.2422633122](https://doi.org/10.1073/pnas.2422633122) | A |
| Bates, T. C. & Gupta, S. (2017). Smart groups of smart people. *Intelligence* | [10.1016/j.intell.2016.11.004](https://doi.org/10.1016/j.intell.2016.11.004) | A |
| Becker, J., Brackbill, D. & Centola, D. (2017). Network dynamics of social influence in the wisdom of crowds. *PNAS* | [10.1073/pnas.1615978114](https://doi.org/10.1073/pnas.1615978114) | K |
| Bell, S. T. et al. (2011). Getting specific about demographic diversity variable and team performance relationships. *J. Management* | [10.1177/0149206310365001](https://doi.org/10.1177/0149206310365001) | K |
| Birhane, A. et al. (2022). Power to the people? Participatory AI. *EAAMO '22* | [10.1145/3551624.3555290](https://doi.org/10.1145/3551624.3555290) | K |
| Bond, G. R., Drake, R. E. & Becker, D. R. (2012). Generalizability of IPS outside the US. *World Psychiatry* | [10.1016/j.wpsyc.2012.01.005](https://doi.org/10.1016/j.wpsyc.2012.01.005) | K |
| Bovens, M. (2007). Analysing and assessing accountability. *European Law Journal* | [10.1111/j.1468-0386.2007.00378.x](https://doi.org/10.1111/j.1468-0386.2007.00378.x) | K |
| Brynjolfsson, E., Li, D. & Raymond, L. (2025). Generative AI at work. *QJE* | [10.1093/qje/qjae044](https://doi.org/10.1093/qje/qjae044) | A |
| Buçinca, Z. et al. (2021). To trust or to think. *Proc. ACM HCI (CSCW)* | [10.1145/3449287](https://doi.org/10.1145/3449287) | K |
| Budzyń, K. et al. (2025). Endoscopist deskilling risk after exposure to AI in colonoscopy. *Lancet Gastroenterol. Hepatol.* | [10.1016/S2468-1253(25)00133-5](https://doi.org/10.1016/S2468-1253(25)00133-5) | A |
| Burton, J. W. et al. (2024). How large language models can reshape collective intelligence. *Nature Human Behaviour* | [10.1038/s41562-024-01959-9](https://doi.org/10.1038/s41562-024-01959-9) | K |
| Capp, M. J. (2017). The effectiveness of universal design for learning: a meta-analysis. *Int. J. Inclusive Education* | [10.1080/13603116.2017.1325074](https://doi.org/10.1080/13603116.2017.1325074) | K |
| Christensen, T. N. et al. (2019). Effects of IPS supplemented with cognitive remediation and work-focused social skills training (Danish RCT). *JAMA Psychiatry* | [10.1001/jamapsychiatry.2019.2291](https://doi.org/10.1001/jamapsychiatry.2019.2291) | A |
| Cornforth, C. (2012). Nonprofit governance research. *Nonprofit and Voluntary Sector Quarterly* | [10.1177/0899764011427959](https://doi.org/10.1177/0899764011427959) | K |
| Credé, M. & Howardson, G. (2017). The structure of group task performance. *J. Applied Psychology* | [10.1037/apl0000176](https://doi.org/10.1037/apl0000176) | K |
| Cui, H. & Yasseri, T. (2024). AI-enhanced collective intelligence. *Patterns* | [10.1016/j.patter.2024.101074](https://doi.org/10.1016/j.patter.2024.101074) | K |
| Dellermann, D. et al. (2019). Hybrid intelligence. *Business & Information Systems Engineering* | [10.1007/s12599-019-00595-2](https://doi.org/10.1007/s12599-019-00595-2) | K |
| Doshi, A. R. & Hauser, O. P. (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. *Science Advances* | [10.1126/sciadv.adn5290](https://doi.org/10.1126/sciadv.adn5290) | K |
| Dotson, K. (2011). Tracking epistemic violence, tracking practices of silencing. *Hypatia* | [10.1111/j.1527-2001.2011.01177.x](https://doi.org/10.1111/j.1527-2001.2011.01177.x) | K |
| Doyle, N. (2020). Neurodiversity at work. *British Medical Bulletin* | [10.1093/bmb/ldaa021](https://doi.org/10.1093/bmb/ldaa021) | K |
| Edmondson, A. (1999). Psychological safety and learning behavior in work teams. *Administrative Science Quarterly* | [10.2307/2666999](https://doi.org/10.2307/2666999) | K |
| Elish, M. C. (2019). Moral crumple zones. *Engaging Science, Technology, and Society* | [10.17351/ests2019.260](https://doi.org/10.17351/ests2019.260) | K |
| Fletcher-Watson, S. et al. (2019). Making the future together. *Autism* | [10.1177/1362361318786721](https://doi.org/10.1177/1362361318786721) | K |
| Frazier, M. L. et al. (2017). Psychological safety: a meta-analytic review and extension. *Personnel Psychology* | [10.1111/peps.12183](https://doi.org/10.1111/peps.12183) | K |
| Fricker, M. (2007). *Epistemic Injustice*. Oxford University Press | [10.1093/acprof:oso/9780198237907.001.0001](https://doi.org/10.1093/acprof:oso/9780198237907.001.0001) | K |
| Goddard, K., Roudsari, A. & Wyatt, J. C. (2012). Automation bias: a systematic review. *JAMIA* | [10.1136/amiajnl-2011-000089](https://doi.org/10.1136/amiajnl-2011-000089) | A |
| Green, B. (2022). The flaws of policies requiring human oversight of government algorithms. *Computer Law & Security Review* | [10.1016/j.clsr.2022.105681](https://doi.org/10.1016/j.clsr.2022.105681) | A |
| Green, B. & Chen, Y. (2019). Disparate interactions. *FAT\* '19* | [10.1145/3287560.3287563](https://doi.org/10.1145/3287560.3287563) | K |
| Häusser, J. A. et al. (2010). Ten years on: the Job Demand–Control(–Support) model. *Work & Stress* | [10.1080/02678371003683747](https://doi.org/10.1080/02678371003683747) | K |
| Hedley, D. et al. (2017). Employment programmes for adults with autism: a systematic review. *Autism* | [10.1177/1362361316661855](https://doi.org/10.1177/1362361316661855) | A |
| Hong, L. & Page, S. E. (2004). Groups of diverse problem solvers can outperform groups of high-ability problem solvers. *PNAS* | [10.1073/pnas.0403723101](https://doi.org/10.1073/pnas.0403723101) | K |
| Horwitz, S. K. & Horwitz, I. B. (2007). The effects of team diversity on team outcomes. *J. Management* | [10.1177/0149206307308587](https://doi.org/10.1177/0149206307308587) | K |
| Humlum, A. & Vestergaard, E. (2025). Large language models, small labor market effects. NBER Working Paper 33777; revised 2026 as "Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI" (Crossref now returns the revised title). Not peer reviewed | [10.3386/w33777](https://doi.org/10.3386/w33777) | A |
| Jenkinson, C. E. et al. (2013). Is volunteering a public health intervention? *BMC Public Health* | [10.1186/1471-2458-13-773](https://doi.org/10.1186/1471-2458-13-773) | A |
| Kay, J., Kasirzadeh, A. & Mohamed, S. (2024). Epistemic injustice in generative AI. *AIES* | [10.1609/aies.v7i1.31671](https://doi.org/10.1609/aies.v7i1.31671) | K |
| Kellogg, K. C., Valentine, M. A. & Christin, A. (2020). Algorithms at work. *Academy of Management Annals* | [10.5465/annals.2018.0174](https://doi.org/10.5465/annals.2018.0174) | K |
| Kim, E. M., Garg, A., Peng, K. & Garg, N. (2025). Correlated errors in large language models. *ICML*, PMLR 267:30038–30066 | No DOI; [PMLR](https://proceedings.mlr.press/v267/kim25e.html) (verified via proceedings page, not Crossref) | A |
| Lorenz, J. et al. (2011). How social influence can undermine the wisdom of crowd effect. *PNAS* | [10.1073/pnas.1008636108](https://doi.org/10.1073/pnas.1008636108) | K |
| Lu, L., Yuan, Y. C. & McLeod, P. L. (2012). Twenty-five years of hidden profiles in group decision making. *PSPR* | [10.1177/1088868311417243](https://doi.org/10.1177/1088868311417243) | A |
| Matthias, A. (2004). The responsibility gap. *Ethics and Information Technology* | [10.1007/s10676-004-3422-1](https://doi.org/10.1007/s10676-004-3422-1) | K |
| Mazzucato, M. (2018). Mission-oriented innovation policies. *Industrial and Corporate Change* | [10.1093/icc/dty034](https://doi.org/10.1093/icc/dty034) | K |
| Nemeth, C. et al. (2001). Devil's advocate versus authentic dissent. *Eur. J. Social Psychology* | [10.1002/ejsp.58](https://doi.org/10.1002/ejsp.58) | K |
| NICE (2021). *Myalgic encephalomyelitis (or encephalopathy)/chronic fatigue syndrome: diagnosis and management* (NG206). Clinical guideline, not peer-reviewed research | No DOI; summarised from search results, guideline not opened | K |
| Noy, S. & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. *Science* | [10.1126/science.adh2586](https://doi.org/10.1126/science.adh2586) | K |
| Ostrom, E. (1990). *Governing the Commons*. Cambridge University Press | [10.1017/CBO9780511807763](https://doi.org/10.1017/CBO9780511807763) | K |
| Parasuraman, R. & Manzey, D. H. (2010). Complacency and bias in human use of automation. *Human Factors* | [10.1177/0018720810376055](https://doi.org/10.1177/0018720810376055) | K |
| Pellicano, E. & den Houting, J. (2022). Shifting from "normal science" to neurodiversity in autism science. *J. Child Psychol. Psychiatry* | [10.1111/jcpp.13534](https://doi.org/10.1111/jcpp.13534) | K |
| Riedl, C. et al. (2021). Quantifying collective intelligence in human groups. *PNAS* | [10.1073/pnas.2005737118](https://doi.org/10.1073/pnas.2005737118) | A |
| Santoni de Sio, F. & Mecacci, G. (2021). Four responsibility gaps with artificial intelligence. *Philosophy & Technology* | [10.1007/s13347-021-00450-x](https://doi.org/10.1007/s13347-021-00450-x) | K |
| Santoni de Sio, F. & van den Hoven, J. (2018). Meaningful human control over autonomous systems. *Frontiers in Robotics and AI* | [10.3389/frobt.2018.00015](https://doi.org/10.3389/frobt.2018.00015) | K |
| Schemmer, M. et al. (2023). Appropriate reliance on AI advice. *IUI '23* | [10.1145/3581641.3584066](https://doi.org/10.1145/3581641.3584066) | K |
| Schulz-Hardt, S. et al. (2006). Group decision making in hidden profile situations: dissent as a facilitator. *JPSP* | [10.1037/0022-3514.91.6.1080](https://doi.org/10.1037/0022-3514.91.6.1080) | K |
| Shakespeare, T. & Watson, N. (2001). The social model of disability: an outdated ideology? *Research in Social Science and Disability* | [10.1016/S1479-3547(01)80018-X](https://doi.org/10.1016/S1479-3547(01)80018-X) | K |
| Shneiderman, B. (2020). Human-centered artificial intelligence. *IJHCI* | [10.1080/10447318.2020.1741118](https://doi.org/10.1080/10447318.2020.1741118) | K |
| Slemp, G. R. et al. (2018). Leader autonomy support in the workplace: a meta-analytic review. *Motivation and Emotion* | [10.1007/s11031-018-9698-y](https://doi.org/10.1007/s11031-018-9698-y) | K |
| Sloane, M. et al. (2022). Participation is not a design fix for machine learning. *EAAMO '22* | [10.1145/3551624.3555285](https://doi.org/10.1145/3551624.3555285) | K |
| Stahl, G. K. et al. (2010). Unraveling the effects of cultural diversity in teams. *JIBS* | [10.1057/jibs.2009.85](https://doi.org/10.1057/jibs.2009.85) | K |
| Stasser, G. & Titus, W. (1985). Pooling of unshared information in group decision making. *JPSP* | [10.1037/0022-3514.48.6.1467](https://doi.org/10.1037/0022-3514.48.6.1467) | K |
| Stilgoe, J., Owen, R. & Macnaghten, P. (2013). Developing a framework for responsible innovation. *Research Policy* | [10.1016/j.respol.2013.05.008](https://doi.org/10.1016/j.respol.2013.05.008) | K |
| Suijkerbuijk, Y. B. et al. (2017). Interventions for obtaining and maintaining employment in adults with severe mental illness. *Cochrane Database Syst. Rev.* | [10.1002/14651858.CD011867.pub2](https://doi.org/10.1002/14651858.CD011867.pub2) | A |
| Susser, D., Roessler, B. & Nissenbaum, H. (2019). Technology, autonomy, and manipulation. *Internet Policy Review* | [10.14763/2019.2.1410](https://doi.org/10.14763/2019.2.1410) | K |
| Tessler, M. H. et al. (2024). AI can help humans find common ground in democratic deliberation. *Science* | [10.1126/science.adq2852](https://doi.org/10.1126/science.adq2852) | K |
| Thompson, A. (2014). Does diversity trump ability? *Notices of the AMS* | [10.1090/noti1163](https://doi.org/10.1090/noti1163) | K |
| Thompson, D. F. (1980). Moral responsibility of public officials: the problem of many hands. *APSR* | [10.2307/1954312](https://doi.org/10.2307/1954312) | K |
| Vaccaro, M., Almaatouq, A. & Malone, T. (2024). When combinations of humans and AI are useful. *Nature Human Behaviour* | [10.1038/s41562-024-02024-1](https://doi.org/10.1038/s41562-024-02024-1) | A |
| Van den Broeck, A. et al. (2016). A review of self-determination theory's basic psychological needs at work. *J. Management* | [10.1177/0149206316632058](https://doi.org/10.1177/0149206316632058) | K |
| van Dijk, H., van Engen, M. L. & van Knippenberg, D. (2012). Defying conventional wisdom. *OBHDP* | [10.1016/j.obhdp.2012.06.003](https://doi.org/10.1016/j.obhdp.2012.06.003) | K |
| van Knippenberg, D., De Dreu, C. K. W. & Homan, A. C. (2004). Work group diversity and group performance: an integrative model. *J. Applied Psychology* | [10.1037/0021-9010.89.6.1008](https://doi.org/10.1037/0021-9010.89.6.1008) | K |
| Woolley, A. W. et al. (2010). Evidence for a collective intelligence factor in the performance of human groups. *Science* | [10.1126/science.1193147](https://doi.org/10.1126/science.1193147) | K |

Works mentioned without a DOI (Sen, *Development as Freedom*; Nussbaum, *Creating Capabilities*; Argyris on double-loop learning; Harding, *Whose Science? Whose Knowledge?*; WHO ICF; UN CRPD) were not bibliographically verified in this pass.

**DOI correction log [S]:** during verification, three DOIs initially recalled by the reviewer were wrong and were corrected before use: Bates & Gupta (2017) → `10.1016/j.intell.2016.11.004`; Häusser et al. (2010) → `10.1080/02678371003683747`; Thompson (1980) → `10.2307/1954312`. Recorded so that the correction is traceable.
