---
type: Assignment
track: Backend AI Engineering
week: 2
phase: Foundations
status: 🔴 Ongoing
tags:
  - api
  - crud
date: 14/07/2026
name: Build your first CRUD API
code: BE-01
---

## Goal

Expand the original two-endpoint Go server into a complete in-memory task API while staying with Go's standard `net/http` package.

## Stage mapping


  ```mermaid
  flowchart TD
    S0["<b>Stage 0:</b> Hello server<br/><i>Configurable PORT, HTTP server</i>"]
    S1["<b>Stage 1:</b> Root and health<br/><i>GET /, GET /health</i>"]
    S2["<b>Stage 2:</b> Read<br/><i>GET /tasks, GET /tasks/{id}, 404s</i>"]
    S3["<b>Stage 3:</b> Create<br/><i>POST /tasks, validation, 201</i>"]
    S4["<b>Stage 4:</b> Update & Delete<br/><i>PUT/DELETE /tasks/{id}</i>"]
    S5["<b>Stage 5:</b> Swagger UI<br/><i>OpenAPI, /docs</i>"]
    S6["<b>Stage 6:</b> Publish & Docs<br/><i>README, tests, CI, Docker</i>"]
    E["<b>Extras:</b> Advanced Features<br/><i>Filters, stats, reset, mutex</i>"]

    S0 ==> S1 ==> S2 ==> S3 ==> S4 ==> S5 ==> S6 ==> E
    
    style S0 fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style S1 fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style S2 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style S3 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style S4 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style S5 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style S6 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style E fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
  ```

## Design decisions

- **Go instead of the two suggested lanes:** the assignment's HTTP and CRUD requirements are language-independent, and the previous project already uses Go.

- **Standard library only:** Go 1.22 supports method-aware route patterns and path wildcards directly in `net/http`.

- **In-memory storage:** the store deliberately resets on process restart, matching the Week 2 learning goal.

- **Pointer fields for updates:** `*bool` distinguishes an omitted `done` field from an explicit `false` value.

- **Strict JSON:** unknown fields, malformed JSON, empty bodies and multiple JSON values are rejected with status 400.

- **Concurrency safety:** a mutex prevents data races when multiple requests access the task list.

- **OpenAPI as a checked-in artifact:** the contract is reviewable at `api/openapi.json` and rendered at `/docs`.

  

## Manual verification checklist



```bash

go run .

```

  

In a second terminal:

```bash

./scripts/demo.sh

```

Then verify:

- `GET /tasks/99` returns 404 and JSON.

- `POST /tasks` with `{}` returns 400 and JSON.

- `DELETE /tasks/{id}` returns 204 with an empty body.

- `/docs` lists and executes the full CRUD cycle.

- After creating tasks, restarting the process restores only the three seed tasks.


## Mortality experiment

Tasks are stored in a Go slice inside the running process. Restarting the server creates a new store from `seedTasks`, so anything created or updated during the previous run disappears. A database will solve this persistence problem in the next stage of the backend track.