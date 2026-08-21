> Synthesized from Courtney Robertson's docs-and-release-rig (CC0 — source hierarchy, decay rule, milestone cadence, coverage discipline, compatibility-claim rule) and Anivar Aravind's developer-docs-framework (MIT — changelog/migration types). 2026-08-20.

# Release documentation

Documentation for a moving target obeys different physics than documentation for a stable one: sources conflict, facts decay, and features land, punt, and revert mid-cycle. This reference covers the knowledge rules; `beta-rc-testing.md` covers the testing loop; `workflows/test-release.md` operationalizes both.

## The source hierarchy (moving targets)

When two sources disagree, the higher one wins — no debate, no averaging:

1. **Your own runtime test on the current build** — the only source describing what the software *does* rather than what someone believes it does.
2. **The official dev note / field guide** on the project's developer channel.
3. **The diff** — the actual commit range in the relevant repositories.
4. **Community roundups** — discovery of items you missed; never a citation, and never copy their phrasing.
5. **Your memory and older notes** — a lead, not a fact.

**Reading implementation code ranks below a published dev note.** Code can be mid-refactor, feature-flagged, or about to be reverted — reading it yields a *hypothesis* about intended behavior, not documentation-grade truth. When a dev note lands, re-check everything previously inferred from code. (For stable, shipped targets the regimes flip — see `evidence-and-validation.md`.)

## The 48-hour decay rule and the daily sweep

During an active beta→RC→GA cycle, working knowledge decays in about 48 hours (an empirical retro number: two documented facts — a feature gate and a dependency upgrade — went wrong inside two days, both from trusting code-reading over the notes that superseded it). So, each working session, **before touching any deliverable**:

1. **Sweep the last 24–48h**: the project's dev-note tag and core blog, the test team's channel, the release milestone in the tracker, repo compare views, relevant chat channels.
2. **Diff the sweep against your docs**: anything new that contradicts, adds to, or makes public what's written?
3. **Correct, and date the delta.** For anything already shared, log a dated update note stating what changed since the last shared version — readers who acted on the old version need the delta, not a silently edited document. Corrections of your own prior claims are stated as corrections, with the correcting source attached.
4. **Re-verify changed features at runtime** where testable; never promote code-reading or a dev note to "confirmed" without a runtime check.
5. **Swap draft/preview links for public ones** as official docs publish.

## Milestone triggers

- **Weekly betas:** churn — features added, fixed, punted; many tickets milestoned late.
- **RC1:** dev notes and field guide finalize; **reconcile the entire coverage map here**; feature set should freeze.
- **RC2:** bug fixes only — confirm nothing previously documented got reverted.
- **GA:** final link swap; verify every claim against the shipped build.

Standing re-checks every pass: does the feature actually engage on this configuration or silently fall back (a silent fallback means the documented benefit doesn't exist for that reader)? · compatibility surfaces for plugins/extensions (removed components, newly-unconditional behavior) · does the integrity/checksum baseline still match? · are previously-reported findings still present?

## Stability of claims

Never publish unstable claims as settled facts. Pre-freeze features carry status labels (announced / landed / verified / punted / reverted); the coverage map keeps **your verification status** distinct from the **feature's ticket status** — they are different claims. Attribute paths, labels, and defaults are verified against the *current* build or its own metadata, never from memory of the previous release.

## The release documentation web

Connect the artifacts — each links the others and the Diátaxis documents it affects: release notes / changelog (Added/Changed/Deprecated/Removed/Fixed/Security; specific; linked) · field guide / dev notes (authoritative per-feature detail) · migration guide (per breaking transition) · known issues · deprecation notices (always with a migration path) · compatibility guidance. A release's how-to/reference/explanation updates are driven from the change-coverage receipt (`workflows/document-a-change.md`).

## Compatibility statements are documentation claims

"Tested up to ⟨version⟩" and its cousins are published claims about runtime behavior, not version-string edits. Earn them: run the real suite against a real install of that version (not only a CI `latest` lane — though reading what `latest` resolved to is itself worth doing) · scoped source diff of the surfaces your code bends · a runtime probe per finding · and **state the evidence ceiling** — name what was *not* run, on the label.

## Originality guardrail

Release coverage synthesizing a community roundup never reuses its phrasing — duplicate content hurts everyone. Facts + public links **in your own words**, your own examples, your own screenshots. Exclude preview-tokened URLs, internal chat links, and private-drive assets; swap in public URLs when official docs publish.
