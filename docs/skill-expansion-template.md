# Skill Expansion Template

Use this template when proposing a new wiki-native lifecycle skill.

The skill must maintain entity pages and render views from the pursuit graph. It
must not treat a flat document as the source of truth.

## Skill Expansion Proposal: `<skill-name>`

Status: proposed

## Summary

Describe the user job this skill performs and why it belongs in
`govcon-pursuit-brain`.

## Lifecycle Fit

| Field | Value |
|---|---|
| Proposed skill name | `<gerund-skill-name>` |
| Canonical job | `<canonical-job-from-lifecycle-taxonomy>` |
| Phase | `plan | create | iterate` |
| Common names | `<aliases users search for>` |
| User goal | `<what the human is trying to accomplish>` |
| Owning / adjacent skills | `<upstream and downstream skills>` |

## Fit Check

- [ ] The canonical job exists in `docs/lifecycle-taxonomy.md`, or this proposal explains why a new row is needed.
- [ ] The skill name follows the repo convention: lowercase, hyphenated, gerund phrase.
- [ ] The skill is wiki-native: it maintains entities and renders views.
- [ ] The skill does not write a flat artifact as the source of truth.
- [ ] The skill has a clear owner in the lifecycle.

## Proposed Frontmatter

```yaml
---
name:
description:
canonical_job:
phase:
common_names:
  -
---
```

Description requirements:

- Third-person.
- Trigger-rich.
- Under the skill platform limit.
- Names the user task and the primary graph/view outputs.

## Source Inputs

### Raw Sources

```text
pursuits/<id>/sources/
```

List the raw inputs the skill may read:

- Solicitation sections.
- Amendments.
- Customer notes.
- Public records.
- Company-context paths, if configured.
- Prior debriefs or lessons, if configured.

### Domain Wiki Pages

List relevant `knowledge/` pages:

- `[[...]]`

### Existing Pursuit Entities

List required and optional entity inputs:

```yaml
required:
  -
optional:
  -
```

## Entity Changes

### Entity Types Created

```yaml
created:
  - type:
    path:
    owner:
    required_fields:
    relationship_vocabulary:
```

### Entity Types Updated

```yaml
updated:
  - type:
    path:
    update_rules:
    conflict_rules:
```

### Claims And Sources

- [ ] The skill creates `claims/` entities for assertable claims it relies on.
- [ ] The skill creates or updates `source-register/` entities.
- [ ] Every claim links to at least one source.
- [ ] Confidence reflects the weakest meaningful claim/source dependency.

## Metadata Obligations

Every entity page must include:

```yaml
id:
type:
title:
tags:
status:
sensitivity:
source:
confidence:
provenance:
last_verified:
next_review_due:
updated:
```

Additional obligations:

- [ ] High-risk outputs use `approval: pending` where appropriate.
- [ ] Company-context-derived entities use the correct sensitivity.
- [ ] Unknowns are recorded as gaps, not filled with guesses.
- [ ] Low-confidence assumptions stay marked low until better evidence is supplied.

## Sensitivity And Governance

- [ ] The skill checks `sensitivity` before loading entity content into context.
- [ ] The skill does not place classified material in the pursuit wiki or model context.
- [ ] CUI, export-controlled, and source-selection-sensitive material is handled only according to the pursuit schema and organizational policy.
- [ ] Competitor-proprietary material is quarantined and not used.
- [ ] The skill cites private company-context by path and does not copy private content unnecessarily.

## View Contract

List rendered views:

```yaml
views:
  - view:
    source_entities:
      required:
      optional:
    required_sections:
    header_requirements:
    confidence_propagation:
    approval_propagation:
    staleness_rule:
```

If the view is new, add or update [view-contract-index.md](view-contract-index.md).

## Workflow Sketch

```text
<Skill Name>:
- [ ] Step 1: Open pursuit wiki and read required context
- [ ] Step 2: Complete intake; record unknowns as gaps
- [ ] Step 3: Create or update entities
- [ ] Step 4: Build claims and source-register support
- [ ] Step 5: Render owned views
- [ ] Step 6: Validate entity structure, links, metadata, and rendered view fidelity
```

## Validation Plan

- [ ] Run `scripts/validate_vault.py` against affected wiki paths.
- [ ] Run `scripts/freshness_audit.py` if time-sensitive pages are created or updated.
- [ ] Confirm view headers follow `conventions/views.md`.
- [ ] Confirm rendered views do not introduce facts absent from entities.
- [ ] Confirm pending approvals are surfaced.

## Evaluation Scenarios

Each new skill should ship at least three scenarios under
`evaluations/<skill-name>.md`.

```markdown
## Eval 1 — <short name>

**Scenario:** <representative user request>

**Inputs:** <files or context>

**Expected behavior:**
- Creates/updates the right entities.
- Links entities correctly.
- Tags entities correctly.
- Renders the expected view.

**Anti-behavior:**
- <things the skill must not do>
```

Evaluation coverage requirements:

- [ ] At least one happy-path scenario.
- [ ] At least one missing/low-confidence evidence scenario.
- [ ] At least one guardrail or anti-behavior scenario.
- [ ] Synthetic fixtures only.

## Validator Implications

```yaml
new_entity_types:
new_required_fields:
new_allowed_values:
new_time_sensitive_folders:
new_view_header_requirements:
validator_change_needed: yes | no
freshness_audit_change_needed: yes | no
```

Do not add validator changes casually. If a convention is judgment-heavy, keep
it as human review or skill behavior.

## Documentation Updates

- [ ] Update `docs/lifecycle-taxonomy.md` if the canonical job changes.
- [ ] Update `conventions/views.md` or the view contract index if a new view is introduced.
- [ ] Update `CONTRIBUTING.md` only if contributor workflow changes.
- [ ] Update examples only with synthetic material.

## Acceptance Criteria

- [ ] The skill is graph-native.
- [ ] The skill has clear upstream and downstream relationships.
- [ ] The skill creates or updates well-formed entities.
- [ ] The skill renders views from entities, not the other way around.
- [ ] The skill includes at least three evaluation scenarios.
- [ ] The skill respects sensitivity, source, confidence, provenance, and approval conventions.
- [ ] The proposal identifies whether validator or freshness-audit changes are needed.
