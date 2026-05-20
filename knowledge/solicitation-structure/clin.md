---
id: clin
type: concept
title: Contract Line Item Number (CLIN)
tags:
  - solicitation-structure
  - cost-and-pricing
status: stable
sensitivity: public
source: FAR 4.10 Uniform Procurement Instrument Identifiers; FAR 15.204-1 (Section B)
confidence: high
updated: 2026-05-19
provenance: domain-wiki-build-v0.2.0 / 2026-05-19
last_verified: 2026-05-19
next_review_due: 2027-05-19
---

# Contract Line Item Number (CLIN)

A priced line item in [[section-c|the requirement]] structure, listed in
Section B (Supplies or Services and Prices/Costs) of a
[[uniform-contract-format]] solicitation. A CLIN groups one priced deliverable
or set of deliverables — services for a period, a quantity of a product, an
option year.

## Key facts

- Each CLIN has a CLIN number, description, quantity, unit of measure, unit
  price, and (often) a not-to-exceed amount.
- Sub-CLINs (SLINs / informational sub-line items) decompose a CLIN further
  without separately pricing it.
- Option-year work is normally separate CLINs (CLIN 1xxx base, 2xxx option 1,
  etc.). Evaluators usually evaluate total price across all CLINs including
  options.
- The proposed [[basis-of-estimate]] and cost narrative must line up to the
  CLIN structure — government cost evaluators read by CLIN.

## Links

- listed in Section B of [[uniform-contract-format]]
- priced via [[basis-of-estimate]]
- evaluated for [[price-reasonableness]] and (cost-reimbursement) [[cost-realism-analysis]]
