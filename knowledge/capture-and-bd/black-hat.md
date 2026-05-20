---
id: black-hat
type: concept
title: Black Hat (Competitive Simulation)
tags:
  - capture-and-bd
  - capture-phase
status: stable
sensitivity: public
source: Common federal capture practice (Shipley-style competitive analysis)
confidence: high
updated: 2026-05-19
provenance: domain-wiki-build-v0.2.0 / 2026-05-19
last_verified: 2026-05-19
next_review_due: 2027-05-19
---

# Black Hat (Competitive Simulation)

A capture-phase competitive simulation where the team **plays each competitor**
and models how that competitor will bid: the likely solution, win themes,
strengths and vulnerabilities, and price posture. The output is a set of
predicted offers concrete enough that the win strategy can be built to beat
them.

## The core technique

For each likely competitor, drop the team's own perspective and answer as
that competitor's capture lead:

1. **Would we bid this, and how badly do we want it?**
2. **What solution would we propose?** Given our typical approach and
   partners.
3. **What would our win themes be?** Against this customer.
4. **Where are we strong on this bid?**
5. **Where are we vulnerable for this requirement?**
6. **What price posture would we take, and why?**

Give each competitor their **best plausible bid** — no strawmen. A Black Hat
that makes competitors look weak produces dangerous overconfidence.

## Outputs

- A competitor entity (page) per likely bidder with profile and assessed offer.
- A comparison matrix scoring competitors and the team across the factors the
  customer will evaluate.
- A **most-probable-winner** read — including, honestly, the cases where it
  is not the team.
- **Counters**, **ghosting opportunities**, and the **team's own exposures**
  (which become real risk entities).

## Ethics

Only **properly sourced information** is used. Competitor-proprietary or
source-selection-sensitive material is **quarantined**, never folded into the
assessment — see [[procurement-integrity-act]].

## Links

- a capture-phase review (distinct from the proposal-phase [[color-team-review]] family)
- informs [[price-to-win]] and [[win-theme]]
- bounded by [[procurement-integrity-act]]
