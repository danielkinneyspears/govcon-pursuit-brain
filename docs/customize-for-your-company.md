# Customize for Your Company

`govcon-pursuit-brain` is the public GovCon pursuit method layer: domain
knowledge, schemas, conventions, playbooks, validators, and pursuit
workflows. This document explains how to pair the public method with your
company's private context so the package works for your specific business.

## The 40/60 split

Roughly 40% of pursuit value can live in an open-source method layer. The
other 60% is company-specific and accumulated through use.

| Public method layer (this package) | Private company context (yours) |
|---|---|
| FAR / DFARS / CFR orientation | Your customer relationships |
| Solicitation structure (UCF, L/M/C) | Incumbent pain, customer politics |
| Source-selection mechanics | Your past performance and CPARS history |
| Bid/no-bid frameworks | Leadership appetite, B&P tolerance |
| Capture playbook (Black Hat, PTW, win themes) | Your discriminators, what you can credibly claim |
| Proposal craft (compliance matrix, color teams) | Your proposal team capacity, voice, doctrine |
| CMMC / FedRAMP / NIST 800-171 basics | Your actual compliance posture and gaps |
| Protest and debrief mechanics | Your prior debrief lessons |
| Public-source research patterns (SAM, USAspending) | Your CRM, internal sales intel, relationship maps |
| Synthetic example pursuits | Your real pursuits (kept private) |

The public method teaches a disciplined GovCon team how to think. The
private context teaches the method what is true for this company.

## What goes private

Keep this in a private repository or controlled workspace. Never put it in
this public package.

```
company-context/
  customers/              # the agencies and program offices you actually serve
  past-performance/       # your approved past-performance library, with CPARS
  key-personnel/          # your bench, clearances, availability, commitments
  partners/               # teaming history, exclusivity, mentor-protégé status
  pricing-guidance/       # wrap rates, indirect ranges, fee posture, PTW rules
  compliance-posture/     # your CMMC, FedRAMP, NIST 800-171, ITAR/EAR state
  debrief-lessons/        # what you learned losing or winning recent pursuits
  approved-proof-points/  # validated claims you may make in proposals
  pursuits/               # active pursuits (also git-ignored by this package)
```

The `pursuits/` directory at the root of this public package is already
git-ignored. That protects pursuit-level data when you use the package
in-place. Your broader company-context belongs in a separate location
under your organization's control.

See [`../schema/company-context.template.md`](../schema/company-context.template.md)
for the per-folder structure, entity types, frontmatter, and sensitivity
rules.

## How skills layer private context on public method

Every skill in this package follows the same pattern when private company
context is available:

1. Read the public method (domain wiki, conventions, schema).
2. Read the company-context: if a `company-context/` (or `--company-context` argument) is configured, read it before intake.
3. Skip intake questions whose answers are in company-context. If the company's pricing-guidance already covers indirect rates, the skill does not ask the user to retype them. The skill cites the company-context source on the resulting entity pages.
4. Augment the pursuit wiki with company-context-derived entities. For example, an approved past-performance reference from `company-context/past-performance/` lands in `pursuits/<id>/entities/past-performance/` for the pursuit, with its `source` tagged to the company-context page and `confidence` propagated.
5. Never copy company-context into the public package. The company-context stays in the company's private repository or workspace; the pursuit wiki *references* it.

Without a configured `company-context/`, skills fall back to user intake.
The method still works, just with less leverage. The package is genuinely
useful without private context; it is more useful with it.

## Naming guidance

Avoid "company brain." It overclaims and implies an enterprise knowledge
system. Use the language below for your private-context layer:

- "Customize for Your Company"
- "Adapt This to Your Company"
- "Using Private Company Context"
- "Company Customization"
- "Customize to Your Company's Needs"

The repo here is named for the *pursuit* brain (the per-pursuit
compounding knowledge graph), which is what the architecture actually
builds. Per-pursuit memory compounds across one bid; company-context
compounds across a company's portfolio. Both are needed; neither is "the
company brain."

## What capture and proposal people actually care about

Many of the things that decide a pursuit do not live in clean artifacts:

- who the customer actually trusts
- incumbent pain and incumbent vulnerability
- bid/no-bid politics inside the company
- leadership appetite and B&P tolerance
- proposal team capacity
- SME usability and availability
- real proof quality vs. boilerplate
- pricing realism (what you can actually bid, not just PTW)
- amendment blast radius across the pursuit
- color team closure quality
- relationship gaps
- teaming politics
- whether the capture plan has momentum or is just words

The pursuit-wiki entity model includes types for each. See the entities
added in v0.2.2: `incumbent-pain/`, `capture-momentum/`,
`decision-politics/`, `team-capacity/`, `proof-points/`,
`pricing-reality/`, `amendment-impact/`, `review-closure/`, and
`relationship-map/`. Most of those entities draw on company-context in
addition to the public solicitation.

## Privacy and sensitivity

The `sensitivity` tag on every entity page enforces the boundary:

- Company-context entities normally carry `sensitivity: company-proprietary`.
- Customer-meeting notes may rise to `sensitivity: source-selection-sensitive` if they reflect non-public evaluation information. See [`../conventions/tagging.md`](../conventions/tagging.md) and [`../knowledge/integrity-and-ethics/procurement-integrity-act.md`](../knowledge/integrity-and-ethics/procurement-integrity-act.md).
- Competitor information from a competitor's protected sources is `sensitivity: competitor-proprietary`, quarantined, not used. See [`../skills/analyzing-competitors/references/competitive-intelligence-ethics.md`](../skills/analyzing-competitors/references/competitive-intelligence-ethics.md).
- CUI, export-controlled, and classified material may only enter the workspace if the organization's policy and the applicable safeguarding rules permit it.

The `scripts/validate_vault.py` validator enforces `sensitivity` rules and
will warn on inappropriate combinations.

## Recommended adoption path

1. Use the public package first. Run a pursuit through the public method with intake-based input. Get a feel for the entity model and the skills.
2. Stand up a minimal `company-context/` in a private repo. Start with the highest-leverage folders: `past-performance/`, `key-personnel/`, `pricing-guidance/`. The rest grows over time.
3. Configure the skills to read the company-context location (the per-pursuit `pursuit.md` schema includes a `company_context_path:` field).
4. Let the company-context compound. Every pursuit produces lessons, reusable proof points, and debrief findings; promote the ones that generalize back into `company-context/`. That is the value-multiplier the public method alone cannot deliver.

## What this is and is not

This package is an open-source GovCon pursuit framework that helps teams
turn capture and proposal work into structured, evidence-backed, reusable
pursuit knowledge.

It is not a complete company brain, a system of record, or a replacement
for CRM, SharePoint, or proposal-management SaaS. It is the method layer
that those systems' data can pour into and the agents the company already
uses can read against.
