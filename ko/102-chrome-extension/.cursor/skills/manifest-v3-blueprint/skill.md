---
name: manifest-v3-blueprint
description: "Manifest V3 구조·서비스 워커 생명주기·manifest.json 필드·DNR·offscreen 가이드. 'manifest v3', 'service worker', 'declarativeNetRequest', 'offscreen document' 요청에 사용한다."
---

# Manifest V3 Blueprint

MV3는 **manifest + service worker + content scripts + UI** 네 축이다. manifest에 선언되지 않은 컴포넌트는 존재하지 않는다.

## manifest.json 스켈레톤

```json
{
  "manifest_version": 3,
  "name": "Extension Name",
  "version": "1.0.0",
  "description": "One-line description for store",
  "permissions": ["storage", "activeTab"],
  "optional_permissions": ["tabs"],
  "host_permissions": ["https://api.example.com/*"],
  "background": {
    "service_worker": "src/background/service-worker.js",
    "type": "module"
  },
  "action": {
    "default_popup": "src/popup/popup.html",
    "default_title": "Open"
  },
  "content_scripts": [{
    "matches": ["https://*.example.com/*"],
    "js": ["src/content/main.js"],
    "run_at": "document_idle"
  }],
  "content_security_policy": {
    "extension_pages": "script-src 'self'; object-src 'self'"
  }
}
```

## 서비스 워커 생명주기

| 특성 | 함의 |
|------|------|
| idle ~30초 후 종료 | 전역 변수 상태 소멸 |
| 이벤트 시 재시작 | cold-start마다 storage에서 복구 |
| DOM 없음 | `window`/`document` 사용 불가 |
| `setInterval` 비권장 | `chrome.alarms` (min period 주의) |

### Idempotent 초기화 패턴

```javascript
// src/background/service-worker.js
async function initialize() {
  const { initialized } = await chrome.storage.session.get('initialized');
  if (initialized) return;
  await setupListeners();
  await chrome.storage.session.set({ initialized: true });
}

chrome.runtime.onInstalled.addListener(initialize);
chrome.runtime.onStartup.addListener(initialize);
initialize();
```

## Storage 선택

| API | 용도 | 지속성 |
|-----|------|--------|
| `chrome.storage.session` | 큐, 임시 세션 | 브라우저 세션 |
| `chrome.storage.local` | 사용자 설정 | 디스크 |
| `chrome.storage.sync` | 설정 동기화(소량) | 계정 동기화 |

항상 `await` 사용. 동시 쓰기는 큐/락 패턴 고려.

## UI 컴포넌트 선언

| UI | manifest | 필수 트리거 |
|----|----------|------------|
| Popup | `action.default_popup` | 아이콘 클릭 |
| Side panel | `side_panel.default_path` | `onClicked` 또는 `setPanelBehavior` |
| Options | `options_ui.page` | 사용자 설정 진입 |
| Omnibox | `omnibox.keyword` | 주소창 키워드 |

**Side panel 주의**: `default_path`만으로는 열리지 않음. popup과 병행 시 popup 버튼으로 `chrome.sidePanel.open()` 호출.

## 아이콘

```json
// ✅ 각 크기별 실제 PNG (16×16, 48×48, 128×128)
"icons": {
  "16": "icons/icon-16.png",
  "48": "icons/icon-48.png",
  "128": "icons/icon-128.png"
}
// ✅ 또는 icons 필드 생략 — Chrome 기본 아이콘
```

존재하지 않는 파일 참조 금지.

## Declarative Net Request (DNR)

`webRequest` blocking 대체. 규칙은 JSON/static ruleset.

```json
"declarative_net_request": {
  "rule_resources": [{
    "id": "ruleset_1",
    "enabled": true,
    "path": "rules/rules.json"
  }]
}
```

동적 규칙은 `chrome.declarativeNetRequest.updateDynamicRules`.

## Offscreen Document

DOM이 필요하지만 SW에 없을 때 (예: clipboard, audio parse):

```javascript
await chrome.offscreen.createDocument({
  url: 'offscreen.html',
  reasons: ['DOM_PARSER'],
  justification: 'Parse HTML off main thread'
});
```

사용 후 `chrome.offscreen.closeDocument()`.

## MV2 → MV3 마이그레이션 체크

- [ ] `background.scripts` → `service_worker` (단일 파일 또는 import)
- [ ] `browser_action` → `action`
- [ ] `web_accessible_resources` 배열 → `{ resources, matches }` 객체
- [ ] CSP 문자열 → `content_security_policy` 객체
- [ ] blocking webRequest → DNR
- [ ] 전역 상태 → storage
- [ ] setTimeout 반복 → alarms

## web_accessible_resources

웹에서 접근 가능해지므로 **최소화**. 필요 시 `matches`로 도메인 제한.

```json
"web_accessible_resources": [{
  "resources": ["injected.css"],
  "matches": ["https://*.example.com/*"]
}]
```
