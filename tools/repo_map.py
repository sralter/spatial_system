"""Generate a compact file map; verify it with ``python3 tools/repo_map.py --check``.

Git supplies the inventory and ignore policy. The map contains directory-grouped
filenames and a content fingerprint, not source text or inferred architecture.
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


MAP_NAME = "repo-map.json"
MAX_FILE_BYTES = 256 * 1024
TEXT_SUFFIXES = frozenset(
    {
        ".md", ".mdc", ".rs", ".py", ".swift", ".sql", ".toml",
        ".json", ".yaml", ".yml", ".sh",
    }
)
TEXT_NAMES = frozenset({"LICENSE", "Makefile", ".gitignore", ".editorconfig"})
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
        arguments[0] == "check-ignore" and result.returncode == 1
    ):
        raise RuntimeError(result.stderr.decode(errors="replace").strip())
    return result.stdout


def build_map(root: Path) -> str:
    """Describe eligible working-tree files, including new and edited files.

    The fingerprint covers paths and bytes. Ignored files, links, datasets,
    coursework, legacy benchmarks, locks, and unsupported formats are outside
    coverage. Oversized or binary files with eligible names are reported.
    """
    inventory = _git(
        root, "ls-files", "-z", "--cached", "--others", "--exclude-standard"
    )
    ignored = set(
        _git(root, "check-ignore", "--no-index", "-z", "--stdin", data=inventory).split(b"\0")
    )
    directories: dict[str, list[str]] = {}
    omitted: dict[str, str] = {}
    fingerprint = hashlib.sha256()
    for raw in sorted(set(inventory.split(b"\0")) - ignored - {b""}):
        relative = os.fsdecode(raw)
        path = Path(relative)
        if (
            relative == MAP_NAME
            or relative.startswith(EXCLUDED_ROOTS)
            or EXCLUDED_PARTS.intersection(path.parts)
            or (
                path.parts[0].startswith(".")
                and path.parts[0] not in {".rules", ".github"}
                and path.parts[0] not in TEXT_NAMES
            )
            or (path.name.startswith(".") and path.name not in TEXT_NAMES)
            or (path.suffix not in TEXT_SUFFIXES and path.name not in TEXT_NAMES)
        ):
            continue
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
        fingerprint.update(raw + b"\0" + hashlib.sha256(content).digest())
    result = {
        "format_version": 1,
        "fingerprint": fingerprint.hexdigest(),
        "directories": dict(sorted(directories.items())),
        "omitted": omitted,
    }
    return json.dumps(result, indent=2, ensure_ascii=True) + "\n"


def main() -> int:
    """Generate the map atomically, or check freshness without writing."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="exit 1 if the map is stale")
    args = parser.parse_args()
    try:
        root = Path(
            os.fsdecode(_git(Path.cwd(), "rev-parse", "--show-toplevel")).strip()
        )
        destination = root / MAP_NAME
        if destination.is_symlink():
            raise RuntimeError("refusing a symlink as the map destination")
        expected = build_map(root)
        current = destination.read_text() if destination.exists() else None
        if current == expected:
            print(f"{MAP_NAME} is current")
            return 0
        if args.check:
            print(
                f"{MAP_NAME} is missing or stale; run python3 tools/repo_map.py",
                file=sys.stderr,
            )
            return 1
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", encoding="utf-8", dir=root, suffix=".tmp", delete=False
            ) as stream:
                temporary = Path(stream.name)
                stream.write(expected)
            temporary.replace(destination)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        print(f"Updated {MAP_NAME} ({len(expected.encode('utf-8')):,} bytes)")
        return 0
    except (OSError, RuntimeError, subprocess.TimeoutExpired) as error:
        print(f"Repository map failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
