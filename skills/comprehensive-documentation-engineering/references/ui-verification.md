> Synthesized from Courtney Robertson's docs-and-release-rig (CC0 — UI verification & label diff). 2026-08-20. Operational steps: `workflows/verify-ui.md`.

# UI verification and label-diff

**The thesis:** the screenshot pass and the wording fact-check are the same task. Separating them is how docs end up describing controls that don't exist under that name. Only the running UI carries the labels — a capability can be described correctly in the source, the dev note, and the PR while the doc still names a menu item that was never there and counts states that are missing.

## The label-diff report (required deliverable)

Any screenshot/UI pass produces, beyond the images, a **label-diff report**: every control name, menu path, and option set **as it actually renders**, fed back to whoever wrote the draft. It lists, for each documented control: what the draft calls it, what the UI actually shows (exact label, exact menu path, exact option set), and whether they match. Template: `templates/ui-label-diff.md`.

Writing UI copy before seeing the UI is fine; **shipping it before seeing the UI is not.**

## Probe first, capture second

Before scripting any capture, **dump the interface's accessibility tree** — every button, tab, and menu with its ARIA label. This finds each control on the first attempt *and* yields the exact labels the fact-check needs. It is the single highest-leverage step; it makes the label-diff nearly free because you're already reading every label. Distinguish observed UI behavior from inferred; report unresolved differences as unresolved.

## The capture rig

- **A persistent real local site** beats a browser sandbox for publishable shots: no sandbox chrome around the canvas, full CLI access to seed users/media/preferences, and the site persists for re-shoots at the next milestone.
- **Content realism as a checklist:** real site name, real admin display name, seeded collaborator users, a featured image, actual pages — that's what makes a screenshot publishable. Caution: deleting placeholder content without replacing it can break components and put an error notice in frame — **reload and re-inspect after any content surgery**.
- **Review every image at full size;** budget 2–3 iterations per shot (clipped composer, panel toggled off, menu closed); never ship the first render.
- **Demo colors must pass contrast** — the accessible choice is also the clean screenshot (a poor hover color can trip the editor's own contrast warning inside the panel you're photographing).

## State and automation

- **Editor/UI state persists server-side per user** (welcome guides, sidebar and panel open/closed, modal state). Seed preferences at rig setup; any mid-run toggle silently changes every subsequent capture and must be undone.
- **Declarative per-shot hooks can't drive a modern editor:** a mention picker needs real keyboard events, a state dropdown needs sequenced clicks with waits, and the canvas may live in an iframe. Build a reusable automation harness rather than per-shot scripts. Known-good patterns worth writing down: network-idle waits may never settle on some local setups — use DOM-content-loaded plus explicit selector waits; typed logins race — set values directly and dispatch input events; a locally-printed admin password may not work as printed — reset via CLI.
- **Pre-authorize keychain approvals and staging sign-offs before unattended sessions** — five-second human decisions that otherwise block an entire autonomous pass.

## The rule

A screenshot is evidence of appearance, not behavior — never promote it to runtime proof (that guardrail lives in `evidence-and-validation.md`). But a screenshot pass **is** the cheapest available audit of documentation language, because you're already looking at every control the doc names. Take the label-diff while you're there. Docs use the UI's exact labels — "the Delete button", never "the red button" — with UI elements bolded and menu paths in the product's own convention.
