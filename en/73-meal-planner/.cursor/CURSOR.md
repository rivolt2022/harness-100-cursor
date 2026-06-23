# Meal Planner Harness

A meal planning agent team harness.

## Structure

```
.cursor/
├── agents/
│   ├── nutritionist.md
│   ├── meal-designer.md
│   ├── recipe-writer.md
│   └── shopping-coordinator.md
├── skills/
│   ├── meal-planner/
│   │   └── skill.md              — Orchestrator
│   ├── nutrition-calculator/
│   │   └── skill.md              — Nutrition calculator (macro/micronutrients, daily intake, meal balance)
│   └── ingredient-substitution-engine/
│       └── skill.md              — Ingredient substitution engine (allergy alternatives, seasonal swaps, budget options)
└── CURSOR.md                     — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/meal-planner` manually, or attach `@.cursor/skills/meal-planner/skill.md` as context before execution.
