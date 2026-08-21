# Workflow: verify UI labels and workflows against the docs

Confirm the documentation names controls, menus, states, and workflows the way the running interface actually renders them. Produces a **label-diff report**. Reference depth: `references/ui-verification.md`.

**The thesis:** the screenshot pass and the wording fact-check are one task. Only the running UI carries the labels — source, dev notes, and PRs can all describe a capability correctly while the doc still names a control that doesn't exist under that name.

## 1 · Pre-authorize (before any unattended session)
Clear the human-only blockers up front: OS keychain/browser-session approvals and sign-off to run the target build on a real staging site. These are five-second decisions that otherwise block an entire pass.

## 2 · Stand up the capture rig
Prefer a persistent real local site over a browser sandbox (no sandbox chrome, CLI seeding, re-shootable next milestone). Seed content realism (real site name, admin display name, collaborator users, featured image, real pages) and **seed editor preferences** (welcome guides off, panel/sidebar state) — UI state persists server-side per user, so an unseeded or mid-run-toggled state silently changes every capture. Confirm the build version you actually landed on.

## 3 · Probe first (highest-leverage step)
Dump the interface's **accessibility tree** — every button, tab, menu with its ARIA label — before scripting any capture. This finds each control on the first attempt and yields the exact labels the fact-check needs, making the label-diff nearly free.

## 4 · Capture (if screenshots are needed)
Use a reusable automation harness, not per-shot declarative hooks (modern editors need real keyboard events, sequenced clicks with waits, and iframe handling). Apply the known-good patterns: DOM-content-loaded + explicit selector waits (network-idle may never settle); set login values directly and dispatch input events; reset an unusable printed password via CLI. Reload and re-inspect after any content surgery (placeholder deletion has knock-on effects). Demo colors must pass contrast. Review every image full-size; budget 2–3 iterations; never ship the first render.

## 5 · Produce the label-diff report (`templates/ui-label-diff.md`)
For every control the docs name: draft's term · actual rendered label · actual menu path · actual option set (counts and names) · match? · notes. Distinguish observed UI behavior from inferred; report unresolved differences as unresolved. Feed the report back to whoever wrote the draft.

## 6 · Reconcile the docs
Update wording to the verified labels; flag renamed labels, changed navigation, altered states, reordered workflows, and missing/needed screenshots. A screenshot is evidence of appearance, not behavior — don't promote it to runtime proof (behavior claims go through `validate-claims.md`).

---
*Provenance: UI verification and label-diff method from Courtney Robertson's docs-and-release-rig (CC0). Full attribution: `references/source-provenance.md`.*
