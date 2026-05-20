# Pursuit: FSSA Enterprise IT Service Desk Recompete

> [!warning] Synthetic example
> This is a fictional pursuit. The agency, solicitation, customer,
> competitors, and all entity content are invented for illustration only.

## Identification

- Opportunity: Enterprise IT Service Desk Recompete (FSSA-DigOps)
- Solicitation / notice number: `SYN-2026-R-0001`
- Customer: Federal Synthetic Services Administration (FSSA), Office of
  Digital Operations
- Contract type: Firm-Fixed-Price
- Set-aside: Total small business set-aside (NAICS 541519)
- Estimated value: $25M–$35M over base + 4 options
- Key dates: RFP released 2026-05-01; proposals due 2026-06-15 14:00 ET
- Created: 2026-05-19 · Updated: 2026-05-19

## Pursuit posture

**Posture: `challenger`**

A different small business is the incumbent. The team has done comparable
service-desk work for adjacent civilian agencies but has no prior contract
with FSSA. Posture branches: emphasize transition risk neutralization,
develop incumbent-capture staffing, document an explicit "why change?" case.

## Mode

**Mode: `full`** — major recompete, full entity model.

## Sensitivity policy

This is a synthetic public example. All entities here carry
`sensitivity: public`. A real pursuit would set this section per the
organization's policy.

## Conventions in force

- Entity pages: [../../conventions/entity-pages.md](../../conventions/entity-pages.md)
- Tagging: [../../conventions/tagging.md](../../conventions/tagging.md)
- Views: [../../conventions/views.md](../../conventions/views.md)
- Domain wiki: [../../knowledge/_schema.md](../../knowledge/_schema.md)

## Conflict resolution

Solicitation > FAR > higher-confidence entity > more-recent entity. Surface,
do not guess.

## Company context (private layer)

- `company_context_path:` (none configured — this is the public-only example)
- `company_context_use:` `none`

## Entity index

| Type | Path | Count | Notes |
|---|---|---|---|
| customer | `entities/customer/` | 1 | FSSA Digital Operations |
| competitors | `entities/competitors/` | 1 | Acme Synthetic Solutions (incumbent) |
| decisions | `entities/decisions/` | 1 | bid-decision: conditional bid |
| claims | `entities/claims/` | 1 | acme-is-incumbent |
| source-register | `entities/source-register/` | 1 | sam-gov-syn-2026 |

## View index

| View | Rendered | Source-of-truth entities |
|---|---|---|
| `views/bid-decision.md` | 2026-05-19 | decisions/bid-decision, customer/, competitors/, claims/ |

## Change log

| Date | Skill | What changed |
|---|---|---|
| 2026-05-19 | qualifying-opportunities (example) | Pursuit created; customer, incumbent competitor, bid decision, supporting claim and source-register populated; bid-decision view rendered. |
