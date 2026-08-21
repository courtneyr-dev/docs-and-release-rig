#!/usr/bin/env python3
"""Inventory documentation across a repository — not just /docs.

Read-only. Emits a machine-readable draft inventory (JSON or Markdown) with a
HEURISTIC content-type guess per file. The guess is a CANDIDATE FOR REVIEW, never
a verdict: it pattern-matches filenames and headings and cannot determine user
intent. Hand-verify every row against references/compass-and-classification.md.

Usage:
  inventory_docs.py [ROOT] [--json] [--include-hidden]
Exit codes: 0 ok · 2 bad usage.
"""
import argparse
import json
import os
import re
import sys

DOC_EXTS = {".md", ".markdown", ".rst", ".adoc", ".asciidoc", ".txt", ".mdx"}
TOOLING = {"mkdocs.yml", "conf.py", "docusaurus.config.js", "docusaurus.config.ts",
           "antora.yml", "hugo.toml", "hugo.yaml", "book.toml", "readthedocs.yml",
           ".readthedocs.yaml", "astro.config.mjs"}
CONTRIB = {"contributing", "testing", "deployment", "branching-strategy", "security",
           "code_of_conduct", "changelog", "history", "support", "maintainers"}

# (regex on lowercased "path + first heading", type, signal) — order = priority.
HEURISTICS = [
    (r"\b(tutorial|getting.?started|first.?steps|learn)\b", "tutorial?", "learning keyword"),
    (r"\b(quickstart|quick.?start|5.?minute)\b", "quickstart?", "quickstart keyword"),
    (r"\bhow.?to\b|/guides?/", "how-to?", "how-to keyword"),
    (r"\b(migrat|upgrade)\b", "migration?", "migration keyword"),
    (r"\b(troubleshoot|faq|common.?(errors|problems))\b", "troubleshooting/reference?", "problem keyword"),
    (r"\b(api|sdk|reference|cli|config(uration)?|endpoints?)\b", "reference?", "reference keyword"),
    (r"\b(architecture|design|concepts?|explanation|why|about|overview|rationale)\b", "explanation?", "concept keyword"),
    (r"\b(runbook|incident|on.?call)\b", "runbook?", "operational keyword"),
    (r"\bchangelog|release.?notes\b", "changelog?", "temporal keyword"),
]


def first_heading(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for _ in range(60):
                line = fh.readline()
                if not line:
                    break
                m = re.match(r"^\s{0,3}#{1,6}\s+(.*)$", line) or re.match(r"^(.+)\n[=-]{3,}\s*$", line)
                if m:
                    return m.group(1).strip()
    except OSError:
        pass
    return ""


def guess_type(rel, heading):
    hay = (rel + " " + heading).lower()
    matches = [(t, s) for pat, t, s in HEURISTICS if re.search(pat, hay)]
    if not matches:
        return "unknown", ""
    if len(matches) > 1:
        return "mixed? " + "/".join(t for t, _ in matches), "multiple signals — likely mixed; classify by section"
    return matches[0]


def main():
    ap = argparse.ArgumentParser(description="Inventory documentation (read-only, heuristic).")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--json", action="store_true", help="JSON output (default: Markdown table)")
    ap.add_argument("--include-hidden", action="store_true")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 2

    rows, tooling_found = [], []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames
                       if d not in {".git", "node_modules", "vendor", ".venv", "dist", "build", "__pycache__"}
                       and (args.include_hidden or not d.startswith("."))]
        for fn in filenames:
            if fn in TOOLING:
                tooling_found.append(os.path.relpath(os.path.join(dirpath, fn), root))
            ext = os.path.splitext(fn)[1].lower()
            if ext not in DOC_EXTS:
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root)
            heading = first_heading(full)
            stem = os.path.splitext(fn)[0].lower()
            if stem in CONTRIB:
                gtype, signal = "contributor/meta", "contributor or meta doc"
            else:
                gtype, signal = guess_type(rel, heading)
            try:
                mtime = os.path.getmtime(full)
            except OSError:
                mtime = 0
            rows.append({"path": rel, "title": heading or fn,
                         "type_guess": gtype, "signal": signal,
                         "last_modified": mtime, "owner": "", "accuracy": "", "notes": ""})

    rows.sort(key=lambda r: r["path"])
    if args.json:
        print(json.dumps({"root": root, "count": len(rows),
                          "docs_tooling_detected": sorted(set(tooling_found)),
                          "rows": rows}, indent=2))
    else:
        print(f"# Documentation inventory (draft) — {root}\n")
        print(f"_{len(rows)} files. Type guesses are HEURISTIC candidates — verify with the compass._\n")
        if tooling_found:
            print(f"**Docs tooling detected:** {', '.join(sorted(set(tooling_found)))}\n")
        print("| Path | Title | Type (guess) | Signal | Owner | Accuracy | Notes |")
        print("|---|---|---|---|---|---|---|")
        for r in rows:
            t = r["title"].replace("|", "\\|")
            print(f"| {r['path']} | {t} | {r['type_guess']} | {r['signal']} |  |  |  |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
