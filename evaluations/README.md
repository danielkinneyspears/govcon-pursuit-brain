# Evaluations

Evaluations are the source of truth for whether a skill works. Because this
package is wiki-native, evaluations check four things beyond the domain answer:
the skill **creates the right entities**, **links them correctly**, **tags them**
(sensitivity, source, confidence, provenance), and **renders a faithful view**
from the entity graph.

## Structure

One file per skill, `evaluations/<skill-name>.md`, with at least three
scenarios.

**Fixtures and worked walkthroughs.** Synthetic, fictional pursuit material
that scenarios reference lives in two places, depending on scope:

- `examples/` — **end-to-end worked synthetic pursuits** (populated
  `pursuit.md`, entity pages, rendered views). The current example is
  `examples/syn-2026-r-0001/`. Use this when a scenario needs a realistic
  pursuit graph as its starting state.
- `evaluations/fixtures/` (created when needed) — **small per-eval inputs**
  that don't merit a full worked example: a stub solicitation excerpt, a
  candidate list, a synthetic competitor reference.

Fixtures and worked walkthroughs are always fictional — never real
solicitation, competitor, or proprietary data.

## Scenario format

```markdown
## Eval N — <short name>

**Scenario:** <a representative task, written as a user request>

**Inputs:** <files or context the skill is given>

**Expected behavior:**
- <observable, verifiable checks — including entity creation, links, tags, and view rendering>

**Anti-behavior:**
- <things the skill must NOT do>
```

## Running

There is no automated runner. Run a scenario with a fresh Claude session that
has the skill available, give it the scenario and inputs, and check the result
against the lists. For wiki-native skills, inspect the pursuit wiki the skill
produced: are the entity pages well-formed and tagged, are the `[[links]]`
correct, and does the rendered view match the entities. Record pass/fail.
