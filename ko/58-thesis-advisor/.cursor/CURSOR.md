# Thesis Advisor Harness

논문 작성의 주제선정→문헌조사→방법론→집필→교정 에이전트 팀 하네스.

## 구조

```
.cursor/
├── agents/
│   ├── topic-explorer.md
│   ├── literature-analyst.md
│   ├── methodology-expert.md
│   ├── writing-coach.md
│   └── proofreader.md
├── skills/
│   ├── thesis-advisor/
│   │   └── skill.md              — 오케스트레이터
│   ├── research-methodology/
│   │   └── skill.md              — 연구 방법론 (설계 매트릭스, 표본, 타당도·신뢰도)
│   └── academic-writing-style/
│       └── skill.md              — 학술 글쓰기 (논문 구조, 문체, APA 인용)
└── CURSOR.md                     — 이 파일
```

## 사용법

Cursor 채팅에서 자연어 요청으로 실행하거나, `/thesis-advisor`로 수동 호출하거나, `@.cursor/skills/thesis-advisor/skill.md`를 컨텍스트로 첨부해 실행한다.
