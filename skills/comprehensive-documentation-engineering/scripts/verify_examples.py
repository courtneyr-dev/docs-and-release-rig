#!/usr/bin/env python3
"""Extract fenced code blocks from Markdown and OPTIONALLY run the safe ones.

Default is EXTRACT-ONLY (a dry run): it lists every fenced block, its language, and
whether it looks runnable — and never executes anything. Execution is opt-in per
language and is refused for any block containing an external-side-effect pattern
(deploy, push, publish, migrate against real DBs, rm -rf, credential use, network
calls), per the execution-verification protocol in references/evidence-and-validation.md.

Running examples still belongs in a disposable sandbox — this tool does not create
one; run it from inside a throwaway copy of the repo. Report marks each block
verified / unverified(skipped-with-reason).

Usage:
  verify_examples.py FILE [--run python] [--run bash] [--json]
Exit codes: 0 all attempted blocks passed (or extract-only) · 1 a run failed · 2 bad usage.
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
import os

FENCE_RE = re.compile(r"^([ \t]*)(`{3,}|~{3,})[ \t]*([\w+-]*)[ \t]*$")
SIDE_EFFECT = re.compile(
    r"\b(rm\s+-rf|sudo|curl|wget|nc\s|ssh\s|scp\s|git\s+push|npm\s+publish|"
    r"pip\s+install|deploy|kubectl\s+apply|terraform\s+apply|drop\s+table|"
    r"migrate|secret|api[_-]?key|password|token)\b", re.IGNORECASE)
RUNNERS = {"python": [sys.executable], "py": [sys.executable],
           "bash": ["bash"], "sh": ["sh"]}


def extract(path):
    blocks, cur, fence, lang, indent, start = [], None, None, None, "", 0
    with open(path, encoding="utf-8", errors="replace") as fh:
        for i, line in enumerate(fh, 1):
            if cur is None:
                m = FENCE_RE.match(line)
                if m:
                    indent, fence, lang, start, cur = m.group(1), m.group(2), (m.group(3) or "").lower(), i, []
            else:
                if line.strip().startswith(fence) and line[:len(indent)] == indent and not line.strip(fence + " \t\n"):
                    blocks.append({"lang": lang, "line": start, "code": "".join(cur)})
                    cur = None
                else:
                    body = line[len(indent):] if line.startswith(indent) else line
                    cur.append(body)
    return blocks


def main():
    ap = argparse.ArgumentParser(description="Extract and optionally run Markdown code blocks (safe by default).")
    ap.add_argument("file")
    ap.add_argument("--run", action="append", default=[], metavar="LANG",
                    help="languages to actually execute (e.g. python, bash). Omit for extract-only.")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not os.path.isfile(args.file):
        print(f"error: no such file: {args.file}", file=sys.stderr)
        return 2

    run_langs = {l.lower() for l in args.run}
    blocks = extract(args.file)
    results, failed = [], 0

    for b in blocks:
        rec = {"line": b["line"], "lang": b["lang"] or "(none)", "status": "extracted", "reason": ""}
        if b["lang"] in run_langs:
            if SIDE_EFFECT.search(b["code"]):
                rec["status"], rec["reason"] = "unverified", "skipped: external-side-effect pattern — run manually in a sandbox"
            elif b["lang"] not in RUNNERS:
                rec["status"], rec["reason"] = "unverified", f"no runner for '{b['lang']}'"
            else:
                with tempfile.NamedTemporaryFile("w", suffix="." + b["lang"], delete=False) as tf:
                    tf.write(b["code"])
                    tmp = tf.name
                try:
                    p = subprocess.run(RUNNERS[b["lang"]] + [tmp], capture_output=True,
                                       text=True, timeout=30)
                    if p.returncode == 0:
                        rec["status"] = "verified"
                    else:
                        rec["status"], rec["reason"], failed = "failed", (p.stderr or p.stdout).strip()[:500], failed + 1
                except subprocess.TimeoutExpired:
                    rec["status"], rec["reason"], failed = "failed", "timeout (30s)", failed + 1
                finally:
                    os.unlink(tmp)
        elif b["lang"] not in run_langs and run_langs:
            rec["reason"] = "not in --run set"
        results.append(rec)

    if args.json:
        print(json.dumps({"file": args.file, "blocks": len(blocks), "failed": failed, "results": results}, indent=2))
    else:
        mode = f"running {sorted(run_langs)}" if run_langs else "extract-only (no execution)"
        print(f"{args.file}: {len(blocks)} code block(s) — {mode}\n")
        for r in results:
            line = f"  L{r['line']:>5} [{r['lang']}] {r['status']}"
            if r["reason"]:
                line += f" — {r['reason']}"
            print(line)
        if not run_langs:
            print("\nExtract-only. Pass --run python / --run bash to execute safe blocks in a disposable sandbox.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
