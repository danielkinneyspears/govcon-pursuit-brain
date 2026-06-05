# Validator Coverage Map

This map shows which documented wiki and pursuit conventions are enforced by
scripts, which are documented-only, and which are intentionally handled through
skill behavior or human review.

The validators are part of the trust layer, but they are not the whole trust
layer. Some conventions are objective and script-checkable; others require
professional judgment, organizational policy, or a skill's context-aware
behavior.

## Current Baseline

Validator run:

```text
python3 scripts/validate_vault.py knowledge examples/syn-2026-r-0001
```

Observed result on 2026-05-22:

```text
validated 104 files across ['knowledge', 'examples/syn-2026-r-0001']
OK — no errors
```

Freshness audit run:

```text
python3 scripts/freshness_audit.py knowledge examples/syn-2026-r-0001 --as-of 2026-05-22
```

Observed result:

```text
audited 101 pages as of 2026-05-22
OK — no freshness issues
```

## Coverage Map

| Convention / requirement | Source | Enforcement status | Enforced by | Notes |
|---|---|---|---|---|
| Entity pages carry YAML frontmatter | `conventions/entity-pages.md` | Enforced | `validate_vault.py` | Entity pages missing frontmatter fail validation. |
| Required entity fields are present | `conventions/entity-pages.md` | Enforced | `validate_vault.py` | Required fields include `id`, `type`, `title`, `tags`, `status`, `sensitivity`, `source`, `confidence`, `provenance`, `last_verified`, `next_review_due`, and `updated`. |
| `tags` field is present and non-empty | `conventions/entity-pages.md` | Enforced | `validate_vault.py` | Handles list-style tags and scalar tags. |
| `status` uses allowed values | `conventions/tagging.md` | Enforced | `validate_vault.py` | Allowed values: `draft`, `active`, `stable`, `verified`, `superseded`. |
| `sensitivity` uses allowed values | `conventions/tagging.md` | Enforced | `validate_vault.py` | Allowed values include `public`, `company-proprietary`, `cui`, `export-controlled`, `classified`, `source-selection-sensitive`, and `competitor-proprietary`. |
| `confidence` uses allowed values | `conventions/tagging.md` | Enforced | `validate_vault.py` | Allowed values: `high`, `medium`, `low`. |
| Domain wiki pages are public | `knowledge/_schema.md`, `conventions/tagging.md` | Enforced as warning | `validate_vault.py` | Non-public sensitivity under `knowledge/` is warned. |
| Date fields parse as ISO dates | `conventions/tagging.md` | Enforced | `validate_vault.py` | Applies to `last_verified`, `next_review_due`, and `updated`. |
| Frontmatter `id` matches filename stem | `conventions/entity-pages.md` | Enforced | `validate_vault.py` | Prevents broken stable IDs. |
| Short wiki links resolve to known entity IDs | `conventions/entity-pages.md` | Enforced | `validate_vault.py` | Checks `[[id]]` and `[[id\|display]]` style links. |
| Time-sensitive folders carry freshness fields | `conventions/tagging.md` | Enforced | `freshness_audit.py` | Applies to configured time-sensitive folders. |
| `next_review_due` is not overdue | `conventions/tagging.md` | Enforced | `freshness_audit.py` | Uses today's date or supplied `--as-of`. |
| Raw source files are not treated as entity pages | `docs/architecture.md` | Enforced by exemption | `validate_vault.py` | `sources/` is excluded from entity-frontmatter validation. |
| Rendered views are not treated as entity pages | `conventions/views.md` | Enforced by exemption | `validate_vault.py` | `views/` is excluded from entity-frontmatter validation. |
| Skill references and templates are not entity pages | Claude Skills package structure | Enforced by exemption | `validate_vault.py` | `references/`, `templates/`, and `SKILL.md` are exempt from entity-frontmatter validation. |
| View header includes renderer/date/source-of-truth/confidence/approval lines | `conventions/views.md` | Documented-only | None today | Candidate for future view-specific validation after view contracts are documented. |
| Views are stale when older than source entities | `conventions/views.md` | Documented-only | None today | Requires view-to-source mapping before automation. |
| Lowest confidence propagates into view header | `conventions/views.md`, `conventions/tagging.md` | Documented-only | Skill behavior / human review | Could be checked once view contracts define source entities. |
| `approval: pending` count propagates into view header | `conventions/views.md`, `conventions/tagging.md` | Documented-only | Skill behavior / human review | Approval is optional and high-risk-output specific. |
| Skills check `sensitivity` before loading entities into context | `conventions/tagging.md` | Documented-only | Skill behavior | Needs proof-skill audit before automation or instruction changes. |
| `classified` material is not placed in model context | `conventions/tagging.md` | Human / organizational control | Human review and policy | Script checks can flag metadata but cannot prove model-context handling. |
| `competitor-proprietary` information is quarantined | `conventions/tagging.md`, `skills/analyzing-competitors` | Skill behavior / human review | Skill instructions | Current validator checks enum value, not quarantine behavior. |
| Entity summaries synthesize rather than paste raw source text | `conventions/entity-pages.md` | Human review | Human review | Not a good candidate for simple script validation. |
| One concept per page | `conventions/entity-pages.md` | Human review | Human review | Concept boundaries require judgment. |
| Typed relationships in `## Links` carry meaningful relationship names | `conventions/entity-pages.md` | Documented-only | Human review | Could be partially linted later, but relationship quality is judgment-heavy. |
| Reciprocal links are added where reverse relationship matters | `conventions/entity-pages.md` | Documented-only | Human review | Reverse relationship necessity is contextual. |
| Obsidian callouts are used sparingly | `conventions/entity-pages.md` | Human review | Human review | Judgment-heavy; not a validator priority. |

## Classification

### Enforced

Objective and structurally checkable conventions:

- Required frontmatter presence.
- Required field presence.
- Allowed enum values.
- ISO date parsing.
- Entity ID / filename agreement.
- Short wiki-link resolution.
- Freshness due dates.

### Documented-Only

Conventions that are specific enough to document but require more context before
automation:

- View header shape.
- View staleness.
- Confidence and approval propagation into views.
- Sensitivity checks before loading or rendering.
- Quarantine behavior.
- Relationship vocabulary.

### Human Review / Intentionally Manual

Conventions that depend on professional judgment:

- Whether a page is truly one concept.
- Whether a summary is a good synthesis.
- Whether a relationship link is meaningful.
- Whether sensitive material is permitted under organizational policy.
- Whether a high-risk output is ready for human approval.

## Why This Boundary Matters

The current validators enforce the core structural trust layer. Adding new
checks before documenting the boundary could create brittle automation around
conventions that are intentionally judgment-based.

Use this map to decide whether a future convention belongs in:

- documentation,
- skill instructions,
- human review,
- `validate_vault.py`,
- `freshness_audit.py`, or
- a future view-specific validator.
