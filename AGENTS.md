# Spatial System agent instructions

Created: 2026-11-10T15:41:23Z
Last updated: 2026-11-10T15:55:25Z

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

If a repository index is available, check its scope and freshness before relying
on it. Account for uncommitted changes and files the index does not cover.
If it is absent or stale, use direct repository inspection; do not install or
repair indexing tools unless that work is agreed.

Retrieve selectively, but read enough context to understand affected behavior
and dependencies. Avoid loading full-repository exports by default.

Treat generated indexes and summaries as navigation aids. Verify consequential
implementation claims against current source code. Use human-reviewed project
documents for architectural intent, and surface discrepancies.

Follow the applicable rules in [.rules/rules.mdc](.rules/rules.mdc), including
the testing rule for verification and the co-authoring rule for agent-tool use.

## Instruction maintenance

Keep project policy in `.rules/` and navigation in this file and its index.
Do not assume an agent automatically discovers the custom `.rules/` directory.

When rule files are added, renamed, or retired, update the index and affected
links. Introduce tool-specific entry points only when needed, referencing the
same authoritative rules rather than copying their contents.
