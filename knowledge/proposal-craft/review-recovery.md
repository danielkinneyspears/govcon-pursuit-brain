---
id: review-recovery
type: concept
title: Review Recovery
tags:
  - proposal-craft
  - review-phase
status: stable
sensitivity: public
source: Common federal proposal practice
confidence: high
updated: 2026-05-19
provenance: domain-wiki-build-v0.2.0 / 2026-05-19
last_verified: 2026-05-19
next_review_due: 2027-05-19
---

# Review Recovery

The disciplined work of **closing every color-team finding that matters**
before the next milestone. A review without recovery is theater — the
weaknesses were found and then shipped anyway.

## The recovery loop

1. **Triage** every finding by severity (deficiency → significant weakness →
   weakness → strength opportunity → administrative). See
   [[strengths-weaknesses-deficiencies]].
2. **Assign** each must-fix finding to a single owner with a due date inside
   the recovery window. Track on an action register.
3. **Drive the fix** — the section author makes the correction.
4. **Verify closure** against the standard: does the corrected content
   satisfy the requirement (per the [[compliance-matrix]]) and answer the
   evaluation concern (per [[section-m]])?
5. **Re-open** any fix that does not actually resolve the finding. "The
   author changed it" is not closure.

## The burn-down

Maintain an honest count of open findings by severity against time
remaining. Open deficiencies are shown as open deficiencies.

## When recovery is at risk

If the must-fix findings will not all close in the window, **escalate** — do
not silently mark open findings closed. An acknowledged open deficiency is a
decision the team made with its eyes open; a hidden one is a near-certain
loss.

## Links

- works the findings from every [[color-team-review]] (especially [[red-team]])
- updates the [[compliance-matrix]] as fixes close
- distinct from but adjacent to [[gold-team]] / [[white-glove]]
