# Knowledge Base Builder Harness

조직 지식관리 체계 구축 에이전트 팀 하네스.

## 구조

```
.cursor/
├── agents/
│   ├── knowledge-collector.md
│   ├── taxonomy-designer.md
│   ├── wiki-builder.md
│   ├── search-optimizer.md
│   └── maintenance-planner.md
├── skills/
│   ├── knowledge-base-builder/
│   │   └── skill.md              — 오케스트레이터
│   ├── information-architecture/
│   │   └── skill.md              — 정보 구조 설계 (IA 4대 체계, 카드 소팅, 태그)
│   └── content-lifecycle-manager/
│       └── skill.md              — 콘텐츠 생명주기 (품질 스코어카드, RACI, 감사)
└── CURSOR.md                     — 이 파일
```

## 사용법

Cursor 채팅에서 자연어 요청으로 실행하거나, `/knowledge-base-builder`로 수동 호출하거나, `@.cursor/skills/knowledge-base-builder/skill.md`를 컨텍스트로 첨부해 실행한다.
