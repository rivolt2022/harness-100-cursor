# API Client Generator Harness

API client SDK generation: a harness in which an agent team collaborates to perform spec parsing, type generation, client code development, testing, and usage documentation.

## Structure

```
.cursor/
├── agents/
│   ├── spec-parser.md       — Spec parser (OpenAPI/GraphQL/gRPC spec analysis, endpoint extraction)
│   ├── type-generator.md    — Type generation (request/response models, enums, unions, generic types)
│   ├── sdk-developer.md     — SDK development (HTTP client, authentication, pagination, retry)
│   ├── test-engineer.md     — Test engineer (unit/integration tests, mocking, snapshots)
│   └── doc-writer.md        — Documentation (README, API reference, usage examples, changelog)
├── skills/
│   ├── api-client-generator/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── openapi-spec-patterns/
│   │   └── skill.md              — API spec analysis patterns guide
│   └── sdk-design-patterns/
│       └── skill.md              — SDK design patterns guide
└── CURSOR.md                — This file
```

## Usage

In Cursor chat, request with `@api-client-generator`.

## Deliverables

All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — User input and API spec information
- `01_spec_analysis.md` — API spec analysis results
- `02_types/` — Generated type definition files
- `03_client/` — SDK client code
- `04_tests/` — Test code
- `05_docs/` — Usage documentation
