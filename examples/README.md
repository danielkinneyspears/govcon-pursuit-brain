# Examples

Synthetic, fictional pursuit walkthroughs showing the architecture in action.
Open these directly to see a populated `pursuit.md`, entity pages, and
rendered views. Use them as templates and as a sanity check on what the
skills are supposed to produce.

> [!warning] Synthetic only
> Every example uses **fictional** customers, competitors, contracts, and
> data. Nothing here describes a real procurement. The agency
> ("FSSA — Federal Synthetic Services Administration") and solicitation
> number ("SYN-2026-R-0001") do not exist.

## Current examples

- **[syn-2026-r-0001](syn-2026-r-0001/)** — *Public-only* worked example. A
  recompete for an IT service desk under a fictional federal agency,
  pursued **without** a configured `company_context_path`. Shows what the
  pursuit graph looks like when only public method + user intake are used.
  This is the floor; the architecture is genuinely useful at this level.

## Planned examples

- **`syn-2026-r-0001-customized`** — the same opportunity, pursued **with**
  a synthetic company-context configured. Shows how the same skills produce
  a tighter, better-grounded pursuit graph when the company-context layer
  is in place. The intent is a side-by-side: public-only vs. customized,
  same opportunity, different leverage.

## Reading the examples

- Start at the pursuit's `pursuit.md` — it lists the entities present and
  the rendered views.
- Follow the wiki-links. Every claim ties back to a source-register entry;
  every competitor links to its assessed offer; the bid-decision view is
  rendered from the bid-decision entity.
- Compare an entity page's `confidence` and `source` to its content — a
  synthetic example shows how to set both honestly.
