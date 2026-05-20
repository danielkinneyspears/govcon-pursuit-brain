---
id: fedramp
type: concept
title: FedRAMP
tags:
  - security-and-compliance
  - fedramp
status: stable
sensitivity: public
source: FedRAMP Program (fedramp.gov); NIST SP 800-53; OMB FedRAMP policy
confidence: high
updated: 2026-05-19
provenance: domain-wiki-build-v0.2.0 / 2026-05-19
last_verified: 2026-05-19
next_review_due: 2026-08-19
---

# FedRAMP

**FedRAMP** — the Federal Risk and Authorization Management Program — is the
government-wide program that standardizes security assessment, authorization,
and continuous monitoring for **cloud services** used by federal agencies.

## Baselines and certification classes

Historically, FedRAMP used **FIPS 199 impact-level baselines** — **Low**,
**Moderate**, and **High** — keyed to the confidentiality, integrity, and
availability impact of the data the system handles.

**As of 2026**, FedRAMP is transitioning to **lettered Certification Classes**
(per NTC-0004, published February 25, 2026, to be formalized in CR26 by end
of June 2026):

| New class | Replaces | Notes |
|---|---|---|
| A | (new pilot) | New pilot baseline |
| B | Li-SaaS and Low | |
| C | Moderate | |
| D | High | |

The terminology is also changing from **"FedRAMP Authorization"** /
**"Authorized"** to **"FedRAMP Certification"** / **"Certified"**, intended
as the single official label across all certification types.

## FedRAMP 20x

FedRAMP 20x is the modernized program direction. As of 2026, the Low and
Moderate authorizations under 20x are set to open by end of 2026, with High
pilot scheduled for 2027.

## What contractors do

- Document the system against the applicable baseline (FedRAMP-tailored
  NIST SP 800-53 controls).
- Engage a **Third-Party Assessment Organization (3PAO)** for the assessment.
- Pursue an **Agency Authorization** (a federal agency sponsors) or a **Joint
  Authorization Board (JAB)** authorization (now the FedRAMP Board under
  recent reorganization).
- Maintain **continuous monitoring** post-authorization.

> [!warning] Terminology in flux
> "Authorized" and "Certified" terminology, and the Low/Moderate/High vs.
> Class A/B/C/D labels, are both in use during the 2026 transition. Verify
> against current FedRAMP guidance and the specific solicitation language.

## Links

- relevant for any cloud-service offering to federal agencies
- aligned to NIST SP 800-53 controls
- distinct from [[cmmc]] (DoD-specific, on-prem and nonfederal systems) and
  [[nist-800-171]] (CUI on nonfederal systems)
