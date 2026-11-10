# Spatial System agent instructions

Created: 2026-11-10T15:41:23Z
Last updated: 2026-11-10T16:40:55Z

## Start here

Read [.rules/rules.mdc](.rules/rules.mdc) to find applicable project guidance.

For project work, read these baseline rules:

- [Co-authoring protocol](.rules/coauthoring_protocol.mdc).
- [Architecture](.rules/architecture.mdc).
- [Security](.rules/security.mdc).
- [Documentation](.rules/documentation_core.mdc).

Read and follow topic-specific rules before performing the corresponding work,
even when they are not automatically attached by the agent tool. Recheck the index
when the task changes scope. The linked documents are authoritative; this entry
point does not replace them.

Before scoping new work, check [project follow-ups](sprints/backlog.md) for relevant
revisit triggers. A backlog entry records deferred work; it does not authorize it.

## Coursework

For coursework, follow its applicable course AGENTS.md and syllabus.
The existing [Rust course instructions](rust/learn/0-rust-for-geospatial/AGENTS.md)
apply within that course directory and its descendants.

Do not extend one course's teaching instructions to other courses automatically.
Use the project architecture rule for the boundary between coursework and
project implementation.

## Repository discovery

Before changing project code, locate the relevant implementation, callers,
tests, and configuration using focused searches or available navigation tools.

Use [repo-map.json](repo-map.json) for compact directory and file orientation.
It contains paths and a freshness fingerprint, not source bodies, symbols, or
architectural claims. Coverage follows Git ignores and the generator's explicit
exclusions, including `data/`, `benchmarks/`, `rust/learn/`, environment/build
artifacts, links, and unsupported file formats. Eligible oversized or binary files
are reported in `omitted`. Files listed within a package may still be historical
learning material; verify their role against the architecture and source.

From the repository root, check freshness before relying on the map:

```sh
python3 tools/repo_map.py --check
```

If it is missing or stale, regenerate it with `python3 tools/repo_map.py`, then
read the relevant map entries. The generator uses current working-tree content,
including eligible untracked files. `--check` does not write. Concurrent source
edits can invalidate the snapshot; recheck when needed.

The [generator](tools/repo_map.py) uses Git and Python's standard library.
Its focused checks run with
`python3 -m unittest discover -s tools -p 'test_repo_map.py' -v`.

Treat generated indexes and summaries as navigation aids. Verify consequential
implementation claims against current source code. Use human-reviewed project
documents for architectural intent, and surface discrepancies.

Follow the applicable rules in [.rules/rules.mdc](.rules/rules.mdc), including
the testing rule for verification and the co-authoring rule for agent-tool use.

## Context efficiency

Reuse instructions and source material already read while they remain current
and available in context. Re-read when relevant files change, context is lost,
or uncertainty requires checking.

Start discovery with the repository map, filenames, symbols, or focused search
results. Read relevant sections before expanding to whole files or directories.

Keep tool output bounded and exclude irrelevant material. Expand deliberately
when additional context is needed for correctness; avoid repeatedly retrieving
the same content through different tools.

Use checkpoints to preserve decisions, unresolved questions, relevant file
locations, and the next action. Link to authoritative explanations rather than
copying large passages.

Treat reduced context use as a means to complete work accurately, not a reason
to omit necessary investigation or verification.

## Instruction maintenance

Keep project policy in `.rules/` and navigation in this file and its index.
Do not assume an agent automatically discovers the custom `.rules/` directory.

When rule files are added, renamed, or retired, update the index and affected
links. Introduce tool-specific entry points only when needed, referencing the
same authoritative rules rather than copying their contents.
