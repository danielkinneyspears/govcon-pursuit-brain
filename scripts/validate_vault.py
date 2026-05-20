#!/usr/bin/env python3
"""Validate the domain wiki (and, optionally, a pursuit wiki) against the
package's conventions.

Checks for every entity page in `knowledge/` (and any path given as an arg):

- All required frontmatter fields present.
- `status`, `sensitivity`, `confidence` values are in the allowed enums.
- Date fields parse as ISO-8601 (YYYY-MM-DD).
- Domain-wiki pages carry `sensitivity: public` (sanity rule; flag otherwise).
- Wiki-link targets (`[[id]]` or `[[id|display]]`) resolve to a page id that
  exists in the vault.

Usage:
  python scripts/validate_vault.py [path ...]

If no paths are given, validates `knowledge/` from the script's repo root.
Exits 0 if the vault is clean; non-zero with a summary of findings otherwise.

Standard library only; no dependencies.
"""
import sys
import os
import re
import datetime
import argparse
from pathlib import Path


REQUIRED_FIELDS = [
    "id", "type", "title", "tags", "status", "sensitivity",
    "source", "confidence", "provenance",
    "last_verified", "next_review_due", "updated",
]

ALLOWED_STATUS = {"draft", "active", "stable", "verified", "superseded"}
ALLOWED_SENSITIVITY = {
    "public", "company-proprietary", "cui", "export-controlled",
    "classified", "source-selection-sensitive", "competitor-proprietary",
}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}

# Files that are not entity pages and are exempt from the per-page checks.
# Wiki-link integrity is still checked on these files; only the entity-page
# frontmatter schema is skipped.
# SKILL.md follows the Anthropic Agent Skills schema (name + description,
# optional fields), not the wiki entity-page schema.
INDEX_FILES = {
    "_index.md", "_schema.md", "_source-policy.md",
    "README.md", "pursuit.md", "SKILL.md",
}

# Directories whose contents are not entity pages:
#   sources/    — raw source documents (the solicitation, debrief, etc.)
#   views/      — rendered views (have a view header, not entity frontmatter)
#   references/ — skill-bundled reference docs (Anthropic Skills spec)
#   templates/  — skill-bundled output templates (Anthropic Skills spec)
NON_ENTITY_DIRS = {"sources", "views", "references", "templates"}


def parse_frontmatter(text):
    """Return a dict of the YAML frontmatter fields (string values), or None
    if the file has no frontmatter."""
    m = re.match(r"^---\n(.*?\n)---\n", text, re.DOTALL)
    if not m:
        return None
    body = m.group(1)
    fields = {}
    current_key = None
    for line in body.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - "):
            # list item belonging to the previous key
            if current_key is not None:
                fields.setdefault(current_key + "_list", []).append(line[4:].strip())
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            fields[key] = value
            current_key = key
    return fields


def is_non_entity_path(path):
    """True if any directory in the path is a NON_ENTITY_DIRS."""
    return any(part in NON_ENTITY_DIRS for part in path.parts)


def collect_pages(roots):
    """Return list of (path, kind) tuples. kind is 'entity' or 'index'."""
    pages = []
    for root in roots:
        for p in Path(root).rglob("*.md"):
            if p.name in INDEX_FILES or is_non_entity_path(p):
                pages.append((p, "index"))
            else:
                pages.append((p, "entity"))
    return pages


def collect_ids(pages):
    """Map id -> path for every entity page that declares an id."""
    ids = {}
    for path, kind in pages:
        if kind != "entity":
            continue
        # id defaults to filename stem
        ids[path.stem] = path
    return ids


WIKI_LINK_RE = re.compile(r"\[\[([a-z][a-z0-9-]*)(?:\|[^\]]*)?\]\]")


def find_wiki_links(text):
    return [m.group(1) for m in WIKI_LINK_RE.finditer(text)]


def is_iso_date(s):
    try:
        datetime.date.fromisoformat(s)
        return True
    except (ValueError, TypeError):
        return False


def validate(paths):
    pages = collect_pages(paths)
    ids = collect_ids(pages)
    errors = []
    warnings = []

    for path, kind in pages:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{path}: cannot read: {exc}")
            continue

        # Wiki-link integrity (run on every page, including indexes)
        for target in find_wiki_links(text):
            if target == "id":
                continue  # schema example
            if target not in ids:
                errors.append(f"{path}: broken wiki-link [[{target}]]")

        if kind == "index":
            continue

        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{path}: missing YAML frontmatter")
            continue

        for field in REQUIRED_FIELDS:
            if field == "tags":
                if "tags_list" not in fm and not fm.get("tags"):
                    errors.append(f"{path}: required field 'tags' missing or empty")
            elif field not in fm:
                errors.append(f"{path}: required field '{field}' missing")

        status = fm.get("status", "")
        if status and status not in ALLOWED_STATUS:
            errors.append(f"{path}: status '{status}' not in {sorted(ALLOWED_STATUS)}")

        sensitivity = fm.get("sensitivity", "")
        if sensitivity and sensitivity not in ALLOWED_SENSITIVITY:
            errors.append(f"{path}: sensitivity '{sensitivity}' not in allowed set")

        confidence = fm.get("confidence", "")
        if confidence and confidence not in ALLOWED_CONFIDENCE:
            errors.append(f"{path}: confidence '{confidence}' not in {sorted(ALLOWED_CONFIDENCE)}")

        # Domain-wiki sanity: pages under knowledge/ should be sensitivity: public
        if any(part == "knowledge" for part in path.parts):
            if sensitivity and sensitivity != "public":
                warnings.append(
                    f"{path}: domain-wiki page with non-public sensitivity '{sensitivity}'")

        for date_field in ("last_verified", "next_review_due", "updated"):
            v = fm.get(date_field, "")
            if v and not is_iso_date(v):
                errors.append(f"{path}: {date_field} '{v}' is not ISO date YYYY-MM-DD")

        fm_id = fm.get("id", "")
        if fm_id and fm_id != path.stem:
            errors.append(f"{path}: frontmatter id '{fm_id}' does not match filename")

    return errors, warnings, len(pages)


def main():
    parser = argparse.ArgumentParser(description="Validate the vault.")
    parser.add_argument("paths", nargs="*", default=["knowledge"],
                        help="paths to validate (default: knowledge)")
    args = parser.parse_args()
    roots = [Path(p) for p in args.paths]
    for r in roots:
        if not r.exists():
            print(f"error: path does not exist: {r}", file=sys.stderr)
            return 2

    errors, warnings, count = validate(roots)

    print(f"validated {count} files across {[str(r) for r in roots]}")
    if warnings:
        print(f"\n{len(warnings)} warnings:")
        for w in warnings:
            print(f"  WARN: {w}")
    if errors:
        print(f"\n{len(errors)} errors:")
        for e in errors:
            print(f"  ERR:  {e}")
        return 1
    print("\nOK — no errors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
