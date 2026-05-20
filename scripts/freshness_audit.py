#!/usr/bin/env python3
"""Flag entity pages whose next_review_due date has passed, plus pages whose
time-sensitive content lacks the freshness fields entirely.

Usage:
  python scripts/freshness_audit.py [--as-of YYYY-MM-DD] [path ...]

Without --as-of, today's date is used. If no paths are given, audits
`knowledge/` from the script's repo root.

Standard library only.
"""
import sys
import os
import re
import datetime
import argparse
from pathlib import Path


# Folders whose pages carry time-sensitive content. Pages here must have
# last_verified and next_review_due.
TIME_SENSITIVE_FOLDERS = {
    "vehicles",
    "thresholds-and-publicizing",
    "ai-and-emerging",
    "security-and-compliance",
    "small-business",
    "past-performance",
    "protests-and-debriefs",
    "task-orders",
    "cost-and-pricing",
}


FIELD_RE = re.compile(r"^(\w+):\s*(.+)$")


def parse_frontmatter_field(text, field):
    """Return the value of a top-level frontmatter field, or None."""
    m = re.match(r"^---\n(.*?\n)---\n", text, re.DOTALL)
    if not m:
        return None
    for line in m.group(1).splitlines():
        m2 = FIELD_RE.match(line)
        if m2 and m2.group(1) == field:
            return m2.group(2).strip()
    return None


def is_iso_date(s):
    try:
        return datetime.date.fromisoformat(s)
    except (ValueError, TypeError):
        return None


def audit(paths, as_of):
    findings = []
    pages_checked = 0
    for root in paths:
        for p in Path(root).rglob("*.md"):
            if p.name.startswith("_"):
                continue
            text = p.read_text(encoding="utf-8")
            pages_checked += 1
            folder = p.parent.name
            time_sensitive = folder in TIME_SENSITIVE_FOLDERS

            last_v = parse_frontmatter_field(text, "last_verified")
            next_due = parse_frontmatter_field(text, "next_review_due")

            if time_sensitive and (not last_v or not next_due):
                findings.append({
                    "path": str(p),
                    "kind": "missing-freshness-fields",
                    "detail": "time-sensitive page lacks last_verified / next_review_due",
                })
                continue

            if next_due:
                d = is_iso_date(next_due)
                if d is None:
                    findings.append({
                        "path": str(p),
                        "kind": "bad-date",
                        "detail": f"next_review_due '{next_due}' is not ISO date",
                    })
                elif d < as_of:
                    days = (as_of - d).days
                    findings.append({
                        "path": str(p),
                        "kind": "overdue",
                        "detail": f"next_review_due {next_due} is {days} days past as-of {as_of}",
                    })
    return findings, pages_checked


def main():
    parser = argparse.ArgumentParser(description="Freshness audit for the vault.")
    parser.add_argument("paths", nargs="*", default=["knowledge"],
                        help="paths to audit (default: knowledge)")
    parser.add_argument("--as-of", default=None,
                        help="as-of date (YYYY-MM-DD); defaults to today")
    args = parser.parse_args()

    if args.as_of:
        as_of = is_iso_date(args.as_of)
        if as_of is None:
            print(f"error: --as-of '{args.as_of}' is not ISO date", file=sys.stderr)
            return 2
    else:
        as_of = datetime.date.today()

    roots = [Path(p) for p in args.paths]
    for r in roots:
        if not r.exists():
            print(f"error: path does not exist: {r}", file=sys.stderr)
            return 2

    findings, count = audit(roots, as_of)

    print(f"audited {count} pages as of {as_of}")
    if not findings:
        print("OK — no freshness issues")
        return 0

    # Group by kind for legibility
    by_kind = {}
    for f in findings:
        by_kind.setdefault(f["kind"], []).append(f)
    for kind in sorted(by_kind):
        items = by_kind[kind]
        print(f"\n{kind}: {len(items)}")
        for f in items:
            print(f"  {f['path']}: {f['detail']}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
