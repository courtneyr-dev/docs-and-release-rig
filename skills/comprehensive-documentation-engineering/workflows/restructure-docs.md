# Workflow: restructure, move, or split documentation (gated)

Moving, splitting, renaming, or mass-rewriting existing docs. **Gated** — requires explicit approval before any file changes. Classify before moving; preserve everything; verify preservation.

## 1 · Classify before touching anything (read-only)
Run `audit-existing-docs.md` (at least inventory + classification) if not already done. You cannot move content correctly before you know what type each piece is. Respect prior deliberate reclassifications found in git history.

## 2 · Clean-tree gate
Repo under git with a clean working tree so every change is one revert from undone. Offer `git init` + initial commit if unversioned, or commit/stash if dirty. Do not proceed otherwise.

## 3 · Propose the migration (`templates/migration-plan.md`)
- Per existing doc/section: **keep / move / split**, each move and each split-part naming its destination type and document (no destination = not approvable).
- List file moves/renames, new files created, and the scope of any rewrite.
- Detect inbound links and navigation dependencies now: `scripts/check_links.py` plus a search for references to the paths you'll move. List the redirects/link updates each move requires — **one redirect per old URL, sub-pages included**, not just the parent; a deleted page redirects to its nearest surviving relative. Where the site has a profile (`templates/site-profile.md`), use its redirect file, path form, and PR label.
- Note reference **scope** if a reference reorg is involved (separately approvable).

## 4 · STOP for approval
Present the plan and scope; wait for an explicit yes on this specific plan. Presenting is not approval; "sure/looks fine" that doesn't address the plan is not approval — ask again. No moves before approval.

## 5 · Execute incrementally and reversibly
- Prefer history-preserving moves (`git mv`) so authorship survives.
- **A move is a rewrite:** content relocated into a type is held to that type's rules and closing self-check exactly like new content — reference tables, teaching, or instruction that arrive inside moved content are rewritten or linked out.
- **Never delete.** Misplaced content is moved, never removed; the parking lot holds content awaiting a not-yet-written destination.
- Update all cross-references and navigation config; create redirects where the platform supports them (relative paths, no trailing slash on the old path unless the platform wants one, permanent status). Put a From/To redirect table in the PR body so reviewers can verify coverage, and apply the repo's redirect label if it has one (discipline after jazzsequence's pantheon-docs-writer, MIT).
- Prefer small, single-section steps over big-bang restructures; commit as you go.

## 6 · Verify preservation and links (don't claim it)
- Compare before/after: an inventory or content diff proving every piece of information survived (moved, not lost). Report the comparison, not a claim.
- Re-run `scripts/check_links.py`; fix or redirect every break; verify none remain.
- Re-verify any standing decision recorded in a plan file (link policies, off-limits directories, scope limits) against the result.

## Guardrails
- Broad restructuring never proceeds without approval, regardless of urgency framing (`adv-02` tests this).
- If the user rejects a classification or move, accept and adjust.
- If preservation can't be verified, say so and stop — never report success on faith.

---
*Provenance: approval/preservation discipline from Romain Lespinasse's agent-skills (MIT), Peter Knego's diataxis-docs-skill (MIT), and Romain Lespinasse's article. Full attribution: `references/source-provenance.md`.*
