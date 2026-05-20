# Pursuit Lifecycle Taxonomy

This is the translation layer between any company's process vocabulary and
this package's skills. It sits above the GovCon-specific vocabulary
(Shipley terms, color teams, Section L/M/C) and speaks in universal jobs
first.

The package operates on two layers:

```
Elemental layer:        Plan / Create / Iterate
                        Canonical jobs (universal)
                        Aliases (common names per shop)
                        Desired outcomes

GovCon method layer:    Shipley-style lifecycle
                        Color teams
                        Section L / M / C, FAR, source selection
                        Proposal artifacts
```

Whatever your shop calls a step ("Black Hat," "competitive intel,"
"incumbent assessment"), the same canonical job underneath does the same
work. This document is the map.

## The three phases

| Phase | Goal |
|---|---|
| Plan | Decide whether and how to pursue, and shape the win. |
| Create | Turn the pursuit position into a compliant, compelling response. |
| Iterate | Test, fix, approve, submit, and learn. |

The phases are loops, not gates. `iterate` results feed the next pursuit's
`plan`, and amendments mid-create return the team to parts of `plan`.
Phases are an organizing frame, not a one-way pipeline.

## How to read these tables

Each canonical job carries:

- Canonical job: the kebab-case id the package uses internally.
- Common names: the aliases your shop probably already uses. Search for any of them; you land on the same canonical job.
- User goal: what a human is trying to accomplish.
- Primary outputs: the entity pages (or views) the job produces.
- Owning skills: which skill(s) in this package perform the job. Most are listed as planned in v0.2.x; the package has only two proof skills today.

## Plan — decide, shape, and position

| Canonical job | Common names | User goal | Primary outputs | Owning skills |
|---|---|---|---|---|
| `opportunity-qualification` | bid/no-bid, gate review, go/no-go, pursuit decision, opportunity qualification, sizing | Decide whether to invest in the pursuit, with a defensible scorecard and pWin. | `decisions/bid-decision`, `customer/`, supporting `claims/` + `source-register/` | `qualifying-opportunities` |
| `customer-and-mission-understanding` | customer analysis, situational analysis, mission analysis | Build a true picture of the customer, their mission, what they're trying to fix. | `customer/`, `customer/mission`, `incumbent-pain/` | planned |
| `relationship-and-influence-mapping` | stakeholder map, influence map, decision-maker mapping, power map | Know who decides, who influences, who trusts whom, and where access is real vs. assumed. | `relationship-map/`, `customer/stakeholders/`, `contacts/` | planned |
| `competitive-intelligence` | Black Hat, competitor analysis, market intel, incumbent assessment, competitive assessment, recompete analysis | Understand who else can win, why, and how to position against them. | `competitors/`, `risks/` (team exposures), ghosting frames, `claims/` + `source-register/`, most-probable-winner read | `analyzing-competitors` |
| `incumbent-vs-challenger-strategy` | posture strategy, defending vs displacing | Set and enforce the pursuit posture, branching every later decision. | `pursuit.md` posture field, `incumbent-pain/`, `decision-politics/` | planned |
| `teaming-and-partner-strategy` | teaming, partner selection, JV strategy, mentor-protégé strategy, subcontractor strategy | Identify capability and PP gaps, recruit credible partners, structure workshare to win. | `teammates/`, `decisions/teaming-decision` | planned |
| `past-performance-fit` | PP qualification, relevancy mapping, PP fit assessment | Score candidate past performance against the actual evaluation criteria and choose the strongest references. | `past-performance/`, claims about relevancy, fit assessment view | planned |
| `solution-shaping` | solution shaping, solution architecture, technical approach shaping | Move the technical solution toward something that wins, well before drafting. | `solution/`, candidate approach entities, `risks/` | planned |
| `price-to-win` | PTW, business case, pricing strategy, target price | Estimate the price that wins; identify levers; tie cost to win strategy. | `decisions/price-to-win`, `pricing-reality/` | planned |
| `win-strategy` | win themes, discriminators, value proposition, ghosting strategy | Convert hot buttons and discriminators into substantiated win themes mapped to evaluation factors. | `themes/`, `discriminators/`, `hot-buttons/`, `proof-points/` | planned |
| `capture-planning` | capture plan, pursuit plan, capture strategy | Run the capture as a managed effort with assigned, dated actions and gate reviews. | `decisions/capture-plan`, `contacts/`, `capture-momentum/`, gate-review decisions | planned |

## Create — turn position into a compliant response

| Canonical job | Common names | User goal | Primary outputs | Owning skills |
|---|---|---|---|---|
| `solicitation-intake` | RFP intake, document analysis, solicitation parsing | Get a clean, structured view of the solicitation into the pursuit. | `sources/`, parsed Section L/M/C/H/K references | planned |
| `compliance-tracing` | solicitation shred, compliance matrix, L/M/C trace, requirements traceability | Convert every requirement into an atomic, owned, trackable item with cross-walk. | `requirements/`, `compliance-matrix` view | planned |
| `clarification-drafting` | Q&A drafting, CO questions, clarification letters | Write the right questions to the contracting officer by the deadline without telegraphing strategy. | `questions/`, question log | planned |
| `amendment-impact-analysis` | amendment shred, amendment impact, modification impact | Re-shred and assess the blast radius of every amendment without losing requirement IDs. | `amendment-impact/`, updated `requirements/` | planned |
| `annotated-outline` | outline, proposal outline, annotated outline | Build a Section L-compliant outline with factor mapping, theme assignment, proof, pages, owners. | `sections/` (annotated), outline view | planned |
| `storyboarding` | storyboards, section planning, mockups | Plan each section's argument, proof, and graphic before drafting. | `sections/` storyboards, `proof-points/`, graphics concepts | planned |
| `sme-data-calls` | SME interviews, expert data calls, technical input gathering, 20-minute SME mode | Capture SMEs' knowledge in plain language and translate it into proposal entities. | `solution/`, `proof-points/`, `claims/`, `risks/` | planned (see `playbooks/sme-data-call.md`) |
| `technical-volume-drafting` | technical approach drafting, technical narrative, solution writing | Convert storyboards and solution into compliant, persuasive technical sections. | `sections/` drafts, view: technical volume | planned |
| `management-volume-drafting` | management approach drafting, staffing approach, transition drafting | Convert the team's operating model into compliant, persuasive management sections. | `sections/` drafts, `team-capacity/`, view: management volume | planned |
| `past-performance-volume` | PP write-ups, past performance references, citations volume | Produce relevant, well-formatted past-performance write-ups. | `past-performance/` write-ups, PP volume view | planned |
| `cost-and-pricing-volume` | cost volume, price volume, pricing buildup, BOE, cost narrative | Produce a defensible cost/price volume with traceable BOE. | `pricing-reality/`, cost narrative entities, cost volume view | planned |
| `claims-and-proof-points` | claim ledger, proof point development, evidence library | Build the assertable claims and their evidence into a reusable, traceable graph. | `claims/`, `proof-points/`, `source-register/` | partial (both proof skills emit these as of v0.2.2) |
| `graphics-and-evidence-packaging` | graphics, action captions, tables, exhibits | Make every graphic earn its page budget; every claim land an action caption. | graphic concepts on `sections/`, exhibits | planned |
| `submission-package-assembly` | production, assembly, packaging, book build | Assemble the final, conforming submission package on schedule. | submission package, file/format compliance | planned |

## Iterate — test, recover, approve, submit, and learn

| Canonical job | Common names | User goal | Primary outputs | Owning skills |
|---|---|---|---|---|
| `solution-review` | Blue Team, solution validation, strategy review | Pressure-test the solution and win strategy before heavy drafting. | `findings/` (Blue), `review-closure/` | planned |
| `storyboard-and-early-draft-review` | Pink Team, early-draft review, structure review | Validate compliance approach, structure, themes, proof points before full drafting. | `findings/` (Pink), `review-closure/` | planned |
| `cost-and-pricing-review` | Green Team, pricing review, cost realism check | Catch pricing-strategy, BOE, realism, and cost-technical-consistency issues before Red. | `findings/` (Green), `review-closure/` | planned |
| `evaluator-perspective-review` | Red Team, mock evaluation, source-selection sim, evaluation board sim | Score the near-final draft as a source-selection evaluator would. Find weaknesses and deficiencies before the government does. | `findings/` (Red) with adjectival ratings, `review-closure/`, integrated verdict | planned |
| `executive-readiness-review` | Gold Team, executive review, go/no-go review | Final executive judgment: submit or not. | `findings/` (Gold), `decisions/submit-or-not` | planned |
| `production-quality-review` | White Glove, book check, production review | A page-by-page human pass over the assembled package — catch production defects, formatting drift, broken cross-references. | `findings/` (White Glove), `review-closure/` | planned |
| `review-recovery` | comment adjudication, recovery, finding closure | Turn findings into owned, assigned, verified-closed corrections. | `review-closure/` records, updated `sections/` and `claims/` | planned |
| `submission-compliance-check` | final compliance check, pre-submission audit, submission verification | Verify the proposal will be accepted (page limits, format, file naming, volume separation, forms, mechanics). | submission-compliance view, go/no-go on submission | planned |
| `debrief-analysis` | debrief, win/loss analysis, post-mortem | Capture and learn from the government's explanation of the evaluation. | `decisions/debrief-analysis`, `debrief-lessons/` (private), promotable lessons | planned |
| `protest-decision-support` | protest support, no-protest decision, protest evaluation | Identify whether a debrief finding suggests a possible protest matter; flag to counsel. | `decisions/protest-flag` (counsel hand-off, no merit assessment) | planned |
| `lessons-learned` | post-mortem, reusable proof update, retrospective, knowledge promotion | Promote pursuit lessons to reusable doctrine; update or retire stale claims. | updates to `proof-points/`, candidates for `company-context/approved-proof-points/` and `company-context/debrief-lessons/` | planned |

## How a search lands you in the right place

The point of this taxonomy is discoverability without learning new jargon:

- A user searching "Green Team" lands on the `cost-and-pricing-review` canonical job.
- A user searching "pricing review" or "cost realism check" lands on the same canonical job.
- A user searching "Black Hat," "competitor analysis," or "market intel" lands on `competitive-intelligence` (skill: `analyzing-competitors`).
- A user searching "bid/no-bid," "go/no-go," or "pursuit decision" lands on `opportunity-qualification` (skill: `qualifying-opportunities`).

The skill frontmatter carries `canonical_job:`, `phase:`, and
`common_names:` so search by any of these resolves to the right skill.

## When the GovCon method layer matters

The elemental layer says what the job is. The GovCon method layer (Shipley
terms, color teams, Section L/M/C, the FAR, source-selection mechanics)
tells you how to do it well in federal acquisition. Both matter: skip the
elemental layer and the package's jargon excludes anyone who calls it
something different; skip the GovCon method layer and you lose the rigor
that makes pursuits actually win against real evaluation boards.

The skills hold both. Frontmatter and headers use the canonical names; the
substance and references draw on the GovCon method layer.

## Mapping to the rest of the package

- The capture-manager and proposal-manager playbooks (`playbooks/`) walk a role through the canonical jobs by phase.
- The domain wiki (`knowledge/`) holds the GovCon method layer's vocabulary: color teams, Section L/M/C, FAR mechanics, vehicles, set-asides.
- The pursuit-wiki entity types are the graph of artifacts the canonical jobs produce and read.
- The two proof skills are entry points to two canonical jobs; most of the table is "planned" in v0.2.x and is the roadmap.

## Updating this taxonomy

If a company has a job their team performs that does not map cleanly here,
add a row. The taxonomy is part of the package's API. Keeping it accurate
across real customer vocabulary is what makes the rest of the package
pluggable.
