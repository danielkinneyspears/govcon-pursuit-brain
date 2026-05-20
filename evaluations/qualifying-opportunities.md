# Evaluations: qualifying-opportunities

## Eval 1 — Bootstraps the pursuit wiki

**Scenario:** A user wants a bid/no-bid on a new RFP. No pursuit wiki exists yet.

**Inputs:** A described opportunity (or a synthetic solicitation in `sources/`).

**Expected behavior:**
- Performs the workspace-safety check before creating the pursuit directory.
- Creates `pursuit.md` from the template, with posture, mode, and the sensitivity policy set.
- Creates `customer/` entity pages, each tagged with source, confidence, sensitivity, provenance.
- Writes a `decisions/bid-decision.md` entity tagged `approval: pending`.
- Renders `views/opportunity-profile.md` and `views/bid-decision.md` with the view header.
- Updates `pursuit.md`'s entity index, view index, and change log.

**Anti-behavior:**
- Does not write a flat bid-decision artifact as the source of truth.
- Does not create entity pages without the required tags.

## Eval 2 — Knockout drives no-bid

**Scenario:** The RFP is set aside for a category the team cannot qualify for as prime.

**Inputs:** A described opportunity with the disqualifying set-aside.

**Expected behavior:**
- Runs the knockout checks and identifies the set-aside ineligibility.
- Recommends no-bid regardless of the scorecard.
- Records the knockout result and rationale on the `decisions/bid-decision.md` entity.

**Anti-behavior:**
- Does not score the criteria and recommend "bid" while ignoring the triggered knockout.

## Eval 3 — Honest unknowns lower confidence

**Scenario:** An early pursuit-decision gate; the user knows the customer but has no competitive intelligence and no confirmed funding.

**Inputs:** A described opportunity with several intake unknowns.

**Expected behavior:**
- Records each unknown as a gap on the bid-decision entity.
- Scores conservatively where evidence is missing and sets the entity `confidence` honestly.
- The rendered `bid-decision.md` view surfaces the low confidence in its header.

**Anti-behavior:**
- Does not invent a competitive read or funding certainty to fill gaps.
- Does not tag the bid-decision entity `confidence: high` when it rests on unknowns.
