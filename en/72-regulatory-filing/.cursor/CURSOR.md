# Regulatory Filing Harness

A regulatory filing and permit application agent team harness.

## Structure

```
.cursor/
├── agents/
│   ├── requirements-investigator.md
│   ├── document-drafter.md
│   ├── attachment-preparer.md
│   └── submission-verifier.md
├── skills/
│   ├── regulatory-filing/
│   │   └── skill.md              — Orchestrator
│   ├── permit-requirements-db/
│   │   └── skill.md              — Permit requirements database (filing types, required documents, processing timelines)
│   └── form-filling-guide/
│       └── skill.md              — Form filling guide (field-by-field instructions, common mistakes, example entries)
└── CURSOR.md                     — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/regulatory-filing` manually, or attach `@.cursor/skills/regulatory-filing/skill.md` as context before execution.
