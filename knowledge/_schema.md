# Domain Wiki Schema

This is the Layer 3 schema for the **domain wiki** — the static, compiled
federal-acquisition knowledge in `knowledge/`. Every skill reads the relevant
domain-wiki pages; this schema tells the skill what the wiki is and how to use
it.

The directory is also an **Obsidian vault**. Open `knowledge/` directly in
Obsidian and the wiki links, tags, frontmatter, callouts, and folders all
work natively. Skills read the same files programmatically.

## Scope

The domain wiki holds durable federal-acquisition knowledge: solicitation
structure and the FAR, source selection, small-business set-asides, contract
vehicles, cost and pricing, past performance, security and compliance,
AI-in-procurement guidance, protests and debriefs, capture and proposal craft.
It is the compiled, navigable replacement for a flat federal-proposal primer.

It does **not** hold anything pursuit-specific. A particular customer, a
particular competitor, a particular requirement — those are pursuit-wiki
entities, never domain-wiki pages.

## Folder organization

Pages are grouped by category folder. The current categories:

```
knowledge/
  _schema.md
  _index.md                        ← Map of Content
  acquisition-regulations/         ← FAR parts and how the FAR is structured
  solicitation-structure/          ← UCF, Sections A–M, SOW/PWS/SOO, CDRL, QASP, CLIN
  source-selection/                ← FAR 15.3, evaluation factors, ratings, discussions
  task-orders/                     ← FAR 16.505 fair opportunity, task-order protests
  contract-types/                  ← FFP, T&M, cost-reimbursement, IDIQ, BPA
  vehicles/                        ← GSA MAS, OASIS+, Polaris, Alliant 3, SEWP, NITAAC
  small-business/                  ← SBA set-asides, size standards, M-P, JVs, NMR
  past-performance/                ← CPARS, recency-relevancy-quality
  cost-and-pricing/                ← cost realism, price reasonableness, TINA, BOE
  capture-and-bd/                  ← bid/no-bid, capture plan, pWin, Black Hat, PTW, themes
  proposal-craft/                  ← compliance matrix, storyboarding, color teams
  special-clauses/                 ← key personnel, options, OCI, data rights, flow-downs
  integrity-and-ethics/            ← Procurement Integrity Act, FAR 3.104
  protests-and-debriefs/           ← debrief, GAO, COFC, agency protest
  security-and-compliance/         ← CUI, CMMC, FedRAMP, NIST 800-171, ITAR/EAR
  ai-and-emerging/                 ← OMB M-25-21, M-25-22, NIST AI RMF
  thresholds-and-publicizing/      ← SAT, MPT, FAR 5.203 synopsis, SAM.gov
```

Pages are identified by their `<id>` (kebab-case, unique across the vault), so
links use the short form `[[id]]` regardless of folder. See
[../conventions/entity-pages.md](../conventions/entity-pages.md).

## Entity types

Domain-wiki pages are all `type: concept`. Each is one federal-acquisition
concept, following the entity-page convention. Domain entities are referenced
by `[[id]]` (no type prefix).

## Tagging

Every page carries `tags:` in its frontmatter. The first tag is the page's
**category** (matching the folder name, e.g., `solicitation-structure`).
Additional tags identify the regulation (`far-part-15`, `sba-13-cfr`,
`nist-800-171`), the lifecycle phase (`capture-phase`, `proposal-phase`), and
any specificity (`set-aside`, `color-team`, `cui`). See
[../conventions/entity-pages.md](../conventions/entity-pages.md) for the tag
conventions.

## Conventions

- One concept per page; pages are short and heavily interlinked.
- Every page carries the standard tags (`sensitivity: public` for all
  domain-wiki pages, plus `source`, `confidence`, `status`, plus the topical
  `tags:` list).
- `source` cites the governing authority — a FAR section, a CFR section, an
  agency rule, an OMB memo, a NIST publication, or a clearly described common
  practice.
- No time-sensitive phrasing. If practice changes, a page gets a dated
  "superseded practice" callout rather than a bare "as of" date.
- Use `> [!warning]` callouts for regulatory-currency notes and other "do not
  get this wrong" content.

## The precedence rule

> [!warning] Authority precedence
> The domain wiki is orienting background, not authority. When it conflicts
> with a higher source, the higher source wins, in this order:
>
> 1. The specific solicitation (Section L governs the proposal).
> 2. The current FAR and the applicable agency supplement.
> 3. This domain wiki.

For any deadline-sensitive or legally adjacent question — debrief windows,
late-proposal rules, size standards, protest timelines, certifications —
verify the current FAR and agency supplement and the actual solicitation
before relying on a domain-wiki page. Domain-wiki pages describe durable
structure; specifics change.

## Index

[`_index.md`](_index.md) is the Map of Content for the vault. It is updated
whenever a page is added.
