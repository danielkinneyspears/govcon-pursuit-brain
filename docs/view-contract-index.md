# View Contract Index

This index describes each rendered view's source entities, required metadata
propagation, expected sections, and validation checks.

Views are read-outs from the pursuit entity graph. They are not sources of
truth. To change what a view says, update the entities and re-render the view.

## View Contract Principles

- Entity pages are the source of truth.
- Views are rendered read-outs and should not be hand-edited.
- A skill reads entities, renders owned views, and notes stale downstream views.
- Every view header surfaces rendering metadata, lowest source confidence, and
  pending approvals.
- A view contract makes source dependencies and readiness checks explicit.

## Standard View Header Contract

Every view should open with:

```markdown
# <View title> — <Opportunity name>

- View rendered by: <skill-name>
- Rendered: <date>
- Source of truth: the pursuit entity graph (this document is a rendered view —
  do not hand-edit; change the entities and re-render)
- Lowest confidence among source entities: <high | medium | low>
- Entities awaiting approval: <count, or "none">
```

## Implemented View Contracts

### `bid-decision.md`

```yaml
view: bid-decision.md
status: implemented-in-example
owning_skill: qualifying-opportunities
source_entities:
  required:
    - decisions/bid-decision
    - customer/
  conditional:
    - competitors/
    - claims/
    - source-register/
rendered_sections_observed:
  - Recommendation
  - Headline
  - Decision drivers
  - Evidence
  - What needs to happen next
header_requirements:
  - view rendered by
  - rendered date
  - source of truth warning
  - lowest confidence among source entities
  - entities awaiting approval
metadata_propagation:
  lowest_confidence: lowest confidence among decision/customer/competitor/claim/source entities used by the view
  approval: pending decision approval must be surfaced in the header
validation_checks:
  - The recommendation in the view matches decisions/bid-decision.
  - Conditional-bid conditions match decisions/bid-decision.
  - pWin and scorecard summary match decisions/bid-decision.
  - Evidence links resolve to claim and source-register entities.
  - The view does not introduce unsupported facts absent from source entities.
  - The rendered date is not older than any source entity update date without staleness being noted.
example_evidence:
  - examples/syn-2026-r-0001/views/bid-decision.md
  - examples/syn-2026-r-0001/entities/decisions/bid-decision.md
  - examples/syn-2026-r-0001/entities/claims/acme-is-incumbent.md
  - examples/syn-2026-r-0001/entities/source-register/sam-gov-syn-2026.md
```

## Planned View Contract Stubs

These views are listed in `conventions/views.md`, but they should not be treated
as fully implemented contracts until examples or owning skills define their
exact sections.

| View | Owning skill | Source entities from current convention | Contract status |
|---|---|---|---|
| `opportunity-profile.md` | `qualifying-opportunities` | opportunity, `customer/` | planned; likely pairs with `bid-decision.md` in first-run pursuit bootstrap |
| `capture-plan.md` | `planning-capture` | `customer/`, `competitors/`, `contacts/`, `themes/`, `risks/` | planned |
| `competitive-assessment.md` | `analyzing-competitors` | `competitors/`, `discriminators/` | planned; proof skill exists, but no example view is present in the current synthetic pursuit |
| `price-to-win.md` | `estimating-price-to-win` | pricing `decisions/`, `competitors/` | planned |
| `win-strategy.md` | `developing-win-strategy` | `themes/`, `discriminators/`, `hot-buttons/` | planned |
| `compliance-matrix.md` | `shredding-solicitations` | `requirements/`, `sections/`, `themes/` | planned |
| `proposal-outline.md` | `outlining-proposals` | `sections/`, `requirements/`, `themes/` | planned |
| `executive-summary.md` | `writing-executive-summaries` | `themes/`, `hot-buttons/`, `customer/` | planned |

## Future View Contract Fields

Each new view contract should include:

```yaml
view:
status: implemented | planned
owning_skill:
source_entities:
  required:
  conditional:
rendered_sections:
header_requirements:
metadata_propagation:
  lowest_confidence:
  approval:
staleness_rule:
validation_checks:
example_evidence:
```

## Validation Boundary

This document does not add validator behavior. It makes the contract visible so
a later change can decide whether view-specific checks are worth automating.

Good candidates for later automation:

- Required view header lines.
- Rendered date format.
- View source-of-truth warning.
- Resolvable wiki links inside views.

Poor candidates for simple automation:

- Whether a view faithfully summarizes source entities.
- Whether the lowest confidence was correctly chosen without a formal
  source-entity manifest.
- Whether pending approvals should block final use.
- Whether the rendered sections are persuasive or complete.
