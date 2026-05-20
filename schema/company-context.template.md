# Company Context — Template

This is the Layer-3 schema for a **private company-context workspace** that
pairs with this public package. Copy this template to your **private**
repository or controlled workspace; do **not** populate it with real company
data inside this public package.

See [`../docs/customize-for-your-company.md`](../docs/customize-for-your-company.md)
for the framing (40% public method, 60% private context).

## Identification

- Organization: `<your company / business unit>`
- Context path: `<the local path skills should read; e.g., ~/company-context/>`
- Created: `<date>` · Updated: `<date>`
- Sensitivity policy: which classifications are permitted (`public`,
  `company-proprietary` always; `cui` / `export-controlled` /
  `source-selection-sensitive` per your organization's policy).

## Folder structure

```
company-context/
  README.md              # this file, populated
  customers/             # one folder per agency / program office
  past-performance/      # one entity page per prior contract
  key-personnel/         # one page per person on the bench
  partners/              # one page per teammate or candidate teammate
  pricing-guidance/      # wrap rates, indirect ranges, fee posture, PTW rules
  compliance-posture/    # your CMMC / FedRAMP / NIST 800-171 / ITAR-EAR state
  debrief-lessons/       # what was learned from prior wins and losses
  approved-proof-points/ # claims validated for proposal use
```

## Entity conventions

Company-context entity pages follow the same conventions as pursuit-wiki
entity pages — see [`../conventions/entity-pages.md`](../conventions/entity-pages.md)
and [`../conventions/tagging.md`](../conventions/tagging.md):

- **One concept per page.**
- **Frontmatter** with `id`, `type`, `title`, `tags`, `status`, `sensitivity`,
  `source`, `confidence`, `provenance`, `last_verified`, `next_review_due`,
  `updated`.
- **Wiki links** as `[[type/id]]` or `[[id]]`.
- **Sensitivity** is `company-proprietary` by default. Anything that would
  be `cui`, `export-controlled`, or `source-selection-sensitive` only enters
  this workspace if your safeguarding rules permit.

## Per-folder content

### `customers/`

One folder per agency / program office, with:

- `agency.md` — mission, organization, how you sell to them, named contacts.
- `program-offices/<name>.md` — specific buying centers and the people in them.
- `stakeholders/<name>.md` — decision-makers and influencers with role,
  disposition (advocate / neutral / skeptical), access quality, last touch.
- `contact-reports/<date>-<who>.md` — engagement records.

### `past-performance/`

One page per prior contract you may cite:

- Contract facts (customer, value, period of performance, your role).
- Scope performed.
- Outcomes delivered (quantified where possible).
- CPARS ratings, PPQ scores, award-fee history.
- Relevance hints: agencies / scopes / sizes this maps cleanly to.
- Approval status: who signed off on this past performance for proposal use,
  and any restrictions.

### `key-personnel/`

One page per named person on the bench:

- Role(s) they can fill.
- Clearance level and status.
- Certifications.
- Availability (current contract, end date, commit-ability).
- Resume of record (or pointer to it).
- Prior pursuits proposed on and outcomes.

### `partners/`

One page per teaming partner or candidate:

- Status (current teammate, candidate, no longer used).
- Capabilities they bring.
- Past performance they bring.
- Set-aside / socioeconomic status.
- Exclusivity arrangements and dates.
- Mentor-protégé agreement status, if applicable.
- Relationship notes (who at the partner, escalation paths).

### `pricing-guidance/`

Pricing posture and rules:

- Approved wrap-rate ranges by labor category.
- Indirect-rate structure and current forward-pricing rate agreements.
- Fee posture by contract type and bid context.
- Price-to-win discipline (when to walk, when to stretch).
- Escalation defaults.
- Subcontractor pricing playbook.

### `compliance-posture/`

Your current state, not the public regime explanations (those live in the
public domain wiki):

- CMMC level achieved / pursuing, with date and assessor.
- FedRAMP authorizations / certifications held.
- NIST 800-171 self-assessment score (SPRS) and POA&M state.
- ITAR / EAR registrations and license history.
- Cybersecurity insurance, incident-response posture.
- Capacity to handle CUI in pursuits.

### `debrief-lessons/`

One page per debrief (won or lost):

- The pursuit (link to or summary of the pursuit wiki, if retained).
- What the government said, by Section M factor.
- What the team thought vs. what the government found.
- Lessons — what to do differently, where it applies (bid/no-bid, capture,
  proposal practice, pricing, review).
- Counsel-flag items if any.

### `approved-proof-points/`

The library of validated claims you may make in proposals:

- The claim, in its general form.
- The proof (which past performance, which metric, which credential).
- The customer types and scopes it maps to.
- Approval — who validated this for use, when, with what restrictions.
- Stale date — when this needs re-validation.

A new claim in a pursuit can be promoted to this library after vetting; a
proof point that has gone stale here can be pulled back into review.

## How skills should read company-context

A pursuit's `pursuit.md` (per the per-pursuit schema) carries a
`company_context_path:` field. Skills check it on every run:

1. If absent → fall back to user intake.
2. If present → before asking the user, read the relevant company-context
   pages and use them as inputs. Cite each as the `source:` on the resulting
   pursuit entity. Propagate `confidence` and `sensitivity`.
3. **Never** copy company-context content into the public package or into a
   shared pursuit workspace where its sensitivity would be at risk.

## Privacy

Company-context is **not part of this public package**. Keep it under your
organization's access controls. The validators in
`scripts/validate_vault.py` will flag inappropriate `sensitivity`
combinations on any pages they see, but the strongest protection is keeping
the data physically out of the public repo.
