---
id: bid-decision
type: decision
title: Bid Decision — FSSA Enterprise IT Service Desk Recompete
tags:
  - decision
  - synthetic-example
  - capture-phase
status: stable
sensitivity: public
source: synthetic example for govcon-pursuit-brain v0.2.2
confidence: medium
provenance: govcon-pursuit-brain-v0.2.2-example / 2026-05-19
last_verified: 2026-05-19
next_review_due: 2026-08-19
updated: 2026-05-19
approval: pending
---

# Bid Decision — FSSA Enterprise IT Service Desk Recompete

> [!warning] Synthetic only
> Fictional bid decision invented to show the format.

## Gate

Bid validation gate (RFP released 2026-05-01; proposals due 2026-06-15).

## Recommendation

**Conditional bid** — pursue with two specific conditions:

1. Secure (synthetic) Acme Federal Holdings as a teaming partner contributing
   ITIL-aligned service-desk past performance by 2026-05-26.
2. Confirm (synthetic) two named candidates for the Service Desk Lead role
   with active clearances by 2026-05-29.

If either condition is unresolved by its date, the recommendation converts
to **no-bid**.

## Knockout checks

| Knockout | Result | Notes |
|---|---|---|
| Set-aside ineligibility | NO | Team qualifies under NAICS 541519 |
| Size standard exceeded | NO | |
| Missing mandatory qualification | UNCERTAIN | Service Desk Lead clearance bench is thin — see condition 2 |
| No contract vehicle | NO | Direct award, not a task order |
| Fatal past-performance gap | NO | Team has adjacent service-desk past performance |
| Unresolvable OCI | NO | None identified |
| Funding is not real | NO | Existing program continuity |
| No time to comply | NO | 4-week window is tight but workable |
| Categorically unacceptable terms | NO | Standard FFP services contract |
| Strategic veto | NO | On-strategy market |

## Scorecard summary

| Category | Weight | Score (1–5) |
|---|---|---|
| Customer and relationship | 20% | 2 (challenger, limited prior contact) |
| Opportunity fit and strategic alignment | 15% | 4 |
| Competitive position | 20% | 3 (vulnerable incumbent helps) |
| Solution and delivery capability | 15% | 3 (staffing risk per condition 2) |
| Financial and business | 20% | 3 |
| Risk and executability | 10% | 3 |
| **Weighted overall** | | **~3.0** |

## pWin

**Estimated pWin: 25%**. Base rate ~25% with ~4 credible bidders; adjusted
slightly down for challenger posture and limited prior FSSA relationship,
slightly up for documented incumbent SLA breaches and a credible
transition-risk-neutralization story we can tell.

Basis: incumbent vulnerability is the principal up-adjustment;
customer-relationship gap is the principal down-adjustment.

## Decision drivers

1. The incumbent is vulnerable on recent service-level breaches (per
   [[acme-is-incumbent]] and prior public information).
2. The team has no prior FSSA relationship — the most important controllable
   gap.
3. Staffing for the Service Desk Lead role is uncertain at the bid
   threshold.

## Gaps and unknowns

- Customer's tolerance for transition risk relative to incumbent loyalty —
  unknown, would need a customer engagement to read (now within the
  post-RFP communication blackout; cannot resolve).
- Likely price ranges of the other two challengers — to be assessed in
  `analyzing-competitors` follow-up.

## Conditions (conditional bid)

| Condition | Owner | Resolve by | Status |
|---|---|---|---|
| Secure (synthetic) Acme Federal Holdings teaming partner | capture lead | 2026-05-26 | open |
| Confirm two named Service Desk Lead candidates with active clearances | staffing lead | 2026-05-29 | open |

## Claims this decision rests on

- [[acme-is-incumbent]]

## Sources cited

- [[sam-gov-syn-2026]]
- `sources/synthetic-rfp-summary.md`

## Links

- pursued: SYN-2026-R-0001 (`pursuit.md`)
- customer: [[fssa]]
- incumbent: [[acme-synthetic-solutions]]
