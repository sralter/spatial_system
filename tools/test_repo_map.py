"""Check inventory exclusions, determinism, and working-tree freshness."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from repo_map import build_map


SCRIPT = Path(__file__).with_name("repo_map.py").resolve()


class RepositoryMapTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        subprocess.run(["git", "init", "--quiet", str(self.root)], check=True)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return path

    def run_cli(self, *arguments):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *arguments],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_deterministic_and_no_source_bodies(self):
        self.write("src/b.rs", 'pub fn named() { let body = "UNIQUE_BODY_SENTINEL"; }')
        self.write("src/a.rs", "pub fn a() {}")
        first = build_map(self.root)
        self.assertEqual(first, build_map(self.root))
        self.assertEqual(json.loads(first)["directories"], {"src": ["a.rs", "b.rs"]})
        self.assertEqual(json.loads(first)["symbols"]["src/b.rs"], [["named", 1]])
        self.assertNotIn("UNIQUE_BODY_SENTINEL", first)

    def test_excludes_data_learning_benchmarks_ignored_files_and_links(self):
        self.write(".gitignore", "ignored/\n")
        for name in (
            "data/raw/data.json", "rust/learn/lesson.rs", "benchmarks/run.py",
            "ignored/private.py", ".aws/secret.json", "target/generated.rs",
            ".env.json",
        ):
            self.write(name, "sensitive content")
        tracked = self.write("ignored/tracked.py", "sensitive tracked content")
        subprocess.run(
            ["git", "-C", str(self.root), "add", "--force", str(tracked)], check=True
        )
        self.write("src/good.rs", "fn good() {}")
        self.write(".rules/policy.mdc", "# Policy")
        (self.root / "src/link.rs").symlink_to(self.root / "ignored/private.py")
        self.assertEqual(
            json.loads(build_map(self.root))["directories"],
            {".": [".gitignore"], ".rules": ["policy.mdc"], "src": ["good.rs"]},
        )

    def test_freshness_covers_edits_additions_deletions_and_check_does_not_write(self):
        source = self.write("src/main.rs", "fn old() {}")
        output = self.root / "repo-map.json"
        self.assertEqual(self.run_cli("--check").returncode, 1)
        self.assertFalse(output.exists())
        self.assertEqual(self.run_cli().returncode, 0)
        original = output.read_bytes()
        self.assertEqual(self.run_cli("--check").returncode, 0)
        source.write_text("fn new() {}")
        self.assertEqual(self.run_cli("--check").returncode, 1)
        self.assertEqual(output.read_bytes(), original)
        self.assertEqual(self.run_cli().returncode, 0)
        self.write("src/added.rs", "fn added() {}")
        self.assertEqual(self.run_cli("--check").returncode, 1)
        self.assertEqual(self.run_cli().returncode, 0)
        source.unlink()
        self.assertEqual(self.run_cli("--check").returncode, 1)

    def test_reports_oversized_and_binary_files(self):
        self.write("large.py", "x" * (256 * 1024 + 1))
        self.write("binary.rs", "\0binary")
        result = json.loads(build_map(self.root))
        self.assertEqual(result["directories"], {})
        self.assertEqual(
            result["omitted"], {"binary.rs": "binary", "large.py": "over 256 KiB"}
        )

    def test_refuses_linked_output_without_overwriting_its_target(self):
        target = self.write("original.txt", "preserve me")
        (self.root / "repo-map.json").symlink_to(target)
        self.assertEqual(self.run_cli().returncode, 1)
        self.assertEqual(target.read_text(), "preserve me")


if __name__ == "__main__":
    unittest.main()
