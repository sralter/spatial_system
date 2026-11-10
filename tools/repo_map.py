"""Generate a compact file and callable map; use --check to verify freshness.

Git supplies the inventory and ignore policy. The map contains directory-grouped
filenames, syntactic callable locations, and a content fingerprint, not bodies
or inferred architecture. --staged reads index blobs for the pre-commit hook.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

try:
    from repo_symbols import extract_symbols
except ModuleNotFoundError as error:
    raise SystemExit(
        "Repository parsers unavailable. Provision tools/.venv with uv sync --project tools, "
        "then use tools/.venv/bin/python."
    ) from error


MAP_NAME = "repo-map.json"
MAX_FILE_BYTES = 256 * 1024
TEXT_SUFFIXES = frozenset(
    {
        ".md", ".mdc", ".rs", ".py", ".swift", ".sql", ".toml",
        ".json", ".yaml", ".yml", ".sh",
    }
)
TEXT_NAMES = frozenset({"LICENSE", "Makefile", ".gitignore", ".editorconfig", "pre-commit"})
EXCLUDED_ROOTS = ("data/", "benchmarks/", "rust/learn/")
EXCLUDED_PARTS = frozenset({"node_modules", "target", "__pycache__", ".venv", ".env"})


def _git(root: Path, *arguments: str, data: bytes | None = None) -> bytes:
    """Run a bounded Git query without invoking a shell."""
    result = subprocess.run(
        ["git", "-C", str(root), *arguments],
        input=data,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=30,
        check=False,
    )
    if result.returncode and not (
        "check-ignore" in arguments and result.returncode == 1
    ):
        raise RuntimeError(result.stderr.decode(errors="replace").strip())
    return result.stdout


def _inventory(root: Path, staged: bool) -> tuple[dict[bytes, bytes | None], set[bytes]]:
    """Select the working tree or index, respecting the corresponding ignore files."""
    if not staged:
        paths = _git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard")
        sources = {path: None for path in paths.split(b"\0") if path}
        ignored = _git(root, "check-ignore", "--no-index", "-z", "--stdin", data=paths)
        return sources, set(ignored.split(b"\0"))
    sources = {}
    for record in _git(root, "ls-files", "--stage", "-z").split(b"\0"):
        if not record:
            continue
        metadata, path = record.split(b"\t", 1)
        mode, object_id, stage = metadata.split()
        if stage != b"0":
            raise RuntimeError("Resolve unmerged index entries before generating the map")
        if mode in {b"100644", b"100755"}:
            sources[path] = object_id
    git_dir = os.fsdecode(_git(root, "rev-parse", "--absolute-git-dir")).strip()
    with tempfile.TemporaryDirectory(prefix="spatial-map-ignores-") as temporary:
        for path, object_id in sources.items():
            if Path(os.fsdecode(path)).name == ".gitignore":
                destination = Path(temporary) / os.fsdecode(path)
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(_git(root, "cat-file", "blob", os.fsdecode(object_id)))
        ignored = _git(
            Path(temporary), f"--git-dir={git_dir}", f"--work-tree={temporary}",
            "check-ignore", "--no-index", "-z", "--stdin",
            data=b"\0".join(sources) + b"\0" if sources else b"",
        )
    return sources, set(ignored.split(b"\0"))


def build_map(root: Path, staged: bool = False) -> str:
    """Describe eligible working-tree files, including new and edited files.

    The fingerprint covers paths and bytes. Ignored files, links, datasets,
    coursework, legacy benchmarks, locks, and unsupported formats are outside
    coverage. Oversized or binary files with eligible names are reported.
    """
    sources, ignored = _inventory(root, staged)
    directories: dict[str, list[str]] = {}
    symbols: dict[str, list[tuple[str, int]]] = {}
    symbol_warnings: dict[str, str] = {}
    omitted: dict[str, str] = {}
    fingerprint = hashlib.sha256()
    for raw in sorted(sources.keys() - ignored):
        relative = os.fsdecode(raw)
        path = Path(relative)
        if (
            relative == MAP_NAME
            or relative.startswith(EXCLUDED_ROOTS)
            or EXCLUDED_PARTS.intersection(path.parts)
            or (
                path.parts[0].startswith(".")
                and path.parts[0] not in {".rules", ".github", ".githooks"}
                and path.parts[0] not in TEXT_NAMES
            )
            or (path.name.startswith(".") and path.name not in TEXT_NAMES)
            or (path.suffix not in TEXT_SUFFIXES and path.name not in TEXT_NAMES)
        ):
            continue
        object_id = sources[raw]
        if object_id is not None:
            size = int(_git(root, "cat-file", "-s", os.fsdecode(object_id)))
            if size > MAX_FILE_BYTES:
                omitted[relative] = "over 256 KiB"
                continue
            content = _git(root, "cat-file", "blob", os.fsdecode(object_id))
        else:
            source = root / path
            if source.is_symlink() or not source.exists():
                continue
            with source.open("rb") as stream:
                content = stream.read(MAX_FILE_BYTES + 1)
        if len(content) > MAX_FILE_BYTES or b"\0" in content:
            omitted[relative] = (
                "over 256 KiB" if len(content) > MAX_FILE_BYTES else "binary"
            )
            continue
        directories.setdefault(path.parent.as_posix(), []).append(path.name)
        if path.suffix in {".py", ".rs", ".swift", ".sql"}:
            symbols[relative], warning = extract_symbols(path.suffix, content)
            if warning:
                symbol_warnings[relative] = warning
        fingerprint.update(raw + b"\0" + hashlib.sha256(content).digest())
    result = {
        "format_version": 2,
        "fingerprint": fingerprint.hexdigest(),
        "directories": dict(sorted(directories.items())),
        "symbols": symbols,
        "symbol_warnings": symbol_warnings,
        "omitted": omitted,
    }
    return json.dumps(result, indent=2, ensure_ascii=True) + "\n"


def _write_map(root: Path, expected: str) -> None:
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=root, suffix=".tmp", delete=False
        ) as stream:
            temporary = Path(stream.name)
            stream.write(expected)
        temporary.replace(root / MAP_NAME)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def _stage_map(root: Path, expected: str, current: str | None) -> None:
    """Replace only the map's index entry, preserving any unstaged map edits."""
    entries = _git(root, "ls-files", "--stage", "--", MAP_NAME)
    previous = None
    if entries:
        object_id = entries.split()[1].decode("ascii")
        previous = _git(root, "cat-file", "blob", object_id).decode("utf-8")
    object_id = _git(root, "hash-object", "-w", "--stdin", data=expected.encode()).strip()
    if current is None or current == previous:
        _write_map(root, expected)
    _git(
        root, "update-index", "--add", "--cacheinfo",
        f"100644,{object_id.decode('ascii')},{MAP_NAME}",
    )


def main() -> int:
    """Generate the map atomically, or check freshness without writing."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="exit 1 if the map is stale")
    parser.add_argument("--staged", action="store_true", help="read staged source and ignore files")
    parser.add_argument(
        "--stage-map", action="store_true", help="stage only the generated map (hook use)"
    )
    args = parser.parse_args()
    if args.stage_map and (not args.staged or args.check):
        parser.error("--stage-map requires --staged and cannot be combined with --check")
    try:
        root = Path(
            os.fsdecode(_git(Path.cwd(), "rev-parse", "--show-toplevel")).strip()
        )
        destination = root / MAP_NAME
        if destination.is_symlink():
            raise RuntimeError("refusing a symlink as the map destination")
        expected = build_map(root, staged=args.staged)
        current = destination.read_text() if destination.exists() else None
        if args.stage_map:
            _stage_map(root, expected, current)
            print(f"Refreshed and staged {MAP_NAME} from the index")
            return 0
        if current == expected:
            print(f"{MAP_NAME} is current")
            return 0
        if args.check:
            print(
                f"{MAP_NAME} is missing or stale; regenerate it with "
                "tools/.venv/bin/python tools/repo_map.py",
                file=sys.stderr,
            )
            return 1
        _write_map(root, expected)
        print(f"Updated {MAP_NAME} ({len(expected.encode('utf-8')):,} bytes)")
        return 0
    except (OSError, RuntimeError, subprocess.TimeoutExpired) as error:
        print(f"Repository map failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
