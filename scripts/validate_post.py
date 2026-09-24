#!/usr/bin/env python3
"""Publish gate: validate the newest devlog post against session artifacts.

Enforces the HANDOFF.md §4/§8 contract mechanically:
  0. frontmatter parses cleanly (no duplicate mapping keys — js-yaml parity)
  1. frontmatter metrics are a subset of session_report metrics and match
  2. archetype differs from the previous post's archetype (rotation rule)
  3. commit_sha is a real commit in this repository
  4. featured_image, when present, resolves to an existing file
  5. status pass requires tests_passed >= 1 in the session report

Exit 0 = post is publishable; exit 1 = reject with the exact reason.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

REPO = Path(__file__).resolve().parent.parent
POST_DIR = REPO / "blog" / "src" / "content" / "blog"
REPORT = REPO / "temp" / "session_report.json"
ASSET_ROOT = REPO / "blog" / "src" / "assets"

REQUIRED = ("title", "pubDate", "task_id", "archetype", "status", "metrics", "commit_sha")


class _UniqueKeyLoader(yaml.SafeLoader):
    """SafeLoader that rejects duplicate mapping keys (js-yaml/Astro parity)."""

    def construct_mapping(self, node, deep=False):
        keys = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in keys:
                raise ValueError(f"duplicate mapping key: {key!r}")
            keys.add(key)
        return super().construct_mapping(node, deep)


def fm(text: str) -> dict:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        raise ValueError("no frontmatter block")
    if yaml is not None:
        return yaml.load(m.group(1), Loader=_UniqueKeyLoader)
    out: dict = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip()
    return out


def newest_posts(n: int = 2) -> list[tuple[Path, dict]]:
    posts = sorted(POST_DIR.glob("*.md"), key=lambda p: p.name, reverse=True)
    out = []
    for p in posts[:n]:
        out.append((p, fm(p.read_text(encoding="utf-8"))))
    return out


def fail(msg: str) -> None:
    print(f"REJECT: {msg}")
    sys.exit(1)


def main() -> None:
    posts = newest_posts(2)
    if not posts:
        fail("no posts found in blog/src/content/blog/")
    path, meta = posts[0]
    print(f"newest post: {path.name}")

    for key in REQUIRED:
        if key not in meta:
            fail(f"missing required frontmatter key: {key}")

    report = json.loads(REPORT.read_text(encoding="utf-8")) if REPORT.exists() else None

    # 1. metrics subset-match against the session report (when one exists)
    if report is not None:
        rm = report.get("metrics", {}) or {}
        for k, v in meta.get("metrics", {}).items():
            if k not in rm:
                fail(f"metric '{k}' not present in temp/session_report.json")
            if str(rm[k]) != str(v):
                fail(f"metric '{k}' mismatch: post={v!r} report={rm[k]!r}")
        tp = report.get("tests_passed")
        if meta.get("status") == "pass" and (tp is None or int(tp) < 1):
            fail("status pass but session report has tests_passed < 1")

    # 2. archetype rotation
    if len(posts) > 1:
        prev = posts[1][1].get("archetype")
        if prev and prev == meta.get("archetype"):
            fail(f"archetype '{prev}' repeats previous post (rotation rule)")

    # 3. commit_sha must exist in this repository
    sha = str(meta.get("commit_sha", ""))
    if not re.fullmatch(r"[0-9a-f]{7,40}", sha):
        fail(f"commit_sha '{sha}' is not a plausible sha")
    r = subprocess.run(
        ["git", "cat-file", "-e", f"{sha}^{{commit}}"], cwd=REPO,
        capture_output=True,
    )
    if r.returncode != 0:
        fail(f"commit_sha '{sha}' does not exist in this repository")

    # 4. featured_image must resolve
    img = meta.get("featured_image")
    if img:
        if str(img).startswith(("http://", "https://")):
            print(f"note: featured_image is remote ({img}); not checking existence")
        else:
            cands = [REPO / "blog" / str(img).lstrip("/"), REPO / str(img).lstrip("/")]
            if not any(c.exists() for c in cands):
                fail(f"featured_image does not resolve: {img}")

    print("OK: newest post is publishable")
    sys.exit(0)


if __name__ == "__main__":
    main()
