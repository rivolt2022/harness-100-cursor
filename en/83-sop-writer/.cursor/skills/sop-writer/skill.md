---
name: sop-writer
description: "standard operating procedure(SOP) agent team to processanalysis→procedure document→checklist→training materials→versionmanagementto Korean creation Full pipeline. 'SOP create it', 'standard operating procedurefrom writing', 'work procedurefrom', 'task ', 'operations procedure', 'procedure document writingplease do', 'checklist create it', 'work process document' etc. SOP writing before skill usage. existing process document procedure document·checklist·training materials writing degreeKRW. However, actual BPM whensystem building, workflow specialist development, ISO authentication company versus is outside this skill's scope."
---

# SOP Writer — standard operating procedure Full pipeline

## Cursor-native Orchestration Notes

- Delegate specialist work using `Task` tool calls to subagents.
- Run independent branches in parallel by issuing multiple `Task` calls together.
- Track progress and dependencies with `TodoWrite`, and keep deliverables in `_workspace/`.
- For external or live systems, prefer MCP tools/resources before manual web steps.
## execution mode

**agent team** — 5 agents communicate directly via Task tool calls to subagents and cross-verify each other's work.

## agent composition

| agent | file | role | type |
|---------|------|------|------|
| process-analyst | `.cursor/agents/process-analyst.md` | current work flow analysis, SIPOC, RACI | general-purpose |
| procedure-writer | `.cursor/agents/procedure-writer.md` | stageby procedure document writing, decision-making minutebasis | general-purpose |
| checklist-designer | `.cursor/agents/checklist-designer.md` | execution inspectiontable, quality design | general-purpose |
| training-developer | `.cursor/agents/training-developer.md` | training guide, scenario annual, assessment document | general-purpose |
| version-controller | `.cursor/agents/version-controller.md` | version management, cross-verification | general-purpose |

## workflow

### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **target process**: work/procedure regarding SOPperson
 - **applied scope**: target departmentfrom/team/
 - ** requirement** (optional): related , authentication(ISO, HACCP etc.)
 - **existing document** (optional): current , work technicalfrom, 
2. `_workspace/` Create the directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/`and skip the corresponding Phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | process analysis | analyst | None | `_workspace/01_process_analysis.md` |
| 2 | procedure document writing | writer | task 1 | `_workspace/02_procedure_document.md` |
| 3a | checklist design | designer | task 2 | `_workspace/03_checklists.md` |
| 3b | training materials work | developer | task 2 | `_workspace/04_training_materials.md` |
| 4 | version management and verify | controller | task 3a, 3b | `_workspace/05_version_control.md` |

task 3a(checklist) and 3b(training materials) ** execution**. task 2(procedure document) only dependency.

**teamKRW between flow:**
- analyst complete → writerto process flow+RACI+example deliver, designerto quality degreepoint deliver
- writer complete → designerto verify standard deliver, developerto difficulty stage+actualnumber case deliver
- designer complete → developerto checklist usage deliver
- controller all deliverable cross-verification. 🔴 required revision findings when Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. verify reportConfirm that all critical revisions from the review report have been addressed
3. Report the final summary to the user:
 - process analysis — `01_process_analysis.md`
 - tablelevel procedure document — `02_procedure_document.md`
 - checklist tax — `03_checklists.md`
 - training materials — `04_training_materials.md`
 - version management and verify — `05_version_control.md`

## task scaleby mode

| user request pattern | execution mode | deploy agent |
|----------------|----------|-------------|
| "SOP create it", "procedure document overall" | **Full pipeline** | 5people beforeKRW |
| " process procedure document only " | **procedure document mode** | analyst + writer + controller |
| "checklist only create it" (procedure document provide) | **checklist mode** | designer + controller |
| "training materials create it" (procedure document provide) | **training mode** | developer + controller |
| " procedure document reviewplease do" | **review mode** | controller |

**existing file utilization**: user existing procedure document, etc. provide applicable stage case.

## data deliver protocol

| strategy | method | also |
|------|------|------|
| File-based | `_workspace/` | Store and share major deliverables |
| Message-based | Task tool calls to subagents | Real-time key information transfer, revision requests |

File naming convention: `{}_{agent}_{deliverable}.{extensionspecialist}`

## error handling

| error type | strategy |
|----------|------|
| existing document None | user person based process re-composition, tablelevel reference |
| requirement people | applicable day framework web searchas research |
| agent failure | Retry once -> proceed without that deliverable, verify report specify |
| verifyfrom 🔴 findings | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
| process | process minuteto eacheach SOP creation |

## test scenario

### flow
**Prompt**: " KRW joining processing process SOP create it. personcompanyteam target 50person scale company."
**expected result**:
- process analysis: hiring→joiningfrom→whensystemetc.record→equipmentdegreegrade→training→OJT flow
- procedure document: stageby detailed procedure + RACI + decision-making minutebasis
- checklist: joining before/day/1weekday/1months inspectiontable
- training materials: personcompanyperson responsible training guide + scenario annual + assessment document
- verify: consistency matrix beforeitem confirm

### existing document utilization flow
**Prompt**: " work checklist training materials create it" + file provide
**expected result**:
- process analysis and procedure document writing case
- providedone `_workspace/02_procedure_document.md` organization
- designer + developer + controller deploy

### error flow
**Prompt**: " team work SOP create it, related document "
**expected result**:
- analysis work content regarding userto question
- answer basedas process re-composition
- verify report "user person based writing — current verify needed" specify

## agentby extension skill

| extension skill | | target agent | role |
|----------|------|-------------|------|
| process-mapping | `.cursor/skills/process-mapping/skill.md` | process-analyst | SIPOC, VSM, RACI, Swim Lane mapping method |
| checklist-design | `.cursor/skills/checklist-design/skill.md` | checklist-designer | checklist type, 7principle, quality design |
