# Risk Register Harness

프로젝트 리스크 관리대장: 리스크식별→확률·영향평가→대응전략수립→모니터링계획→상태보고서까지 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```
.cursor/
├── agents/
│   ├── risk-identifier.md        — 리스크 식별 (카테고리별 리스크 도출, RBS)
│   ├── assessment-analyst.md     — 확률·영향 평가 (정량/정성 분석, 리스크 매트릭스)
│   ├── response-strategist.md    — 대응 전략 수립 (회피/전가/완화/수용)
│   ├── monitoring-planner.md     — 모니터링 계획 (KRI, 트리거, 주기)
│   └── report-writer.md          — 상태 보고서 (대시보드, 트렌드, 경영진 보고)
├── skills/
│   ├── risk-register/
│   │   └── skill.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── risk-scoring-matrix/
│   │   └── skill.md              — 리스크 평가 매트릭스 (assessment-analyst 확장)
│   └── risk-response-patterns/
│       └── skill.md              — 리스크 대응 전략 패턴 (response-strategist 확장)
└── CURSOR.md                     — 이 파일
```

## 사용법

Cursor 채팅에서 자연어 요청으로 실행하거나, `/risk-register`로 수동 호출하거나, `@.cursor/skills/risk-register/skill.md`를 컨텍스트로 첨부해 실행한다.
## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_risk_identification.md` — 리스크 식별 보고서
- `02_risk_assessment.md` — 확률·영향 평가 매트릭스
- `03_response_strategy.md` — 대응 전략 계획서
- `04_monitoring_plan.md` — 모니터링 계획
- `05_status_report.md` — 리스크 상태 보고서
