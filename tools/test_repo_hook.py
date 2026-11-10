"""Verify the real pre-commit hook in isolated repositories, never the user's index."""

import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


PROJECT = Path(__file__).resolve().parent.parent


class HookTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.git("init", "--quiet")
        self.git("config", "user.name", "Map test")
        self.git("config", "user.email", "map-test@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.git("config", "core.hooksPath", ".githooks")
        (self.root / "tools").mkdir()
        (self.root / ".githooks").mkdir()
        for name in ("repo_map.py", "repo_symbols.py"):
            shutil.copyfile(PROJECT / "tools" / name, self.root / "tools" / name)
        shutil.copyfile(PROJECT / ".githooks/pre-commit", self.root / ".githooks/pre-commit")
        (self.root / ".githooks/pre-commit").chmod(0o755)
        (self.root / "tools/.venv").symlink_to(PROJECT / "tools/.venv", target_is_directory=True)
        (self.root / ".gitignore").write_text("tools/.venv\n")
        (self.root / "query.py").write_text("def staged(): pass\n")
        self.git(
            "add", ".gitignore", "tools/repo_map.py", "tools/repo_symbols.py",
            ".githooks/pre-commit", "query.py",
        )

    def git(self, *arguments, check=True):
        return subprocess.run(
            ["git", "-C", str(self.root), *arguments],
            capture_output=True, text=True, check=check,
        )

    def run_hook(self):
        return subprocess.run(
            [str(self.root / ".githooks/pre-commit")],
            cwd=self.root, capture_output=True, text=True, check=False,
        )

    def entries(self):
        return {
            line.split("\t", 1)[1]: line.split("\t", 1)[0]
            for line in self.git("ls-files", "--stage").stdout.splitlines()
        }

    def test_staged_snapshot_preserves_partial_staging_and_uses_staged_ignores(self):
        before = self.entries()
        (self.root / "query.py").write_text("def unstaged(): pass\n")
        (self.root / "untracked.py").write_text("def untracked(): pass\n")
        (self.root / ".gitignore").write_text("tools/.venv\nquery.py\n")
        result = self.run_hook()
        self.assertEqual(result.returncode, 0, result.stderr)
        after = self.entries()
        after.pop("repo-map.json")
        self.assertEqual(before, after)
        mapped = json.loads(self.git("show", ":repo-map.json").stdout)
        self.assertEqual(mapped["symbols"]["query.py"], [["staged", 1]])
        self.assertNotIn("untracked.py", mapped["symbols"])
        self.assertEqual((self.root / "query.py").read_text(), "def unstaged(): pass\n")

    def test_real_commit_includes_current_map(self):
        self.git("commit", "--quiet", "-m", "Exercise map hook")
        mapped = json.loads(self.git("show", "HEAD:repo-map.json").stdout)
        self.assertEqual(mapped["symbols"]["query.py"], [["staged", 1]])
        self.assertEqual(self.git("status", "--porcelain").stdout, "")

    def test_preserves_unstaged_map_edits(self):
        self.git("commit", "--quiet", "-m", "Initial map")
        output = self.root / "repo-map.json"
        output.write_text('{"local edit": true}\n')
        (self.root / "query.py").write_text("def changed(): pass\n")
        self.git("add", "query.py")
        result = self.run_hook()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(output.read_text(), '{"local edit": true}\n')
        mapped = json.loads(self.git("show", ":repo-map.json").stdout)
        self.assertEqual(mapped["symbols"]["query.py"], [["changed", 1]])

    def test_uses_staged_generator_modules(self):
        (self.root / "tools/repo_symbols.py").write_text("raise RuntimeError('unstaged tool edit')")
        result = self.run_hook()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_environment_blocks_commit_without_staging_changes(self):
        before = self.entries()
        (self.root / "tools/.venv").unlink()
        result = self.git("commit", "--quiet", "-m", "Must fail", check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("tools/.venv is missing", result.stderr)
        self.assertEqual(self.entries(), before)


if __name__ == "__main__":
    unittest.main()
