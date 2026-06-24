---
name: chrome-messaging-patterns
description: "MV3 컴포넌트 간 메시지 패스·타입 계약·에러 처리 패턴. popup/content/background 통신. 'chrome.runtime.sendMessage', '메시지 패싱', 'content script 통신' 요청에 사용한다."
---

# Chrome Messaging Patterns

MV3에서 **popup · content script · service worker**는 서로 다른 컨텍스트다. 직접 함수 호출 불가 — 메시지로만 통신한다.

## 메시지 흐름

```
Popup ──sendMessage──► Service Worker ──tabs.sendMessage──► Content Script
         ◄──response──                    ◄──response──
```

Content script는 대부분 `chrome.*` API 제한 → background에 위임.

## 타입 계약 (권장)

`_workspace/message-contract.md` 또는 `src/core/messaging/types.ts`:

```typescript
export type Message =
  | { type: 'GET_PAGE_TEXT' }
  | { type: 'SAVE_SETTING'; payload: { key: string; value: unknown } }
  | { type: 'API_FETCH'; payload: { url: string; method: string } };

export type ResponseMap = {
  GET_PAGE_TEXT: { text: string };
  SAVE_SETTING: { ok: boolean };
  API_FETCH: { data: unknown };
};
```

## Popup → Background

```javascript
// popup.js
const response = await chrome.runtime.sendMessage({ type: 'GET_PAGE_TEXT' });
```

## Background 핸들러 (async)

```javascript
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  (async () => {
    switch (message.type) {
      case 'GET_PAGE_TEXT': {
        const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        const [{ result }] = await chrome.scripting.executeScript({
          target: { tabId: tab.id },
          func: () => document.body.innerText.slice(0, 50000),
        });
        sendResponse({ text: result });
        break;
      }
      default:
        sendResponse({ error: 'UNKNOWN_TYPE' });
    }
  })();
  return true; // async sendResponse 필수
});
```

## Background → Content

```javascript
const tabId = sender.tab?.id ?? (await chrome.tabs.query({ active: true, currentWindow: true }))[0].id;
const response = await chrome.tabs.sendMessage(tabId, { type: 'HIGHLIGHT_SELECTION' });
```

Content에 리스너 없으면 "Could not establish connection" — 주입 여부 확인.

## Content Script 리스너

```javascript
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'HIGHLIGHT_SELECTION') {
    // DOM 작업 — 가볍게 유지
    sendResponse({ ok: true });
  }
  return true;
});
```

## Long-lived Port (스트림/고빈도)

```javascript
// popup
const port = chrome.runtime.connect({ name: 'stream' });
port.onMessage.addListener(handleChunk);

// background
chrome.runtime.onConnect.addListener((port) => {
  if (port.name !== 'stream') return;
  // ...
});
```

## 흔한 버그

| 증상 | 원인 | 수정 |
|------|------|------|
| sendResponse undefined | async without `return true` | IIFE + return true |
| Connection error | content 미주입 | matches, programmatic inject |
| SW에서 DOM | SW에 document 없음 | content 또는 offscreen |
| 레이스 | 병렬 storage 쓰기 | 큐/직렬화 |

## 관심사 분리

| 레이어 | 책임 |
|--------|------|
| Content | DOM 읽기/쓰기, 이벤트 훅 |
| Background | API, auth, storage, tabs, DNR |
| Popup/Side panel | 표시, 사용자 입력, sendMessage만 |

비즈니스 로직을 content/popup에 두지 않는다.

## core/messaging 래퍼 (선택)

```typescript
export function sendMessage<T extends Message['type']>(
  msg: Extract<Message, { type: T }>
): Promise<ResponseMap[T]> {
  return chrome.runtime.sendMessage(msg);
}
```

타입 안전 + 에러 통일 처리.
