# Open Source Launcher Harness

An agent team harness for preparing open source project launches covering code cleanup, documentation, licensing, and community building.

## Structure

```
.cursor/
├── agents/
│   ├── code-organizer.md        — Code organizer (restructuring, refactoring, code standards)
│   ├── doc-writer.md            — Documentation writer (README, contributing guide, API docs, tutorials)
│   ├── license-specialist.md    — License specialist (license selection, compatibility, legal review)
│   ├── community-manager.md     — Community manager (governance, CoC, issue templates, CI/CD)
│   └── launch-reviewer.md       — Launch reviewer (cross-validation, launch readiness, final checklist)
├── skills/
│   ├── open-source-launcher/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── license-compatibility-matrix/
│   │   └── skill.md              — Open source license compatibility guide
│   └── community-health-metrics/
│       └── skill.md              — Open source community health metrics guide
└── CURSOR.md                    — This file
```

## Usage

In Cursor chat, request with `@open-source-launcher`.

## Deliverables

All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_code_organization.md` — Code cleanup plan and results
- `02_documentation.md` — Documentation package (README, guides, etc.)
- `03_license_review.md` — License review and selection
- `04_community_setup.md` — Community setup and governance
- `05_launch_report.md` — Launch review report
- `generated_files/` — Generated files (README, LICENSE, CONTRIBUTING, etc.)
