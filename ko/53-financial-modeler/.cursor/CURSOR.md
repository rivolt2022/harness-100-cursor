# Financial Modeler Harness

수익 모델, 비용 구조, 시나리오 분석, 밸류에이션까지 재무 모델링 전 과정을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```
.cursor/
├── agents/
│   ├── revenue-modeler.md        — 수익 모델 설계
│   ├── cost-analyst.md           — 비용 구조 분석
│   ├── scenario-planner.md       — 시나리오 분석
│   ├── valuation-expert.md       — 밸류에이션
│   └── model-reviewer.md         — 교차 검증
├── skills/
│   ├── financial-modeler/
│   │   └── skill.md              — 오케스트레이터
│   ├── dcf-valuation/
│   │   └── skill.md              — DCF 밸류에이션 (WACC, FCFF, 터미널 밸류)
│   ├── sensitivity-analysis/
│   │   └── skill.md              — 민감도 분석 (토네이도, 시나리오 테이블, 브레이크이븐)
│   └── unit-economics/
│       └── skill.md              — 단위 경제학 (LTV/CAC, 공헌이익, 코호트 분석)
└── CURSOR.md                     — 이 파일
```

## 사용법

Cursor 채팅에서 자연어 요청으로 실행하거나, `/financial-modeler`로 수동 호출하거나, `@.cursor/skills/financial-modeler/skill.md`를 컨텍스트로 첨부해 실행한다.
