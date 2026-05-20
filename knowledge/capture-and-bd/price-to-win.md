---
id: price-to-win
type: concept
title: Price-to-Win (PTW)
tags:
  - capture-and-bd
  - cost-and-pricing
  - capture-phase
status: stable
sensitivity: public
source: Common federal capture practice (Shipley-style price-to-win analysis)
confidence: high
updated: 2026-05-19
provenance: domain-wiki-build-v0.2.0 / 2026-05-19
last_verified: 2026-05-19
next_review_due: 2027-05-19
---

# Price-to-Win (PTW)

The estimate of **the price the bid has to reach to win** — built from the
customer's budget and competitors' likely pricing, **not** from the team's own
cost. PTW and a bottom-up cost estimate answer different questions: cost says
what the work costs the team; PTW says what the customer is willing and
likely to pay the winner.

## Method (compact)

1. **Establish the evaluation context** — [[best-value-tradeoff]] or [[lpta]];
   how price is weighted; whether [[cost-realism-analysis]] applies.
2. **Estimate the customer's budget** as a range from signals: prior contract
   value (escalated and scope-adjusted), signaled [[igce]], comparable
   awards, scope-built ROM. Never solicit or accept the actual IGCE.
3. **Estimate each competitor's likely price** from the [[black-hat]]
   profile: their cost structure, their posture (aggressive / market /
   premium), and the solution they would propose.
4. **Set the price-to-win range and target**:
   - Under LPTA, target at or just below the lowest credible competitor price,
     with a realism floor.
   - Under best-value, target the highest price the team's non-price
     advantage can defend.
5. **Reconcile against the team's bottom-up cost**. Where cost exceeds
   target, identify and quantify pricing levers (labor mix, level of effort,
   indirect rates, subcontractor strategy, fee, escalation, solution scope).
   If no realistic combination of levers reaches the target, **report that**;
   it belongs back in the [[bid-no-bid]] decision.

## Anti-patterns

- Substituting the team's bottom-up cost for the target.
- Reporting a single confident number instead of a range with a stated basis.
- Reaching the target by making the bid unrealistic (especially under cost
  realism, where the government adjusts an unrealistic low cost upward).

## Links

- depends on [[black-hat]] for competitor reads
- consistent with [[best-value-tradeoff]] or [[lpta]] posture
- constrains the [[basis-of-estimate]]
- fed back into [[bid-no-bid]] when unbridgeable
