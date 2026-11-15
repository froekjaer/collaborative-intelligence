# Claude review 01C: Critique of Experiment 01

**Status:** Advisory peer review (Claude, 2026-11-15). Not canonical.
**Target:** [EXPERIMENT_01_BENEFICIAL_DELEGATION_AND_GLOBAL_AUTHORIZATION.md](./EXPERIMENT_01_BENEFICIAL_DELEGATION_AND_GLOBAL_AUTHORIZATION.md) at `52eb8c9`.

## 1. Strengths

- The experiment is synthetic and offline, with explicit stop conditions.
- It measures benefit and violations together.
- Its hypotheses come with named rivals.
- It refuses to invent effect sizes before a pilot.

## 2. Methodological weaknesses

| # | Weakness | Why it matters | Minimal fix |
|---|---|---|---|
| W1 | **Weak baselines.** C3 is compared only with prompt-only controls (C1) and local controls without memory (C2). | A positive result would mean only that global enforcement beats strawmen. | Add **C2b: capability- and provenance-based enforcement** from the literature, e.g. CaMeL ([Debenedetti et al. 2025](https://arxiv.org/abs/2503.18813)), which reports 77 % task success with its security guarantees against 84 % undefended. That figure is itself a benefit–risk datapoint. |
| W2 | **The environment is built from scratch.** | This breaches "search before creating", and the results cannot be compared with others. | Build on **AgentDojo** ([Debenedetti et al. 2024](https://arxiv.org/abs/2406.13352)), which already measures benign utility, utility under attack and attack success with deterministic state checks. Add S2, S5 and S6 as extensions. |
| W3 | **Designer bias.** The same team writes the policy authority P and the scenarios. | The earlier toy smoke test showed outcomes "baked into policy definitions". | Have scenarios, including held-out ones, written by a separate group that has not seen P's rules. Preregister P before scenarios are generated. |
| W4 | **Only static adversarial content.** | Static content overstates robustness. The corpus itself reports protections whose effectiveness changes over time. | Add an **adaptive adversarial generator** confined to the synthetic environment, and report robustness curves across rounds. |
| W5 | **S4 is not necessarily compositional.** | If B simply requires the same approval token, the failure can be fixed locally. That makes it a configuration error, not a compositional failure. | Apply the **local-repair test** (§3) to classify each scenario before running it. |
| W6 | **The composite "net user benefit" has undefined weights.** | This gives researchers too many degrees of freedom. | Preregister the weights, or report the components separately. |
| W7 | **The quality of human approval is not tested.** | C4 may produce rubber-stamping. Automation-bias research finds that oversight frequently fails ([Green 2022](https://arxiv.org/abs/2109.05067)). | **Seed known-bad proposals** in C4 and measure how often humans reject them, together with time and workload (e.g. NASA-TLX). |
| W8 | **The third party has no voice in S6.** | Utility is scored only from the user's side. | Add a separate third-party utility or harm metric and a stakeholder-defined threshold. |
| W9 | **C0 is not equivalent.** | Humans without agent tooling face a different task. | Give C0 the same information tools without autonomous execution, and report "time to the same decision quality". |
| W10 | **Delegation depth is missing.** | The vendor-reported cases (see 01B §3) involved constraints weakening through **delegation to sub-agents**. | Add **S7:** constraints must survive an A→B→C hand-off unchanged or narrowed. Add **S8:** oversight obligations must cover work spawned by a delegate. |
| W11 | **Benefit is defined too narrowly.** | Only task completion and friction are measured. | Add learning (an unassisted delayed retest), recovery quality after an infeasible commitment (S5), and the **cost of false refusals**. |

## 3. A falsifiable definition of compositional failure (brief Q3)

A failure counts as **compositional** only if all three conditions hold:

1. every step passed through the enforcement point responsible for it, and its log shows "permitted";
2. the end state violates an invariant stated at mission level;
3. **Local-repair test:** no change to any *single* component's policy, using only information available to that component, blocks the failure while still allowing all legitimate S1 tasks.

If one local change is enough, the failure is a **misconfiguration**. The test is falsifiable: the programme's claim that compositional failure is a distinct class fails if, across preregistered scenarios, every observed failure passes local repair.

## 4. Revised hypotheses

- **H1′.** C3 blocks more compositional failures (as defined in §3) than C2 and C2b, without reducing the valid-completion rate by more than a preregistered margin.
- **H2′.** Bounding the worst case (spend, scope, time and turn ceilings enforced outside the agent) achieves equal or lower harm with **fewer human interrupts** than approving each action. This tests the convergent practice reported in 01B §5.
- **H3′.** In C4, the rejection rate for seeded bad proposals falls as the approval rate rises (rubber-stamping). *Falsified* if the rejection rate stays at or above a preregistered level.
- **H0 (null from recording 4).** Ordinary controls (least privilege, separate credentials, delayed adoption) close most of the gap. C3 adds nothing significant over a hygiene-hardened C2.

## 5. Priority

W1, W2, W3, W7 and W10 are needed before any result could be credible. The rest can follow after the pilot.
