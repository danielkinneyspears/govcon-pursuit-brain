# Bid/No-Bid Criteria

The knockout checks, the weighted scorecard, pWin estimation, and the validation
checklist for `qualifying-opportunities`. The scorecard and pWin become the
content of the `decisions/bid-decision.md` entity.

## Contents
- How to use this file
- Knockout checks
- The weighted scorecard
- pWin estimation
- Reading the result
- Validation checklist

## How to use this file

Run the knockout checks first; a triggered knockout drives the recommendation.
Then score the six categories, 1–5, each score carrying one line of evidence
keyed to a `source`. Where evidence is an unknown, score conservatively and tag
the bid-decision entity's `confidence` accordingly. Estimate pWin separately.

## Knockout checks

A knockout makes the opportunity unwinnable or non-viable on its face. Any
**yes** drives a no-bid; an **uncertain** becomes a condition in a
conditional-bid recommendation.

- **Set-aside ineligibility** — set aside for a category the team cannot qualify
  for as prime.
- **Size standard** — the team exceeds the NAICS small-business size standard on
  a small-business acquisition.
- **Missing mandatory qualification** — a required certification, clearance,
  facility approval, or accreditation not held and not obtainable in time.
- **No contract vehicle** — a task order under an IDIQ the team does not hold.
- **Fatal past-performance gap** — past performance is pass/fail (or effectively
  gating) and the team has none relevant, and cannot team for it.
- **Unresolvable OCI** — an organizational conflict of interest that cannot be
  mitigated or waived.
- **Funding is not real** — no identified budget or appropriation.
- **No time to comply** — too little schedule to produce a compliant proposal.
- **Categorically unacceptable terms** — terms leadership has ruled out.
- **Strategic veto** — work that conflicts with strategy enough that leadership
  will not staff or fund it.

## The weighted scorecard

Six categories, weighted to 100%. Score each 1–5 (1 strongly unfavorable, 3
neutral/uncertain, 5 strongly favorable); average within a category; apply the
weight.

| # | Category | Weight | Criteria (score each) |
|---|---|---|---|
| 1 | Customer and relationship | 20% | customer knowledge and access; requirement shaping; incumbency / relationship strength |
| 2 | Opportunity fit and strategic alignment | 15% | strategic fit; capability match to scope; qualification fit |
| 3 | Competitive position | 20% | competitive landscape; differentiation; incumbent strength |
| 4 | Solution and delivery capability | 15% | solution maturity; staffing and key personnel; past performance |
| 5 | Financial and business | 20% | value and margin; funding certainty; B&P cost vs. expected value; contract type risk |
| 6 | Risk and executability | 10% | OCI and compliance risk; teaming dependency; schedule feasibility; terms and executability |

The overall score is the weighted sum of the category averages, on the 1–5
scale. Report the overall score, every category average, and the
lowest-scoring criteria — those are the decision drivers.

## pWin estimation

Estimate probability of win as a percentage — a disciplined judgment, not a feeling:

1. **Base rate.** With *N* credible bidders and nothing else, start near 1/*N*.
2. **Adjust** up for a genuine customer relationship, documented requirement
   shaping, real discriminators, and a reachable price-to-win; down for a strong
   incumbent competitor, a commodity offer, or an unreachable price.
3. **Anti-optimism.** Incumbents lose; a relationship is not a commitment;
   "we can do the work" is a threshold, not an advantage. If you cannot name a
   concrete reason this offer beats the field, pWin is low.
4. **State the basis** — the one or two factors that most move the number.

A pWin below roughly 25–30% on a costly pursuit usually argues for no-bid unless
the strategic value is exceptional and explicitly stated.

## Reading the result

- **No-bid** — any knockout triggered; or a low score; or a pWin too low to
  justify the B&P investment.
- **Conditional bid** — attractive but hinging on specific, resolvable
  uncertainty. Name each condition, assign an owner, set a date.
- **Bid** — no knockouts, a solid score, a pWin that justifies the investment.

## Validation checklist

```
- [ ] pursuit.md exists, with posture, mode, and sensitivity policy set
- [ ] Customer entities created and tagged (source, confidence, sensitivity, provenance)
- [ ] Every score has a line of evidence; low-confidence scores are marked
- [ ] Every intake unknown is recorded as a gap on the bid-decision entity
- [ ] Knockouts all checked; any yes/uncertain is reflected in the recommendation
- [ ] The recommendation is consistent with the knockouts, the score, and pWin
- [ ] The bid-decision entity is tagged approval: pending
- [ ] opportunity-profile.md and bid-decision.md views rendered with the view header
- [ ] pursuit.md entity index, view index, and change log updated
```
