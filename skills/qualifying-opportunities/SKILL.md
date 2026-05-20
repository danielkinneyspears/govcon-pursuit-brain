---
name: qualifying-opportunities
description: Runs a structured bid/no-bid gate review for a US Federal opportunity and bootstraps the pursuit's knowledge wiki. Use when deciding whether to pursue or bid a federal solicitation, RFP, RFQ, RFI, sources-sought notice, or IDIQ task order — for a bid/no-bid decision, pursuit decision, gate review, opportunity qualification, go/no-go, or pWin assessment. Creates the pursuit wiki and its schema, builds the customer and bid-decision entities, and renders the opportunity-profile and bid-decision views.
canonical_job: opportunity-qualification
phase: plan
common_names:
  - bid/no-bid
  - gate review
  - go/no-go
  - pursuit decision
  - opportunity qualification
  - sizing
  - pursuit gate
---

# Qualifying Opportunities

Decide whether to pursue or bid a US Federal opportunity — and, because this is
usually the first skill to touch a pursuit, **bootstrap the pursuit wiki** it
will live in. The expensive mistake in federal BD is spending bid-and-proposal
money on bids that were never winnable; this skill makes that decision
deliberately, on evidence, and records it as the first entities in the pursuit's
knowledge graph.

## When to use this skill

Use this skill at any bid/no-bid gate — an early pursuit decision, a preliminary
bid decision, or post-RFP bid validation. It both renders the decision and, on
first run, creates the pursuit wiki that every later skill builds on.

It does not build the win plan — that is `planning-capture` and
`developing-win-strategy`. It decides whether there should be a win plan at all.

## Architecture

This skill is wiki-native. Read [docs/architecture.md](../../docs/architecture.md)
and the [conventions](../../conventions/) before running it. The skill **reads**
sources and the domain wiki, **maintains** pursuit entity pages, and **renders**
views — it never writes a flat artifact as a source of truth.

Relevant domain-wiki pages: `[[uniform-contract-format]]`, `[[section-m]]`,
`[[far-part-15-source-selection]]`, `[[best-value-tradeoff]]`, `[[lpta]]`.

## Inputs

**Required:** the opportunity — a described lead, or a solicitation document
placed in `pursuits/<id>/sources/`.

**Existing pursuit wiki**, if this is not the first run: read `pursuit.md` and
the existing `customer/`, `competitors/`, and `decisions/` entities; do not
re-create them.

**Private company context (recommended).** If `pursuit.md` carries a
`company_context_path:` field, **read the relevant company-context pages
before intake** — `customers/<this-agency>/`, `past-performance/`,
`key-personnel/`, `pricing-guidance/`, `compliance-posture/`,
`debrief-lessons/`, `approved-proof-points/`. Treat them as authoritative
sources for the questions they answer. See
[../../docs/customize-for-your-company.md](../../docs/customize-for-your-company.md).
Without company-context, the skill still runs from intake — just with less
leverage.

## Intake

Ask these as a numbered list. **Skip questions whose answers are already in
the solicitation, an existing pursuit entity, or the configured
company-context.** When company-context answers a question, cite the
company-context page on the resulting entity (use its path as `source:`,
inherit its `confidence`, tag the resulting entity
`sensitivity: company-proprietary`). Unknowns are valid answers and lower
`confidence`; never guess.

1. **The opportunity.** Agency and program office, scope, contract type,
   estimated value, period of performance, set-aside, solicitation number. Is a
   document available?
2. **The gate and posture.** Which gate is this (pursuit decision / bid decision
   / bid validation)? What is the team's competitive posture — incumbent,
   challenger, teaming partner, outsider?
3. **Customer relationship.** Prior relationship with this customer and office;
   any shaping or engagement to date; the incumbent, and whether it is the team.
4. **Capability and past performance.** Can the team perform the work? Is there
   recent, relevant past performance? Are required clearances, certifications,
   and the NAICS size standard met?
5. **Competition and funding.** Likely bidders; realistic competitiveness; is
   funding confirmed; known or estimated budget?
6. **Strategic fit and blockers.** Strategic alignment; blockers — OCI, a
   teaming dependency, a missing vehicle, capacity, unacceptable terms.

## Workflow

```
Bid/No-Bid Gate Review:
- [ ] Step 1: Bootstrap or open the pursuit wiki; read company-context if configured
- [ ] Step 2: Complete intake; record unknowns as gaps
- [ ] Step 3: Build the customer entities
- [ ] Step 4: Run knockout checks and the weighted scorecard
- [ ] Step 5: Estimate pWin; form the recommendation
- [ ] Step 6: Write the bid-decision entity + supporting claims/ and source-register/ entities
- [ ] Step 7: Render the views and validate
```

**Step 1: Bootstrap or open the pursuit wiki; read company-context.** If
`pursuits/<id>/pursuit.md` does not exist, perform the workspace-safety check
(confirm the location is not in tracked version control; see the pursuit
`.gitignore`), then create the pursuit directory and `pursuit.md` from
`schema/pursuit-schema.template.md` — setting identification, **posture**,
**mode** (`full` or `lite`), the **sensitivity policy**, and the
**`company_context_path:`** if a private company-context workspace is
configured. If it exists, read it. If a `company_context_path` is set, read
the relevant company-context pages now (customers, past performance, key
personnel, pricing guidance, compliance posture, debrief lessons, approved
proof points) — they will short-circuit several intake questions.

**Step 2: Intake.** Work the intake questions. Carry every unknown forward as a
gap; an honest unknown beats a confident guess.

**Step 3: Customer entities.** Create `entities/customer/` pages — the agency,
the program office, and one `customer/stakeholders/<name>.md` per known
decision-maker or influencer. Tag each with `source`, `confidence`,
`sensitivity`, `provenance`. In `lite` mode, the customer may be a single page.

**Step 4: Knockouts and scorecard.** Run the knockout checks and the weighted
six-category scorecard in `references/bid-no-bid-criteria.md`. A triggered
knockout drives the recommendation regardless of score. Every score carries one
line of evidence; where the evidence is an unknown, score conservatively.

**Step 5: pWin and recommendation.** Estimate pWin per the criteria file,
applying its anti-optimism discipline. Form one recommendation: **bid**,
**no-bid**, or **conditional bid** (with specific, assigned, dated conditions).

**Step 6: Bid-decision entity + claims and source-register.** Write
`entities/decisions/bid-decision.md`: the gate, the knockout results, the
scorecard, pWin, the recommendation, the rationale, and the gaps. Link it to
the customer entities and to any `competitors/` stubs. Tag it
`approval: pending` — a bid decision is a high-risk output awaiting a human
gate decision. If competitors were named, create low-confidence
`competitors/<name>.md` stubs for `analyzing-competitors` to enrich later.

Then build the supporting evidence graph:

- `entities/claims/`: write one claim entity per **assertable** fact the
  bid decision rests on. Examples: "Customer is the same buying office that
  bought the prior contract," "Team holds an active SBA 8(a) certification,"
  "Funding line is confirmed in agency budget request." Each claim entity
  carries the claim text, the owner who can defend it, the assertion type
  (`known fact` / `assessed` / `hypothesis`), the proposal use, and a status.
- `entities/source-register/`: write one source entity per **external
  source** the claims rest on. SAM.gov notices, USAspending records, agency
  budget documents, prior award notices, customer meeting notes (from the
  pursuit's contact reports), company-context pages. Each source entity
  carries the source URL or path, authority (which rung of the
  [_source-policy.md](../../knowledge/_source-policy.md) ladder), directness,
  recency, independence, and a date pulled.

Every claim links to one or more sources; every source lists the claims it
supports. Confidence on the bid-decision entity is then the **lowest** claim
confidence it rests on.

**Step 7: Render and validate.** Render two views to `pursuits/<id>/views/`:
`opportunity-profile.md` and `bid-decision.md`, per
[conventions/views.md](../../conventions/views.md). Run the validation checklist
in `references/bid-no-bid-criteria.md`. Update `pursuit.md`'s entity index, view
index, and change log.

## Output

A bootstrapped pursuit wiki: `pursuit.md` (with `company_context_path` if
configured), the `customer/` entities, the `decisions/bid-decision.md`
entity, supporting `claims/` and `source-register/` entities, optional
`competitors/` stubs, and the `opportunity-profile.md` and `bid-decision.md`
views.

Tell the user: the recommendation, the score and pWin, the top decision
drivers, the most important gaps, and that the bid decision is `approval: pending`.

## References

- `references/bid-no-bid-criteria.md`: the knockout checks, the weighted six-category scorecard, pWin estimation, and the validation checklist.

## Guardrails

- **Bootstrap safely.** Before creating the pursuit wiki, confirm its location
  is not tracked in version control; a pursuit wiki holds sensitive material.
- **Honest unknowns beat confident guesses.** Never invent a relationship, a
  competitor read, or funding certainty. Record gaps; set `confidence` honestly.
- **Knockouts are not negotiable.** A real disqualifier yields a no-bid (or a
  conditional bid contingent on resolving it), regardless of score.
- **The bid decision is decision support.** It is `approval: pending` until a
  human gate owner decides. The skill informs the call; it does not make it.
- **Maintain the graph, render the view.** Entities are the source of truth; the
  views are rendered read-outs and are never hand-edited.
- **Company-context stays private.** When the skill draws on a configured
  `company_context_path`, it **references** the company-context pages by
  path; it does **not copy** their content into the pursuit wiki. The
  resulting pursuit entities carry `sensitivity: company-proprietary` where
  the underlying fact came from company-context. See
  [../../docs/customize-for-your-company.md](../../docs/customize-for-your-company.md).
