---
id: capture-manager
type: playbook
title: Capture Manager Playbook
tags:
  - playbook
  - capture-and-bd
status: stable
sensitivity: public
source: Common federal capture practice (Shipley-style gated lifecycle); this package's skill set
confidence: high
provenance: domain-wiki-build-v0.2.0 / 2026-05-19
last_verified: 2026-05-19
next_review_due: 2027-05-19
updated: 2026-05-19
---

# Capture Manager Playbook

**Audience.** The capture manager owning a federal pursuit from
opportunity-identification through bid validation. You are the person who
decides whether the team should chase this work and, if so, what it will take
to win.

**Soul of the role.** Win the bid before the RFP releases. Most of what a
proposal can do has already been decided by Section M, the customer's
relationship with the field, and the price. Your job is to influence those
inputs while they are still movable.

## Gate 0: Opportunity identification

**You create / open:** a pursuit wiki for the opportunity (a skill bootstraps
it; see `qualifying-opportunities` (a skill in `skills/`) in `skills/`). Set the pursuit posture
honestly — incumbent-defending, challenger, favored-challenger, outsider, or
teaming-partner. Posture branches every later decision.

**You read:** [[bid-no-bid]], [[set-aside-overview]], the relevant
`vehicles/` (in `knowledge/`) page if a vehicle constrains the bid.

**You write entity pages:** the agency and program office in `customer/`; any
known stakeholders.

**Failure mode:** pursuing every opportunity that looks interesting. Posture
and bid/no-bid discipline exist to prevent this.

## Gate 1: Pursuit decision

**You decide:** does the pursuit justify capture resources? Drive the first
gate review with `qualifying-opportunities` (a skill in `skills/`)'s scorecard and knockouts.

**You write:** `01-bid-decision` entity with the scorecard, pWin estimate,
and recommendation. Tag it `approval: pending` until a leadership owner signs
off.

**You read:** [[set-aside-overview]], [[size-standards-and-naics]], the
relevant SBA program page if a set-aside applies.

**Failure mode:** scoring high because the team likes the work. Honest
unknowns beat confident guesses; mark `confidence: low` where evidence is
thin.

## Capture phase work (between gates)

You are now spending capture money. Each week, advance these workstreams:

- **Customer engagement** (legitimate, within the
  [[procurement-integrity-act]] limits). Build `contacts/` entities for each
  engagement; record what the customer signaled and what message you
  delivered.
- **Black Hat competitive read.** Build `competitors/` entities for each
  likely bidder using [[black-hat]] discipline; never accept
  [[procurement-integrity-act|source-selection-sensitive]] or
  competitor-proprietary information.
- **Shaping responses.** Sources-sought, RFI, draft-RFP comments — all
  rung-5 official channels, never private informational advantage.
- **Teaming.** Identify capability and past-performance gaps; structure
  workshare per [[limitation-on-subcontracting]] and (if applicable)
  [[sba-mentor-protege]].
- **Hot buttons and discriminators.** Build `hot-buttons/` and
  `discriminators/` entities. Apply the four-part discriminator test:
  valuable, true, provable, **rare**.
- **Price-to-win.** Estimate the budget range and competitor prices; set the
  target the bid must reach. Document in `04-price-to-win`.

**Source register (`source-register/`).** Every claim about the customer,
competitors, budget, or incumbent traces to a source page — SAM.gov notice,
USAspending record, public press, customer meeting note. Treat anything
unsourced as `confidence: low` until grounded.

## Posture branching

Your posture, set at Gate 0, changes the work:

- **Incumbent-defending.** Emphasize continuity, [[cpars|CPARS]] evidence,
  proven performance, low transition risk. Hardest enemy is complacency.
  Force an explicit "incumbent vulnerability" entity in `risks/` — what
  could make the customer change.
- **Challenger.** Neutralize transition risk early. Develop
  incumbent-capture staffing. Make "why change?" explicit. Ghost incumbent
  pain through positive frames in `discriminators/`, never named
  disparagement.
- **Favored challenger.** Be ambitious but disciplined. The biggest risk is
  pricing too high relative to a hungrier competitor.
- **Outsider.** The early work is access, not strategy. Most of the gate
  reviews honestly recommend no-bid until access is built.
- **Teaming-partner.** Your job is to sell the prime, not the customer.
  Document `teammates/` with the value the prime can claim from your
  participation.

## Gate 2: Preliminary bid decision

**You decide:** given a draft RFP (or imminent RFP) and the maturing capture
plan, do we intend to bid? Re-run the qualifying skill at the bid-decision
gate; compare to Gate 1 explicitly.

**You write:** the win strategy artifact — themes, discriminators, hot
buttons, posture, price posture — in `05-win-strategy` (a view rendered
from the corresponding entity pages).

**Failure mode:** failing to flip a no-bid when the field firmed up
differently than expected.

## Gate 3: Bid validation

**You decide:** given the **actual** released RFP and the current capture
position, do we still bid? Compare Section L and Section M to what you
shaped for; if either departs significantly from expectations, return to
[[bid-no-bid]].

**You hand off:** the pursuit wiki to the proposal manager (see
[[proposal-manager]]). The capture plan is now the proposal's substrate;
the proposal manager works with what you handed them.

**Failure mode:** treating handoff as throwing the pursuit over a wall. You
remain the customer-facing lead through submission and the debrief.

## What a good capture manager does that nothing else does

- Builds and protects the **customer relationship** through legitimate
  channels.
- Forces the **honest read** at every gate — including the no-bids.
- Owns the **evidence base** (`source-register/`) for the pursuit's
  intelligence claims.
- Sets the **posture** and refuses to let later work drift away from it.
