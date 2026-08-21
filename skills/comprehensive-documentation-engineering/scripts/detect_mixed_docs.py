#!/usr/bin/env python3
"""Flag LIKELY mixed-purpose Markdown documents. Read-only, heuristic.

Scores each file for signals of each Diátaxis type. A file showing strong signals
for 2+ types is flagged as a CANDIDATE for splitting. This is a heuristic classifier:
it cannot determine user intent and MUST NOT be treated as a verdict. Every flag is a
prompt to apply the compass by hand (references/compass-and-classification.md).

Usage:
  detect_mixed_docs.py [ROOT] [--json] [--threshold N]
Exit codes: 0 ok (flags are informational) · 2 bad usage.
"""
import argparse
import glob
import json
import os
import re
import sys

SIGNALS = {
    "tutorial": [r"\bin this tutorial\b", r"\bwe(?:'|\s)?ll\b", r"\byou(?:'|\s)?ll (?:build|learn|create)\b",
                 r"\bnotice that\b", r"\bstep \d+\b", r"\bfirst,? (?:we|you)\b"],
    "how-to": [r"\bhow to\b", r"\bif you (?:want|need)\b.*\bdo\b", r"\bto (?:achieve|configure|deploy|enable)\b",
               r"\bprerequisites?\b", r"^\s*\d+\.\s", r"\brefer to the\b.*\breference\b"],
    "reference": [r"\|\s*parameter\s*\|", r"\|\s*type\s*\|", r"\breturns?\b", r"\bdefault:?\b",
                  r"\b(GET|POST|PUT|PATCH|DELETE)\s+/", r"\bmust (?:be|not)\b", r"\bsignature\b"],
    "explanation": [r"\bthe reason (?:for|why)\b", r"\bbecause\b", r"\btrade.?offs?\b", r"\bhistorically\b",
                    r"\bwhy (?:we|it|this)\b", r"\balternativ\w+\b", r"\bunderstanding\b"],
}


def score(text):
    low = text.lower()
    out = {}
    for typ, pats in SIGNALS.items():
        hits = sum(1 for p in pats if re.search(p, low, re.MULTILINE))
        out[typ] = hits
    return out


def main():
    ap = argparse.ArgumentParser(description="Flag likely mixed-purpose docs (heuristic, read-only).")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--threshold", type=int, default=2,
                    help="min signal-hits for a type to count as 'strong' (default 2)")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 2

    files = [f for ext in ("md", "markdown", "mdx")
             for f in glob.glob(os.path.join(root, "**", f"*.{ext}"), recursive=True)
             if os.sep + ".git" + os.sep not in f and "node_modules" not in f]

    flagged = []
    for f in files:
        try:
            with open(f, encoding="utf-8", errors="replace") as fh:
                sc = score(fh.read())
        except OSError:
            continue
        strong = [t for t, n in sc.items() if n >= args.threshold]
        if len(strong) >= 2:
            flagged.append({"path": os.path.relpath(f, root), "strong_types": sorted(strong), "scores": sc})

    flagged.sort(key=lambda r: (-len(r["strong_types"]), r["path"]))
    if args.json:
        print(json.dumps({"files_scanned": len(files), "threshold": args.threshold, "flagged": flagged}, indent=2))
    else:
        print(f"Scanned {len(files)} files. {len(flagged)} CANDIDATE mixed document(s) "
              f"(≥2 types scoring ≥{args.threshold}).")
        print("Heuristic only — confirm each with the compass; do not split mechanically.\n")
        for r in flagged:
            print(f"  {r['path']}: strong signals for {', '.join(r['strong_types'])}  {r['scores']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
