---
tags:
  - policy
---

# Domain Wiki — Source Policy

The **authority ladder** for any factual claim in this vault. When sources
disagree, the higher rung wins. The `source` field on every page should cite
the highest-available rung that supports the claim; `confidence` reflects how
firmly the claim rests on that source.

> [!warning] Most important rule
> When a specific solicitation contradicts anything in this wiki, the
> **solicitation governs**. The wiki is orienting background.

## The ladder (highest → lowest)

| Rung | Source type | Examples | Notes |
|---|---|---|---|
| 1 | **The specific solicitation** | The RFP, RFI, sources-sought notice, draft RFP, amendments, Q&A for the pursuit | Section L governs the proposal. Always. |
| 2 | **Statute** | U.S. Code (10 U.S.C., 41 U.S.C., 5 U.S.C., 28 U.S.C., etc.); annual NDAA | Authoritative; trumps regulation when in conflict. |
| 3 | **The FAR and the applicable agency supplement** | 48 CFR Chapter 1 (FAR) at [acquisition.gov/far](https://www.acquisition.gov/far); DFARS (DoD), HHSAR, AGAR, DEARS/DOEAR, AFFARS, etc. | The default regulatory authority for federal acquisition. The supplement controls where it adds requirements. |
| 4 | **Other CFR text** | 13 CFR (SBA programs), 32 CFR (e.g., CMMC), 22 CFR (ITAR), 15 CFR (EAR), 48 CFR (FAR & supplements) at [ecfr.gov](https://www.ecfr.gov/) | Cite the eCFR for the current text. |
| 5 | **Official agency program pages and final rules** | GSA program pages (Alliant 3, OASIS+, Polaris, MAS); DoD CIO CMMC; SBA program pages; NARA CUI Registry; CPARS.gov; SAM.gov | The agency's own current page beats secondary reporting. Confirm the URL still resolves and the date stamp is current. |
| 6 | **OMB memos and circulars** | M-25-21, M-25-22, A-130 | Cite the WhiteHouse.gov copy when available. |
| 7 | **NIST publications** | SP 800-171, SP 800-53, AI RMF, NIST AI 600-1 (GenAI Profile) | Cite the published version with revision. |
| 8 | **GAO and COFC decisions** | GAO bid-protest decisions; COFC opinions | Authoritative for protest precedent; not for procurement policy generally. |
| 9 | **Public award and contract data** | USAspending API, SAM.gov contract opportunities and awards, CPARS (where the team has access) | Strong for what was bought, by whom, at what value; weaker for evaluation reasoning. |
| 10 | **Trade press, law-firm bulletins, training providers** | Federal News Network, Washington Technology, NextGov, Bloomberg Government, Shipley, APMP, Wiley, Crowell, Holland & Knight | Useful for orientation and current-state reporting; **always verify against the primary source** before relying. |
| 11 | **Common practice** | Shipley capture lifecycle, color-team naming and timing, win-theme construction | Defensible domain practice; not regulatory authority. |
| 12 | **This wiki** | These pages | Orienting reference. Pages in `status: stable` are compiled from public sources, not human-verified; treat accordingly. |

## How to apply the ladder

- A **page citing only a higher rung** (1–4) is high-confidence. A page that
  must rely on rung 10 or 11 should be tagged `confidence: medium` at best.
- A **claim that depends on common practice or secondary reporting alone**
  must say so. Never present trade-press reporting as authority.
- When primary sources conflict (e.g., the FAR text and an agency supplement),
  the **supplement controls within the agency's scope**.
- When this wiki and a specific solicitation conflict, the **solicitation
  controls**. Always.

## Verification expectation

For any **deadline-sensitive, threshold-sensitive, or legally adjacent**
claim — debrief windows, late-proposal rules, size standards, thresholds,
certifications, vehicle status, protest timelines — verify against the
**current primary source** at rung 3, 4, 5, 6, or 7 before relying on a wiki
page. Then update the page's `last_verified` date and (if upgraded) its
`status` from `stable` to `verified`.

## A note on currency

Pages in this wiki carry **`last_verified`** and **`next_review_due`** fields
in their frontmatter (see [../conventions/tagging.md](../conventions/tagging.md)).
The `scripts/freshness-audit` tool flags pages whose review is overdue, with
priority on time-sensitive categories (vehicles, thresholds, security and
compliance, AI memos, small-business certifications, protest timing).
