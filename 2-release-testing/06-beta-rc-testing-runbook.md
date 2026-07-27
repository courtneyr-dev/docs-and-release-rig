# Beta/RC testing runbook — how each release drop gets tested

**Context:** written for the WordPress 7.1 cycle (Beta 3 → RC1 → RC2 → GA), and
generalizable to any release train with weekly drops.

> Generalized from production work. Hosting infrastructure, host names, and connection
> details are omitted, and platforms are described by *tier* rather than by name —
> the tier is what matters to the method.

Goal: thorough on security and functionality, with the smallest possible amount of
human babysitting. Everything that can run unattended, runs unattended.

## Environments, organized by when they can be tested

The organizing insight is that **test environments do not all become testable at the
same moment**, and pretending otherwise is what makes release testing feel chaotic.
Group them by update timing, not by importance:

**Immediate — testable the moment the release deploys**

1. **Local disposable environments** — a local-site app, containerized WordPress at
   multiple PHP versions, and WordPress Playground. Update instantly and
   automatically. No human action.
2. **Self-managed hosting with shell access** — a beta-channel plugin plus WP-CLI over
   key-based SSH. Updates on demand. No human action.
3. **Managed hosting, production tier** — updates when the platform propagates the
   build, or is forced via WP-CLI where the platform allows it. Needs a human to open
   the connection once per session.

**Deferred — always tested later**

4. **Managed hosting, staging tier** — the platform takes time to surface a new core
   version. Test it on its own schedule once it actually shows the release. This is a
   feature of the method, not a failure: staging propagation delay is itself a finding
   worth documenting for site owners.

## The human's per-drop checklist (deliberately small)

1. On drop day, flag that the build is out — or let the milestone sweep catch it.
2. Open the connection to any managed sites being tested this pass. Authenticate once.
3. Approve the upgrade run against a real hosted site, since it changes that site's
   core version. Rollback is part of the run.
4. Everything else is automated.

## The automated per-drop loop

**Phase 0 — re-anchor (about 10 minutes).** Sweep the release's dev-note tag, the drop
announcement, and the core and test channels for what changed, plus any ad-hoc
variations other testers are trying. Re-point every test spec at the new dev notes.
*This phase is why the docs stay accurate: specs are re-anchored to sources before any
testing happens, not after.*

**Phase 1 — update the immediate environments** to the new build, then confirm the
version. Never assume an auto-updating environment landed where you think it did;
check it.

**Phase 2 — security audit of the changed surface.** Fan out across the changed and
newly-added surfaces with an independent panel of frontier models, each auditing the
same diff separately, then adversarially reconcile. Prioritize by surface: REST diff
since the last tag, then any new API controllers, batch endpoints, media and
attachment handling, comment/notes REST plus sanitization of mentions, any AI client
code, and any direct database changes. Security-classified findings route privately
through coordinated disclosure — never to public issue trackers.

**Phase 3 — functionality.**

- *Unattended, every immediate environment:* install and upgrade integrity, core
  checksum verification, Site Health, post and page CRUD, the media pipeline including
  the format matrix, new-block markup validity and front-end asset loading, revisions,
  real-database integrity including character set and collation, cron, and
  permalinks/sitemap/robots against a real web server.
- *Browser-driven, against real URLs:* the editor scenarios a CLI cannot reach —
  composer UIs, modals, interactive states, keyboard and screen-reader paths for new
  blocks, the command palette — plus a plugin-compatibility sweep that requires the
  editor to actually load. Heavier, so batch these.
- *Load and real hosting:* media at scale, batch upload under real resource limits,
  and front-end block rendering through a real page cache.

**Phase 4 — regressions and banking.** Anything that changed versus the prior milestone
goes at the **top** of the session summary. Update every spec's results table with a
column per milestone, plus the run log and the status notes — in the same session,
while it is still true.

## Definition of done, per drop

Every P0 spec executed with all applicable variations in every applicable immediate
environment; P1 specs in at least two environments; P2 exploratory in one; every
security surface audited and reconciled; deferred environments completed when the
build propagates to them. The loop ends at the last RC with a go/no-go readiness
summary.

## Why the definition of done is written down

A release-testing loop without an explicit stop condition either ends early because
someone got tired, or never ends. "Looks done" is not a stop condition. The per-drop
definition above is deterministic: you can hand it to someone else and they can tell
you whether the pass is finished without asking you.
