#!/usr/bin/env python3
"""Scan a finished handoff/report file for likely confidentiality leaks. Read-only.

For SEC-SCRUB-1: a privately-disclosed finding must be reduced to a bare
acknowledgment with ALL traces removed, then the file grepped to confirm zero traces.
This flags common leak patterns (severity scores, CVE ids, exploit/reproduction
language, endpoint/function fingerprints, disclosure-platform names, secret-like
tokens, local filesystem paths). It CANNOT prove a file is clean — a human must
confirm and a human must supply case-specific terms via --term. Absence of flags is
necessary, not sufficient.

Usage:
  scrub_check.py FILE [--term SECRETWORD ...] [--json]
Exit codes: 0 no patterns flagged · 1 patterns flagged (review) · 2 bad usage.
"""
import argparse
import json
import os
import re
import sys

PATTERNS = [
    ("CVE id", r"\bCVE-\d{4}-\d{4,7}\b"),
    ("CVSS / severity score", r"\bCVSS\b|\bseverity[:=]\s*(critical|high|medium|low)\b|\b\d\.\d\s*/\s*10\b"),
    ("exploit/reproduction language", r"\b(exploit|proof.?of.?concept|\bPoC\b|reproduc\w+|payload|bypass|0-?day)\b"),
    ("disclosure platform names", r"\b(HackerOne|Bugcrowd|h1|security@|/advisories/|GHSA-[\w-]+)\b"),
    ("endpoint/function fingerprint", r"\b(function|def|endpoint|route)\s+[\w:./]+\(|\b[A-Za-z_]\w*\(\)"),
    ("secret-like token", r"\b(sk|pk|ghp|xox[baprs]|AKIA)[-_][A-Za-z0-9]{8,}\b|\b[A-Fa-f0-9]{32,}\b"),
    ("local filesystem path", r"(/Users/|/home/|C:\\\\|/private/tmp/|/var/folders/)\S+"),
    ("private repo hint", r"\b(git@|ssh://)\S+|\bprivate repo\b"),
]


def main():
    ap = argparse.ArgumentParser(description="Flag likely confidentiality leaks in a handoff file (read-only).")
    ap.add_argument("file")
    ap.add_argument("--term", action="append", default=[], help="case-specific term that MUST NOT appear (repeatable)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not os.path.isfile(args.file):
        print(f"error: no such file: {args.file}", file=sys.stderr)
        return 2

    with open(args.file, encoding="utf-8", errors="replace") as fh:
        lines = fh.readlines()

    checks = list(PATTERNS) + [(f"custom term: {t}", re.escape(t)) for t in args.term]
    flags = []
    for i, line in enumerate(lines, 1):
        for label, pat in checks:
            for m in re.finditer(pat, line, re.IGNORECASE):
                flags.append({"line": i, "pattern": label, "match": m.group(0)[:80]})

    if args.json:
        print(json.dumps({"file": args.file, "flags": flags}, indent=2))
    else:
        if flags:
            print(f"{len(flags)} potential leak pattern(s) in {args.file} — REVIEW each; scrub or confirm intentional:\n")
            for f in flags:
                print(f"  L{f['line']:>4} [{f['pattern']}] {f['match']!r}")
        else:
            print(f"No known leak patterns flagged in {args.file}.")
        print("\nThis is necessary, not sufficient. A human must confirm the scrub and add --term for "
              "case-specific mechanism/endpoint/platform names.")
    return 1 if flags else 0


if __name__ == "__main__":
    sys.exit(main())
