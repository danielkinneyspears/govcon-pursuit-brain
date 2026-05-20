# Competitive Intelligence Ethics

What competitor information may be used in a federal competitive assessment, and
how the `sensitivity` tag enforces the line. Read this before any competitor
research.

## Contents
- The principle
- In bounds
- Out of bounds
- The sensitivity tag does the enforcing
- Handling questionable information

## The principle

Competitive intelligence in federal contracting is the analysis of *public and
legitimately available* information. It is forecasting, not espionage.
Information anyone could lawfully obtain is fair to analyze; information that is
non-public, proprietary, or source-selection-sensitive is not — regardless of
how it became available.

## In bounds

- Government award and contract data (public award notices, contract histories,
  spending data).
- Publicly available past-performance reputation.
- Public-facing competitor material — websites, press releases, capability
  statements, conference talks, job postings.
- Public market research and trade press.
- The team's own prior experience competing against the firm — the team's
  knowledge, not the competitor's protected information.
- General industry knowledge — cost-structure patterns, common methodologies,
  publicly known partnerships.

A competitor entity built from these is tagged `sensitivity: public`.

## Out of bounds

- A competitor's proprietary information — cost data, technical solutions,
  internal strategy, pricing models, unreleased proposal content — however
  obtained.
- Source-selection-sensitive information — anything non-public about the
  government's evaluation, the competitive range, other offerors' proposals or
  rankings, or the independent government cost estimate.
- Protected information from a competitor's current or former employees.
- Anything obtained through misrepresentation or covered by a confidentiality
  obligation.

## The sensitivity tag does the enforcing

This package does not need a separate "redaction" skill, because the
`sensitivity` tag on every entity page is the control:

- A competitor entity may only carry `sensitivity: public` (or
  `company-proprietary`, for the team's own internal analysis *of* the
  competitor).
- If information would make a page `sensitivity: competitor-proprietary` or
  `sensitivity: source-selection-sensitive`, it does not go on the page. Such
  material is **quarantined** — kept out of the pursuit wiki and out of model
  context — not summarized, not "used carefully."
- A skill that cannot build a competitor page without crossing into protected
  information stops and reports the gap. An intelligence gap is closed by better
  public research, never by improper information.

## Handling questionable information

If competitor information of uncertain provenance surfaces:

- Do not use it until its source is confirmed proper.
- If it appears proprietary or source-selection-sensitive, quarantine it and
  escalate to contracts or legal counsel.
- When a user supplies a competitor "fact" with an unclear source, ask where it
  came from before relying on it. Flag it; do not fold it in.

Improperly obtained information can disqualify a bid and carry criminal
liability. Rigorous analysis of legitimate information is both the ethical floor
and the only sound practice.
