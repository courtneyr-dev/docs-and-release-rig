#!/usr/bin/env python3
"""Compare control labels named in documentation against labels observed in the UI.

Read-only. Takes (a) a Markdown doc and (b) a JSON file of observed UI labels — the
accessibility-tree dump from the probe-first step in workflows/verify-ui.md — and
reports which documented control names do NOT appear in the running interface.

This tool does NOT drive a browser: capture the accessibility tree with whatever
automation the environment provides, save it as JSON, then run this. It cannot know
which quoted strings in a doc are control names, so it extracts CANDIDATES (bolded
text, `code` spans, and quoted strings) — every flag is a candidate for review.

Observed-labels JSON: either a list of strings, or a list of objects with a "name"
(and optional "role"/"path") key — the common accessibility-tree shapes.

Usage:
  compare_ui_labels.py DOC.md OBSERVED.json [--json]
Exit codes: 0 no unmatched candidates · 1 unmatched candidates found · 2 bad usage.
"""
import argparse
import json
import os
import re
import sys

BOLD = re.compile(r"\*\*([^*\n]{2,60})\*\*")
CODE = re.compile(r"`([^`\n]{2,60})`")
QUOTED = re.compile(r"[\"“]([A-Z][^\"”\n]{1,58})[\"”]")
MENU_PATH = re.compile(r"\*\*([^*\n]{2,80}?\s*>\s*[^*\n]{2,80})\*\*")


def norm(s):
    return re.sub(r"\s+", " ", s.strip().lower().strip(".:")).strip()


def load_observed(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    labels = []
    def walk(node):
        if isinstance(node, str):
            labels.append(node)
        elif isinstance(node, dict):
            for key in ("name", "label", "title", "text"):
                if isinstance(node.get(key), str):
                    labels.append(node[key])
            for v in node.values():
                if isinstance(v, (list, dict)):
                    walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)
    walk(data)
    return labels


def main():
    ap = argparse.ArgumentParser(description="Diff documented control labels against observed UI labels.")
    ap.add_argument("doc")
    ap.add_argument("observed", help="JSON accessibility-tree dump or list of label strings")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    for p in (args.doc, args.observed):
        if not os.path.isfile(p):
            print(f"error: no such file: {p}", file=sys.stderr)
            return 2

    text = open(args.doc, encoding="utf-8", errors="replace").read()
    candidates = {}
    for rx, kind in ((MENU_PATH, "menu path"), (BOLD, "bold (UI element)"),
                     (CODE, "code span"), (QUOTED, "quoted label")):
        for m in rx.finditer(text):
            raw = m.group(1).strip()
            candidates.setdefault(norm(raw), {"raw": raw, "kind": kind})

    observed = load_observed(args.observed)
    obs_norm = {norm(o) for o in observed if o and o.strip()}

    matched, unmatched = [], []
    for key, info in sorted(candidates.items()):
        # menu paths match if every segment is observed
        segs = [norm(s) for s in re.split(r">", info["raw"])] if ">" in info["raw"] else [key]
        hit = all(any(seg == o or (len(seg) > 3 and seg in o) for o in obs_norm) for seg in segs)
        (matched if hit else unmatched).append(info | {"key": key})

    result = {"doc": args.doc, "observed_labels": len(obs_norm),
              "candidates": len(candidates), "matched": len(matched),
              "unmatched": unmatched}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{args.doc}: {len(candidates)} label candidate(s) vs {len(obs_norm)} observed UI label(s).")
        print(f"  matched: {len(matched)}   unmatched: {len(unmatched)}\n")
        if unmatched:
            print("Unmatched candidates (CANDIDATES FOR REVIEW — not all are control names):")
            for u in unmatched:
                print(f"  [{u['kind']}] {u['raw']!r}")
            print("\nFor each real control name here, the doc may name a control that does not exist "
                  "under that label. Record in templates/ui-label-diff.md.")
        else:
            print("Every label candidate has a match in the observed UI.")
    return 1 if unmatched else 0


if __name__ == "__main__":
    sys.exit(main())
