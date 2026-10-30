#!/usr/bin/env python3
"""Download only licensed, checksummed assets in datasets.json, under its byte cap."""
import json
from pathlib import Path
import urllib.request

from baseline import ROOT, sha256


def main():
    manifest = json.loads((ROOT / "datasets.json").read_text())
    used = 0
    for entry in manifest["datasets"]:
        if "url" not in entry:
            continue
        if not entry.get("sha256") or not entry.get("license_source"):
            raise ValueError("Review license and checksum before downloading")
        path = ROOT / entry["path"]
        if path.is_file():
            if sha256(path) != entry["sha256"]:
                raise ValueError(f"Existing asset checksum mismatch: {path}")
            used += path.stat().st_size
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            temporary = path.with_suffix(path.suffix + ".part")
            try:
                with urllib.request.urlopen(entry["url"], timeout=60) as source, temporary.open("wb") as target:
                    while chunk := source.read(1024 * 1024):
                        used += len(chunk)
                        if used >= manifest["download_budget_bytes"]:
                            raise ValueError("Point-cloud download budget exceeded")
                        target.write(chunk)
                if sha256(temporary) != entry["sha256"]:
                    raise ValueError("Downloaded asset checksum mismatch")
                temporary.replace(path)
            finally:
                temporary.unlink(missing_ok=True)
        if used >= manifest["download_budget_bytes"]:
            raise ValueError("Point-cloud download budget exceeded")
        print(f"Verified {entry['id']}: {path.stat().st_size:,} bytes; {entry['license']}")
    print(f"Total public point-cloud assets: {used:,} bytes")


if __name__ == "__main__":
    main()
