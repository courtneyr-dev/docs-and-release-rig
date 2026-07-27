# UI verification & the label-diff report

**Retro from a real screenshot and fact-check pass, July 2026.**

The claim this file defends: **the screenshot pass and the wording fact-check are the
same task, and separating them is how docs end up describing controls that do not exist
under that name.**

Generalized from production work; dashboard and authorization specifics are omitted.

---

## The finding that makes the case

Two claims in a draft article used **invented control names**. Not wrong concepts —
wrong labels. The draft said "responsive editing" and described three interactive
states.

The actual UI, verified by reading it:

- The control is under the **View** menu, labeled **"Responsive styles"**, with the
  help text *"Style changes apply only to the selected viewport."*
- The Button block's **State** selector offers a **PSEUDO STATE** dropdown with
  **five** options: Default, Hover, Focus, Focus-visible, Active.

A reader following the draft would have searched the interface for a menu item that was
never there, and would have counted two states that were missing. Neither error is
detectable by reading the source, the dev note, or the PR — all three describe the
capability correctly. Only the running UI carries the labels.

**Writing UI copy before seeing the UI is fine.** Shipping it before seeing the UI is
not. So the screenshot pass has a required deliverable beyond the images: a **label-diff
report** listing every control name, menu path, and option set as it actually renders,
fed back to whoever wrote the draft.

---

## What worked, and is worth repeating

**A real local site as the capture rig.** Creating a disposable local site and updating
it to the exact beta build took under five minutes, and beat a browser-based sandbox for
article screenshots: no sandbox chrome around the canvas, full command-line access for
seeding users, media, and preferences, and the site persists for re-shoots at the next
milestone.

**Probe first, capture second.** Dumping the editor's **accessibility tree** — every
button, tab, and menu with its ARIA label — before writing any capture steps found each
control on the first attempt *and* produced the exact labels the fact-check needed. This
is the single highest-leverage step in the whole pass, and it is why the label-diff
report costs almost nothing once you are already there.

**Content realism as a checklist, not an afterthought.** Naming the site something real,
giving the admin a real display name, seeding collaborator users, a featured image, and
actual pages is what makes a screenshot publishable. One caution learned the hard way:
deleting placeholder content without replacing it broke a navigation block and put an
error notice directly in frame. Placeholder cleanup has knock-on effects — reload and
re-inspect after any content surgery.

**Review every image at full size.** Each shot took two or three iterations: a clipped
composer, a panel toggled off, a menu that closed. Budget for iteration. Never ship the
first render.

---

## What to fix next time

1. **Pre-authorize dashboards before unattended sessions.** One planned screenshot died
   on two things only a human can do: an OS keychain approval for a browser session, and
   sign-off to run a beta build on a real staging site. Both are five-second decisions
   that block an entire autonomous pass. Do them *before* handing off the task.
2. **Editor state persists server-side — reset it up front.** Welcome guides, sidebar
   open/closed state, and modal panel state are stored per user in the database. A
   capture that accidentally toggles a panel silently changes every subsequent capture.
   Seed preferences at rig setup, and treat any mid-run UI toggle as state that must be
   undone.
3. **Automation harness, not per-shot scripting.** Simple declarative hooks — click,
   hover, evaluate-before — cannot drive a modern block editor: a mention picker needs
   real keyboard events, a state dropdown needs sequenced clicks with waits, and the
   canvas lives inside an iframe. Every interesting shot ended up as a hand-written
   browser-automation script. That pattern belongs folded back into the tooling so the
   next pass starts from a working harness.
4. **Known-good automation patterns, written down.** Network-idle waits never settle on
   some local-site setups — use DOM-content-loaded plus explicit selector waits. Typing
   into a login form races; set values directly and dispatch input events. A
   locally-reported admin password may not work as printed; reset it via the CLI and
   move on. These cost about thirty minutes of debugging that a checklist eliminates.
5. **Demo colors must pass contrast.** The first hover-state color chosen for a
   screenshot triggered the editor's own contrast warning badge — inside the panel being
   photographed. The accessible choice is also the clean screenshot.

---

## The rule

A screenshot is evidence of appearance, not evidence of behavior — a point made more
formally in `../3-security-methods/09-evidence-and-validation-standard.md`, where "a
screenshot is not runtime proof" is an explicit guardrail.

But a screenshot pass **is** the cheapest available audit of documentation language,
because you are already looking at every control the doc names. Take the label-diff
while you are there.
