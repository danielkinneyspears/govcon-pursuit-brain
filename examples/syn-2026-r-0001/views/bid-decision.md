# Bid Decision — FSSA Enterprise IT Service Desk Recompete

- View rendered by: qualifying-opportunities (example run)
- Rendered: 2026-05-19
- Source of truth: the pursuit entity graph (this document is a **rendered
  view** — do not hand-edit; change the entities and re-render)
- Lowest confidence among source entities: medium
- Entities awaiting approval: 1 (`decisions/bid-decision` is `approval: pending`)

> [!warning] Synthetic example
> Fictional pursuit for illustration. See `pursuit.md` for context.

## Recommendation

**Conditional bid** — pursue with two specific conditions that, if
unresolved by their assigned dates, convert the recommendation to no-bid.

| Condition | Owner | Resolve by | Status |
|---|---|---|---|
| Secure Acme Federal Holdings as a teaming partner contributing ITIL service-desk past performance | capture lead | 2026-05-26 | open |
| Confirm two named Service Desk Lead candidates with active clearances | staffing lead | 2026-05-29 | open |

## Headline

- **Estimated pWin: 25%** — base 25% for ~4 credible bidders; modest
  up-adjustment for documented incumbent SLA breaches; modest down-adjustment
  for limited prior FSSA relationship.
- **Weighted scorecard: ~3.0 / 5** — middle-of-the-road; the upside is
  incumbent vulnerability, the constraints are relationship and staffing.
- **Posture:** challenger.

## Decision drivers

1. Incumbent (`competitors/acme-synthetic-solutions`) is vulnerable on
   recent service-level breaches.
2. Team has no prior FSSA relationship — the most important controllable
   gap.
3. Staffing for the Service Desk Lead role is uncertain at the bid
   threshold.

## Evidence

- Claim: [[acme-is-incumbent]] — Acme Synthetic Solutions holds the
  predecessor contract.
- Source: [[sam-gov-syn-2026]] — SAM.gov award notice for the predecessor
  contract.

## What needs to happen next

- The capture lead works the teaming-partner condition; the staffing lead
  works the personnel condition.
- An executive owner needs to approve this `conditional bid` (the
  decision entity is `approval: pending`).
- `analyzing-competitors` runs next to enrich the other likely-bidder
  entities and quantify the incumbent's specific exposures.
