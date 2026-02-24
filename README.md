# Public Agents Marketplace

This repository is a dual-distribution marketplace for agent skills:

1. Anthropic Claude Code plugins via `/.claude-plugin/marketplace.json`.
2. Codex skills via Git path install from `skills/.curated/*`.

## Repository Layout

```text
.
├── .claude-plugin/
│   └── marketplace.json
├── skills/
│   ├── .curated/
│   │   └── <skill-package>/
│   │       ├── SKILL.md
│   │       └── .claude-plugin/plugin.json
│   └── .experimental/
│       └── <skill-package>/
├── scripts/
│   ├── generate_plugin_manifests.py
│   ├── generate_marketplace.py
│   ├── validate_codex_skills.py
│   └── validate_anthropic_plugins.py
└── .github/workflows/validate-distribution.yml
```

## Install From Anthropic Marketplace

```bash
claude plugin marketplace add <owner>/public-agents
claude plugin install estonia-public-sources@public-agents
```

## Install In Codex

Use the Codex skill installer with a repo path:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <owner>/public-agents \
  --path skills/.curated/estonia-public-sources
```

## Publishing Workflow

Run generators and validators:

```bash
python3 scripts/generate_plugin_manifests.py
python3 scripts/generate_marketplace.py
python3 scripts/validate_codex_skills.py
python3 scripts/validate_anthropic_plugins.py
```

CI enforces these checks and fails if generated files are out of date.
