# MLOps Competition Harness

Kaggle/데이콘 같은 데이터 경진대회를 **CV 신뢰 → 재현 가능 파이프라인 → 전략적 제출** 순으로 운영하는 에이전트 팀 하네스.

## 핵심 원칙

1. **CV가 ground truth** — CV↔public LB 상관 r ≥ 0.85 목표
2. **베이스라인 즉시 제출** — CV-LB 괴리 조기 발견
3. **전처리는 fold 내부 fit** — 누수 차단
4. **Dual final submission** — CV champion + public peak
5. **데이콘** — Private Score 복원 가능 코드 패키지

## 구조

```
.cursor/
├── agents/
│   ├── competition-strategist.md     — 대회 전략·일정·제출 슬롯
│   ├── feature-engineer.md           — fold-safe 피처 파이프라인
│   ├── training-optimizer.md         — 베이스라인·튜닝·앙상블
│   ├── validation-submission-analyst.md — CV·LB 정합성·제출 검증
│   └── mlops-reviewer.md             — 재현성·규칙·Go/No-Go
├── skills/
│   ├── mlops-competition/skill.md    — 오케스트레이터
│   ├── leaderboard-strategy/skill.md — public/private·shake-up
│   ├── cv-leakage-guard/skill.md     — split·누수·adversarial
│   ├── experiment-tracking-blueprint/skill.md — MLflow/DVC·제출 매핑
│   ├── ensemble-strategy/skill.md    — blend·stack·다양성
│   └── platform-playbook/skill.md    — Kaggle vs 데이콘 규칙
└── CURSOR.md
```

## 사용법

Cursor 채팅창에 `@mlops-competition`으로 요청한다.

## 산출물

`_workspace/`:
- `00_input.md` — 대회·데이터·제약
- `01_competition_plan.md` — 전략·제출 캘린더·리스크
- `02_feature_pipeline.md` — EDA·fold-safe 파이프라인
- `03_training_plan.md` — 모델·튜닝·앙상블
- `04_validation_submission.md` — CV-LB·제출 검증
- `05_mlops_review.md` — 최종 QA·Go/No-Go
- `pipeline_code/` — 재현 스크립트
- `submission/` — CSV·검증 스크립트
- `experiments/` — run 로그

## 관련 스킬 빠른 참조

| 상황 | 스킬 |
|------|------|
| shake-up / 제출 슬롯 | `leaderboard-strategy` |
| 누수·GroupKFold | `cv-leakage-guard` |
| MLflow·DVC | `experiment-tracking-blueprint` |
| 앙상블 | `ensemble-strategy` |
| 데이콘 코드 제출 | `platform-playbook` |
