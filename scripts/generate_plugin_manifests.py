#!/usr/bin/env python3
"""Generate .claude-plugin/plugin.json for each skill package."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from distribution_specs import plugin_manifest
from skill_metadata import iter_skill_packages, repo_root


def _json_text(payload: dict) -> str:
    return json.dumps(payload, indent=2) + "\n"


def _write_if_changed(path: Path, content: str) -> bool:
    if path.is_file() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if any plugin manifest is out of date.",
    )
    args = parser.parse_args()

    root = repo_root()
    packages = iter_skill_packages(root)
    changed = 0

    for pkg in packages:
        manifest_path = pkg.path / ".claude-plugin" / "plugin.json"
        content = _json_text(plugin_manifest(pkg))
        if _write_if_changed(manifest_path, content):
            changed += 1
            print(f"updated {manifest_path.relative_to(root)}")

    if args.check and changed > 0:
        print(f"error: {changed} plugin manifest(s) are out of date")
        return 1

    print(f"ok: checked {len(packages)} package(s), updated {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
