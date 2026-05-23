# Convention — Views

A **view** is a human-facing document rendered from the pursuit's entity graph.
Views are how this package delivers the familiar federal proposal artifacts — a
bid decision, a capture plan, a compliance matrix, a win strategy — without
making any of them the source of truth.

## Contents
- The rule: the graph is the source of truth
- Where views live
- The view catalog
- Rendering a view
- The view header
- Regeneration and staleness
- Views and approval

## The rule: the graph is the source of truth

The entity pages are authoritative. A view is a read-out of them at a moment in
time. This means:

- A skill never edits a view by hand to change its content. To change what a
  view says, change the entities, then re-render.
- A skill never reads a view to learn a fact. It reads the entities.
- If a view and the entities disagree, the entities are right and the view is
  stale.

A hand-edited view silently diverges from the graph and corrupts the one
guarantee the architecture offers. Do not do it.

## Where views live

Views live in a pursuit's `views/` directory:

```
pursuits/<id>/views/
```

Each view is a Markdown file named for what it is (`compliance-matrix.md`,
`win-strategy.md`).

## The view catalog

The package's views correspond one-to-one with the numbered artifacts of the
sibling package `federal-proposal-skills`, so the two packages produce the same
deliverables:

| View | Rendered from | Owning skill |
|---|---|---|
| `opportunity-profile.md` | the opportunity, `customer/` | qualifying-opportunities |
| `bid-decision.md` | `decisions/`, scoring entities | qualifying-opportunities |
| `capture-plan.md` | `customer/`, `competitors/`, `contacts/`, `themes/`, `risks/` | planning-capture |
| `competitive-assessment.md` | `competitors/`, `discriminators/` | analyzing-competitors |
| `price-to-win.md` | pricing `decisions/`, `competitors/` | estimating-price-to-win |
| `win-strategy.md` | `themes/`, `discriminators/`, `hot-buttons/` | developing-win-strategy |
| `compliance-matrix.md` | `requirements/`, `sections/`, `themes/` | shredding-solicitations |
| `proposal-outline.md` | `sections/`, `requirements/`, `themes/` | outlining-proposals |
| `executive-summary.md` | `themes/`, `hot-buttons/`, `customer/` | writing-executive-summaries |
| ... | ... | ... |

A skill owns the views it renders and re-renders them whenever the entities
behind them change.
For the current view contract index, including the example-backed
`bid-decision.md` contract and planned view stubs, see
[../docs/view-contract-index.md](../docs/view-contract-index.md).

## Rendering a view

To render a view, a skill:

1. Identifies the entities the view draws from (the table above, and the
   skill's own definition).
2. Reads their current state from the graph.
3. Composes the view document — applying the same federal proposal standards the
   sibling package applies (a compliance matrix still cross-walks L/M/C; a win
   strategy view still maps themes to Section M factors).
4. Writes it to `views/`, with the header below.

A view may be a table (the compliance matrix is a table over `requirements/`
pages), a narrative (the executive summary), or a structured report (the bid
decision). The form follows the artifact.

## The view header

Every view opens with a header that marks it as rendered and dates it against
the graph:

```markdown
# <View title> — <Opportunity name>

- View rendered by: <skill-name>
- Rendered: <date>
- Source of truth: the pursuit entity graph (this document is a rendered view —
  do not hand-edit; change the entities and re-render)
- Lowest confidence among source entities: <high | medium | low>
- Entities awaiting approval: <count, or "none">
```

The last two lines propagate the tagging: a view inherits the lowest
`confidence` and surfaces any `approval: pending` from the entities it renders.

## Regeneration and staleness

When an entity changes, every view that renders from it is stale until
re-rendered. A skill that updates entities re-renders the views it owns and
notes which other views are now stale so they can be regenerated. A view's
`Rendered` date older than the entities it draws from is the staleness signal.

## Views and approval

Because a view surfaces `approval: pending` from its entities, a view built from
unapproved high-risk entities is visibly not final. A bid-decision view whose
underlying `decisions/` entity is `approval: pending` shows that in its header.
The view is honest about its own readiness.
