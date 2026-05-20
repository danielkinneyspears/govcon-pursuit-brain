---
id: data-rights
type: concept
title: Data Rights
tags:
  - special-clauses
status: stable
sensitivity: public
source: FAR Subpart 27.4 (acquisition.gov/far/subpart-27.4); DFARS Subpart 227.71 / 227.72 (DoD technical data and software)
confidence: high
updated: 2026-05-19
provenance: domain-wiki-build-v0.2.0 / 2026-05-19
last_verified: 2026-05-19
next_review_due: 2027-05-19
---

# Data Rights

**Data rights** clauses determine **what the government may do** with the
technical data, software, and copyrighted material a contractor develops or
delivers under a federal contract — and what rights the contractor retains.

## The two regimes

- **Civilian agencies** — FAR Subpart 27.4. Standard clauses at FAR 52.227-14
  (Rights in Data — General) and others.
- **DoD** — DFARS Subpart 227.71 (technical data, non-commercial items) and
  Subpart 227.72 (computer software, non-commercial items). Standard clauses
  at DFARS 252.227-7013 (technical data) and 252.227-7014 (computer software).

## Categories of rights (DoD framing, broadly similar to FAR)

- **Unlimited Rights** — government may use, modify, reproduce, release,
  perform, display, or disclose, without restriction. Typical for data
  developed exclusively at government expense.
- **Government Purpose Rights** — full use within the government and to
  third parties for government purposes (not commercial); typically a
  **5-year period**, after which the rights convert to unlimited.
- **Limited Rights** (data) / **Restricted Rights** (software) — narrowest
  rights; the contractor retains commercial rights and the government's use
  is limited.
- **Commercial Computer Software License** — for [[far-part-12-commercial|commercial software]],
  the standard commercial license applies (FAR 12.212 / DFARS 227.7202).
- **Specially Negotiated License Rights** — bespoke arrangements.

## Marking and assertions

- Contractors must **assert** restrictions on delivered data and software by
  marking, with assertions made in the contract (DFARS 252.227-7017 for
  pre-award identification).
- **Improper or missing markings** can default the data to unlimited rights.

## Why it matters in the proposal

- The team should know going in what intellectual property would deliver
  under each clause and what could be lost.
- Solicitation Section H or attachments may require specific data-rights
  assertions; treat them as compliance matrix rows.
- For commercial offerings, **commercial license terms** are the default;
  attempts to impose non-commercial data-rights clauses on commercial items
  should be questioned (FAR 12.211, 12.212).

## Links

- typically incorporated via Section I and tailored in
  [[section-h-special-contract-requirements]]
- inventoried in [[compliance-matrix]]
- distinct from [[itar-ear]] (export controls) and [[cui]] (information
  protection)
