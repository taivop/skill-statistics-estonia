#!/usr/bin/env python3
"""Distribution document builders for Anthropic plugin files."""

from __future__ import annotations

from typing import Any

from skill_metadata import SkillPackage


DEFAULT_MARKETPLACE_NAME = "marketplace"
DEFAULT_MARKETPLACE_OWNER = "Taivo Marketplace"


def plugin_manifest(pkg: SkillPackage) -> dict[str, Any]:
    manifest: dict[str, Any] = {
        "name": pkg.distribution.plugin_name,
        "version": pkg.distribution.plugin_version,
        "description": pkg.description,
    }
    if pkg.distribution.plugin_author:
        manifest["author"] = {"name": pkg.distribution.plugin_author}
    return manifest


def marketplace_document(
    packages: list[SkillPackage], name: str, owner_name: str
) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []

    for pkg in sorted(packages, key=lambda p: p.distribution.plugin_name):
        if not pkg.distribution.publish_anthropic:
            continue
        entry: dict[str, Any] = {
            "name": pkg.distribution.plugin_name,
            "source": f"./{pkg.rel_path.as_posix()}",
            "description": pkg.description,
        }
        if pkg.distribution.plugin_author:
            entry["author"] = {"name": pkg.distribution.plugin_author}
        entries.append(entry)

    return {"name": name, "owner": {"name": owner_name}, "plugins": entries}
