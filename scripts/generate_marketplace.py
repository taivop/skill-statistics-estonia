#!/usr/bin/env python3
"""Generate Anthropic marketplace file at .claude-plugin/marketplace.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from distribution_specs import (
    DEFAULT_MARKETPLACE_NAME,
    DEFAULT_MARKETPLACE_OWNER,
    marketplace_document,
)
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
    parser.add_argument("--name", default=DEFAULT_MARKETPLACE_NAME)
    parser.add_argument("--owner-name", default=DEFAULT_MARKETPLACE_OWNER)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if marketplace file is out of date.",
    )
    args = parser.parse_args()

    root = repo_root()
    packages = iter_skill_packages(root)
    marketplace = marketplace_document(packages, args.name, args.owner_name)
    out_path = root / ".claude-plugin" / "marketplace.json"
    changed = _write_if_changed(out_path, _json_text(marketplace))

    if changed:
        print(f"updated {out_path.relative_to(root)}")
    else:
        print(f"ok: {out_path.relative_to(root)} already up to date")

    if args.check and changed:
        print("error: marketplace file is out of date")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
