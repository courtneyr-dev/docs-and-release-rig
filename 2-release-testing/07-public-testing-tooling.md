# Public release-testing tooling

<!-- canonical-source-banner -->
> **Provenance for the agent skill.** The transferable pattern in this page is generalized in the skill at [`../skills/comprehensive-documentation-engineering/`](../skills/comprehensive-documentation-engineering/) — see [`references/beta-rc-testing.md`](../skills/comprehensive-documentation-engineering/references/beta-rc-testing.md). This page is the unique real-work record behind it.


The runbook in document 06 doesn't start from nothing. The prior release cycle (WordPress 7.0)
produced **public, reusable testing tooling** that I built and shipped openly, and that the 7.1
cycle was designed to fork and extend.

Both repositories below are public. Every link was verified to resolve for a logged-out visitor.

---

## WordPress 7.0 automated test runner

**https://github.com/courtneyr-dev/wp7-test-automation**

A Node.js and Playwright command-line runner that executes **123 test steps** against a WordPress
7.0 beta site.

**Coverage — 14 areas:** general administration (REST API, sitemaps, error checking), admin UI and
responsive behavior, new block functionality, typography and font library management, visual
revision controls, responsive editing, navigation overlays and block updates, media uploads,
pattern editing, and real-time collaboration.

**How it works:**

- Authenticates by standard login **or pre-exported cookies**, so it works against sites behind
  two-factor authentication or single sign-on — which is what makes it usable against real hosting
  rather than only local installs.
- Emits a JSON results file, viewable through an included HTML reporter.
- Captures screenshots for failed steps, so a failure arrives with evidence attached.
- Writes to a configurable output directory.

**The part I'd point at: the README documents its own limitations.** It names what the runner
*cannot* cover — real-time collaboration (needs genuinely simultaneous users), custom PHP blocks,
subjective UI assessment, server-side checks, accessibility, and cross-browser validation.

Those are honest constraints of browser automation, not gaps in test design, and saying so in the
README is the difference between a tool a colleague can trust and one they'll over-rely on. It is
the same honest-gaps rule that governs every report in this portfolio, applied to a tool instead of
a document — and it's why the 7.1 program kept a **manual exploratory layer and a browser split**
in the matrix rather than assuming automation had it covered.

## WordPress 7.0 test launcher and Playground blueprint

**https://github.com/courtneyr-dev/WP7-testing**

Community-facing testing infrastructure, two pieces:

1. **An interactive test launcher** (`index.html`, served via GitHub Pages) — a checklist interface
   letting any tester track progress across WordPress 7.0 beta features.
2. **A WordPress Playground blueprint** (`wp70-comprehensive-blueprint.json`) — load it into
   Playground and get a pre-configured beta testing environment in a browser tab, with no local
   setup at all.

This one is a **documentation artifact disguised as tooling.** The barrier to community beta
testing is almost never willingness; it's the setup cost and not knowing what to check. A blueprint
removes the first barrier and a checklist removes the second. Between them they turn "please test
the beta" — a request most people can't act on — into two clicks.

That framing is the same instinct behind a good quick-start guide: the measure of the document is
how quickly a stranger gets to a working state, not how completely it describes the system.

---

## How this fed the 7.1 program

The 7.1 strategy explicitly planned to **fork the 7.0 suite rather than generalize it mid-cycle**,
with the reasoning written down at the time: the release window was 4.5 weeks, generalization and
delivery were competing goals, and attempting both risked losing both. Generalize into a
version-agnostic suite *after* the cycle, not during it.

Recording the tradeoff — and the intended follow-up — is what keeps a decision like that from
looking, six months later, like nobody thought about it.
