---
name: chrome-messaging-patterns
description: "MV3 inter-component message passing, type contracts, and error-handling patterns. popup/content/background communication. Use for 'chrome.runtime.sendMessage', 'message passing', 'content script communication' requests."
---

# Chrome Messaging Patterns

In MV3, **popup · content script · service worker** live in separate contexts. No direct function calls — messages only.

## Message Flow

```
Popup ──sendMessage──► Service Worker ──tabs.sendMessage──► Content Script
         ◄──response──                    ◄──response──
```

Content scripts have limited `chrome.*` APIs → delegate to background.

## Type Contract (Recommended)

`_workspace/message-contract.md` or `src/core/messaging/types.ts`:

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

## Background Handler (async)

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
  return true; // required for async sendResponse
});
```

## Background → Content

```javascript
const tabId = sender.tab?.id ?? (await chrome.tabs.query({ active: true, currentWindow: true }))[0].id;
const response = await chrome.tabs.sendMessage(tabId, { type: 'HIGHLIGHT_SELECTION' });
```

"No Could not establish connection" if no content listener — verify injection.

## Content Script Listener

```javascript
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'HIGHLIGHT_SELECTION') {
    // DOM work — keep lightweight
    sendResponse({ ok: true });
  }
  return true;
});
```

## Long-lived Port (stream / high frequency)

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

## Common Bugs

| Symptom | Cause | Fix |
|---------|-------|-----|
| sendResponse undefined | async without `return true` | IIFE + return true |
| Connection error | content not injected | matches, programmatic inject |
| DOM in SW | no document in SW | content or offscreen |
| race | parallel storage writes | queue/serialize |

## Separation of Concerns

| Layer | Responsibility |
|-------|----------------|
| Content | DOM read/write, event hooks |
| Background | API, auth, storage, tabs, DNR |
| Popup/Side panel | display, user input, sendMessage only |

Do not put business logic in content/popup.

## core/messaging Wrapper (Optional)

```typescript
export function sendMessage<T extends Message['type']>(
  msg: Extract<Message, { type: T }>
): Promise<ResponseMap[T]> {
  return chrome.runtime.sendMessage(msg);
}
```

Type safety + unified error handling.
