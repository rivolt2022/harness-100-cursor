---
name: chrome-extension
description: "Manifest V3 크롬 익스텐션 풀 개발 하네스. 아키텍처·manifest·서비스 워커·UI·콘텐츠 스크립트·보안·Web Store 심사까지 에이전트 팀이 수행한다. '크롬 익스텐션 만들어줘', 'manifest.json', 'content script', 'service worker', 'popup', 'side panel', 'Chrome Web Store 출시', '권한 최소화', 'MV3 마이그레이션' 요청에 사용한다. 단, Firefox/Safari 전용 WebExtension 포크, 네이티브 메시징 호스트 앱 전체 개발, 악성 스크래핑/우회 목적은 범위가 아니다."
---

# Chrome Extension — Manifest V3 풀 개발 파이프라인

프로덕션급 **Manifest V3** 익스텐션을 설계·구현·검증·스토어 준비까지 한 번에 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 `Task` 툴로 Subagent를 호출해 협업하고 산출물을 교차 검증한다.

## Cursor 네이티브 오케스트레이션 메모

- 전문 작업은 `Task` 툴로 Subagent를 호출해 위임한다.
- UI(popup/sidepanel)와 background/content는 병렬 `Task` 가능(인터페이스 합의 후).
- 진행은 `TodoWrite`, 산출물은 `_workspace/` 및 `extension/` 코드 트리에 정리한다.
- Chrome API·심사 정책은 웹 검색 또는 [Chrome Developers](https://developer.chrome.com/docs/extensions) 문서를 우선한다.
- 브라우저 검증이 필요하면 MCP 브라우저로 `chrome://extensions` 로드·동작 확인을 시도한다.

## MV3 핵심 원칙 (Phase 0)

1. **서비스 워커는 휘발성** — 전역 변수 상태 금지, `chrome.storage` + cold-start 복구.
2. **콘텐츠 스크립트는 얇게** — DOM 추출/주입만, 비즈니스 로직은 background.
3. **최소 권한** — `activeTab`, `optional_permissions`, 구체적 `host_permissions`.
4. **메시지 비동기** — `onMessage`에서 async 시 `return true` + `sendResponse`.
5. **원격 코드 실행 금지** — CSP 준수, 샌드박스 iframe만 예외적 동적 실행.
6. **스토어 출시** — `CHROMEWEBSTORE.md` + 개인정보 처리방침 URL 준비.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| extension-architect | `.cursor/agents/extension-architect.md` | MV3 아키텍처, manifest, 폴더 구조 | general-purpose |
| background-runtime-engineer | `.cursor/agents/background-runtime-engineer.md` | 서비스 워커, storage, alarms, API 허브 | general-purpose |
| ui-builder | `.cursor/agents/ui-builder.md` | popup, side panel, options UI | general-purpose |
| content-integration-engineer | `.cursor/agents/content-integration-engineer.md` | content scripts, scripting, DOM 연동 | general-purpose |
| extension-reviewer | `.cursor/agents/extension-reviewer.md` | 보안·권한·심사·최종 QA | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터)

1. 사용자 입력 추출:
   - **기능**: 무엇을, 어떤 페이지/탭에서
   - **UI**: popup / side panel / options / 없음(action only)
   - **페이지 연동**: content script 필요 여부, 주입 시점
   - **네트워크**: API 호출, DNR(차단/수정) 필요 여부
   - **권한 민감도**: host 범위, tabs, cookies 등
   - **출시**: 로컬만 / Chrome Web Store
2. `_workspace/00_input.md` 저장.
3. 실행 모드 결정.

### Phase 2: 팀 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 아키텍처·manifest | architect | 없음 | `_workspace/01_architecture.md`, `extension/manifest.json` 스켈레톤 |
| 2a | Background 런타임 | background | 1 | `_workspace/02_background_runtime.md`, `extension/src/background/` |
| 2b | UI 레이어 | ui-builder | 1 | `_workspace/03_ui_spec.md`, `extension/src/popup/` 등 |
| 2c | Content 연동 | content | 1 | `_workspace/04_content_integration.md`, `extension/src/content/` |
| 3 | 보안·심사 리뷰 | reviewer | 1~2c | `_workspace/05_extension_review.md` |

- 2a/2b/2c는 **메시징 계약**(architect) 확정 후 병렬 가능.
- reviewer 🔴 시 담당 에이전트 재작업 (최대 2회).

### Phase 3: 통합

1. `extension/` 빌드·로드 절차 README.
2. cold-start·메시지·권한 시나리오 테스트 체크리스트.
3. 스토어 출시 시 `CHROMEWEBSTORE.md` 초안.

## 권장 디렉터리 구조

```
extension/
├── manifest.json
├── src/
│   ├── background/service-worker.ts
│   ├── content/
│   ├── popup/
│   ├── sidepanel/          # 선택
│   ├── options/            # 선택
│   └── core/
│       ├── messaging/
│       ├── storage/
│       └── types/
├── icons/                  # 16/48/128 실제 PNG 또는 manifest에서 생략
└── README.md
```

## 작업 규모별 모드

| 요청 패턴 | 모드 | 에이전트 |
|----------|------|----------|
| 익스텐션 전체 신규 | 풀 파이프라인 | 5명 |
| manifest/아키텍처만 | 설계 모드 | architect + reviewer |
| popup/UI만 | UI 모드 | ui-builder + architect + reviewer |
| content script만 | 콘텐츠 모드 | content + background + reviewer |
| MV2→MV3 마이그레이션 | 마이그레이션 모드 | architect + background + reviewer |
| 스토어 심사 대응 | 출시 모드 | reviewer + architect |
| 보안·권한 감사 | 리뷰 모드 | reviewer 단독 |

## 데이터 전달 프로토콜

| 전략 | 경로 | 용도 |
|------|------|------|
| 설계 문서 | `_workspace/` | 아키텍처·스펙·리뷰 |
| 소스 | `extension/` | 실행 가능 코드 |
| 스토어 | `CHROMEWEBSTORE.md` | 대시보드 복붙용 메타 |
| 메시지 계약 | `_workspace/message-contract.md` | 타입·라우팅 (architect 생성) |

## 에러 핸들링

| 이슈 | 대응 |
|------|------|
| SW idle 후 상태 유실 | storage 복구 + idempotent init |
| onMessage 응답 없음 | `return true`, async IIFE |
| tab.url undefined | `tabs` 권한 또는 `activeTab` 패턴 |
| CSP inline 차단 | 외부 .js, no inline script |
| broad host 거절 | 도메인 축소, optional_permissions |
| side panel 안 열림 | onClicked 또는 setPanelBehavior |
| content script 미주입 | matches, run_at, scripting 권한 |
| 심사 거절 | webstore-publishing 스킬로 justification |

## 테스트 시나리오

### 정상 — 페이지 요약 popup
**프롬프트**: "현재 탭 본문 요약하는 MV3 익스텐션, popup UI."
**기대**: activeTab, 얇은 content, background API, 메시지 계약, reviewer Go.

### side panel + storage
**프롬프트**: "북마크 사이드패널, 설정은 options 페이지."
**기대**: side panel 오픈 트리거, chrome.storage.local, CSP 준수.

### 출시 준비
**프롬프트**: "Web Store 제출용 권한 정리와 개인정보 처리방침 초안."
**기대**: 최소 권한 manifest, CHROMEWEBSTORE.md, reviewer 체크리스트.

## 에이전트별 확장 스킬

| 스킬 | 경로 | 대상 |
|------|------|------|
| manifest-v3-blueprint | `.cursor/skills/manifest-v3-blueprint/skill.md` | architect, background |
| extension-security-privacy | `.cursor/skills/extension-security-privacy/skill.md` | architect, reviewer |
| chrome-messaging-patterns | `.cursor/skills/chrome-messaging-patterns/skill.md` | background, ui, content |
| webstore-publishing | `.cursor/skills/webstore-publishing/skill.md` | reviewer, architect |
| extension-testing-debug | `.cursor/skills/extension-testing-debug/skill.md` | background, reviewer |
