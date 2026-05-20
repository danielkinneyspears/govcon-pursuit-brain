# Convention — Tagging

Every entity page carries metadata tags in its frontmatter. The tags are
load-bearing: they are how the package handles sensitivity, provenance,
confidence, and human approval without separate machinery. A skill never writes
an untagged entity page.

## Contents
- sensitivity
- source
- confidence
- provenance
- status
- last_verified and next_review_due
- approval
- Why the tags matter

## sensitivity

The classification of the information on the page. It determines whether and how
the page may be handled.

| Value | Meaning |
|---|---|
| `public` | Publicly available information. |
| `company-proprietary` | The offeror's own proprietary or business-confidential information. |
| `cui` | Controlled Unclassified Information — requires safeguarding per the applicable agency rules. |
| `export-controlled` | Subject to export-control regimes. |
| `classified` | National-security classified information. |
| `source-selection-sensitive` | Non-public information about a federal evaluation or competing proposals. |
| `competitor-proprietary` | A competitor's proprietary information. |

**The handling rule.** Before a skill pulls an entity page into model context or
into a view, it checks `sensitivity`. `classified` material must not be placed
in a pursuit wiki or model context. `cui`, `export-controlled`, and
`source-selection-sensitive` material may be handled only where the
organization's policy and the applicable safeguarding rules permit, and the
pursuit schema (`pursuit.md`) records whether they do. `competitor-proprietary`
information is quarantined, not used (see `analyzing-competitors`). When in
doubt, a skill flags the page and asks rather than proceeding.

A page's `sensitivity` is the highest classification of anything on it. A
synthesized summary that would reveal CUI is itself CUI.

## source

Where the page's knowledge came from — a citation, not a vague label. For a
domain-wiki page: the FAR section or authority. For a pursuit page: the
solicitation section, the customer meeting, the public record, the teammate data
call. `source` is what makes a claim checkable. A page whose `source` is "the
model's general knowledge" is a page to verify before relying on.

## confidence

How much to trust the page's content: `high`, `medium`, or `low`.

- `high` — verified against a primary source.
- `medium` — a reasonable inference from real evidence.
- `low` — an assumption, an unconfirmed report, or a gap filled provisionally.

A skill carries `confidence` into its reasoning and into views: a win strategy
that rests on a `low`-confidence competitor assessment says so. Confidence is
raised by getting better sources, never by editing the field.

## provenance

The audit trail: which skill or build last created or updated the page, and
when, written `<skill-name-or-build-id> / <date>`. When several skills touch a
page over a pursuit, **append** rather than overwrite, so the page's history is
visible. `provenance` is how an adopter answers "where did this come from and
what produced it."

Examples:

- `provenance: domain-wiki-build-v0.2.0 / 2026-05-19` — a compiled domain-wiki
  page from the v0.2.0 build.
- `provenance: analyzing-competitors / 2026-05-19` — a pursuit page created
  by the analyzing-competitors skill on that date.
- `provenance: analyzing-competitors / 2026-05-19; developing-win-strategy / 2026-05-22`
  — multiple skills touched the page.

`provenance` is required on every entity page (domain and pursuit).

## status

The maturity of the entity:

| Value | Meaning |
|---|---|
| `draft` | Created, not yet reviewed. |
| `active` | In use during a live pursuit; not yet verified. |
| `stable` | **Domain-wiki convention.** Compiled from authoritative public sources, internally consistent, and suitable as orienting reference. **Not yet human-verified or source-confirmed against the current FAR/CFR/agency text.** Most domain-wiki pages in v0.2.x carry this status. |
| `verified` | Human-confirmed against the primary source or by a qualified reviewer. The target state for any page used in a high-stakes pursuit. |
| `superseded` | Kept for history; no longer current. |

> [!warning] `stable` is not `verified`
> A `stable` page is a reasonable starting point. Before relying on it for a
> deadline-sensitive or high-stakes decision, **verify it against the primary
> source** (FAR, CFR, agency program page, OMB memo, NIST publication) and
> upgrade the page to `verified` — recording the verifier and date in
> `provenance` and updating `last_verified`.

## last_verified and next_review_due

Two date fields that drive **freshness control**, distinct from `updated`
(which records any change to the page).

- **`last_verified`** — the date the page was last checked against its primary
  source. For new compiled pages, this is the build date.
- **`next_review_due`** — the date by which the page should be re-verified.
  Default cadence is **90 days** for time-sensitive content (vehicles,
  thresholds, regulatory currency, OMB memos, security and compliance) and
  **365 days** for durable structural content (FAR Part overviews, UCF
  sections, definitional concepts).

The `scripts/freshness-audit` validator flags pages where `next_review_due` is
in the past, or where time-sensitive content lacks the fields entirely.

## approval

Optional, for high-risk entities and the views built from them. A bid decision,
a price-to-win target, a final win strategy, a submitted response — these carry
`approval: pending` until a named human approves, then `approval: <name> / <date>`.
A view is not "final" while any entity it renders from is `approval: pending`.
This is the human-in-the-loop gate; skills surface what is awaiting approval
rather than presenting unapproved high-risk output as settled.

## Why the tags matter

A federal pursuit handled by an AI raises immediate questions from any serious
adopter: where did this come from, can it be trusted, is it safe to process, and
did a human sign off. In a flat-document package those are bolted-on features.
Here they are five frontmatter fields that every page already carries — so
provenance, sensitivity control, confidence propagation, and approval gating are
properties of the architecture, not extra skills.
