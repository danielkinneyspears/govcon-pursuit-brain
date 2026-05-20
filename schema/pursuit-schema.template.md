# Pursuit: <Opportunity name>

This file is `pursuit.md` — the Layer 3 schema and index for one pursuit wiki.
The first skill to run on a pursuit creates it from this template. Every skill
reads it first. It is created at `pursuits/<solicitation-id>/pursuit.md`.

## Identification

- Opportunity: <name>
- Solicitation / notice number: <number, or "pre-RFP">
- Customer: <agency / program office>
- Contract type: <FFP / T&M / cost-reimbursement / IDIQ task order / unknown>
- Set-aside: <type, or "full and open" / "unknown">
- Estimated value: <range, or "unknown">
- Key dates: <RFP release, proposal due — as known>
- Created: <date> · Updated: <date>

## Pursuit posture

The team's competitive position on this pursuit. This field branches guidance
across the package — capture, competitive analysis, win themes, transition,
staffing, and review all read it.

**Posture: <one of>**
- `incumbent-defending` — the team holds the work and is defending it.
- `challenger` — a competitor is the incumbent; the team is challenging.
- `favored-challenger` — no incumbent advantage against the team, or the team is
  the front-runner on a new requirement.
- `outsider` — the team has little customer access or relationship.
- `teaming-partner` — the team is pursuing as a subcontractor on another prime's
  team.
- `recompete-after-incumbent-pain` — a recompete where the incumbent has known
  performance problems.

<One or two sentences on what this posture means for the pursuit.>

## Mode

**Mode: <full | lite>**

- `full` — the complete entity model; for major pursuits.
- `lite` — a reduced model for small or fast pursuits (e.g., short task orders):
  the customer as one page, requirements grouped rather than one page each,
  fewer entity types. Skills scale entity granularity to this field.

## Sensitivity policy

What information classifications are permitted in this pursuit wiki, per the
organization's policy and the applicable safeguarding rules. Skills check this
before writing an entity (see [../conventions/tagging.md](../conventions/tagging.md)).

- `public` — permitted.
- `company-proprietary` — permitted.
- `cui` — <permitted with the controls stated here | NOT permitted in this workspace>
- `export-controlled` — <permitted with controls | NOT permitted>
- `source-selection-sensitive` — <handling rule>
- `competitor-proprietary` — quarantined, never used.
- `classified` — never permitted in this workspace.

<State the safeguarding controls in force, or that only public and
company-proprietary material may enter this workspace.>

## Conventions in force

- Entity pages: [../conventions/entity-pages.md](../conventions/entity-pages.md)
- Tagging: [../conventions/tagging.md](../conventions/tagging.md)
- Views: [../conventions/views.md](../conventions/views.md)
- Domain wiki: [../knowledge/_schema.md](../knowledge/_schema.md)

## Conflict resolution

When sources disagree, resolve in this order:

1. The solicitation itself (Section L governs the proposal).
2. The current FAR and the applicable agency supplement.
3. A higher-`confidence` entity over a lower-`confidence` one.
4. A more recent entity over an older one (`provenance` date).

When a conflict cannot be resolved, the entity records both readings, tags
`confidence: low`, and the skill surfaces it to the user rather than guessing.

## Entity index

The entity types present in this pursuit wiki, updated as skills add them.

| Type | Path | Count | Notes |
|---|---|---|---|
| customer | `entities/customer/` | 0 | |
| competitors | `entities/competitors/` | 0 | |
| hot-buttons | `entities/hot-buttons/` | 0 | |
| discriminators | `entities/discriminators/` | 0 | |
| themes | `entities/themes/` | 0 | |
| requirements | `entities/requirements/` | 0 | |
| solution | `entities/solution/` | 0 | |
| sections | `entities/sections/` | 0 | |
| risks | `entities/risks/` | 0 | |
| teammates | `entities/teammates/` | 0 | |
| key-personnel | `entities/key-personnel/` | 0 | |
| past-performance | `entities/past-performance/` | 0 | |
| contacts | `entities/contacts/` | 0 | |
| decisions | `entities/decisions/` | 0 | |
| findings | `entities/findings/` | 0 | |
| questions | `entities/questions/` | 0 | |
| claims | `entities/claims/` | 0 | assertable claims with source/owner/use |
| source-register | `entities/source-register/` | 0 | external sources backing claims |
| relationship-map | `entities/relationship-map/` | 0 | "who really decides and who trusts whom" |
| incumbent-pain | `entities/incumbent-pain/` | 0 | identified customer pain with the incumbent |
| capture-momentum | `entities/capture-momentum/` | 0 | weekly snapshot of pursuit traction |
| decision-politics | `entities/decision-politics/` | 0 | team + customer decision politics |
| team-capacity | `entities/team-capacity/` | 0 | bench, bandwidth, skills available for the bid |
| proof-points | `entities/proof-points/` | 0 | reusable validated claim + evidence pairs |
| pricing-reality | `entities/pricing-reality/` | 0 | what the team can actually bid given constraints |
| amendment-impact | `entities/amendment-impact/` | 0 | per-amendment blast-radius analysis |
| review-closure | `entities/review-closure/` | 0 | per-finding closure record |

## Company context (private layer)

If a private `company-context/` workspace is available, this pursuit can draw
on it. Configure the location here; skills check this field before asking the
user to retype information that is already known.

- `company_context_path:` `<absolute path; e.g., ~/company-context/>`
- `company_context_use:` `<full | read-only | none>`

If absent or set to `none`, skills fall back to user intake. See
[../docs/customize-for-your-company.md](../docs/customize-for-your-company.md)
and [./company-context.template.md](./company-context.template.md).

## View index

The rendered views present in `views/`, updated as skills render them.

| View | Rendered | Source-of-truth entities |
|---|---|---|
| | | |

## Change log

| Date | Skill | What changed |
|---|---|---|
| <date> | <skill> | Pursuit created |
