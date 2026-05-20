# Changelog

All notable changes to this package are documented here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/); versions follow semantic versioning.

## [0.2.4] — unreleased

Internal-review cleanup. Four small fixes from a cross-package audit.

### Fixed
- **`.gitignore` now excludes `.obsidian/`.** Obsidian creates user-local
  vault state (workspace, plugin settings, graph layout) under
  `knowledge/.obsidian/`. That directory is now git-ignored so it does
  not leak on first push.
- **`scripts/validate_vault.py` exempts SKILL.md and the `references/`
  / `templates/` directories** from the entity-page schema check.
  SKILL.md follows the Anthropic Agent Skills schema (name + description,
  optional fields), not the wiki entity-page schema; skill-bundled
  `references/` and `templates/` files are not entity pages. Wiki-link
  integrity is still verified across those files. Running the validator
  across the whole repo (`validate_vault.py knowledge playbooks examples
  skills`) is now clean: **114 files, 0 errors**.
- **`knowledge/_index.md`** now links `_source-policy.md` from the intro,
  alongside `_schema.md`. The authority ladder is part of the trust
  layer and should be discoverable from the MOC.
- **`evaluations/README.md`** reconciles the fixture story. End-to-end
  worked synthetic pursuits live in `examples/` (e.g.,
  `examples/syn-2026-r-0001/`); small per-eval inputs go in
  `evaluations/fixtures/` (created on first use). The prior README
  claimed a fixtures directory that did not exist.

## [0.2.3] — unreleased

Taxonomy release. Reframes the package's vocabulary to lead with **universal
pursuit-job names** ("competitive intelligence," "compliance tracing") and
treat GovCon-specific names ("Black Hat," "Pink Team") as aliases. The point
is **discoverability without making users learn the package's jargon**.

### Added — the lifecycle taxonomy
- **`docs/lifecycle-taxonomy.md`** — the master translation table. Defines
  the **three-phase elemental layer** (**Plan / Create / Iterate**) and
  enumerates **36 canonical jobs** across them, each with:
  - **Canonical job** (kebab-case id used internally)
  - **Common names** (the aliases your shop probably uses)
  - **User goal** (what a human is trying to accomplish)
  - **Primary outputs** (the entity pages or views the job produces)
  - **Owning skills** (this package's skills that perform the job; most
    marked **planned** in v0.2.x — the taxonomy is the roadmap).
- The taxonomy explicitly declares the package's **two abstraction layers**:
  an elemental layer (universal jobs + aliases) and a GovCon method layer
  (Shipley terms, color teams, Section L/M/C, FAR mechanics). Both matter;
  the elemental layer makes the package pluggable across companies, the
  method layer keeps the rigor that wins against real evaluation boards.

### Changed — architecture and README
- **`docs/architecture.md`** opens with a new "Two abstraction layers"
  section pointing to the taxonomy as the translation surface.
- **`README.md`** now leads (after the status) with a "The work, in
  universal terms — Plan, Create, Iterate" section: a compact 3-row table
  showing the canonical jobs by phase, and a pointer to the full taxonomy.

### Changed — skill frontmatter
Both proof skills now declare their canonical job, phase, and common names
in YAML frontmatter, so a search by any common name resolves to the right
skill:

- `qualifying-opportunities` → `canonical_job: opportunity-qualification`,
  `phase: plan`, common names *bid/no-bid, gate review, go/no-go, pursuit
  decision, opportunity qualification, sizing, pursuit gate*.
- `analyzing-competitors` → `canonical_job: competitive-intelligence`,
  `phase: plan`, common names *Black Hat, competitor analysis, market
  intelligence, market intel, incumbent assessment, competitive assessment,
  recompete analysis*.

Skill files added beyond v0.2.x follow the same convention; the taxonomy
doc is the source of truth for the canonical-job vocabulary.

### Not yet
- The 34 canonical jobs without owning skills today remain the planned
  build. The taxonomy doc is also the **roadmap** in this sense: each
  "planned" row is a skill to build.
- The customized synthetic example, the sibling package's parallel
  vocabulary update, and posture-branching across all skills remain open
  from prior reviews.

## [0.2.2] — unreleased

Positioning + customization release. Addresses an external strategic-framing
review that flagged the **40% public method / 60% private company context**
split. Reframes the package as the **public GovCon pursuit method layer**,
not a "company brain," and adds the scaffolding for organizations to pair
the public method with their own private context.

### Added — customization framing
- **`docs/customize-for-your-company.md`** — the 40/60 split, what stays
  public vs. private, how skills layer private company-context on top of
  the public method, naming guidance ("Customize for Your Company,"
  **not** "company brain"), and the recommended adoption path. Explicitly
  states what the package **is not** (system of record, replacement for
  CRM/SharePoint/proposal-management SaaS).
- **`schema/company-context.template.md`** — the per-folder schema for a
  private `company-context/` workspace (`customers/`, `past-performance/`,
  `key-personnel/`, `partners/`, `pricing-guidance/`, `compliance-posture/`,
  `debrief-lessons/`, `approved-proof-points/`). To be copied into the
  user's **private** repository or controlled workspace; not populated
  inside this public package.
- **README** opens with the framing ("public GovCon pursuit method layer")
  and adds a "Customize for Your Company" section.

### Added — new pursuit entity types
Nine new entity types added to the pursuit-wiki schema and architecture
doc, all of which surface the things capture and proposal people actually
care about that do not live in clean artifacts:

- `relationship-map/` — "who really decides and who trusts whom."
- `incumbent-pain/` — identified customer pain with the incumbent.
- `capture-momentum/` — weekly snapshots of whether the pursuit has real
  traction or is just words.
- `decision-politics/` — team-side and customer-side decision politics.
- `team-capacity/` — bench, bandwidth, skills available for this bid.
- `proof-points/` — reusable validated claim + evidence pairs (these
  promote into `company-context/approved-proof-points/` over time).
- `pricing-reality/` — what the team can actually bid, given internal
  constraints (distinct from price-to-win analysis).
- `amendment-impact/` — per-amendment blast-radius analysis.
- `review-closure/` — per-finding closure record (verified, re-opened,
  deferred).

Both `docs/architecture.md` and `schema/pursuit-schema.template.md`
updated. The pursuit-schema also adds `company_context_path:` and
`company_context_use:` fields so a per-pursuit configuration can tell
skills whether to layer in the private context.

### Changed — proof skills layer company-context and emit claims/sources
- **`qualifying-opportunities`** — Step 1 now reads any configured
  `company_context_path:` before intake; intake skips questions company-
  context already answers and cites the company-context page as the
  `source:` on resulting entities. Step 6 now emits supporting
  `entities/claims/` (assertable facts the bid decision rests on) and
  `entities/source-register/` (the external sources backing those claims)
  in addition to the bid-decision entity itself.
- **`analyzing-competitors`** — Step 1 reads company-context (`partners/`,
  `debrief-lessons/`, `customers/<this-agency>/`) before competitor
  research. New Step 6 emits claims and source-register entries for the
  competitor reads. Both skills carry guardrails that **company-context is
  referenced, never copied**, and that resulting pursuit entities carry
  `sensitivity: company-proprietary` where the underlying fact came from
  company-context.

### Added — synthetic example
- **`examples/syn-2026-r-0001/`** — a worked, public-only synthetic
  pursuit (the fictional FSSA Enterprise IT Service Desk Recompete) with a
  populated `pursuit.md`, customer entity, incumbent competitor entity, a
  bid-decision entity (conditional bid), a supporting claim, a
  source-register entry, and a rendered bid-decision view. Shows the
  architecture working end to end at the public-method-only level.
- `examples/README.md` — names a planned **customized variant**
  (`syn-2026-r-0001-customized`) that will show the same opportunity with
  a synthetic `company-context/` configured, for side-by-side comparison.

### Changed — validator
- `scripts/validate_vault.py` exempts `README.md` and `pursuit.md`, plus
  any file under `sources/` or `views/` directories, from the entity-page
  frontmatter schema check. Wiki-link integrity is still verified on
  those files. Validator now clean across `knowledge/` + `playbooks/` +
  `examples/` (109 files, 0 errors).

### Not yet
- Claim and source-register **skills** (skills that systematically build
  and curate these entity types) are still planned; v0.2.2 wires the
  pattern into the two existing proof skills.
- The **customized** synthetic example (same opportunity with company-
  context layered on) is named as planned, not yet built.
- The full lifecycle skill set (shred, amendment impact, SME data-call,
  proposal-management, etc.) ported to the wiki-native architecture
  remains the major roadmap item.

## [0.2.1] — unreleased

Trust-layer release. Addresses an external skill-architecture and GovCon
practitioner review that flagged unenforced trust metadata, two factual
errors, and the need for governance scaffolding (validators, freshness
gates, source policy, claim ledger, role playbooks).

### Fixed (factual)
- **Alliant 3 contract ceiling.** GSA's official Alliant 3 page lists **no
  ceiling**; the prior page incorrectly stated $75 billion (a figure that
  appeared in trade-press reporting during source selection). Corrected.
- **CMMC Level 1.** Aligned to the 32 CFR Part 170 final rule's **15
  requirements** from FAR 52.204-21 (three physical-protection practices
  consolidated into one). The prior page's "17 practices" reflected an
  earlier CMMC Level 1 Assessment Guide pre-consolidation.

### Trust layer (enforced)
- **`provenance`, `last_verified`, `next_review_due`** frontmatter fields
  added to all 93 entity pages. Time-sensitive categories carry a 90-day
  review cadence; durable structural pages carry a 365-day cadence.
- **`status: stable`** formally defined in `conventions/tagging.md` as
  "compiled from authoritative public sources, internally consistent, not
  yet human-verified or source-confirmed." Explicit `verified` and
  `superseded` transitions documented. The `stable` → `verified` upgrade
  path now has a clear meaning.
- **`knowledge/_source-policy.md`** — the authority ladder: the
  solicitation > statute > FAR + agency supplement > other CFR > official
  agency pages > OMB memos > NIST > GAO/COFC decisions > public award data >
  trade press > common practice > this wiki. Every page's `source` should
  cite the highest rung it rests on.

### Added — validators
- **`scripts/validate_vault.py`** — checks every entity page for required
  frontmatter fields, enum compliance (status, sensitivity, confidence),
  date-format validity, frontmatter-id-to-filename match, broken wiki-link
  targets, and a sanity rule that domain-wiki pages carry
  `sensitivity: public`.
- **`scripts/freshness_audit.py`** — flags pages whose `next_review_due` is
  past, plus time-sensitive pages missing the freshness fields entirely.
  Supports an `--as-of` date for what-if checks.
- Vault status: validator clean across `knowledge/` + `playbooks/` (100
  files; 0 errors; 0 warnings).

### Added — claims and source register
- `docs/architecture.md` updated to introduce two pursuit-wiki entity
  types: **`claims/`** (assertable claims with source, owner, use, and
  status) and **`source-register/`** (external sources backing claims, with
  authority, directness, recency, independence). Together they make
  pursuit evidence traceable: every claim links to its sources, and every
  source links back to the claims it supports.
- `schema/pursuit-schema.template.md` updated with both new entity-type
  rows in the entity index.

### Added — role playbooks
- **`playbooks/`** — role and scenario guides that turn the knowledge graph
  into an operating system for specific people.
  - `playbooks/capture-manager.md` — gate-by-gate, with explicit posture
    branching.
  - `playbooks/proposal-manager.md` — kickoff through submission, including
    backward scheduling, the question/amendment loop, and recovery
    discipline.
  - `playbooks/sme-data-call.md` — the "20-minute SME mode" the reviewer
    asked for: eight plain-language questions, with proposal-team
    translation of answers into entities, and a technical-accuracy review
    loop back to the SME.

### Fixed (page)
- `knowledge/cost-and-pricing/igce.md` — the *concept page* about IGCE is
  `sensitivity: public` (it contains only public information about what an
  IGCE is); the warning clarifies that *actual IGCE documents* in a
  pursuit are `sensitivity: source-selection-sensitive`.

### Not yet
- The claim and source-register entity types are defined; the skills that
  create and maintain them are planned, not built.
- Posture branching across all skills (incumbent vs. challenger) is
  documented in the playbooks but not yet enforced in skill workflows.
- Synthetic end-to-end pursuit example (the reviewer's `examples/`) is
  planned.
- The full lifecycle skill set (shred, amendment impact, SME data-call
  skill, etc.) remains the roadmap item.

## [0.2.0] — unreleased

Domain-wiki expansion. Turns the starter knowledge base into a comprehensive,
Obsidian-compatible GovCon vault, sourced against the FAR, CFR, SBA
regulations, NIST publications, and current OMB memos.

### Added
- **93 entity pages** in `knowledge/`, organized into 17 category folders
  (acquisition-regulations, solicitation-structure, source-selection,
  task-orders, contract-types, vehicles, small-business, past-performance,
  cost-and-pricing, capture-and-bd, proposal-craft, special-clauses,
  integrity-and-ethics, protests-and-debriefs, security-and-compliance,
  ai-and-emerging, thresholds-and-publicizing).
- **Obsidian-compatible vault** — the `knowledge/` directory opens directly
  in Obsidian; YAML frontmatter `tags:`, `[[wiki-link]]` references, folder
  organization, and `> [!warning]` / `> [!note]` callouts all work natively.
- `_index.md` — a Map of Content (MOC) listing every page by category, with
  tag conventions documented at the bottom.
- Updated `_schema.md` and `conventions/entity-pages.md` to document the
  vault structure, folder layout, tag conventions, and callout patterns.

### Current accuracy notes (as of 2026-05-19)
- Acquisition thresholds: micro-purchase $15,000, simplified acquisition
  $350,000 (effective October 1, 2025).
- Truthful Cost or Pricing Data (formerly TINA) threshold: $10,000,000 for
  contracts entered after June 30, 2026 (2026 NDAA § 1804).
- OMB AI memos: M-25-21 (use) and M-25-22 (acquisition), issued April 3, 2025,
  replaced M-24-10 and M-24-18.
- CMMC 2.0 Program Rule effective December 2024; Level 2 self-assessments
  required since November 10, 2025; third-party assessments phase in from
  November 2026.
- NIST SP 800-171 Rev. 3 finalized May 14, 2024; Rev. 2 still controls under
  current CMMC requirements pending DoD rulemaking.
- FedRAMP transitioning to lettered Certification Classes A–D under NTC-0004
  (Feb 2026) / CR26 (mid-2026); "Authorization" terminology replacing with
  "Certification."
- IT GWAC landscape: Alliant 3 Phase I NTP issued March 10, 2026 ($75B
  ceiling); OASIS+ Phase II rolling awards from May 2026; Polaris pools
  awarding through FY2026; SEWP VI delayed to mid-2026 (147 → ~1,000
  primes); **CIO-SP4 cancelled** by NITAAC; GSA consolidating major IT
  vehicles.
- SBA Mentor-Protégé final rule effective January 16, 2025: reduced
  past-performance requirement for protégé joint-venture partners; protégé
  must perform ≥40% of JV work.
- SBA program-specific set-asides (8(a), SDVOSB, WOSB/EDWOSB, HUBZone) all
  require active SBA-issued certification; self-certification no longer
  accepted.

### Planned
- The remaining lifecycle skills, ported to the wiki-native architecture,
  to reach parity with the sibling package `federal-proposal-skills`.

## [0.1.0] — unreleased

Initial build — architecture and proof slice.

### Added
- Repository scaffold: Claude Code plugin manifest, marketplace manifest,
  license, contributing guide.
- `docs/architecture.md` — the three-layer LLM Wiki architecture for federal
  pursuits: raw sources, the domain and pursuit wikis, and the schemas.
- `conventions/` — entity page format, tagging (sensitivity, source, confidence,
  provenance, approval), and view rendering.
- `knowledge/` — the starter domain wiki: a schema and a set of interlinked
  federal-acquisition entity pages.
- `schema/pursuit-schema.template.md` — the Layer 3 template for a new pursuit
  wiki.
- Two proof skills: `qualifying-opportunities` (bootstraps a pursuit wiki and
  its first entities) and `analyzing-competitors` (maintains a rich competitor
  entity subgraph).
- `evaluations/` — evaluation conventions and scenarios for the proof skills.

### Planned
- The remaining lifecycle skills, ported to the wiki-native architecture, to
  reach parity with the sibling package `federal-proposal-skills`.
