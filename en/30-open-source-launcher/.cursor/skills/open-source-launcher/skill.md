---
name: open-source-launcher
description: "open source project launching  code , documentation , license , community until inthisbefore teamthis to countlower  launching pipeline. 'open source items ', 'project open source-ize', 'GitHub items ', 'open source license ', 'README ', 'CONTRIBUTING guide only', 'open source community ', ' ', 'CI/CD setup', 'code items before ' etc. open source launching beforein this  for. READMEonly necessarylower license only necessary inalso supported. , actual  creation, GitHub configuration API , package tree deployment execution this of scope ."
---

# Open Source Launcher — open source project launching pipeline

## Cursor-native Orchestration Notes

- Delegate specialist work using `Task` tool calls to subagents.
- Run independent branches in parallel by issuing multiple `Task` calls together.
- Track progress and dependencies with `TodoWrite`, and keep deliverables in `_workspace/`.
- For external or live systems, prefer MCP tools/resources before manual web steps.
## execution 

**inthisbefore team** — 5peoplethis Task tool calls to subagentsas direct and  verification.

## inthisbefore setup

| inthisbefore | day | role | type |
|---------|------|------|------|
| code-organizer | `.cursor/agents/code-organizer.md` | , refactoring, code | general-purpose |
| doc-writer | `.cursor/agents/doc-writer.md` | README, contributionguide, APIdocumentation | general-purpose |
| license-specialist | `.cursor/agents/license-specialist.md` | license, compatibility, -based | general-purpose |
| community-manager | `.cursor/agents/community-manager.md` | governance, CoC, thistemplate, CI/CD | general-purpose |
| launch-reviewer | `.cursor/agents/launch-reviewer.md` | verification, launchingalso, finallist | general-purpose |

## workflow

### Phase 1:  (this direct count)

1. user from :
    - **project code**: open source-izeto code or 
    - **project target**: library/framework/also/this
    - **upper user**:  this project forto authorization
    - **license ** (optional): upperfor allowed ,   etc.
    - **existing documentation** (optional): this the README, documentation
2. `_workspace/`  project rootin creation
3.  to `_workspace/00_input.md`in 
4. existing daythis  `_workspace/`in and corresponding Phase cases
5. request scopein  **execution  decision**

### Phase 2: team setup and execution

|  |  | responsible | of |  |
|------|------|------|------|--------|
| 1 | code  | code-organizer |  | `_workspace/01_code_organization.md` |
| 2a | documentation  | doc-writer |  1 | `_workspace/02_documentation.md` |
| 2b | license  | license-specialist |  1 | `_workspace/03_license_review.md` |
| 3 | community setup | community-manager |  1, 2a, 2b | `_workspace/04_community_setup.md` |
| 4 | launching review | launch-reviewer |  1~3 | `_workspace/05_launch_report.md` |

 2a(documentation)and 2b(license) **parallel execution**.

**team between  :**
- organizer completed → doc-writerto project ·API before, licenseto dependency  before, communityto /test procedure before
- doc-writer completed → communityto CONTRIBUTINGand this template consistency confirmation request
- license completed → doc-writerto license section content before, communityto CLA/DCO before
- community completed → reviewerto before configuration before
- reviewer all   verification. 🔴 required modification   corresponding inthisbeforeto modification request →  → verification (maximum 2)

### Phase 3: integrated and final 

1. `_workspace/` and `_workspace/generated_files/` within all day confirmation
2. review reportof 🔴 required modificationthis   confirmation
3. final  userto report:
    - code  — `01_code_organization.md`
    - documentation package — `02_documentation.md`
    - license — `03_license_review.md`
    - community — `04_community_setup.md`
    - launching report — `05_launch_report.md`
    - creation day — `generated_files/` (README, LICENSE, CONTRIBUTING, CI etc.)

##  per 

| user request pattern | execution  |  inthisbefore |
|----------------|----------|-------------|
| "open source launching before " | ** launching** | 5people before |
| "README " | **documentation ** | doc-writer + reviewer |
| "license " | **license ** | license-specialist + reviewer |
| "CI/CD setup" | **CI ** | community-manager + reviewer |
| "open source items before " | **review ** | reviewer  |

## data before as

| strategy |  | foralso |
|------|------|------|
| day  | `_workspace/`  | week   and shared |
| creation day | `_workspace/generated_files/` | projectin actual to day |
| message  | Task tool calls to subagents | real-time core information before, modification request |

## error 

| error type | strategy |
|----------|------|
| code provided | day open source project templateand list provided |
| project language people | for configuration(EditorConfig, gitignore)as in progress, languageper   |
| license  |  package or license change   |
| inthisbefore failure | 1 retry → failure  corresponding  this in progress, review reportin  people |
| reviewfrom 🔴  | corresponding inthisbeforein modification request →  → verification (maximum 2) |

## test 

### normal 
****: "this Python CLI also open sourceas itemslower . MIT licenseas, PyPIin deploymentand ."
** result**:
- code: pyproject.toml setup,  -ize,  , .gitignore
- documentation: README(badge+Quick Start+API), CONTRIBUTING, CHANGELOG
- license: MIT , dependency compatibility confirmation, LICENSE day creation
- community: GitHub Actions CI, PyPI deployment workflow, this/PR template
- review: beforeitem  , launching final list

### existing day for 
****: "README this existing, license and CI setup" + README 
** result**:
- existing README `_workspace/generated_files/README.md`as 
- license  + CI  : license + community + reviewer 

### error 
****: "open source , code    "
** result**:
- code   day open source listand template  provided
- "code provided after detailed analysis possible" people
- for project  + documentation template + license  provided


## inthisbeforeper extension 

|  | as | -ize upper inthisbefore | role |
|------|------|-----------------|------|
| license-compatibility-matrix | `.cursor/skills/license-compatibility-matrix/skill.md` | license-specialist | license compatibility , SPDX,  license,  resolution |
| community-health-metrics | `.cursor/skills/community-health-metrics/skill.md` | community-manager, doc-writer | CHAOSS metric, GitHub configuration, this/PR template, contribution onboarding |
