#!/usr/bin/env python3
"""Check local (relative) Markdown links and heading anchors. Read-only.

Verifies that relative links and in-page/anchor targets resolve on disk. Does NOT
make network requests by default (a link checker that hits the network is slow and
flaky in CI) — external URLs are listed as 'skipped (external)'. For handoff link
hygiene (public-URL-resolves-logged-out), verify those manually or with curl per
workflows/security-audit-handoff.md.

Usage:
  check_links.py [ROOT] [--json]
Exit codes: 0 no broken local links · 1 broken local links found · 2 bad usage.
"""
import argparse
import glob
import json
import os
import re
import sys

LINK_RE = re.compile(r"\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.*)$")


def slug(text):
    # Match GitHub's heading-anchor slugifier: lowercase, strip punctuation
    # (keeping word chars, whitespace, hyphens), then replace EACH whitespace
    # char with a hyphen WITHOUT collapsing runs — so "## 1 · Prompts" → "1--prompts"
    # (the dropped "·" leaves two spaces → two hyphens), as GitHub renders it.
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s", "-", s).strip("-")


def anchors_for(path):
    out = set()
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                m = HEADING_RE.match(line)
                if m:
                    out.add(slug(m.group(1)))
    except OSError:
        pass
    return out


def main():
    ap = argparse.ArgumentParser(description="Check local Markdown links/anchors (read-only).")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 2

    files = [f for ext in ("md", "markdown", "mdx")
             for f in glob.glob(os.path.join(root, "**", f"*.{ext}"), recursive=True)
             if os.sep + ".git" + os.sep not in f and "node_modules" not in f]

    anchor_cache, broken, external, checked = {}, [], 0, 0
    for f in files:
        try:
            with open(f, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            continue
        for target in LINK_RE.findall(text):
            if target in ("#", ""):  # bare placeholder anchor ([text](#)) — "fill in later"
                continue
            if target.startswith("#"):  # in-page anchor
                checked += 1
                anchor_cache.setdefault(f, anchors_for(f))
                if slug(target[1:]) not in anchor_cache[f]:
                    broken.append({"file": os.path.relpath(f, root), "link": target, "reason": "no such heading anchor"})
                continue
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
                external += 1
                continue
            checked += 1
            path_part, _, frag = target.partition("#")
            dest = os.path.normpath(os.path.join(os.path.dirname(f), path_part)) if path_part else f
            if not os.path.exists(dest):
                broken.append({"file": os.path.relpath(f, root), "link": target, "reason": "path does not exist"})
            elif frag and os.path.isfile(dest) and dest.lower().endswith((".md", ".markdown", ".mdx")):
                anchor_cache.setdefault(dest, anchors_for(dest))
                if slug(frag) not in anchor_cache[dest]:
                    broken.append({"file": os.path.relpath(f, root), "link": target, "reason": "no such heading anchor in target"})

    result = {"files_scanned": len(files), "local_links_checked": checked,
              "external_skipped": external, "broken": broken}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Scanned {len(files)} files · checked {checked} local links · skipped {external} external.")
        if broken:
            print(f"\n{len(broken)} broken local link(s):")
            for b in broken:
                print(f"  {b['file']}: {b['link']}  ({b['reason']})")
        else:
            print("No broken local links.")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
