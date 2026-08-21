# Audit / testing handoff — <target>

> One self-contained file. No internal wiki-links, no local paths — inline content or link **public** URLs only. Verify every link resolves logged-out before including; never link a private repo (describe by name/author instead). Re-verify findings live if the target is reachable.

**Confidentiality banner:** _(matched to the audience — e.g. "Public references only. One security-classified issue was responsibly disclosed through a private channel and is withheld here — no mechanism, location, severity, or reproduction.")_

## 1 · Intro and context
Target · environment and stack · versions · verification date.

## 2 · Findings
> One per finding, **mechanism → evidence → fix**, with a sources line linking each to its authoritative reference (dev note/announcement · issue/PR · tracker ticket). Privately-disclosed findings appear as a bare acknowledgment only.

### Finding 1 — <title>
- **Mechanism:** _____
- **Evidence:** _____ (marker: ____)
- **Fix:** _____
- **Sources:** _____

## 3 · Stack facts (verified)
_____

## 4 · Tested and cleared (non-issues — don't re-chase)
> Explicit negative results; this section often saves the recipient more time than the findings.
- _____

## 5 · Not covered — honest gaps
- _____

## 6 · How this was tested
- **Methods (prose):** _____
- **Prompts (verbatim, re-runnable):**
  ```
  <prompt>
  ```
- **Tooling (labeled by actual use):**
  | Tool / skill / model | used / available / staged / authored | Public link (or "named, not linked" if private) |
  |---|---|---|
  | | | |
- **Accuracy note:** which component actually performed the reasoning: _____

## 7 · Consolidated sources (all public)
- _____

---
**Pre-handoff checklist:**
- [ ] Every link resolves for a logged-out visitor (no private repos linked)
- [ ] Confidential findings scrubbed to a bare acknowledgment; **grepped the file to confirm zero traces** (`scripts/scrub_check.py`)
- [ ] Every tool/model labeled by actual use; accuracy note present
- [ ] Findings re-verified live where the target is reachable
- [ ] Secrets, PII, and infrastructure specifics redacted

---
*Provenance: section order and rules from the audit handoff standard in Courtney Robertson's docs-and-release-rig (CC0). Full attribution: `references/source-provenance.md`.*
