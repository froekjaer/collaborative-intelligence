# Claude review 01D: OT resilience, continued operation and human consequences

**Status:** Advisory peer review (Claude, 2026-11-15). Not canonical.
**Sources:** BSides recording 1 (de-identified) and standard safety-engineering literature cited from reviewer knowledge. Those citations were not re-verified in this session and are marked †.

## 1. Six distinct capabilities (brief Q6)

| Capability | Meaning | Typical failure |
|---|---|---|
| Independent observability | Monitoring and recording that share no infrastructure with the system they watch | Monitoring is lost together with the IT network it runs on |
| Engineered fallback | Local control that survives the loss of supervisory networks | It is assumed to exist but has not been rehearsed (rec. 1 stresses this) |
| Safe shutdown | A transition to a safe state that protects people and equipment | It is overridden in favour of uptime |
| Manual control | People operating without automation | Skills have atrophied and procedures are out of date |
| Restoration | Rebuilding from known-good configuration and firmware | Hidden dependencies such as directory services, name resolution, licences and certificates (rec. 1) |
| Resynchronisation | Reconnecting with business and partner systems | Slow and error-prone, and it creates pressure to cut corners |

## 2. Where these conflict

1. **Safety versus continuity.** Safe shutdown and continued operation pull in opposite directions. The safety function must take precedence (IEC 61511†). An AI agent that optimises for availability must never sit inside the safety function.
2. **Isolation versus observability.** Islanding for fallback can cut the channels that observability depends on. One-way paths to independent storage reduce this tension (rec. 1).
3. **Automation versus manual competence.** The more operation is automated, the less practised manual fallback becomes. This is the classic **"ironies of automation"** (Bainbridge 1983†). **This is the most important human consequence:** more AI autonomy in OT can erode the very fallback that makes autonomy acceptable. It links directly to the ISC concern about deskilling.
4. **Restoration speed versus integrity.** Fast restoration from stored configurations is valuable only if the stored copies are themselves trustworthy. The recovery path must be treated as part of what has to be protected.
5. **Rapid response versus expiring access.** Remote access helps recovery but widens exposure. Recording 1 describes physically time-limited access windows. That is a strong pattern: **delegation that expires on its own, enforced outside software**.

## 3. Consequences for people and organisations

- **Who carries recovery?** Recording 1 recommends rehearsing restoration with the staff who will actually be on shift at the worst moment, not with the most senior experts. Resilience is a property of staffing and training, not only of architecture.
- **Key-person risk.** SANS 2026 reports that 68 % of organisations would be put at serious risk by losing one or two key individuals ([Infosecurity Magazine](https://infosecurity-magazine.com/news/ot-incidents-third-industrial)). AI could ease this by capturing tacit knowledge, or worsen it by concentrating expertise.
- **Small operators.** Water utilities and local energy providers rarely have dedicated staff for AI security. Controls that need specialist capacity will be unevenly adopted, which is a distributional risk.
- **All hazards.** Recording 1 claims that most outages come from human error and natural causes, not from attackers. The claim is unverified, but if it is broadly true, resilience investment should be judged against all hazards, not against AI threats alone.

## 4. Implications for the programme

- AI's most defensible near-term role in OT is **outside the safety function**, **read-only** through one-way paths, assisting diagnosis and restoration planning. This agrees with the ISC observation that safety-critical decisions remain with humans.
- Propose measuring **manual-fallback competence over time** as a resilience metric alongside AI benefit, for example time to operate safely in degraded mode during exercises.
- Proposed hypothesis **R1:** sites that introduce AI-assisted operations without scheduled degraded-mode exercises show declining manual-fallback performance within one to two years. *Falsified* if exercise performance stays stable.

## 5. Opportunities we risk overlooking

- AI-assisted **restoration rehearsal**: generating realistic recovery drills and checking configuration custody for completeness.
- AI help in **mapping dependencies** (licences, certificates, directory services) that today are discovered only during a real recovery.
- A **"recover one site on paper"** exercise (rec. 1), with AI acting as challenger rather than operator.
