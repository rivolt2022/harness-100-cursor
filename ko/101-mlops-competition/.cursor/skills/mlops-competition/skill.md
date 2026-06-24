---
name: mlops-competition
description: "Kaggle/데이콘 등 데이터 경진대회 대응을 포함한 MLOps 하네스. 문제정의, 피처 엔지니어링, 모델 학습/튜닝, CV 설계, 제출 전략, 리더보드 해석, 재현 가능한 운영 체계를 팀으로 수행한다. '캐글 대회 전략 짜줘', '데이콘 제출 점수 올려줘', 'CV 누수 점검', '앙상블 설계', '대회용 MLOps 파이프라인' 요청에 사용한다."
---

# MLOps Competition — 대회형 MLOps 풀 파이프라인

Kaggle/데이콘 등 데이터 경진대회에서 **오프라인 CV를 신뢰할 수 있는 기준**으로 삼고, 재현 가능한 파이프라인으로 제출까지 운영한다.

## 실행 모드

**에이전트 팀** — 5명이 `Task` 툴로 Subagent를 호출해 협업하고 산출물을 교차 검증한다.

## Cursor 네이티브 오케스트레이션 메모

- 전문 작업은 `Task` 툴로 Subagent를 호출해 위임한다.
- 독립 브랜치(피처 vs 학습)는 여러 `Task` 호출을 한 번에 실행해 병렬 처리한다.
- 진행 및 의존성은 `TodoWrite`로 추적하고 산출물은 `_workspace/`에 정리한다.
- 대회 규칙·메트릭·최신 LB는 웹 검색 또는 MCP로 확인한다(수동 추측 금지).
- Kaggle API/데이터 다운로드가 필요하면 사용자 환경·자격 증명을 먼저 확인한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| competition-strategist | `.cursor/agents/competition-strategist.md` | 문제 구조화, 점수 전략, 일정/리스크, 제출 슬롯 운영 | general-purpose |
| feature-engineer | `.cursor/agents/feature-engineer.md` | 전처리, 피처 생성, fold 내 fit 누수 방지 | general-purpose |
| training-optimizer | `.cursor/agents/training-optimizer.md` | 베이스라인→튜닝→앙상블, 비용 최적화 | general-purpose |
| validation-submission-analyst | `.cursor/agents/validation-submission-analyst.md` | CV 설계, CV-LB 정합성, 제출 검증 | general-purpose |
| mlops-reviewer | `.cursor/agents/mlops-reviewer.md` | 재현성/운영성/규칙 준수 최종 QA | general-purpose |

## 워크플로우

### Phase 0: 대회 원칙 (모든 Phase에 적용)

1. **베이스라인을 즉시 제출**한다. CV와 public LB의 괴리를 조기에 발견한다.
2. **CV가 ground truth**다. CV↔public LB 상관이 약하면(목표 r ≥ 0.85) 모델 개선보다 CV 재설계가 우선이다.
3. **전처리는 fold 내부에서만 fit**한다(scaler, imputer, target encoding 등).
4. **최종 제출은 2개 전략**을 병행한다: (A) public LB 최대화, (B) CV 신뢰 모델.
5. **Private Score 복원 가능**한 코드·환경을 처음부터 설계한다(데이콘 2차 평가 대비).

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **플랫폼**: Kaggle / 데이콘 / 기타
   - **대회 정보**: 평가 메트릭, 제출 형식, 일일 제출 한도, 최종 선택 파일 수
   - **데이터 특성**: 테이블/이미지/텍스트/시계열, IID/그룹/시간 의존
   - **목표**: 상위권/메달/베이스라인/제출 안정화
   - **제약**: GPU/시간/팀 규모/외부 데이터·사전학습 모델 허용 여부
   - **기존 자산** (선택): 노트북, LB 점수, 실험 로그
2. `_workspace/` 디렉토리를 생성한다.
3. 입력을 `_workspace/00_input.md`에 저장한다.
4. 기존 산출물이 있으면 해당 Phase를 건너뛴다.
5. 요청 범위에 따라 **실행 모드**를 결정한다.

### Phase 2: 팀 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 대회 전략 수립 | strategist | 없음 | `_workspace/01_competition_plan.md` |
| 2a | 피처/전처리 설계 | feature | 작업 1 | `_workspace/02_feature_pipeline.md` |
| 2b | 모델/튜닝 설계 | training | 작업 1 | `_workspace/03_training_plan.md` |
| 3 | CV/제출 전략 | validation | 작업 2a, 2b | `_workspace/04_validation_submission.md` |
| 4 | MLOps 리뷰 | reviewer | 작업 1~3 | `_workspace/05_mlops_review.md` |

**팀원 간 소통 흐름:**
- strategist 완료 → feature/training에 메트릭·제출 한도·일정·리스크 전달
- feature 완료 → validation에 split 정책·누수 체크리스트·파이프라인 스니펫 전달
- training 완료 → validation에 모델 후보·CV 점수·앙상블 후보 전달
- validation 완료 → strategist에 LB 괴리·제출 우선순위 전달, reviewer에 검증 결과 전달
- reviewer는 전 산출물 교차 검증. 🔴 필수 수정 시 담당 에이전트에 `Task`로 재작업 요청 → 재검증 (최대 2회)

- 작업 2a/2b는 **병렬** 실행한다.

### Phase 3: 통합 및 제출 준비

1. `submission/`에 제출 생성 스크립트·검증 스크립트·README를 정리한다.
2. 실험 추적 표(MLflow/DVC 또는 스프레드시트)와 제출 파일을 1:1 매핑한다.
3. CV-LB 상관 로그, 최종 제출 후보 2~3개, Go/No-Go를 사용자에게 보고한다.

## CV-LB 정합성 프로토콜

| 단계 | 행동 | 통과 기준 |
|------|------|----------|
| 1 | 단순 베이스라인 1~3개를 early submit | 제출 포맷·메트릭 방향 확인 |
| 2 | CV 점수 vs public LB를 표로 기록 | 상관계수 r 추적 |
| 3 | r < 0.85 또는 부호 불일치 | adversarial validation, split 재설계 |
| 4 | fold 간 std/mean < 20% | 안정적 CV |
| 5 | shake-up 대비 | CV 신뢰 모델을 최종 후보에 반드시 포함 |

**분할 선택 가이드:**

| 데이터 특성 | 권장 CV | 주의 |
|------------|---------|------|
| IID 테이블 | StratifiedKFold (5~10) | target encoding fold 내 |
| 그룹(고객/매장) | GroupKFold / StratifiedGroupKFold | 그룹 누수 |
| 시계열 | TimeSeriesSplit, PurgedKFold+embargo | 미래 정보 누수 |
| 시공간 | Block / spatial holdout | 지역 편향 |

## 작업 규모별 모드

| 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------|----------|---------------|
| "대회 전체 전략+모델링" | 풀 파이프라인 | 5명 전원 |
| "CV/누수 점검만" | 검증 모드 | validation + reviewer |
| "피처 엔지니어링만" | 피처 모드 | feature + reviewer |
| "앙상블/튜닝만" | 학습 모드 | training + validation + reviewer |
| "제출 개선만" | 제출 모드 | validation + strategist + reviewer |
| "최종 점검만" | 리뷰 모드 | reviewer 단독 |
| "데이콘 코드 제출 준비" | 코드 감사 모드 | reviewer + strategist + training |

**기존 파일 활용**: 노트북·LB 로그·제출 CSV가 있으면 `_workspace/`에 복사 후 해당 단계만 실행한다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` | 전략·파이프라인·검증 문서 |
| 코드 기반 | `_workspace/pipeline_code/` | 재현 가능 학습/추론 스크립트 |
| 제출 기반 | `_workspace/submission/` | CSV·검증 로그·생성 명령 |
| 실험 기반 | `_workspace/experiments/` | run 메타데이터, LB 매핑 |
| 메시지 기반 | `Task` Subagent | 수정 요청, 긴급 리스크 공유 |

파일명 컨벤션: `{순번}_{주제}.{md|py|csv}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| CV ≫ LB (오프라인 과대) | 누수·split·메트릭 구현·train/test 분포 차이 조사 |
| CV ≪ LB | 메트릭 방향 오류, 제출 포맷, post-processing 버그 점검 |
| shake-up (public↑ private↓) | public LB 과적합 가정, CV 신뢰 모델로 최종 선택 전환 |
| 일일 제출 한도 소진 | explore 슬롯 중단, exploit·오프라인 실험 집중 |
| 재현 불가 | seed lock, `requirements.txt`/uv lock, 데이터 해시 기록 |
| 제출 실패 | sample_submission 대비 row 수·컬럼·dtype·인덱스 검증 스크립트 |
| 외부 데이터 누수 | 사전학습/외부 데이터와 test 중복 adversarial 검사 |
| GPU 부재 | 경량 모델·서브샘플 CV·Optuna trial 축소 |
| 에이전트 실패 | 1회 재시도 → 실패 시 리뷰에 누락 명시 |

## 테스트 시나리오

### 정상 흐름 — Kaggle 탭ular
**프롬프트**: "Kaggle Playground 시리즈 분류 대회. 상위 10% 목표. XGBoost+LightGBM 앙상블."
**기대 결과**:
- strategist: 메트릭·제출 한도·주간 계획·dual submission 정책
- feature: fold-safe Pipeline, target encoding 가드
- training: 베이스라인 3종 + Optuna + rank blend
- validation: StratifiedKFold, CV-LB 상관 추적표, 제출 검증 체크리스트
- reviewer: 재현성·누수·Go 판단

### 데이콘 코드 감사 흐름
**프롬프트**: "데이콘 본선 끝났고 Private 5위. 코드 제출용으로 파이프라인 정리해줘."
**기대 결과**:
- `/data` 경로 규칙, UTF-8 CSV, Private Score 복원 README
- `pipeline_code/` 단일 진입점(`train.py`/`predict.py` 또는 `main.py`)
- mlops-reviewer: 필수 수정·환경 문서·실행 검증 절차

### 에러 흐름 — CV-LB 불일치
**프롬프트**: "CV 0.92인데 public LB는 0.78이야. 뭐가 문제야?"
**기대 결과**:
- validation 모드 우선 투입
- 누수·split·adversarial validation·메트릭 구현 점검 목록
- 모델 개선 제안 **전에** CV 재설계 권고

## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 | 역할 |
|------|------|----------|------|
| leaderboard-strategy | `.cursor/skills/leaderboard-strategy/skill.md` | strategist, validation | public/private, shake-up, 제출 슬롯 |
| cv-leakage-guard | `.cursor/skills/cv-leakage-guard/skill.md` | feature, validation | split·누수·adversarial validation |
| experiment-tracking-blueprint | `.cursor/skills/experiment-tracking-blueprint/skill.md` | training, reviewer | MLflow/DVC, 제출 매핑 |
| ensemble-strategy | `.cursor/skills/ensemble-strategy/skill.md` | training, validation | blend/stack/rank, 다양성 |
| platform-playbook | `.cursor/skills/platform-playbook/skill.md` | strategist, reviewer | Kaggle vs 데이콘 규칙 |
