---
id: proposal-manager
type: playbook
title: Proposal Manager Playbook
tags:
  - playbook
  - proposal-craft
status: stable
sensitivity: public
source: Common federal proposal practice (Shipley-style proposal lifecycle); this package's skill set
confidence: high
provenance: domain-wiki-build-v0.2.0 / 2026-05-19
last_verified: 2026-05-19
next_review_due: 2027-05-19
updated: 2026-05-19
---

# Proposal Manager Playbook

**Audience.** The proposal manager owning a federal pursuit from RFP release
through submission. The capture manager (see [[capture-manager]]) handed you
a pursuit wiki with the customer, competitors, themes, and the price-to-win
target. Your job is to convert that into a compliant, responsive, compelling
submission, on schedule.

**Soul of the role.** A federal proposal is won by **process** as often as by
content. Discipline beats heroics.

## Day 0: Kickoff

**You read:** Section L, Section M, Section C, Section H, Section K of the
released RFP. Then [[compliance-matrix]], [[section-l]], [[section-m]],
[[section-c]]. Then [[blue-team]] / [[pink-team]] / [[red-team]] /
[[gold-team]] / [[white-glove]] in `proposal-craft/`.

**You build:** the proposal schedule **backward** from the proposal due
date. Reserve a recovery window after every review (see [[review-recovery]]).
If the work does not fit the time, surface that **now** to leadership — not
the week before Red.

**You assign:** every volume to a volume lead; every section to one
accountable author. Unassigned sections are how requirements get missed.

**You write entity pages / views:** a `09-proposal-management/` workspace (or
its entities — schedule, assignments, action register, question log,
amendment log). A skill exists for this in the sibling
`federal-proposal-skills` package; the wiki-native skill is planned.

## Day 1–N: Shredding and outlining

**You run:** the shred. Build the [[compliance-matrix]] from Sections L, M,
and C. Every requirement is atomic; the cross-walk (L ↔ M ↔ C) is populated.
Flag conflicts and ambiguities as **CO questions** — submit them by the
solicitation's question deadline.

**You build:** the annotated outline, structured to Section L. Every section
gets owner, factor mapping, theme assignment, proof points, and a page
allocation weighted by Section M importance (not evenly). Storyboard every
substantive section before drafting.

**You run:** [[blue-team]] on the solution and win strategy
*before* heavy drafting. A wrong solution caught at Blue costs hours; the
same wrong solution caught at Red costs a recovery cycle.

## Drafting

**You enforce:** drafting from approved storyboards only. Drafting from a
blank page is the failure mode this package exists to prevent.

**You enforce:** the [[procurement-integrity-act|procurement-integrity]]
boundary on what claims may be made. Every claim that touches a competitor
or the customer's evaluation traces to a `source-register/` entity.

**You watch:** the [[compliance-matrix]] status column. A section "Drafted"
without verification against the requirement is not compliant — only
verified is.

## Q&A and amendments

**You run** the question log: every team question becomes a candidate CO
question. Submit by the deadline; do not telegraph strategy.

**For every amendment:** acknowledge it formally, re-shred the affected
sections, update the compliance matrix (preserving requirement IDs), assess
the schedule impact (a moved due date or new requirements may change the
plan), and notify affected section owners. A late-absorbed amendment is one
of the most preventable losses.

## Pink, Red, Gold, White Glove, Green

**You schedule and host** the color reviews per [[color-team-review]]. You
do not score; reviewers score. You **drive recovery** per
[[review-recovery]] after each review: every must-fix finding has an owner,
a due date, and a verified-closure check.

**Green Team (cost).** Run [[green-team]] on the cost volume before Red.
Confirm the cost-technical consistency check passes and the
[[basis-of-estimate]] is sufficient.

**White Glove.** A page-by-page production pass on the assembled package
after Gold. Distinct from the [[submission-compliance-check]].

## Submission

**You verify:** every page-limit, format, file-naming, volume-separation,
and submission-mechanics rule from [[section-l]] and Section K. Run the
[[submission-compliance-check]]. Submit **with margin** — portals fail and
uploads run long. Late is late under FAR 15.208.

**You record:** delivery confirmation, the submission timestamp, the
versions submitted.

## Posture branching (inherited from capture)

The pursuit posture (from `pursuit.md`) changes some choices:

- **Incumbent-defending.** Lean into [[cpars]] proof and continuity. Resist
  the temptation to over-engineer change for change's sake.
- **Challenger.** Lead transition risk hard in the transition section.
  Use `risks/` entities to surface and resolve transition concerns the
  evaluator will have on your behalf.

## Common failure modes

- Schedule fantasy: committing to a schedule that does not fit between
  kickoff and submission. Backward planning prevents this; ignoring backward
  planning's verdict causes it.
- Reviewer-comment dump: a Red Team without [[review-recovery]] is
  theater. Findings without owners do not get fixed.
- Hidden non-compliance: a section that addresses a requirement
  loosely without explicitly answering it. The compliance matrix's
  `Compliant` status is the gate; verify, do not assume.
- Lost amendments: failing to fully re-shred after an amendment. Set
  the cadence: every amendment triggers a focused re-shred and an owner
  notification.

## What a good proposal manager does that nothing else does

- Owns the **schedule** and refuses to lie to it.
- Owns the **process** — kickoff, reviews, recovery, production.
- Drives **compliance discipline** through the matrix.
- Protects the team's time from churn — fewer reviews, run well, beat many
  reviews run loosely.
