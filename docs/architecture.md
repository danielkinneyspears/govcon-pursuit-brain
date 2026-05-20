# Architecture: The Pursuit Brain

This package treats a federal pursuit as a knowledge graph that compounds,
not a stack of documents. This document explains the model. Every skill in
the package assumes it; read it before reading any skill.

## Contents
- Two abstraction layers: elemental and GovCon method
- The problem with flat artifacts
- The LLM Wiki pattern
- Layer 1: raw sources
- Layer 2: the two wikis
- Layer 3: the schemas
- The pursuit wiki entity model
- Views: artifacts rendered from the graph
- The skill's job: read, maintain, render
- Why the graph compounds
- Lite mode
- Relationship to federal-proposal-skills

## Two abstraction layers: elemental and GovCon method

Before the three layers of the LLM Wiki pattern, the package speaks at two
abstraction layers:

```
Elemental layer:        Plan / Create / Iterate
                        Canonical jobs (universal)
                        Aliases (common names per shop)
                        Desired outcomes

GovCon method layer:    Shipley-style lifecycle
                        Color teams (Blue/Pink/Green/Red/Gold/White Glove)
                        Section L / M / C, FAR, source selection
                        Proposal artifacts
```

The elemental layer answers "what job is being done?" in universal terms:
`competitive-intelligence`, `compliance-tracing`,
`evaluator-perspective-review`. The GovCon method layer answers "how do we
do that job well in federal acquisition?" with Shipley terminology, color
teams, and FAR / source-selection vocabulary.

A user who searches "Green Team," "pricing review," or "cost realism check"
should land in the same conceptual area. Skills carry `canonical_job:`,
`phase:`, and `common_names:` in their frontmatter to make that work. The
full translation table lives in [lifecycle-taxonomy.md](lifecycle-taxonomy.md).

Both layers matter. Skip the elemental layer and the package's jargon
excludes anyone who calls things by a different name. Skip the GovCon
method layer and you lose the rigor that makes pursuits win against real
evaluation boards.

## The problem with flat artifacts

A federal pursuit produces a lot of documents: a bid decision, a capture
plan, a competitive assessment, a compliance matrix, an outline, section
drafts, a cost narrative, color review reports, a debrief analysis. Treat
each as a flat file and the knowledge inside them never connects. A
competitor exists as a row in the competitive assessment, a price
assumption in the price-to-win file, and a ghosting line in the win
strategy: three mentions, no link. Ask a question that crosses documents
("if this discriminator does not hold up, what breaks?") and the only
answer is to re-read everything and reconstruct the connections by hand,
every time.

Knowledge that does not connect does not compound. That is the ceiling a
flat-artifact package hits.

## The LLM Wiki pattern

This package applies the LLM Wiki pattern (described by Andrej Karpathy in
April 2026): instead of retrieving from raw documents on every query, an
LLM compiles knowledge into a maintained, interlinked wiki and then reasons
over that wiki. Knowledge accumulates and synthesizes across sources
rather than being rediscovered.

The pattern has three layers:

1. Raw sources: the unprocessed inputs.
2. The wiki: knowledge compiled into small, interlinked, single-concept pages.
3. The schema: a configuration document that tells the model what the wiki is, the conventions it follows, and how to resolve conflicts.

This package instantiates all three for federal pursuits.

## Layer 1: raw sources

The unprocessed inputs to a pursuit: the solicitation and its amendments,
the FAR and agency supplements, sources-sought notices and RFIs,
customer-meeting notes, market research, public competitor information,
teammate data-call returns, and, at the end, the government's debrief.

Raw sources for a pursuit live in that pursuit's `sources/` directory.
They are never edited; they are *read* and *compiled into* Layer 2.

## Layer 2: the two wikis

There are two wikis, with different lifespans.

### The domain wiki: `knowledge/`

Compiled, static federal-acquisition knowledge: the Uniform Contract
Format, FAR Part 15 source selection, best-value vs. LPTA, color team
reviews, what a discriminator is. One concept per page, interlinked. It is
shared across every pursuit and changes only when federal practice
changes. It is this package's compiled version of a federal proposal
primer, but as a navigable graph, so a skill loads the three concepts it
needs rather than a whole primer.

### The pursuit wiki: `pursuits/<id>/`

A living entity graph for one opportunity: the customer, the competitors,
the requirements, the win themes, the risks, each a page, all interlinked.
It is created when a pursuit begins and grows and updates through the
lifecycle. It is the Pursuit Brain.

## Layer 3: the schemas

Each wiki has a schema, the Layer 3 configuration that makes the wiki
legible and keeps it consistent.

- `knowledge/_schema.md`: the domain wiki's schema. Its scope, entity types, page conventions, and the rule that the FAR and a specific solicitation outrank the wiki.
- A pursuit's `pursuit.md`: the pursuit wiki's schema *and* its index. What this opportunity is, the pursuit posture (incumbent, challenger, teaming partner), the conventions in force, the sensitivity rules, and how to resolve conflicting information. Every skill reads `pursuit.md` first.

The per-pursuit schema is created from `schema/pursuit-schema.template.md`.

## The pursuit wiki entity model

A pursuit wiki is a directory of entity pages, grouped by type. Each page
is one entity, follows [conventions/entity-pages.md](../conventions/entity-pages.md),
and links to related entities with `[[type/id]]` wiki links.

```
pursuits/<solicitation-id>/
  pursuit.md                 ← Layer 3: schema + index for this pursuit
  sources/                   ← Layer 1: the solicitation, notes, debrief
  entities/
    customer/                ← the agency, the program office, one page per stakeholder
    competitors/             ← one page per competitor
    hot-buttons/             ← one page per customer hot button
    discriminators/          ← one page per validated discriminator
    themes/                  ← one page per win theme
    requirements/            ← one page per shredded requirement
    solution/                ← one page per solution element
    sections/                ← one page per proposal section
    risks/                   ← one page per pursuit or performance risk
    teammates/               ← one page per teaming partner
    key-personnel/           ← one page per proposed key person
    past-performance/        ← one page per past-performance reference
    contacts/                ← one page per customer engagement (contact report)
    decisions/               ← one page per gate decision or recorded trade-off
    findings/                ← one page per color team finding
    questions/               ← one page per question to the contracting officer
    claims/                  ← one page per assertable claim (with source, owner, use)
    source-register/         ← one page per external source the pursuit relies on
    relationship-map/        ← synthesized "who really decides and who trusts whom"
    incumbent-pain/          ← one page per identified customer pain with the incumbent
    capture-momentum/        ← weekly capture-momentum snapshot (real or just words?)
    decision-politics/       ← team-side and customer-side decision politics
    team-capacity/           ← the team's bandwidth and skills available for this bid
    proof-points/            ← reusable proof points (validated claim + evidence)
    pricing-reality/         ← what the team can actually bid, given internal constraints
    amendment-impact/        ← per-amendment blast-radius analysis
    review-closure/          ← per-finding closure record
  views/                     ← rendered artifacts (see below)
```

> [!note] Claim ledger and source register
> Two pursuit entity types deserve special mention. `claims/` holds each
> assertable claim the pursuit makes ("we performed this work," "the
> incumbent is vulnerable on staffing," "this is a strength under Factor 2").
> Each claim entity carries its source, the owner who can defend it, the
> assertion type (known fact, assessed, hypothesis), the proposal use, and
> a status (draft, approved, withdrawn). `source-register/` holds each
> external source the pursuit's claims rest on: SAM.gov notices, USAspending
> records, competitor press releases, job postings, agency budget signals,
> incumbent CPARS where lawfully accessible, CRM notes, customer meetings.
> Each source carries authority, directness, recency, independence, and a
> recorded date pulled. Together they make the pursuit's evidence
> traceable: every claim links to one or more sources, and every source
> links back to the claims it supports.


The entity types are the nouns of a federal pursuit. The *value* is the
edges: a `themes/` page links to the `discriminators/` page it rests on,
the `hot-buttons/` page it serves, the `requirements/` factor it is
scored under, the `past-performance/` pages that prove it, and the
`sections/` pages that thread it. Follow those links and the whole logic
of the bid is traversable.

Not every pursuit uses every entity type, and a pursuit wiki starts small.
The first skill to run creates `pursuit.md` and a handful of pages, and
later skills add the rest.

## Views: artifacts rendered from the graph

Federal proposal work still needs flat documents: a capture manager wants
a capture plan, a color team wants a compliance matrix, an executive wants
a bid decision. In this package those are *views*, documents rendered
from the entity graph, not authored directly.

```
pursuits/<id>/views/
  bid-decision.md            rendered from decisions/, the opportunity, scoring entities
  capture-plan.md            rendered from customer/, competitors/, themes/, contacts/, ...
  competitive-assessment.md  rendered from competitors/, discriminators/
  compliance-matrix.md       rendered from requirements/, sections/, themes/
  win-strategy.md            rendered from themes/, discriminators/, hot-buttons/
  ...
```

A view is generated, reviewed by humans, and regenerated when its
underlying entities change. The entity graph is the source of truth; the
view is a read-out. This is the reconciliation with the sibling package:
every numbered artifact `federal-proposal-skills` produces exists here
too, as a view.

## The skill's job: read, maintain, render

Every skill in this package does three things, in this order:

1. Read `pursuit.md`, the relevant domain-wiki pages, the relevant pursuit entities, and any new raw sources.
2. Maintain. Create and update entity pages: new entities, new links, updated tags, following the conventions. This is the skill's real work.
3. Render (or re-render) the view(s) the skill owns from the current entity graph, and tell the user what changed.

A skill never treats a view as the source of truth, never edits a view by
hand, and never lets an entity page go untagged (see
[conventions/tagging.md](../conventions/tagging.md)).

## Why the graph compounds

The payoff is reasoning that crosses the whole pursuit cheaply:

- An amendment lands. The skill updates the affected `requirements/` pages. Every `sections/`, `themes/`, and `findings/` page that links to them is one traversal away. The blast radius is visible immediately, and every dependent view re-renders. No hunt through thirty files.
- A discriminator weakens. Follow the backlinks from `discriminators/<x>` to every `themes/` page that rests on it, every `sections/` page that threads those themes, and the bid's pWin. The consequence of the weakness is a query, not an investigation.
- The debrief arrives. `analyzing-debriefs` traverses `themes/ → discriminators/ → requirements/ → findings/` to see, across the entire pursuit, what the government rewarded and what it did not, and writes lessons as `decisions/` entities that the next pursuit's bid decision can link to. Knowledge crosses pursuits.

Each skill run leaves the graph richer and more connected than it found
it. That is what "compounds" means.

## Lite mode

A three-day task order does not need a sixty-page entity graph. The
pursuit schema (`pursuit.md`) carries a `mode` field:

- `full`: the complete entity model, for major pursuits.
- `lite`: a reduced model. The customer as one page rather than a stakeholder set, requirements grouped rather than one page each, fewer entity types. Skills scale entity granularity to the `mode`.

The architecture is the same; the resolution changes. A skill checks
`mode` before deciding how finely to decompose.

## Relationship to federal-proposal-skills

`federal-proposal-skills` is the sibling package: the same lifecycle, the
same domain knowledge, the same guardrails, expressed as a flat artifact
pipeline. This package is the wiki-native expression of the same soul.
The two are launched together so their users can tell us which model
serves real pursuits better: the simple, predictable pipeline, or the
compounding graph. Skill names are intentionally shared between the
packages; a `qualifying-opportunities` exists in both, and does the same
job by a different means.
