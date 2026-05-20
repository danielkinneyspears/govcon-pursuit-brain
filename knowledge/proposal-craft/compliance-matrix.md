---
id: compliance-matrix
type: concept
title: Compliance Matrix
tags:
  - proposal-craft
  - proposal-phase
status: stable
sensitivity: public
source: Common federal proposal practice
confidence: high
updated: 2026-05-19
provenance: domain-wiki-build-v0.2.0 / 2026-05-19
last_verified: 2026-05-19
next_review_due: 2027-05-19
---

# Compliance Matrix

A table that inventories **every requirement** in a solicitation and
cross-walks it to the proposal location that addresses it. The compliance
matrix is the spine of a compliant proposal — every later proposal artifact
works against it.

## How it is built

By "shredding" the solicitation: every directive in [[section-l]],
[[section-m]], and [[section-c]] is extracted as **one atomic, separately
verifiable requirement**. Compound instructions get split into atomic rows.

## The cross-walk

Each requirement is linked across the proposal triad:

- The **Section L** instruction that governs where it is written.
- The **Section M** factor that scores it.
- The **Section C / SOW / PWS / SOO** requirement it implements.

A conflict between L and M, or a Section M factor with no Section L
instruction (or vice versa), is a candidate question for the contracting
officer — flag it, don't guess.

## Status tracking

Each row carries a **status** (Not Started / In Draft / Drafted / Compliant /
At Risk / N/A) and an **owner**. A proposal is ready to ship only when every
mandatory requirement is **Compliant**.

> [!warning] No orphans, no compounds
> Every mandatory requirement is in the matrix; every row is atomic. Compounds
> hide missed obligations and unsupported claims.

## Links

- inventories [[section-c]]
- cross-walks [[section-l]] and [[section-m]]
- the spine of proposal-craft work
- consumed by [[red-team]] and [[blue-team]] / [[pink-team]] / [[gold-team]] reviews
