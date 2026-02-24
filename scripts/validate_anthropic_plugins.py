#!/usr/bin/env python3
"""Validate Anthropic plugin manifests and marketplace consistency."""

from __future__ import annotations

import json
from pathlib import Path
import sys

from distribution_specs import (
    DEFAULT_MARKETPLACE_NAME,
    DEFAULT_MARKETPLACE_OWNER,
    marketplace_document,
    plugin_manifest,
)
from skill_metadata import iter_skill_packages, repo_root


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _check(cond: bool, message: str, errors: list[str]) -> None:
    if not cond:
        errors.append(message)


def main() -> int:
    root = repo_root()
    errors: list[str] = []
    packages = iter_skill_packages(root)

    # Validate per-package plugin manifests.
    for pkg in packages:
        plugin_path = pkg.path / ".claude-plugin" / "plugin.json"
        _check(plugin_path.is_file(), f"missing plugin manifest: {plugin_path}", errors)
        if not plugin_path.is_file():
            continue

        actual = _load_json(plugin_path)
        expected = plugin_manifest(pkg)
        if actual != expected:
            errors.append(
                f"plugin manifest mismatch: {plugin_path.relative_to(root)} "
                f"(run scripts/generate_plugin_manifests.py)"
            )

        _check(
            isinstance(actual.get("name"), str) and bool(actual["name"].strip()),
            f"invalid plugin name in {plugin_path}",
            errors,
        )
        _check(
            isinstance(actual.get("version"), str) and bool(actual["version"].strip()),
            f"invalid plugin version in {plugin_path}",
            errors,
        )
        _check(
            isinstance(actual.get("description"), str)
            and bool(actual["description"].strip()),
            f"invalid plugin description in {plugin_path}",
            errors,
        )

    # Validate marketplace file.
    marketplace_path = root / ".claude-plugin" / "marketplace.json"
    _check(
        marketplace_path.is_file(),
        f"missing marketplace file: {marketplace_path}",
        errors,
    )
    if marketplace_path.is_file():
        actual_marketplace = _load_json(marketplace_path)
        expected_marketplace = marketplace_document(
            packages, DEFAULT_MARKETPLACE_NAME, DEFAULT_MARKETPLACE_OWNER
        )
        if actual_marketplace != expected_marketplace:
            errors.append(
                "marketplace mismatch at .claude-plugin/marketplace.json "
                "(run scripts/generate_marketplace.py)"
            )

        _check(
            isinstance(actual_marketplace.get("name"), str)
            and bool(actual_marketplace["name"].strip()),
            "marketplace.name must be a non-empty string",
            errors,
        )
        owner = actual_marketplace.get("owner")
        _check(
            isinstance(owner, dict)
            and isinstance(owner.get("name"), str)
            and bool(owner["name"].strip()),
            "marketplace.owner.name must be a non-empty string",
            errors,
        )
        plugins = actual_marketplace.get("plugins")
        _check(isinstance(plugins, list), "marketplace.plugins must be a list", errors)

        if isinstance(plugins, list):
            seen: set[str] = set()
            for idx, entry in enumerate(plugins):
                if not isinstance(entry, dict):
                    errors.append(f"marketplace.plugins[{idx}] must be an object")
                    continue
                name = entry.get("name")
                source = entry.get("source")
                desc = entry.get("description")
                _check(
                    isinstance(name, str) and bool(name.strip()),
                    f"marketplace.plugins[{idx}].name invalid",
                    errors,
                )
                _check(
                    isinstance(source, str) and source.startswith("./"),
                    f"marketplace.plugins[{idx}].source must start with ./",
                    errors,
                )
                _check(
                    isinstance(desc, str) and bool(desc.strip()),
                    f"marketplace.plugins[{idx}].description invalid",
                    errors,
                )
                if isinstance(name, str):
                    if name in seen:
                        errors.append(f"duplicate marketplace plugin name: {name}")
                    seen.add(name)

    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        print(f"failed with {len(errors)} error(s)")
        return 1

    print(
        f"ok: validated {len(packages)} plugin manifest(s) and marketplace configuration"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
