#!/usr/bin/env python3
"""Compare installed conda package identities/hashes with the explicit lock."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent


def main():
    expected = {line.strip() for line in (ROOT / "environment-osx-arm64.lock").read_text().splitlines()
                if line.startswith("https://")}
    packages = [json.loads(p.read_text()) for p in (ROOT / ".env/conda-meta").glob("*.json")]
    actual = {p["url"] + "#" + p["md5"] for p in packages}
    if not expected or expected != actual:
        raise SystemExit(f"Environment mismatch; missing={sorted(expected-actual)}, extra={sorted(actual-expected)}")
    if Path(sys.prefix).resolve() != (ROOT / ".env").resolve():
        raise SystemExit("Run using .env/bin/python")
    print(f"Verified {len(actual)} package identities and recorded archive hashes")


if __name__ == "__main__":
    main()
