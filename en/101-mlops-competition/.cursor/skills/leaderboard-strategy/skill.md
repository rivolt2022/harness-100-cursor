---
name: leaderboard-strategy
description: "Leaderboard strategy for competition settings: public/private split management, shake-up handling, and submission-slot optimization."
---

# Leaderboard Strategy

## Goal
Reduce public-LB overfitting while preserving private-LB stability.

## Checklist
- Track public-private delta continuously.
- Keep a diversified candidate portfolio (not a single model).
- Split submissions into exploration vs exploitation slots.
- Preserve 2-3 robust final candidates.
