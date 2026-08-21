#!/usr/bin/env python3
"""Structural validator for the eval suite (schema, not behavior).

Eval schema and validator contract adapted from Romain Lespinasse's agent-skills
(MIT) — evals.json format and check-evals.js; re-implemented in Python with a
category field and file-existence checks added.

Checks evals.json is an array of objects with: unique non-empty `id`, non-empty
`prompt`, non-empty `expected_output`, non-empty `assertions[]`, non-empty `files[]`
whose paths exist relative to the skill root, and a `category` drawn from the known set.

Usage: check_evals.py [EVALS.json]
Exit codes: 0 valid · 1 invalid · 2 bad usage.
"""
import json
import os
import sys

CATEGORIES = {"activation", "classification", "writing", "audit", "architecture",
              "workflow", "safety", "evidence", "release", "ui", "security",
              "governance", "dx", "style", "diagrams", "localization",
              "adversarial", "regression", "packaging"}


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else \
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "evals.json")
    if not os.path.isfile(path):
        print(f"error: no such file: {path}", file=sys.stderr)
        return 2
    root = os.path.dirname(os.path.dirname(os.path.abspath(path)))

    try:
        evals = json.load(open(path, encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"  ❌ ERROR: invalid JSON: {e}")
        return 1
    if not isinstance(evals, list):
        print("  ❌ ERROR: evals.json must be a JSON array")
        return 1

    ok, ids = True, set()
    for i, e in enumerate(evals):
        if not isinstance(e, dict):
            print(f"  ❌ ERROR: eval[{i}] is not an object")
            ok = False
            continue
        missing = [f for f in ("id", "prompt", "expected_output") if not e.get(f)]
        if not isinstance(e.get("assertions"), list) or not e.get("assertions"):
            missing.append("assertions[]")
        if not isinstance(e.get("files"), list) or not e.get("files"):
            missing.append("files[]")
        if missing:
            print(f"  ❌ ERROR: eval[{i}] ({e.get('id','?')}) missing: {', '.join(missing)}")
            ok = False
        eid = e.get("id")
        if eid in ids:
            print(f"  ❌ ERROR: duplicate eval id: {eid}")
            ok = False
        if eid:
            ids.add(eid)
        cat = e.get("category")
        if cat and cat not in CATEGORIES:
            print(f"  ❌ ERROR: eval[{i}] ({eid}) unknown category: {cat}")
            ok = False
        for f in e.get("files") or []:
            if not os.path.exists(os.path.join(root, f)):
                print(f"  ❌ ERROR: eval {eid} references missing file: {f}")
                ok = False

    if not ok:
        return 1
    by_cat = {}
    for e in evals:
        by_cat[e.get("category", "uncategorized")] = by_cat.get(e.get("category", "uncategorized"), 0) + 1
    print(f"  ✅ {len(evals)} evals validated across {len(by_cat)} categories")
    for c in sorted(by_cat):
        print(f"     {c}: {by_cat[c]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
