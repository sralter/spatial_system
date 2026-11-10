# Project follow-ups

Created: 2026-11-10T15:55:25Z
Last updated: 2026-11-10T15:55:25Z

Deferred items from the project-rules review. Check the revisit triggers when
scoping new work; entries are not implementation authorization or scheduled jobs.
Update each item's status and link its agreed task or resolution when work begins.

| Item | Status | Revisit trigger | Next bounded action |
|---|---|---|---|
| Repository intelligence | Deferred | Next agent-tool discussion after rules reconciliation | Identify one navigation need; evaluate existing search first, then a small candidate set such as Codeindex and Codeix if useful. Verify current capabilities and language coverage before adoption. |
| Index automation and storage | Deferred | Before adopting an index | Agree on freshness, exclusions, local storage versus versioning, and token costs. Decide whether a watcher, hook, or CI check is warranted. |
| Tool-specific rule loading | Deferred | Before using another agent/editor integration | Verify it reads root AGENTS.md and relevant topic rules. Add an entry point only if required, referencing the authoritative rules. |
| Verification tooling and CI | Deferred | When a component has meaningful code to verify | Select its formatter, linter, tests, and minimal CI checks using existing ecosystem tools. Do not standardize an unused language's stack in advance. |
| Additional navigation or token tools | Deferred | After a specific gap or repeated cost is observed | Evaluate one capability at a time; avoid overlapping memory systems and speculative agent orchestration. |
| Existing tracked datasets | Deferred | Before maintaining or extending the legacy benchmark work | Inventory tracked fixtures/results and propose migration outside Git while retaining provenance. Obtain agreement before moving, deleting, untracking, or rewriting history. |
| Root changelog | Deferred | Next agreed project documentation checkpoint | Establish CHANGELOG.md under the changelog rule with a concise initial entry; do not backfill every historical commit. |
| Durable task records | Deferred | Before the next sprint or task record | Decide which records must be versioned and adjust ignore exceptions narrowly. Only this backlog receives a new tracking exception; other new sprint files remain ignored. |
| Future language directories | Deferred | Before adding project Python or Swift source | Review the existing python/ and swift/ ignore rules and agree on the component layout before exposing intended source files to Git. |
| Logging framework and scrubber | Deferred | When diagnostic needs justify implementation | Scope the logging framework and automatic scrubber, including synthetic privacy checks. Define a separate access boundary if protected values must be inaccessible to the application. |

## Governing guidance

- [Root agent instructions](../AGENTS.md) and the [rule index](../.rules/rules.mdc).
- [Dependencies](../.rules/dependencies.mdc) for tool evaluation and installation.
- [Data and artifacts](../.rules/pipeline_io.mdc) for data preservation and migration.
- [Changelog](../.rules/changelog.mdc) and [logging and errors](../.rules/logging_and_errors.mdc).
