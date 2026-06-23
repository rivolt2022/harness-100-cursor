# Meal Planner Harness

식단 관리의 영양분석→식단설계→레시피→장보기목록→조리가이드를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```
.cursor/
├── agents/
│   ├── nutritionist.md        — 영양 분석 (영양소 요구량, 식이제한, 목표 설정)
│   ├── meal-designer.md       — 식단 설계 (일간/주간 식단표, 칼로리·영양소 배분)
│   ├── recipe-writer.md       — 레시피 작성 (재료, 조리법, 영양정보, 대체재료)
│   └── shopping-coordinator.md — 장보기·조리 가이드 (장보기목록, 조리순서, 밀프렙)
├── skills/
│   ├── meal-planner/
│   │   └── skill.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── nutrition-calculator/
│   │   └── skill.md           — 영양소 계산 엔진 (nutritionist, meal-designer용)
│   └── ingredient-substitution-engine/
│       └── skill.md           — 식재료 대체 엔진 (recipe-writer용)
└── CURSOR.md                  — 이 파일
```

## 사용법

Cursor 채팅에서 자연어 요청으로 실행하거나, `/meal-planner`로 수동 호출하거나, `@.cursor/skills/meal-planner/skill.md`를 컨텍스트로 첨부해 실행한다.
## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_nutrition_analysis.md` — 영양 분석 보고서
- `02_meal_plan.md` — 식단표
- `03_recipes.md` — 레시피 모음
- `04_shopping_list.md` — 장보기 목록
- `05_cooking_guide.md` — 조리 가이드 및 밀프렙 플랜
