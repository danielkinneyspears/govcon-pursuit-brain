# Convention — Entity Pages

Every page in the domain wiki and every page in a pursuit wiki is an **entity
page**. This document defines the format. Skills must follow it exactly;
consistency is what makes the graph traversable.

The pages are also designed to open as an **Obsidian vault**. The
`[[wiki-link]]` syntax, the YAML frontmatter, the tag conventions, the folder
organization, and the callouts all match Obsidian defaults so the same files
work as both a Claude-facing knowledge base and a human-facing vault. Point
Obsidian at `knowledge/` (or at a `pursuits/<id>/` directory) and it opens
correctly.

## Contents
- One concept per page
- File location, folders, and entity IDs
- Frontmatter
- Tags
- Body structure
- Wiki links
- The Links section
- Obsidian callouts
- Keeping pages small

## One concept per page

An entity page describes exactly one entity: one competitor, one requirement,
one win theme, one stakeholder, one concept. If a page is describing two things,
it is two pages. Single-concept pages are what let a skill load precisely what
it needs and what let links mean something specific.

## File location, folders, and entity IDs

A pursuit entity lives at `entities/<type>/<id>.md`. A domain entity lives in
`knowledge/<category>/<id>.md` — the domain wiki is organized into category
folders (see `knowledge/_schema.md` for the current set: `acquisition-regulations/`,
`solicitation-structure/`, `source-selection/`, `small-business/`, `vehicles/`,
`security-and-compliance/`, `ai-and-emerging/`, `protests-and-debriefs/`,
`capture-and-bd/`, `proposal-craft/`, etc.).

The `<id>` is kebab-case, stable, and unique across the whole vault — once
assigned, it does not change, because other pages link to it.

The canonical reference to a pursuit entity is `<type>/<id>` — for example
`competitors/acme-corp`, `requirements/m-2-03`, `themes/zero-transition-risk`.
Domain-wiki entities are referenced by `<id>` alone — for example `[[section-m]]`,
`[[lpta]]`, `[[cmmc]]`. Because IDs are vault-unique, Obsidian resolves the
short form regardless of folder.

Requirement IDs reuse the solicitation-derived scheme from the shred
(`l-3-2-01`, `m-2-03`, `pws-4-1-02`) lowercased — see the
`shredding-solicitations` skill.

## Frontmatter

Every entity page opens with YAML frontmatter. The fields:

```yaml
---
id: acme-corp
type: competitor
title: Acme Corporation
tags:
  - competitor
  - capture-phase
status: draft            # draft | active | verified | superseded
sensitivity: public      # see conventions/tagging.md
source: <where this knowledge came from>
confidence: medium       # high | medium | low — see conventions/tagging.md
provenance: analyzing-competitors / 2026-05-19
updated: 2026-05-19
---
```

`id`, `type`, and `title` identify the entity. `status` tracks maturity.
`sensitivity`, `source`, `confidence`, and `provenance` are the load-bearing
metadata defined in [tagging.md](tagging.md) — they are never omitted.
Pursuit-specific entity types may add fields (a `requirement` page adds
`mandatory`; see the relevant skill), but the fields above are always present.

## Tags

The `tags:` list in frontmatter is Obsidian-native (Obsidian indexes it
automatically) and lets humans and skills filter the vault by topic. Use it
generously but consistently.

Tag conventions:

- **Lowercase, hyphenated**, no spaces.
- **Topic tag (required)** — the page's primary domain area: `source-selection`,
  `solicitation-structure`, `small-business`, `vehicles`,
  `security-and-compliance`, `ai-and-emerging`, `protests-and-debriefs`,
  `cost-and-pricing`, `capture-and-bd`, `proposal-craft`,
  `acquisition-regulations`, `past-performance`, `task-orders`,
  `special-clauses`, `integrity-and-ethics`, `thresholds-and-publicizing`.
- **Regulation tag (when applicable)** — the controlling authority:
  `far-part-15`, `far-part-19`, `far-part-16`, `dfars`, `sba-13-cfr`,
  `nist-800-171`, `omb-memo`, `cmmc`, `fedramp`, `itar-ear`.
- **Lifecycle phase tag (when applicable)** — `capture-phase`, `proposal-phase`,
  `review-phase`, `post-submission`.
- **Specificity tags** as needed: `set-aside`, `color-team`, `compliance-matrix`,
  `win-theme`, `cui`, `protest`.

Keep tag counts modest — typically three to five per page. Tags do not replace
links: a `[[wiki-link]]` records a *relationship*, a tag records a *category*.

## Body structure

After the frontmatter:

```markdown
# <Title>

<A short synthesized summary — two to five sentences. What this entity is, and
the one thing a reader most needs to know about it. Synthesized from the
sources, not pasted from them.>

## <Type-specific sections>

<Each entity type has a small, consistent set of sections — a competitor page
has an assessed offer; a requirement page has the requirement text and its
compliance status; a theme page has the benefit and the proof. The skill that
owns the entity type defines these sections.>

## Links

<Typed links to related entities — see below.>
```

The summary is compiled knowledge: a skill reads the raw sources and *writes the
synthesis*, it does not quote the sources at length. Raw text stays in
`sources/`.

## Wiki links

A link to another entity is written `[[type/id]]`, or `[[type/id|display text]]`
when the display text should differ. Domain-wiki links are `[[id]]`.

Examples: `[[competitors/acme-corp]]`, `[[requirements/m-2-03]]`,
`[[hot-buttons/transition-risk|the customer's transition-risk concern]]`,
`[[lpta]]`.

Links are a convention, not a feature Claude resolves automatically. A skill
traverses the graph by following `[[ ]]` references and by grepping for them —
to find everything that links *to* an entity (its backlinks), grep the pursuit
for `[[type/id]]`.

## The Links section

Every entity page ends with a `## Links` section listing its relationships to
other entities. Each link is **typed** — the relationship is named — so the edge
carries meaning:

```markdown
## Links

- serves [[hot-buttons/transition-risk]]
- rests on [[discriminators/cleared-bench]]
- scored under [[requirements/m-2]]
- proven by [[past-performance/dla-network-ops]]
- threaded in [[sections/3-2-transition-approach]]
- contrasts with [[competitors/acme-corp]]
```

Use a consistent relationship vocabulary within a type (the owning skill defines
it). When entity A links to entity B and the reverse relationship also matters,
add the reciprocal link on B — but do not over-link; a link should mean
something a skill or a reader would actually traverse.

## Obsidian callouts

Pages may use Obsidian callouts (GitHub-flavored Markdown extension) to mark
content that should not blend into normal prose. Used sparingly, they make a
critical caveat or example visible at a glance.

```markdown
> [!warning] Regulatory currency
> Verify against the current FAR text and the actual solicitation before
> relying on this page for a deadline-sensitive task.

> [!note]
> Context the skill or reader needs.

> [!tip]
> Practical guidance.

> [!example]
> A worked example, not normative.
```

Reserve `> [!warning]` for genuine "do not get this wrong" content —
regulatory currency, procurement-integrity limits, sensitivity rules, hard
deadlines. Overusing it dilutes the signal.

## Keeping pages small

An entity page is short by design — a synthesized summary, a few type-specific
sections, and its links. If a page is growing long, it is probably trying to be
several entities, or it is pasting raw source text. Split it, or move the raw
text back to `sources/`. Small, well-linked pages are the whole point.
