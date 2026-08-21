# Coverage and traceability matrix

Two indexes prove completeness from both directions. The per-capability rows (ID → sources → destination file → test) live in `capability-ledger.md`; this file proves (A) every source's distinct contributions landed somewhere concrete, and (B) every shipped file traces back to specific capabilities and sources. No "covered generally" entries — every cell names exact files or capability IDs.

## A · Source → capabilities → destination files (every source fully represented)

### S1 — Lespinasse article (MIT-spirit / ideas)
| Contribution | Capability | Destination file(s) |
|---|---|---|
| discover→classify→propose→execute frame | AUD-PROC-1, SAFE-RO-1 | `workflows/audit-existing-docs.md`, `workflows/plan-new-docs.md` |
| methodology embedded in tooling holds across contributors | GOV-CONTRIB-1 | `references/governance-and-freshness.md` |
| no reorg without sign-off | SAFE-GATE-1 | `SKILL.md`, `workflows/restructure-docs.md`, `workflows/plan-new-docs.md` |
| preserve content through reorganization | SAFE-PRES-1 | `workflows/restructure-docs.md` |

### S2 — rlespinasse/agent-skills (MIT)
| Contribution | Capability | Destination file(s) |
|---|---|---|
| four-type + compass classification, results table | DIA-CORE-1/3, AUD-CLASS-1 | `references/compass-and-classification.md`, `templates/classification-matrix.md` |
| git-history respect for prior reclassification | DIA-BOUND-2 | `references/compass-and-classification.md`, `workflows/audit-existing-docs.md` |
| boundary cases (troubleshooting/FAQ/README/migration) | DIA-BOUND-1 | `references/compass-and-classification.md` |
| docs-tooling adaptation (mkdocs/docusaurus/antora/hugo) | ARCH-TOOL-1 | `workflows/plan-new-docs.md`, `references/information-architecture.md` |
| per-quadrant page templates | WRITE-CT-*, WRITE-PAD-1 | `templates/content-templates.md` |
| small-project pragmatism, preserve, ask-before-change | SAFE-SMALL-1, SAFE-PRES-1, SAFE-GATE-1 | `SKILL.md`, workflows |
| evals schema + validator + promptfoo/claude-CLI harness | PKG-EVAL-1, TEST-SCHEMA-1 | `tests/evals.json`, `tests/check_evals.py`, `scripts/validate_skill.py` |
| agentskills.io packaging (≤500-line, description pattern) | PKG-FM-1, PKG-DESC-1, PKG-DISC-1 | `SKILL.md`, `references/source-provenance.md` |
| verify-readme-features (claim-status taxonomy, sub-claims, file:line, docs≠evidence) | AUD-FEAT-1/2, EVID-TRACE-1 | `workflows/validate-claims.md`, `references/evidence-and-validation.md` |
| conventional-commit (format, types, splitting, fixup guardrail, execution safety) | AUX-COMMIT-1..4 | `references/repo-workflow-practices.md` |
| verify-pr-logs (--log-failed first, triage, code-vs-CI, log-injection defense) | AUX-CI-1/2 | `references/repo-workflow-practices.md` |
| pin-github-actions (SHA pinning, batch resolve, API-injection defense, major-jump, dependabot) | AUX-PIN-1..3 | `references/repo-workflow-practices.md` |
| local-branches-status (batch loop, six-column report, actionable notes, no-fetch/no-delete) | AUX-BRANCH-1 | `references/repo-workflow-practices.md` |
| drawio-export-tools (ask-first disclosure, tool matrix, output templates) | AUX-DRAWIO-1 | `references/repo-workflow-practices.md` |
| french-language (diacritics mandatory across file types, tech-terms-stay-English, typography, format rules) | AUX-LANG-1 | `references/repo-workflow-practices.md`, `references/accessibility-and-localization.md` |

### S3 — keithpatton/diataxis-agent-skill (CC BY-SA 4.0)
| Contribution | Capability | Destination file(s) |
|---|---|---|
| operating modes (classify/audit/generate/restructure) + mode inference | Router, WRITE-GEN-1 | `SKILL.md`, `workflows/write-or-revise.md` |
| generate-mode policy (stated or classify-confirm) | WRITE-GEN-1 | `SKILL.md`, `workflows/write-or-revise.md` |
| classification output = quadrant + confidence + evidence | AUD-CLASS-1, DIA-CORE-3 | `references/compass-and-classification.md`, `templates/classification-matrix.md` |
| refusal-as-success | WRITE-GEN-1 | `SKILL.md`, `workflows/write-or-revise.md` |
| violation detection signals + failure modes + counterexamples + confidence calibration | 5 core anti-patterns, blur zones | `references/anti-patterns.md` |
| non-goals / scope boundaries | PKG-DESC-1 | `SKILL.md` (non-trigger boundaries) |
| CC BY-SA compliance + CITATION | PKG-CITE-1, PKG-LIC-1 | `CITATION.cff`, `LICENSE`, `references/source-provenance.md` |

### S4 — peterknego/diataxis-docs-skill (MIT AND CC-BY-SA-4.0)
| Contribution | Capability | Destination file(s) |
|---|---|---|
| clean-tree git gate | SAFE-CLEAN-1 | `workflows/plan-new-docs.md`, `workflows/restructure-docs.md` |
| persistent plan file (transient/persistent lifecycle, trim-commit, reruns) | SAFE-PLAN-1 | `templates/migration-plan.md`, `workflows/plan-new-docs.md` |
| reference scope as separately-approvable | SAFE-GATE-2 | `templates/migration-plan.md`, `workflows/plan-new-docs.md` |
| not-created = reason + remedy | SAFE-PLAN-1, DIA-WORK-3 | `templates/migration-plan.md`, `workflows/plan-new-docs.md` |
| keep/move/split with mandatory destinations | SAFE-PLAN-1, WRITE-MOVE-1 | `templates/migration-plan.md`, `workflows/restructure-docs.md` |
| parking lot | WRITE-PARK-1 | `templates/migration-plan.md` |
| write order reference→…→tutorial + rationale | SAFE-ORDER-1 | `workflows/plan-new-docs.md` |
| batched single question round | SAFE-ASK-1 | `workflows/plan-new-docs.md` |
| move-is-a-rewrite | WRITE-MOVE-1 | `workflows/restructure-docs.md` |
| section-granularity compass self-checks | DIA-CORE-7 | type sheets, `references/compass-and-classification.md` |
| autodoc rule (incl. section level) | ARCH-AUTODOC-1 | `references/reference.md`, `references/information-architecture.md` |
| measured numbers carry provenance | DIA-REF (provenance), EVID-REC-1 | `references/reference.md`, `references/evidence-and-validation.md` |
| tutorial execution-verification protocol | DIA-TUT-10, EVID-EXEC-1 | `references/tutorials.md`, `references/evidence-and-validation.md` |
| README wiring, standing-decision re-verification | SAFE-README-1, SAFE-CONV-1 | `workflows/plan-new-docs.md` |
| C4 diagram rules (levels, evidence, thin-repo, Mermaid subset) | DGM-C4-1/2 | `references/diagrams.md` |
| explicit-invocation-only for heavy workflows | PKG-GUARD-1 | `SKILL.md` |
| license-split practice | PKG-LIC-1 | `LICENSE`, `references/source-provenance.md` |
| explanation source-mining (ADRs/commits/RFCs) | DIA-EXP-8 | `references/explanation.md` |

### S5 — Claude Marketplaces listing (third-party summary)
| Contribution | Capability | Destination file(s) |
|---|---|---|
| install metadata + "anti-template" framing (confirming S6) | PKG-INST-1, WRITE-PAD-1 | `README.md`, `SKILL.md` |
| (recorded as third-party interpretation, not doctrine) | — | `provenance/research-report.md` §5 C11 |

### S6 — sammcj/agentic-coding (Apache-2.0)
| Contribution | Capability | Destination file(s) |
|---|---|---|
| "approach not template" as an instruction | WRITE-PAD-1, DIA-WORK-3 | `SKILL.md`, `references/diataxis-foundations.md` |
| why-exactly-four grounding | DIA-CORE-4 | `references/diataxis-foundations.md` |
| per-type review questions + boundary self-check | WRITE-ITER-1, WRITE-MIX-1 | `workflows/write-or-revise.md` |
| flow-is-paramount articulation | DIA-HOW-5 | `references/how-to-guides.md` |
| functional-vs-deep as constraints-vs-liberation | DIA-QUAL-1/2/3 | `references/diataxis-foundations.md` |
| multi-user-type / multi-environment structuring | DIA-HIER-3, ARCH-AUD-1 | `references/information-architecture.md` |
| "what Diátaxis cannot do" limits | DIA-QUAL-3 | `references/diataxis-foundations.md` |
| minimalist documentation (not all four types) | WRITE-PAD-1 | `references/content-types.md`, `SKILL.md` |
| living documentation rationale | GOV-PROD-1 | `references/governance-and-freshness.md` |
| review sign lists (boundary/flow/audience) | anti-patterns | `references/anti-patterns.md` |
| British-English house-style example | PKG-HOUSE-1 | `references/style-overrides.md` |

### S7 — anivar/developer-docs-framework (MIT)
| Contribution | Capability | Destination file(s) |
|---|---|---|
| 27 rules w/ incorrect/correct pairs | WRITE-*, WRITE-STYLE-*, ARCH-*, GOV-*, DX-*, AUD-* | `references/anti-patterns.md`, type sheets, `style-overrides.md`, `governance-and-freshness.md`, `developer-experience.md`, `documentation-audits.md` |
| 14 content types | WRITE-CT-1..8 | `references/content-types.md`, `templates/content-templates.md` |
| pluggable style overrides (6) | WRITE-STYLE-OVR-1, DX-CULT-1 | `references/style-overrides.md` |
| adoption funnel + bottleneck | DX-FUN-1, AUD-GAP-3 | `references/developer-experience.md` |
| audience matrix | DX-AUD-1, ARCH-AUD-1 | `references/developer-experience.md`, `references/information-architecture.md` |
| time-to-hello-world, interactivity ladder | DX-TTHW-1, DX-INT-1 | `references/developer-experience.md` |
| maturity model + archetypes | AUD-MAT-1/2 | `references/documentation-audits.md`, `templates/gap-analysis.md` |
| audit process (inventory→classify→gap→prioritize→plan) | AUD-INV-1/2, AUD-PROC-1 | `workflows/audit-existing-docs.md`, `templates/*` |
| docs-as-code + CI checks | ARCH-CODE-1 | `references/governance-and-freshness.md` |
| versioning + lifecycle | ARCH-VER-1, GOV-VER-1 | `references/governance-and-freshness.md` |
| freshness cadences, docs-are-done, ownership | GOV-FRESH-1, GOV-DONE-1, GOV-OWN-1 | `references/governance-and-freshness.md` |
| partner both-sides + production readiness + program | DX-PART-1/2/3 | `references/developer-experience.md`, `references/content-types.md` |
| measurement metrics | DX-MEAS-1 | `references/developer-experience.md`, `references/governance-and-freshness.md` |
| localization practices | GOV-LOC-1 | `references/accessibility-and-localization.md` |
| accessibility rules | GOV-A11Y-1 | `references/accessibility-and-localization.md` |
| anti-pattern checklist (named smells) | anti-patterns | `references/anti-patterns.md` |
| templates for every type + ADR + glossary | WRITE-CT-*, GOV-CONTRIB-1 | `templates/content-templates.md` |
| training-data distrust warning | (framing) | `references/content-types.md` intro, `SKILL.md` altitude |
| diagrams general guidance | DGM-1 | `references/diagrams.md` |

### S8 — diataxis.fr (CC BY-SA 4.0) — the authoritative doctrine
| Contribution | Capability | Destination file(s) |
|---|---|---|
| four needs/forms, map, compass | DIA-CORE-1/2/3/6 | `references/diataxis-foundations.md`, `references/compass-and-classification.md` |
| foundations (two dimensions, completeness argument) | DIA-CORE-4 | `references/diataxis-foundations.md` |
| functional vs deep quality theory | DIA-QUAL-1/2/3 | `references/diataxis-foundations.md` |
| per-type principles + language exemplars | DIA-TUT-*, DIA-HOW-*, DIA-REF-*, DIA-EXP-* | four type sheets, `references/style-overrides.md` |
| tutorials-vs-how-to & reference-vs-explanation deep treatments | DIA-DIST-1/2 | `references/compass-and-classification.md`, type sheets |
| the workflow (guide-not-plan, no empty structures, one step, organic growth, complete-not-finished) | DIA-WORK-1/2/3/4, DIA-APPLY-1 | `references/diataxis-foundations.md`, `SKILL.md` |
| complex-hierarchies (landing pages, ~7 list rule, two-dimensional) | DIA-HIER-1/2/3, ARCH-IA-4 | `references/information-architecture.md` |
| translation program mechanics | GOV-LOC-2 | `references/accessibility-and-localization.md` |
| attribution/citation requirements | PKG-CITE-1 | `CITATION.cff`, `references/source-provenance.md`, all CC BY-SA sheet headers |

### S9 — docs-and-release-rig (CC0)
| Contribution | Capability | Destination file(s) |
|---|---|---|
| docs-as-testable-claims thesis | (framing) | `SKILL.md`, `references/evidence-and-validation.md` |
| source hierarchy | REL-HIER-1, EVID-HIER-1 | `references/release-documentation.md`, `references/evidence-and-validation.md` |
| 48h decay + daily sweep + dated delta | REL-DECAY-1 | `workflows/test-release.md`, `references/release-documentation.md` |
| milestone triggers + standing re-checks | REL-TRACK-1, REL-CHECK-1 | `references/release-documentation.md` |
| coverage map (structure, originality guardrail, gap-in-another-doc) | AUD-COV-1/2/3 | `templates/coverage-map.md`, `workflows/test-release.md` |
| change-coverage receipt (11 reconciliations + gate) | REL-RECEIPT-1, REL-CHANGE-1 | `workflows/document-a-change.md`, `templates/change-coverage-receipt.md` |
| UI verification & label-diff (probe-first, rig, state, automation, contrast) | UI-DIFF-1, UI-PROBE-1, UI-VERIFY-1, UI-RIG-1, UI-STATE-1, UI-AUTO-1, UI-A11Y-1, UI-EVID-1 | `workflows/verify-ui.md`, `references/ui-verification.md`, `templates/ui-label-diff.md`, `scripts/compare_ui_labels.py` |
| beta/RC runbook (env timing, 4-phase, DoD, go/no-go) | REL-RUN-1/2, REL-DOD-1 | `references/beta-rc-testing.md`, `workflows/test-release.md`, `templates/release-test-report.md` |
| environment-fidelity ladder + upgrade gotcha | REL-ENV-1 | `references/beta-rc-testing.md` |
| public testing tooling (blueprint+checklist, README-documents-limits) | REL-PUB-1 | `references/beta-rc-testing.md` |
| external-PR audit (held CI, probe both branches, guards fail once, credit) | REL-EXT-1 | `references/beta-rc-testing.md`, `references/evidence-and-validation.md` |
| compatibility statement = runtime claim | REL-COMPAT-1 | `references/release-documentation.md`, `workflows/test-release.md` |
| evidence & validation standard (ladder, 20-step, prove-by-firing, no-third-door, controls, null-result, escape hatch, safe-proof) | EVID-LADDER-1, EVID-LOOP-1, EVID-FIRE-1, EVID-DOOR-1, EVID-CTRL-1, EVID-NULL-1, EVID-ESC-1, SEC-PROOF-1 | `references/evidence-and-validation.md`, `templates/evidence-bundle.md` |
| fired vs source-attested, claim markers | EVID-MARK-1 | `references/evidence-and-validation.md`, `templates/evidence-bundle.md` |
| audit handoff standard (self-contained, link hygiene, section order, tested-and-cleared, honest gaps, verbatim prompts, accuracy labels) | SEC-HAND-1/2, SEC-LABEL-1, SEC-CLEAR-1 | `workflows/security-audit-handoff.md`, `templates/audit-handoff.md`, `references/security-documentation.md` |
| bare-acknowledgment scrubbing + grep-proof | SEC-SCRUB-1 | `references/security-documentation.md`, `workflows/security-audit-handoff.md`, `scripts/scrub_check.py` |
| disclosure routing + responsible language | SEC-DISC-1, SEC-LANG-1 | `references/security-documentation.md` |
| multi-model adversarial panel | SEC-PANEL-1 | `references/security-documentation.md`, `references/beta-rc-testing.md` |
| remediation verification | SEC-REM-1 | `references/security-documentation.md` |
| docs-site IA (5 sections, a11y/privacy own pages) | ARCH-SITE-1 | `references/information-architecture.md` |
| repo docs split + private SECURITY channel | ARCH-REPO-1 | `references/information-architecture.md`, `references/security-documentation.md` |
| repo-specific lint for recurring findings | GOV-LINT-1 | `references/governance-and-freshness.md` |
| skill-description advice ("when to use") | PKG-DESC-1 | `SKILL.md` |

## B · Shipped file → capabilities it carries → sources

| File | Principal capabilities | Sources |
|---|---|---|
| `SKILL.md` | router, compass, SAFE-*, evidence standards, quality bar, PKG-DESC/DISC/GUARD | all |
| `references/diataxis-foundations.md` | DIA-CORE-2/4/5, DIA-QUAL-*, DIA-WORK-*, DIA-APPLY-1 | S8, S6, S2 |
| `references/compass-and-classification.md` | DIA-CORE-3/6/7, DIA-DIST-1/2, DIA-BOUND-1/2 | S8, S3, S2 |
| `references/tutorials.md` | DIA-TUT-1..13, EVID-EXEC-1 | S8, S4 |
| `references/how-to-guides.md` | DIA-HOW-1..8, WRITE-OUT-1 | S8, S6, S7 |
| `references/reference.md` | DIA-REF-1..6, ARCH-AUTODOC-1 | S8, S4, S7 |
| `references/explanation.md` | DIA-EXP-1..8 | S8, S4 |
| `references/anti-patterns.md` | 5 core violations + all named smells, blur zones | S3, S7, S8 |
| `references/information-architecture.md` | ARCH-IA-*, ARCH-LINK-1, ARCH-AUD-1, ARCH-SITE-1, ARCH-REPO-1, ARCH-TOOL-1, DIA-HIER-1/2/3 | S8, S4, S6, S7, S9 |
| `references/content-types.md` | WRITE-CT-1..8, WRITE-CT-6/7 | S7 |
| `references/style-overrides.md` | WRITE-STYLE-1..6, WRITE-STYLE-OVR-1, PKG-HOUSE-1 | S7, S8, S6 |
| `references/documentation-audits.md` | AUD-MAT-1/2, AUD-PROC-1, AUD-COV pointer | S7, S9 |
| `references/developer-experience.md` | DX-* | S7 |
| `references/governance-and-freshness.md` | GOV-*, ARCH-CODE-1, ARCH-VER-1 | S7, S9 |
| `references/release-documentation.md` | REL-HIER/TRACK/DECAY/CHECK/COMPAT/STABLE | S9, S7 |
| `references/beta-rc-testing.md` | REL-RUN/DOD/ENV/PUB/EXT, SEC-PANEL | S9 |
| `references/evidence-and-validation.md` | EVID-*, AUD-FEAT-2, SEC-PROOF-1, REL-HIER | S9, S2, S4 |
| `references/ui-verification.md` | UI-* | S9 |
| `references/security-documentation.md` | SEC-* | S9 |
| `references/diagrams.md` | DGM-1, DGM-C4-1/2 | S7, S4 |
| `references/accessibility-and-localization.md` | GOV-A11Y-1, GOV-LOC-1/2, AUX-LANG-1 (pointer) | S7, S9, S8, S2 |
| `references/repo-workflow-practices.md` | AUX-COMMIT-1..4, AUX-CI-1/2, AUX-PIN-1..3, AUX-BRANCH-1, AUX-DRAWIO-1, AUX-LANG-1 | S2 (six sibling skills) |
| `references/source-provenance.md` | PKG-CITE/LIC | all |
| `workflows/audit-existing-docs.md` | AUD-INV/CLASS/GAP/PROC, DIA-BOUND-2 | S1, S2, S7, S9 |
| `workflows/plan-new-docs.md` | SAFE-CLEAN/PLAN/ASK/ORDER/README, DIA-WORK-3, ARCH-AUTODOC | S4, S8 |
| `workflows/write-or-revise.md` | WRITE-GEN/MIX/ITER, DIA-WORK-2 | S3, S6, S8 |
| `workflows/restructure-docs.md` | SAFE-GATE/PRES/LINK/INCR, WRITE-MOVE | S1, S2, S4 |
| `workflows/document-a-change.md` | REL-RECEIPT/CHANGE, GOV-DONE | S9, S7 |
| `workflows/validate-claims.md` | AUD-FEAT, EVID-EXEC/FIRE/DOOR | S2, S9, S4 |
| `workflows/verify-ui.md` | UI-* | S9 |
| `workflows/test-release.md` | REL-* | S9 |
| `workflows/security-audit-handoff.md` | SEC-HAND/SCRUB/LABEL/CLEAR | S9 |
| `templates/*` | one per output artifact (see ledger destinations) | S4, S7, S9 |
| `scripts/inventory_docs.py` | AUD-INV-2 | S2, S7 |
| `scripts/check_links.py` | AUD-GAP-1, SAFE-LINK-1 | S7 |
| `scripts/detect_mixed_docs.py` | AUD-CLASS-2 | S2, S3 |
| `scripts/verify_examples.py` | EVID-EXEC-2 | S7, S9, S4 |
| `scripts/compare_ui_labels.py` | UI-DIFF-1 | S9 |
| `scripts/scrub_check.py` | SEC-SCRUB-1 | S9 |
| `scripts/validate_skill.py`, `tests/check_evals.py` | PKG-EVAL-1, TEST-SCHEMA-1 | S2 |
| `tests/evals.json` | TEST-ACT/CLASS/BEHAVE/ADV-1 | prompt + S2 |

## Completeness check
- **All 9 sources appear in index A** with named contributions and concrete destinations.
- **All 21 references, 9 workflows, 12 templates, 7 scripts, and the test suite appear in index B** with the capabilities they carry and their sources.
- **Zero "covered generally" cells.** Every capability ID in `capability-ledger.md` names a destination file; every destination file here names its capabilities and sources.
- **Exclusions** (non-diataxis sibling skills in S2; WordPress-specific literal values in S9) are the only non-retained items, justified at the foot of `capability-ledger.md`.
