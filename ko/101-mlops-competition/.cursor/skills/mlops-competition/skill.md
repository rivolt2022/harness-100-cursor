---
name: mlops-competition
description: "Kaggle/데이콘 등 데이터 경진대회 대응을 포함한 MLOps 하네스. 문제정의, 피처 엔지니어링, 모델 학습/튜닝, CV 설계, 제출 전략, 리더보드 해석, 재현 가능한 운영 체계를 팀으로 수행한다. '캐글 대회 전략 짜줘', '데이콘 제출 점수 올려줘', 'CV 누수 점검', '앙상블 설계', '대회용 MLOps 파이프라인' 요청에 사용한다."
---

# MLOps Competition — 대회형 MLOps 풀 파이프라인

## 실행 모드

**에이전트 팀** — 5명이 `Task` 툴로 Subagent를 호출해 협업하고 산출물을 교차 검증한다.

## Cursor 네이티브 오케스트레이션 메모

- 전문 작업은 `Task` 툴로 Subagent를 호출해 위임한다.
- 독립 브랜치는 여러 `Task` 호출을 한 번에 실행해 병렬 처리한다.
- 진행 및 의존성은 `TodoWrite`로 추적하고 산출물은 `_workspace/`에 정리한다.
- 외부 또는 실시간 시스템은 수동 웹 작업보다 MCP 도구/리소스를 우선 사용한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| competition-strategist | `.cursor/agents/competition-strategist.md` | 문제 구조화, 점수 전략, 일정/리스크 관리 | general-purpose |
| feature-engineer | `.cursor/agents/feature-engineer.md` | 전처리, 피처 생성, 누수 방지 | general-purpose |
| training-optimizer | `.cursor/agents/training-optimizer.md` | 모델링, 튜닝, 앙상블 최적화 | general-purpose |
| validation-submission-analyst | `.cursor/agents/validation-submission-analyst.md` | CV 설계, 제출 파일 검증, 리더보드 해석 | general-purpose |
| mlops-reviewer | `.cursor/agents/mlops-reviewer.md` | 재현성/운영성/품질 리뷰 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **대회 정보**: Kaggle/데이콘, 리더보드 메트릭, 제출 규칙
   - **데이터 특성**: 테이블/이미지/텍스트/시계열
   - **목표**: 상위권/베이스라인/제출 안정화
   - **제약**: GPU/시간/팀 규모/외부 데이터 허용 여부
2. `_workspace/00_input.md`에 정리한다.
3. 실행 모드를 결정한다.

### Phase 2: 팀 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 대회 전략 수립 | strategist | 없음 | `_workspace/01_competition_plan.md` |
| 2a | 피처/전처리 설계 | feature | 작업 1 | `_workspace/02_feature_pipeline.md` |
| 2b | 모델/튜닝 설계 | training | 작업 1 | `_workspace/03_training_plan.md` |
| 3 | CV/제출 전략 | validation | 작업 2a, 2b | `_workspace/04_validation_submission.md` |
| 4 | MLOps 리뷰 | reviewer | 작업 1~3 | `_workspace/05_mlops_review.md` |

- 작업 2a/2b는 병렬 실행한다.
- reviewer가 🔴 필수 수정을 발견하면 담당 에이전트에 재작업 요청(최대 2회).

### Phase 3: 통합

1. 제출 파일 생성/검증 절차를 `submission/`에 정리한다.
2. 재현성 체크리스트(시드/환경/데이터 버전)를 확정한다.
3. 최종 요약과 다음 제출 액션을 보고한다.

## 작업 규모별 모드

| 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------|----------|---------------|
| "대회 전체 전략+모델링" | 풀 파이프라인 | 5명 전원 |
| "CV/누수 점검만" | 검증 모드 | validation + reviewer |
| "피처 엔지니어링만" | 피처 모드 | feature + reviewer |
| "제출 개선만" | 제출 모드 | validation + strategist + reviewer |
| "최종 점검만" | 리뷰 모드 | reviewer 단독 |

## 에러 핸들링

- **리더보드 급변(shake-up)**: public/private gap 가설 수립 후 CV 재설계.
- **데이터 누수 의심**: 시간/그룹/ID 기반 split으로 즉시 전환.
- **재현 불가**: 환경 잠금(`requirements`/seed/path) 우선 복구.
- **제출 실패**: 포맷/컬럼/인덱스 검증 스크립트 자동 생성.

## 에이전트별 확장 스킬

| 스킬 | 경로 | 대상 |
|------|------|------|
| leaderboard-strategy | `.cursor/skills/leaderboard-strategy/skill.md` | strategist, validation |
| cv-leakage-guard | `.cursor/skills/cv-leakage-guard/skill.md` | feature, validation |
| experiment-tracking-blueprint | `.cursor/skills/experiment-tracking-blueprint/skill.md` | training, reviewer |
