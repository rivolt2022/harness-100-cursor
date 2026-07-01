# Chrome Extension Harness

Agent-team harness for Manifest V3 Chrome extensions: **architecture → background → UI → content → security & review**.

## Core Principles

1. **Service workers are ephemeral** — `chrome.storage` + cold-start recovery
2. **Keep content scripts thin** — DOM only; logic in background
3. **Least privilege** — `activeTab`, `optional_permissions`
4. **Async messaging** — `return true` + `sendResponse`
5. **Store** — `CHROMEWEBSTORE.md` + privacy policy

## Structure

```
.cursor/
├── agents/
│   ├── extension-architect.md
│   ├── background-runtime-engineer.md
│   ├── ui-builder.md
│   ├── content-integration-engineer.md
│   └── extension-reviewer.md
├── skills/
│   ├── chrome-extension/skill.md          — orchestrator
│   ├── manifest-v3-blueprint/skill.md
│   ├── extension-security-privacy/skill.md
│   ├── chrome-messaging-patterns/skill.md
│   ├── webstore-publishing/skill.md
│   └── extension-testing-debug/skill.md
└── CURSOR.md
```

## Usage

In Cursor chat, request with `@chrome-extension`.

**Examples**
- "Build an MV3 extension with a dark-mode toggle on YouTube pages"
- "Migrate MV2 background page to MV3"
- "Web Store review rejected — write host_permissions justification"
## Deliverables

- `_workspace/00_input.md` ~ `05_extension_review.md`
- `_workspace/message-contract.md`
- `extension/` — manifest + source
- `CHROMEWEBSTORE.md` — store listing (for release)

## Skill Quick Reference

| Situation | Skill |
|-----------|-------|
| manifest / SW | `manifest-v3-blueprint` |
| permissions / CSP | `extension-security-privacy` |
| popup↔background | `chrome-messaging-patterns` |
| store release | `webstore-publishing` |
| SW won't start | `extension-testing-debug` |
