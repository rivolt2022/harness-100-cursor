# MLOps Competition Harness

Kaggle/데이콘 같은 데이터 경진대회를 포함해, 문제 정의→피처/모델링→검증→제출→재현 가능한 운영까지 에이전트 팀이 협업하는 하네스.

## 구조

```
.cursor/
├── agents/
│   ├── competition-strategist.md     — 대회 전략가 (문제 구조화, 점수 전략, 시간/리스크 관리)
│   ├── feature-engineer.md           — 피처 엔지니어 (전처리, 피처 생성, 누수 방지)
│   ├── training-optimizer.md         — 학습 최적화 엔지니어 (모델링, 튜닝, 앙상블)
│   ├── validation-submission-analyst.md — 검증/제출 분석가 (CV 설계, 제출 전략, LB 변동 대응)
│   └── mlops-reviewer.md             — MLOps 리뷰어 (재현성, 운영성, 최종 QA)
├── skills/
│   ├── mlops-competition/
│   │   └── skill.md                  — 오케스트레이터
│   ├── leaderboard-strategy/
│   │   └── skill.md                  — 리더보드 전략 (public/private split, shake-up 대응)
│   ├── cv-leakage-guard/
│   │   └── skill.md                  — CV/데이터 누수 방지 가이드
│   └── experiment-tracking-blueprint/
│       └── skill.md                  — 실험 추적/재현성 템플릿
└── CURSOR.md                         — 이 파일
```

## 사용법

Cursor 채팅에서 자연어 요청으로 실행하거나, `/mlops-competition`로 수동 호출하거나, `@.cursor/skills/mlops-competition/skill.md`를 컨텍스트로 첨부해 실행한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 문제/데이터/제약 입력 정리
- `01_competition_plan.md` — 대회 전략 및 실행 계획
- `02_feature_pipeline.md` — 피처/전처리 파이프라인
- `03_training_plan.md` — 모델/튜닝/앙상블 계획
- `04_validation_submission.md` — CV/제출 전략 및 리더보드 분석
- `05_mlops_review.md` — 재현성/운영성 리뷰
- `submission/` — 제출 파일 및 생성 스크립트
