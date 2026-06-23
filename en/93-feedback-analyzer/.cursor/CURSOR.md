# Feedback Analyzer Harness

A customer/employee feedback analysis harness. An agent team collaborates to handle everything from data collection through sentiment analysis, topic classification, trend detection, and insight reporting.

## Structure

```
.cursor/
├── agents/
│   ├── data-collector.md       — Feedback data collection and cleansing
│   ├── sentiment-analyst.md    — Sentiment analysis (positive/negative/neutral, intensity)
│   ├── topic-classifier.md    — Topic classification (categories, keyword clustering)
│   ├── trend-detector.md      — Trend detection (time series, anomaly detection)
│   └── insight-writer.md      — Insight report (action items, prioritization)
├── skills/
│   ├── feedback-analyzer/
│   │   └── skill.md           — Orchestrator (team coordination, workflow, error handling)
│   ├── sentiment-scoring/
│   │   └── skill.md           — Sentiment analysis scoring (sentiment-analyst extension)
│   └── text-analytics-methods/
│       └── skill.md           — Text analytics methodology (topic-classifier extension)
└── CURSOR.md                  — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/feedback-analyzer` manually, or attach `@.cursor/skills/feedback-analyzer/skill.md` as context before execution.
## Outputs

All outputs are saved to the `_workspace/` directory:
- `00_input.md` — Raw feedback data and analysis requirements
- `01_data_collection.md` — Data collection and cleansing results
- `02_sentiment_analysis.md` — Sentiment analysis results
- `03_topic_classification.md` — Topic classification results
- `04_trend_report.md` — Trend analysis results
- `05_insight_report.md` — Comprehensive insight report
