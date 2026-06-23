# Fitness Program Harness

A fitness program design agent team harness.

## Structure

```
.cursor/
├── agents/
│   ├── program-architect.md
│   ├── exercise-guide.md
│   ├── nutrition-linker.md
│   └── template-builder.md
├── skills/
│   ├── fitness-program/
│   │   └── skill.md              — Orchestrator
│   ├── periodization-engine/
│   │   └── skill.md              — Periodization engine (linear/undulating/block periodization, deload cycles)
│   └── exercise-biomechanics/
│       └── skill.md              — Exercise biomechanics (movement patterns, muscle activation, form cues)
└── CURSOR.md                     — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/fitness-program` manually, or attach `@.cursor/skills/fitness-program/skill.md` as context before execution.
