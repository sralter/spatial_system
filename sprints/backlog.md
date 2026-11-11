# Project follow-ups

Created: 2026-11-10T15:55:25Z
Last updated: 2026-11-10T21:57:35Z

Deferred items from the project-rules review. Check the revisit triggers when
scoping new work; entries are not implementation authorization or scheduled jobs.
Update each item's status and link its agreed task or resolution when work begins.

## Backlog maintenance

Mark finished items `Complete` with a concise resolution and a link to the
relevant task, implementation, or decision. Do not delete them simply because
the work is finished. Keep recently completed items visible alongside active
items until a later backlog review.

Preserve unresolved parts explicitly. Implementation finished, human review
pending, and usefulness evaluation pending are distinct states; completing one
does not close the others. Keep remaining work visible in the item's status or
as a linked follow-up.

During backlog reviews, move older completed entries into a `Completed` section.
If that section becomes unwieldy, move its history into a linked yearly archive.
Create the section or archive when needed, retaining resolutions and links.

## Open and recently completed items

| Item | Status | Revisit trigger | Next bounded action |
|---|---|---|---|
| Repository intelligence | Callable map implemented; human review pending | Normal project navigation tasks | Use the file/callable map and context-efficiency guidance. Observe usefulness before adding a reference graph; token savings remain unmeasured. See tools/README.md and the implementation checkpoint below. |
| Index automation and storage | Pre-commit refresh implemented; human review pending | First commit with the tooling update | The hook generates from staged source and stages only repo-map.json. Watchers and CI remain separate decisions; new clones need explicit local hook setup. |
| Tool-specific rule loading | Deferred | Before using another agent/editor integration | Verify it reads root AGENTS.md and relevant topic rules. Add an entry point only if required, referencing the authoritative rules. |
| Verification tooling and CI | Deferred | When a component has meaningful code to verify | Select its formatter, linter, tests, and minimal CI checks using existing ecosystem tools. Do not standardize an unused language's stack in advance. |
| Additional navigation or token tools | Deferred | After a specific gap or repeated cost is observed | Evaluate one capability at a time; avoid overlapping memory systems and speculative agent orchestration. A repository MCP server is deferred; reconsider a query interface over the existing map if map size or repeated retrieval costs justify it. |
| Existing tracked datasets | Deferred | Before maintaining or extending the legacy benchmark work | Inventory tracked fixtures/results and propose migration outside Git while retaining provenance. Obtain agreement before moving, deleting, untracking, or rewriting history. |
| Root changelog | Initial document established; human review pending | Current planning-document checkpoint | See [CHANGELOG.md](../CHANGELOG.md). No historical backfill or release process was introduced. |
| Durable task records | Existing Sprint 1 record reused; future tracking decisions deferred | Before creating a later sprint/task record | The already tracked [Sprint 1 plan](spatial_edge_platform_sprint_1_v0.0.1.md) holds the closeout and provisional sequence. Do not create every future record now; agree on its durable location and a narrow ignore exception when scoped. No ignore rules changed in this checkpoint. |
| Sprint 1 closeout and engine sequence | Plan rewritten; human review pending | Review the rules-aligned Sprint 1 plan | Agree on checkpoint 1A, then complete the evidence/contract discussion. Later SQL, reader, pruning and operating-mode milestones remain proposals, not implementation authorization. See [Sprint 1](spatial_edge_platform_sprint_1_v0.0.1.md). |
| Legacy benchmark runtime footprint | Deferred; keep local artifacts | Separately agreed Sprint 1 inventory checkpoint | Inventory environments, caches, downloaded/generated data and raw runs read-only. Retain the retrospective and evidence; no cleanup, untracking, package adoption or benchmark rerun is authorized. Tracked-data migration remains the separate unresolved item above. |
| Future language directories | Deferred | Before adding project Python or Swift source | Review the existing python/ and swift/ ignore rules and agree on the component layout before exposing intended source files to Git. |
| Logging framework and scrubber | Deferred | When diagnostic needs justify implementation | Scope the logging framework and automatic scrubber, including synthetic privacy checks. Define a separate access boundary if protected values must be inaccessible to the application. |

## Repository intelligence evaluation

Reviewed on 2026-11-10. This checkpoint covers repository inspection, upstream
documentation, and Codeix's language-feature declarations; neither indexer was
installed or executed. It does not establish local correctness or efficiency gains.

The current reusable Rust library remains the small `add` scaffold. Other Rust
files under its package include historical learning notes. Keep those distinct
from engine implementation when selecting a representative navigation task.

| Option | Relevant documented capability | Limitation or adoption cost |
|---|---|---|
| Existing ripgrep and direct inspection | Available now and reads the current working tree directly | Text matches do not establish compiler-resolved references. |
| [Codeindex](https://github.com/maxgfr/codeindex) | Rust/Python parsing, import/call navigation, explicit freshness checks, and scoped exclusions | Swift uses regex fallback; SQL-aware navigation is not established. Its JavaScript toolchain would need a runtime check and installation-cost review. |
| [Codeix](https://github.com/montanetech/codeix) | Portable JSONL index, MCP queries, change watching, and a documented standalone-binary distribution | Its documented language table and [Cargo features](https://github.com/montanetech/codeix/blob/main/Cargo.toml) include Rust/Python but do not list Swift or SQL. Generated text entries can duplicate comments and string literals. |

Retain ordinary search as the baseline. No current evidence requires adopting an
indexer. Codeindex is a candidate for richer structural navigation; Codeix is a
candidate when a portable map is the primary need. Neither is a verified solution
for all planned project languages.

The human's priority order is reduced repeated reading and context/token use,
then a portable repository map, then navigation precision. Tool evaluation should
therefore assess total retrieval overhead, not rank products by feature count.

First agree on retrieval discipline in the root instructions: reuse already-read
context while current, use compact maps and bounded searches to locate material,
expand only when needed for a complete answer, and preserve useful checkpoints.
This behavior is now recorded in the root instructions with compact-map usage.

Before any trial, agree on three representative retrieval questions, a pinned
version, installation location and estimated costs, and output storage. Compare
context supplied, repeated file reads, retrieval round trips, and answer quality.
Use actual token usage only if available; byte or character counts are proxies
and must be labeled as such. Exclude
coursework, legacy benchmarks, datasets, environments, and secrets from project
indexing. Check edits to uncommitted source, missed/ambiguous references, exclusion
behavior, and whether results are more useful than direct search. Token savings
and installation footprint remain unmeasured.

Keep trial outputs local. Watchers, hooks, CI, and persistent MCP registration
remain separate decisions. The goal is one useful capability, not installing
both products or the rest of the previously suggested tool stack.

## Deterministic map implementation

The human delegated the initial file map and subsequently requested callable
locations across Python, Rust, Swift, and SQL, plus automatic commit-time refresh.
The human approved an isolated parser environment and automatic staging of only
the map generated from staged files.

[tools/README.md](../tools/README.md) is the authoritative setup and usage guide.
The parser set is declared in tools/pyproject.toml and tools/uv.lock; the ignored
local environment occupies approximately 18 MB. No external indexer, LLM-assisted
summaries, reference graph, watcher, or CI setup was introduced.

Fifteen tests passed, covering four-language extraction, explicit parse warnings,
working-tree freshness and exclusions, and the real pre-commit hook in isolated
repositories. Hook tests cover partial staging, staged ignore files and generator
modules, preservation of unstaged map edits, and failure without the environment.
Only temporary test repositories received test commits; this project has not been
staged or committed by the agent.

Human review remains pending. Usefulness and token savings remain unmeasured;
evaluate them during normal tasks before adding more retrieval infrastructure.

## Governing guidance

- [Root agent instructions](../AGENTS.md) and the [rule index](../.rules/rules.mdc).
- [Dependencies](../.rules/dependencies.mdc) for tool evaluation and installation.
- [Data and artifacts](../.rules/pipeline_io.mdc) for data preservation and migration.
- [Changelog](../.rules/changelog.mdc) and [logging and errors](../.rules/logging_and_errors.mdc).
