# Chrome Extension Harness

Manifest V3 크롬 익스텐션을 **아키텍처 → background → UI → content → 보안·심사**까지 에이전트 팀이 협업하는 하네스.

## 핵심 원칙

1. **Service worker는 휘발성** — `chrome.storage` + cold-start 복구
2. **Content script는 얇게** — DOM만, 로직은 background
3. **최소 권한** — `activeTab`, `optional_permissions`
4. **메시지 비동기** — `return true` + `sendResponse`
5. **스토어** — `CHROMEWEBSTORE.md` + 개인정보 처리방침

## 구조

```
.cursor/
├── agents/
│   ├── extension-architect.md
│   ├── background-runtime-engineer.md
│   ├── ui-builder.md
│   ├── content-integration-engineer.md
│   └── extension-reviewer.md
├── skills/
│   ├── chrome-extension/skill.md          — 오케스트레이터
│   ├── manifest-v3-blueprint/skill.md
│   ├── extension-security-privacy/skill.md
│   ├── chrome-messaging-patterns/skill.md
│   ├── webstore-publishing/skill.md
│   └── extension-testing-debug/skill.md
└── CURSOR.md
```

## 사용법

Cursor 채팅창에 `@chrome-extension`으로 요청한다.

**예시**
- "YouTube 페이지에 다크모드 토글 MV3 익스텐션 만들어줘"
- "MV2 background page를 MV3로 마이그레이션해줘"
- "Web Store 심사 거절됐어 — host_permissions 정당화 작성해줘"
## 산출물

- `_workspace/00_input.md` ~ `05_extension_review.md`
- `_workspace/message-contract.md`
- `extension/` — manifest + 소스
- `CHROMEWEBSTORE.md` — 스토어 listing (출시 시)

## 스킬 빠른 참조

| 상황 | 스킬 |
|------|------|
| manifest / SW | `manifest-v3-blueprint` |
| 권한·CSP | `extension-security-privacy` |
| popup↔background | `chrome-messaging-patterns` |
| 스토어 출시 | `webstore-publishing` |
| SW 안 켜짐 | `extension-testing-debug` |
