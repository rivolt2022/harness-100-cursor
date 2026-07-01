# Exam Prep Harness

시험 준비의 출제경향→약점진단→맞춤학습→모의고사→오답분석 에이전트 팀 하네스.

## 구조

```
.cursor/
├── agents/
│   ├── trend-analyst.md
│   ├── diagnostician.md
│   ├── learning-designer.md
│   ├── examiner.md
│   └── error-analyst.md
├── skills/
│   ├── exam-prep/
│   │   └── skill.md              — 오케스트레이터
│   ├── bloom-taxonomy-engine/
│   │   └── skill.md              — Bloom 분류학 (인지 수준별 문항, 학습 활동 매핑)
│   └── error-pattern-analyzer/
│       └── skill.md              — 오답 패턴 분석 (5-Type 분류, 개념 결손 추적)
└── CURSOR.md                     — 이 파일
```

## 사용법

Cursor 채팅창에 `@exam-prep`으로 요청한다.
