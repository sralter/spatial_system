# Repository map tooling

Created: 2026-11-10T17:00:44Z
Last updated: 2026-11-10T17:00:44Z

The [repository map](../repo-map.json) provides compact file and callable locations
for agents and humans. It is a syntactic navigation aid; current source remains
the authority for implementation claims.

## Setup

Use the existing project Python and uv from the repository root:

```sh
uv sync --project tools --python python3 --no-managed-python
```

The [manifest](pyproject.toml) and lockfile fix the parser set because grammar
changes can change extracted symbols. Python uses its standard AST; Rust, Swift,
and SQL use Tree-sitter grammars. The installed environment is `tools/.venv`,
which is ignored by Git. The initial macOS ARM64 setup downloaded approximately
1.7 MB of wheels and occupied approximately 18 MB locally.

## Map entries and coverage

`directories` groups filenames by directory. `symbols` maps source paths to
`[qualified_name, one_based_line]` pairs. For example, an entry under
`tools/repo_map.py` named `build_map` identifies `tools/repo_map.py:build_map`.
Classes, modules, implementations, protocols, and extensions qualify callable
names; overloads retain separate entries and line numbers.

Python covers declared functions, async functions, nested functions, and methods.
Rust covers function definitions and trait requirements. Swift covers functions,
methods, protocol requirements, initializers, deinitializers, and subscripts.
SQL covers declared functions and procedures; query calls are not declarations.

Non-code files remain in the file inventory without fabricated callable entries.
The map excludes datasets, legacy benchmarks, `rust/learn/`, ignored files,
environment/build artifacts, links, and unsupported formats. Eligible oversized
or binary files appear in `omitted`. Source files within an existing package can
still be historical learning material.

`symbol_warnings` reports parse errors rather than claiming complete coverage.
Macros, runtime-generated callables, SQL dialect differences, and embedded bodies
can limit extraction. This map does not resolve types, calls, or references.

## Manual refresh and verification

```sh
tools/.venv/bin/python tools/repo_map.py
tools/.venv/bin/python tools/repo_map.py --check
tools/.venv/bin/python tools/repo_map.py --staged --check
tools/.venv/bin/python -m unittest discover -s tools -p 'test_repo_*.py' -v
```

The default view includes eligible tracked and untracked working-tree files.
`--staged` reads index blobs and staged ignore files. Equivalent inputs produce
the same map; no wall-clock timestamp is embedded. Checks exit 1 for a stale or
missing map without rewriting it. The fingerprint covers included paths and bytes.

## Automatic refresh at commit

The tracked [.githooks/pre-commit](../.githooks/pre-commit) refreshes and stages
only `repo-map.json`, using the staged generator modules and staged source.
It preserves other index entries, partial staging, and existing unstaged map edits.
If map edits are preserved, its working-tree copy may remain different from the
newly staged map. A normal working-tree check can also report stale after a
partial commit; regenerate when the current working-tree view is needed.

There is no background watcher. The hook does not install dependencies or access
the network. Missing setup or a generator failure blocks the commit with an error.
Map parse warnings are recorded, not treated as compiler-validation failures.

For a new clone, inspect existing hook configuration before opting in:

```sh
git config --get core.hooksPath
git config --local core.hooksPath .githooks
```

Do not overwrite an existing hook setup without agreement. Git clones do not copy
this repository-local configuration. The initial tooling commit must include both
`tools/repo_map.py` and `tools/repo_symbols.py` in the index so the hook can run its
staged modules. Normal Git staging and commit ownership follow
[the commit rule](../.rules/documentation_commits.mdc).
