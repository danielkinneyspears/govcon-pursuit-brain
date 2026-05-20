# The Black Hat Method

How to build competitor entity pages, bid the job as each competitor, and render
the assessment view.

## Contents
- What a Black Hat is for
- The competitor entity page
- Bidding the job as a competitor
- The comparison matrix
- Most-probable-winner analysis
- Ghosting legitimately
- Recording the team's exposures
- Validation checklist

## What a Black Hat is for

A Black Hat answers one question: what will the team actually compete against?
Its output is a set of predicted offers concrete enough that win-strategy work
can be built to beat them. If the assessment does not change what the proposal
will say, it failed. In this package the assessment is a subgraph — competitor
entities linked to the customer, the team's exposures, and (later) the counter
themes.

## The competitor entity page

Each `entities/competitors/<name>.md` page follows the entity-page convention
and has these type-specific sections:

- **Summary** — two to four sentences: who they are and the one thing that most
  matters about them on this bid.
- **## Profile** — qualifications and fit (size, set-aside eligibility, vehicle
  holdings, clearances); relevant past performance; customer relationship and
  incumbency; typical technical approach; typical price posture; capacity and
  motivation; recent relevant wins and losses. Tag each item known or assessed.
- **## Assessed offer** — the "bid as them" result (below).
- **## Ghosting opportunity** — one real, evidence-based weakness, framed
  legitimately (below).
- **## Links** — to `customer/` hot buttons the competitor threatens, to
  `risks/` exposures it creates, and to the incumbent relationship.

Set the page `confidence` to the weakest claim the assessment relies on. A
competitor page built mostly from inference is `confidence: low`, and that
propagates into every view and decision that reads it.

## Bidding the job as a competitor

For the `## Assessed offer` section, drop the team's perspective and answer as
that competitor's capture lead:

1. Would we bid this, and how badly do we want it?
2. What solution would we propose, given our typical approach and partners?
3. What would our win themes be against this customer?
4. Where are we genuinely strong on this bid?
5. Where are we genuinely vulnerable for *this* requirement and *this* customer?
6. What price posture would we take, and why?

Give each competitor their best plausible bid. If the prediction makes a
competitor look foolish, it is wrong.

## The comparison matrix

The `competitive-assessment.md` view includes a matrix scoring each competitor
and the team across the factors the customer will evaluate (from the
`[[section-m]]` expectations). The matrix is *rendered from* the competitor
entities — it is a read-out, not a separate authored table. Factors where every
bidder scores alike are not discriminators; the win is decided where scores
spread.

## Most-probable-winner analysis

The view states who is most likely to win *today*, before the team's win
strategy is applied, and why — including, honestly, the cases where it is not
the team. The pursuit posture in `pursuit.md` frames this: an
`incumbent-defending` posture and a `challenger` posture start from very
different baselines. Overstating the team's position here guarantees a weak
strategy.

## Ghosting legitimately

A `## Ghosting opportunity` targets a real, evidence-based weakness in a
competitor's likely approach, framed as a positive, proven statement of the
team's strength so the evaluator draws the contrast. Proposal text names no
competitor and makes no unsupported negative claim. (The competitor *entity
page* may name the competitor — it is internal; the rendered proposal text
derived from it must not.) Illegitimate ghosting — unsupported claims,
disparagement, implied inside knowledge — is both an integrity problem and
unpersuasive; do not produce it.

## Recording the team's exposures

Run the Black Hat on the team itself: what will competitors ghost about the
team's likely bid? Record each exposure as its own `entities/risks/<slug>.md`
page, linked from the competitor entity that would exploit it. These risk
entities are real outputs — `developing-win-strategy` reads them and must give
each a response. An exposure known and unaddressed is the most predictable way
to lose.

## Validation checklist

```
- [ ] Each bidder has a competitor entity with all type-specific sections
- [ ] Each competitor was bid as themselves, with a best plausible offer (no strawmen)
- [ ] Every claim has a source tag or is marked assessed; page confidence is set honestly
- [ ] Only properly sourced information was used; nothing competitor-proprietary
- [ ] Ghosting opportunities target real weaknesses and are framed legitimately
- [ ] The team's exposures are recorded as risks/ entities, linked from competitors
- [ ] competitive-assessment.md is rendered from the entities, with the view header
- [ ] Most-probable-winner analysis is honest, including non-favorable cases
- [ ] pursuit.md entity index, view index, and change log updated
```
