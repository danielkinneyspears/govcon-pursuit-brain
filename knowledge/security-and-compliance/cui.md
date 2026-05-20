---
id: cui
type: concept
title: Controlled Unclassified Information (CUI)
tags:
  - security-and-compliance
  - cui
status: stable
sensitivity: public
source: 32 CFR Part 2002; National Archives CUI Registry (archives.gov/cui)
confidence: high
updated: 2026-05-19
provenance: domain-wiki-build-v0.2.0 / 2026-05-19
last_verified: 2026-05-19
next_review_due: 2026-08-19
---

# Controlled Unclassified Information (CUI)

**Controlled Unclassified Information** is information the executive branch
creates or possesses that the government, or an entity acting on its behalf,
must safeguard or disseminate under law, regulation, or government-wide
policy — but that is **not classified**. The CUI program is established by
**Executive Order 13556** and standardized at **32 CFR Part 2002**, with the
**National Archives (NARA)** as the Executive Agent.

## The CUI Registry

NARA maintains the **CUI Registry** at archives.gov/cui — the government-wide
online repository for CUI categories, markings, and handling controls.
Categories are grouped into roughly **20 organizational index groupings**
containing well over **100 individual categories and subcategories**.

Common groupings include:

- **Defense** (e.g., Controlled Technical Information, Naval Nuclear
  Propulsion Information).
- **Critical Infrastructure**.
- **Export Controlled** (cross-referenced with [[itar-ear]]).
- **Privacy** (PII / PHI).
- **Procurement and Acquisition** (Source Selection Information, Contract
  Bid Information, Proprietary Manufacturing).
- **Law Enforcement, Financial, Tax, Statistical**, and others.

## Marking and handling

CUI is **marked** with banner markings (e.g., `CUI`) and may include
category-specific dissemination controls (e.g., `CUI//SP-CTI` for Controlled
Technical Information). Handling controls — access, encryption, storage,
destruction — follow 32 CFR § 2002 and the safeguarding rules in
[[nist-800-171]] when in nonfederal systems.

## For federal contractors

- Contractors handling CUI on behalf of the government generally must protect
  it per **NIST SP 800-171** (see [[nist-800-171]]).
- DoD contractors are additionally subject to [[cmmc]] requirements.
- A pursuit wiki may **not** contain CUI unless the organization's policy and
  the applicable safeguarding rules permit it; classify the pursuit's
  `sensitivity` accordingly (see `conventions/tagging.md`).

## Links

- protected on nonfederal systems per [[nist-800-171]]
- DoD compliance via [[cmmc]]
- cross-cuts [[itar-ear]] for export-controlled material
