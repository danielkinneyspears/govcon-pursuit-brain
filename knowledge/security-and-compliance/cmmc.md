---
id: cmmc
type: concept
title: Cybersecurity Maturity Model Certification (CMMC) 2.0
tags:
  - security-and-compliance
  - cmmc
  - dod
status: stable
sensitivity: public
source: 32 CFR Part 170 (CMMC Program); DoD CIO CMMC (dodcio.defense.gov)
confidence: high
updated: 2026-05-19
provenance: domain-wiki-build-v0.2.0 / 2026-05-19
last_verified: 2026-05-19
next_review_due: 2026-08-19
---

# Cybersecurity Maturity Model Certification (CMMC) 2.0

The **Cybersecurity Maturity Model Certification** is the DoD program for
verifying that defense contractors implement adequate cybersecurity to
protect Federal Contract Information (FCI) and [[cui|Controlled Unclassified
Information]].

## The three CMMC levels

- **Level 1 — Foundational**. The **15 basic safeguarding requirements of FAR
  52.204-21** for protecting Federal Contract Information (FCI), as confirmed
  in the **32 CFR Part 170 final rule**. **Annual self-assessment**.
- **Level 2 — Advanced**. The **110 controls of [[nist-800-171|NIST SP
  800-171]] Rev. 2**. Most contractors handling CUI fall here.
- **Level 3 — Expert**. Subset of NIST SP 800-172 controls on top of Level 2,
  for the most sensitive programs.

> [!note] 15 requirements vs. 17 practices
> Earlier CMMC 2.0 materials (and the Level 1 Assessment Guide v2.13) describe
> 17 practices derived from the FAR 52.204-21 requirements. The **32 CFR
> final rule** consolidated three physical-protection practices into one
> (`PE.L1-B.1.IX — Manage Visitors & Physical Access [FCI Data]`), bringing
> the total to **15**, aligning to the 15 distinct FAR 52.204-21
> requirements. Cite the 32 CFR rule, not earlier guides.

## Status and timeline (2026)

- The **CMMC Program Rule** (32 CFR Part 170) became **effective December
  2024**.
- The companion **DFARS rule** (48 CFR amendment, DFARS 252.204-7021) became
  effective **November 10, 2025** — new Level 2 contracts began requiring
  **self-assessments** at that date.
- Beginning **November 2026** (per the phased rollout in 32 CFR Part 170),
  **third-party assessments by C3PAOs** are required for many Level 2
  contracts.
- DoD currently bases CMMC Level 2 on **NIST SP 800-171 Rev. 2** (110
  controls in 14 families). A transition to **Rev. 3** will follow separate
  rulemaking.

## What contractors must do

- Conduct a Level 2 **self-assessment** against the 110 controls, plus a
  **System Security Plan (SSP)** and a **Plan of Action and Milestones
  (POA&M)** for unmet controls.
- Submit the score to the **Supplier Performance Risk System (SPRS)**.
- Schedule a C3PAO assessment in the year the contract requires Level 2
  certification.

## Links

- protects [[cui]]
- implements [[nist-800-171]] (Rev. 2 currently; Rev. 3 in a future
  rulemaking)
- DoD-specific compliance regime; civilian agencies use other CUI
  safeguarding paths
