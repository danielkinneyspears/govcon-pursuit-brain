# Contributing

This package improves through real pursuit work and through federal BD
practitioners correcting the domain knowledge. Read
[docs/architecture.md](docs/architecture.md) and the [`conventions/`](conventions/)
before contributing — this package is wiki-native, and the conventions are not
optional.

## Two kinds of contribution

1. **Domain knowledge** — corrections and additions to the domain wiki
   (`knowledge/`), or to a skill's federal-acquisition guidance.
2. **Skill behavior** — improvements to how a skill maintains the pursuit wiki
   or renders views, observed when Claude actually runs it.

Do not commit real solicitation text, real competitor data, or proprietary or
sensitive material. Use synthetic examples only.

## Authoring conventions

- **Skills** follow the same discipline as the sibling package
  `federal-proposal-skills`: gerund names (lowercase, hyphens); third-person,
  trigger-rich descriptions under 1024 characters; `SKILL.md` bodies under 500
  lines; numbered workflow checklists; intake questions before output;
  validation loops. The difference is that skills here **maintain entity pages
  and render views** rather than writing flat artifacts.
- **Entity pages** follow [conventions/entity-pages.md](conventions/entity-pages.md):
  the frontmatter schema, the body structure, and one-concept-per-page.
- **Wiki links** follow the `[[type/id]]` convention in
  [conventions/entity-pages.md](conventions/entity-pages.md). Links are typed
  where the relationship matters.
- **Tags** — every page carries the metadata in
  [conventions/tagging.md](conventions/tagging.md): `sensitivity`, `source`,
  `confidence`, `provenance`. These are load-bearing, not decoration.
- **Views** are rendered, never hand-authored as the source of truth. See
  [conventions/views.md](conventions/views.md).
- **The domain wiki** (`knowledge/`) is static, compiled federal-acquisition
  knowledge. New entity pages there follow `knowledge/_schema.md`.

## Evaluations

Each skill ships at least three evaluation scenarios under `evaluations/`. They
test wiki-native behavior — does the skill create the right entities, link them
correctly, tag them, and render a faithful view — using synthetic fixtures only.

## License

Contributions are accepted under the Apache 2.0 License (see [LICENSE](LICENSE)).
