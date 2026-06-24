---
name: chrome-extension
description: "Manifest V3 Chrome extension full-development harness. Agent team handles architecture, manifest, service worker, UI, content scripts, security, and Web Store review. Use for 'build a Chrome extension', 'manifest.json', 'content script', 'service worker', 'popup', 'side panel', 'Chrome Web Store release', 'minimize permissions', 'MV3 migration'. Out of scope: Firefox/Safari-only WebExtension forks, full native messaging host app development, malicious scraping or bypass tooling."
---

# Chrome Extension — Manifest V3 Full Development Pipeline

Design, implement, verify, and prepare for store release of production-grade **Manifest V3** extensions end to end.

## Execution Mode

**Agent team** — 5 agents collaborate via `Task` subagent calls and cross-validate deliverables.

## Cursor Native Orchestration Notes

- Delegate specialized work via `Task` subagent calls.
- UI (popup/sidepanel) and background/content can run in parallel `Task` calls (after interface agreement).
- Track progress with `TodoWrite`; organize deliverables in `_workspace/` and the `extension/` code tree.
- Prefer web search or [Chrome Developers](https://developer.chrome.com/docs/extensions) docs for Chrome API and review policy.
- When browser verification is needed, use MCP browser to try loading `chrome://extensions` and confirm behavior.

## MV3 Core Principles (Phase 0)

1. **Service workers are ephemeral** — no global state; `chrome.storage` + cold-start recovery.
2. **Keep content scripts thin** — DOM extract/inject only; business logic in background.
3. **Least privilege** — `activeTab`, `optional_permissions`, specific `host_permissions`.
4. **Async messaging** — on async `onMessage`, use `return true` + `sendResponse`.
5. **No remote code execution** — CSP compliance; sandboxed iframe only for exceptional dynamic execution.
6. **Store release** — prepare `CHROMEWEBSTORE.md` + privacy policy URL.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| extension-architect | `.cursor/agents/extension-architect.md` | MV3 architecture, manifest, folder structure | general-purpose |
| background-runtime-engineer | `.cursor/agents/background-runtime-engineer.md` | Service worker, storage, alarms, API hub | general-purpose |
| ui-builder | `.cursor/agents/ui-builder.md` | popup, side panel, options UI | general-purpose |
| content-integration-engineer | `.cursor/agents/content-integration-engineer.md` | content scripts, scripting, DOM integration | general-purpose |
| extension-reviewer | `.cursor/agents/extension-reviewer.md` | security, permissions, review, final QA | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator)

1. Extract user input:
   - **Features**: what, on which pages/tabs
   - **UI**: popup / side panel / options / none (action only)
   - **Page integration**: content script needed or not, injection timing
   - **Network**: API calls, DNR (block/modify) needed or not
   - **Permission sensitivity**: host scope, tabs, cookies, etc.
   - **Release**: local only / Chrome Web Store
2. Save `_workspace/00_input.md`.
3. Decide execution mode.

### Phase 2: Team Execution

| Order | Work | Owner | Depends | Deliverable |
|-------|------|-------|---------|-------------|
| 1 | Architecture & manifest | architect | none | `_workspace/01_architecture.md`, `extension/manifest.json` skeleton |
| 2a | Background runtime | background | 1 | `_workspace/02_background_runtime.md`, `extension/src/background/` |
| 2b | UI layer | ui-builder | 1 | `_workspace/03_ui_spec.md`, `extension/src/popup/` etc. |
| 2c | Content integration | content | 1 | `_workspace/04_content_integration.md`, `extension/src/content/` |
| 3 | Security & review | reviewer | 1~2c | `_workspace/05_extension_review.md` |

- 2a/2b/2c can run in parallel after **messaging contract** (architect) is fixed.
- On reviewer 🔴, owning agent rework (max 2 rounds).

### Phase 3: Integration

1. `extension/` build and load procedure in README.
2. Cold-start, messaging, and permission scenario test checklist.
3. `CHROMEWEBSTORE.md` draft when releasing to store.

## Recommended Directory Structure

```
extension/
├── manifest.json
├── src/
│   ├── background/service-worker.ts
│   ├── content/
│   ├── popup/
│   ├── sidepanel/          # optional
│   ├── options/            # optional
│   └── core/
│       ├── messaging/
│       ├── storage/
│       └── types/
├── icons/                  # 16/48/128 real PNG or omit in manifest
└── README.md
```

## Request-Scale Modes

| Request pattern | Mode | Agents |
|-----------------|------|--------|
| Full new extension | Full pipeline | all 5 |
| manifest/architecture only | Design mode | architect + reviewer |
| popup/UI only | UI mode | ui-builder + architect + reviewer |
| content script only | Content mode | content + background + reviewer |
| MV2→MV3 migration | Migration mode | architect + background + reviewer |
| store review response | Release mode | reviewer + architect |
| security/permission audit | Review mode | reviewer only |

## Data Handoff Protocol

| Strategy | Path | Purpose |
|----------|------|---------|
| Design docs | `_workspace/` | architecture, specs, review |
| Source | `extension/` | runnable code |
| Store | `CHROMEWEBSTORE.md` | dashboard copy-paste metadata |
| Message contract | `_workspace/message-contract.md` | types & routing (architect creates) |

## Error Handling

| Issue | Response |
|-------|----------|
| State lost after SW idle | storage recovery + idempotent init |
| onMessage no response | `return true`, async IIFE |
| tab.url undefined | `tabs` permission or `activeTab` pattern |
| CSP inline blocked | external .js, no inline script |
| broad host rejected | narrow domains, optional_permissions |
| side panel won't open | onClicked or setPanelBehavior |
| content script not injected | matches, run_at, scripting permission |
| review rejected | justification via webstore-publishing skill |

## Test Scenarios

### Happy path — page summary popup
**Prompt**: "MV3 extension that summarizes current tab body text, popup UI."
**Expected**: activeTab, thin content, background API, message contract, reviewer Go.

### side panel + storage
**Prompt**: "Bookmark side panel, settings on options page."
**Expected**: side panel open trigger, chrome.storage.local, CSP compliance.

### release prep
**Prompt**: "Web Store submission permission cleanup and privacy policy draft."
**Expected**: minimal-permission manifest, CHROMEWEBSTORE.md, reviewer checklist.

## Per-Agent Extended Skills

| Skill | Path | Audience |
|-------|------|----------|
| manifest-v3-blueprint | `.cursor/skills/manifest-v3-blueprint/skill.md` | architect, background |
| extension-security-privacy | `.cursor/skills/extension-security-privacy/skill.md` | architect, reviewer |
| chrome-messaging-patterns | `.cursor/skills/chrome-messaging-patterns/skill.md` | background, ui, content |
| webstore-publishing | `.cursor/skills/webstore-publishing/skill.md` | reviewer, architect |
| extension-testing-debug | `.cursor/skills/extension-testing-debug/skill.md` | background, reviewer |
