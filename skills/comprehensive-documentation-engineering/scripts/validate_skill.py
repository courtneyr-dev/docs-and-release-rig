#!/usr/bin/env python3
"""Structural validator for this skill package. Read-only.

Checks: SKILL.md frontmatter (name kebab-case ≤64, description present ≤1024),
that every reference/workflow/template the SKILL.md and workflows point at exists,
that reference sheets adapted from CC BY-SA sources carry an attribution header,
and that tests/evals.json passes the eval schema (delegates to check_evals.py).

Usage: validate_skill.py [SKILL_DIR]
Exit codes: 0 valid · 1 problems found · 2 bad usage.
"""
import json
import os
import re
import subprocess
import sys

CCBYSA_FILES = {  # reference sheets adapting Diátaxis doctrine — must carry a CC BY-SA header
    "references/diataxis-foundations.md", "references/compass-and-classification.md",
    "references/tutorials.md", "references/how-to-guides.md", "references/reference.md",
    "references/explanation.md", "references/anti-patterns.md",
    "references/information-architecture.md", "references/style-overrides.md",
    "references/accessibility-and-localization.md",
}
# references/diagrams.md is intentionally NOT here: it is MIT text describing the
# C4 model (c4model.com content is CC BY 4.0), not a Diátaxis CC BY-SA adaptation.


def frontmatter(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if km:
            fm[km.group(1)] = km.group(2).strip()
    return fm, text


def main():
    root = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else \
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not os.path.isdir(root):
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 2

    problems, notes = [], []

    # 1. SKILL.md frontmatter
    skill_md = os.path.join(root, "SKILL.md")
    if not os.path.isfile(skill_md):
        problems.append("SKILL.md missing")
    else:
        fm, body = frontmatter(skill_md)
        if fm is None:
            problems.append("SKILL.md has no YAML frontmatter")
        else:
            name = fm.get("name", "")
            if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
                problems.append(f"name not kebab-case: {name!r}")
            if len(name) > 64:
                problems.append("name exceeds 64 chars")
            if name and os.path.basename(root) != name:
                notes.append(f"note: dir '{os.path.basename(root)}' != name '{name}' (ok if intentionally installed elsewhere)")
            desc = fm.get("description", "")
            if not desc:
                problems.append("description missing")
            elif len(desc) > 1024:
                problems.append(f"description {len(desc)} chars > 1024")
            if "use when" not in desc.lower():
                notes.append("note: description should state WHEN to use (\"Use when …\")")

        # 2. referenced files exist
        for rel in sorted(set(re.findall(r"`(references/[\w-]+\.md|workflows/[\w-]+\.md|templates/[\w-]+\.md|scripts/[\w.]+)`", body))):
            if not os.path.exists(os.path.join(root, rel)):
                problems.append(f"SKILL.md points at missing file: {rel}")

    # 3. workflow cross-references exist
    wf_dir = os.path.join(root, "workflows")
    if os.path.isdir(wf_dir):
        for wf in os.listdir(wf_dir):
            if not wf.endswith(".md"):
                continue
            with open(os.path.join(wf_dir, wf), encoding="utf-8") as fh:
                wtext = fh.read()
            for rel in set(re.findall(r"`((?:references|templates|scripts|workflows)/[\w.-]+)`", wtext)):
                if not os.path.exists(os.path.join(root, rel)):
                    problems.append(f"workflows/{wf} points at missing file: {rel}")

    # 4. CC BY-SA attribution headers
    for rel in sorted(CCBYSA_FILES):
        p = os.path.join(root, rel)
        if not os.path.isfile(p):
            problems.append(f"expected reference sheet missing: {rel}")
            continue
        head = open(p, encoding="utf-8").read(600).lower()
        if "cc by-sa" not in head and "cc-by-sa" not in head:
            problems.append(f"{rel} missing CC BY-SA attribution header")

    # 5. evals
    evals = os.path.join(root, "tests", "evals.json")
    checker = os.path.join(root, "tests", "check_evals.py")
    if os.path.isfile(evals) and os.path.isfile(checker):
        r = subprocess.run([sys.executable, checker, evals], capture_output=True, text=True)
        if r.returncode != 0:
            problems.append("tests/evals.json failed schema validation:\n" + (r.stdout + r.stderr).strip())
    else:
        problems.append("tests/evals.json or tests/check_evals.py missing")

    for n in notes:
        print(n)
    if problems:
        print(f"\n✗ {len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\n✓ skill package structurally valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
