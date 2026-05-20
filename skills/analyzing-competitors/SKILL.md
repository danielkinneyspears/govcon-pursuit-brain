---
name: analyzing-competitors
description: Produces a Black Hat competitive assessment for a US Federal opportunity as a wiki of competitor entities. Use when the user needs competitive analysis, a Black Hat review or session, competitor profiling, an incumbent assessment, or to understand the competitive field for a federal bid. Creates and enriches one competitor entity page per likely bidder (modeling each competitor's probable solution, price posture, and win themes from that competitor's point of view) records the team's exposures as risk entities, and renders the competitive-assessment view.
canonical_job: competitive-intelligence
phase: plan
common_names:
  - Black Hat
  - competitor analysis
  - market intelligence
  - market intel
  - incumbent assessment
  - competitive assessment
  - recompete analysis
---

# Analyzing Competitors

Run a Black Hat competitive assessment and record it as a living subgraph of the
pursuit wiki: one entity page per competitor, each modeling how that competitor
will bid. The core technique is perspective — bid the job *as each competitor
would*. The wiki payoff is that the assessment does not sit in one flat
document: each competitor page links to the customer hot buttons it threatens,
the team's exposures it creates, and later the win themes built to counter it.

## When to use this skill

Use this skill during capture, once a pursuit wiki exists (created by
`qualifying-opportunities`), to assess the competitive field. It enriches any
low-confidence `competitors/` stubs the bid-decision left behind, and it feeds
price-to-win and win-strategy work.

## Architecture

This skill is wiki-native. Read [docs/architecture.md](../../docs/architecture.md)
and the [conventions](../../conventions/) first. It **reads** sources and
entities, **maintains** `competitors/` and `risks/` entity pages, and **renders**
the `competitive-assessment.md` view. Relevant domain-wiki pages:
`[[discriminator]]`, `[[best-value-tradeoff]]`, `[[lpta]]`.

## Inputs

**Required:** an existing pursuit wiki. Read `pursuit.md` (note the **posture** —
it frames the whole assessment), the `customer/` entities, the
`decisions/bid-decision.md` entity, and any `competitors/` stubs.

**Private company context (recommended).** If `pursuit.md` carries a
`company_context_path:`, read these company-context folders before intake:

- `partners/`: competitors that are *also* your partners on other deals, or
  former partners, or candidate teammates here. The relationship history is
  load-bearing.
- `debrief-lessons/`: what prior debriefs told you about how these
  competitors actually bid against you.
- `customers/<this-agency>/`: your prior interactions with this customer
  that reveal what the customer thinks of each competitor.

See [../../docs/customize-for-your-company.md](../../docs/customize-for-your-company.md).

**Before any competitor research**, read
`references/competitive-intelligence-ethics.md`. Only properly sourced
information may enter a competitor entity page.

## Intake

Ask these as a numbered list. Skip what existing entities answer.

1. **The field.** Who are the known and suspected bidders? Is there an
   incumbent, and who is it? (The set-aside and vehicle in `pursuit.md` bound the
   field.)
2. **What is known per competitor.** For each likely bidder — size, relevant
   past performance, customer relationship, typical technical approach, typical
   price posture, recent wins and losses. What is the source of each claim?
3. **The incumbent's standing.** If the incumbent is a competitor, how is the
   customer relationship — strong, strained, fatigued? Known performance
   problems?
4. **The team's position.** Briefly, where is the team strong and weak relative
   to this field? (Used to assess exposure, not to set strategy.)
5. **Sources.** What public or properly obtained sources are available?

Where the team does not know something, that is an intelligence gap — record it
on the competitor entity with `confidence: low`; do not invent it.

## Workflow

```
Black Hat Competitive Assessment:
- [ ] Step 1: Open the pursuit wiki; read company-context if configured; read CI ethics
- [ ] Step 2: Complete intake; confirm the competitive field
- [ ] Step 3: Create or enrich a competitor entity per bidder
- [ ] Step 4: Bid the job as each competitor (the Black Hat)
- [ ] Step 5: Record ghosting opportunities and the team's exposures
- [ ] Step 6: Emit claims/ and source-register/ entities for the competitor reads
- [ ] Step 7: Render the competitive-assessment view; validate
```

**Step 1: Open and read.** Read `pursuit.md`, the customer entities, the bid
decision, the competitor stubs, and the CI ethics reference. If
`pursuit.md` carries a `company_context_path`, read the relevant
`partners/`, `debrief-lessons/`, and `customers/` company-context pages —
they are first-rung sources for prior-relationship facts. Cite the
company-context pages on the resulting competitor and source entities.

**Step 2: Confirm the field.** List the credible bidders; distinguish *likely*
from *possible*; treat the incumbent as its own case.

**Step 3: Competitor entities.** For each bidder, create or enrich
`entities/competitors/<name>.md` per `references/black-hat-method.md` — the
`## Profile` section (qualifications, past performance, relationship/incumbency,
typical approach, typical price posture, capacity, recent wins/losses). Tag every
claim's `source` and set the page `confidence` to the weakest claim it relies
on. Mark each item known or assessed.

**Step 4: Bid as them.** For each competitor entity, write the
`## Assessed offer` section by switching perspective: would they bid, their
likely solution, their likely win themes, their genuine strengths and
vulnerabilities on *this* bid, and their likely price posture. Give each
competitor their best plausible bid — no strawmen.

**Step 5: Ghosting and exposures.** On each competitor page, write a
`## Ghosting opportunity` section — a real, evidence-based competitor weakness,
framed as a positive, proven statement of the team's strength (no competitor
named in proposal text; the entity page may name them). Then create one
`entities/risks/<slug>.md` page per exposure the team carries that a competitor
will exploit, linked from the competitor entity — these feed `developing-win-strategy`.

**Step 6: Claims and source-register.** Emit the evidence graph:

- `entities/claims/`: write one claim entity per **assertable** competitor
  fact ("Acme Corp is the incumbent on the predecessor contract,"
  "Acme's typical labor mix runs 30% senior / 70% mid-level," "Acme has
  current TS/SCI bench across the region"). Each claim has the claim text,
  the owner who can defend it, the assertion type
  (`known fact` / `assessed` / `hypothesis`), and a status.
- `entities/source-register/`: write one source entity per external
  source the claims rest on: SAM.gov / USAspending records, Acme's public
  website and press releases, current public job postings, prior public
  awards, and any cited company-context page. Tag the source's rung on the
  [_source-policy.md](../../knowledge/_source-policy.md) authority ladder.

For competitor-proprietary or source-selection-sensitive material that the
team must not use, **do not create a claim or source entity**. Quarantine it
per [competitive-intelligence-ethics.md](references/competitive-intelligence-ethics.md).

**Step 7: Render and validate.** Render `views/competitive-assessment.md` from
the competitor, risk, claims, and source-register entities, including the
comparison matrix and an honest most-probable-winner read. Run the validation
checklist in `black-hat-method.md`. Update `pursuit.md`.

## Output

A `competitors/` subgraph (one entity per bidder), `risks/` entities for the
team's exposures, supporting `claims/` and `source-register/` entities, and
the `competitive-assessment.md` view.

Tell the user: the likely field, the most-probable winner and why, the strongest
ghosting opportunities, the team's most dangerous exposures, and the biggest
intelligence gaps.

## References

- `references/black-hat-method.md`: competitor entity sections, the "bid as them" technique, the comparison matrix, ghosting, exposures, and the validation checklist.
- `references/competitive-intelligence-ethics.md`: which competitor information may be used, and how the `sensitivity` tag quarantines what may not.

## Guardrails

- **Properly sourced information only.** Never use, seek, or speculate from a
  competitor's proprietary information or any source-selection-sensitive
  material. Quarantine such material with the `sensitivity` tag; do not fold it
  into an entity. See the ethics reference.
- **No strawmen.** Give each competitor their strongest plausible bid.
- **Mark assessed vs. known.** A predicted competitor offer is an assessment —
  set `confidence` honestly; never state a prediction as fact.
- **Be as honest about us as about them.** The team's exposures get the same
  candor as competitors' weaknesses, recorded as real `risks/` entities.
- **Maintain the graph, render the view.** The competitor, risk, claim, and
  source-register entities are the source of truth; the assessment view is a
  rendered read-out.
- **Company-context stays private.** When the skill draws on a configured
  `company_context_path`, it **references** the company-context pages by
  path; it does **not copy** their content into the pursuit wiki. Resulting
  pursuit entities carry `sensitivity: company-proprietary` where the
  underlying fact came from company-context. See
  [../../docs/customize-for-your-company.md](../../docs/customize-for-your-company.md).
