---
name: local-council-volis
description: Use VOLIS municipal council information system for local council agendas, decisions, minutes, and voting records.
---

# Local Council Data (VOLIS)

## Use when
- You need municipal council operations (agendas, decisions, minutes, votes).
- You need cross-municipality council data where available in VOLIS.

## Avoid when
- You need city-specific systems that are outside VOLIS.

## Inputs
- Municipality, period, and document type.

## Outputs
- Council operation records with links and metadata.

## Primary endpoint
- VOLIS: https://www.volis.ee/

## Workflow
1. Select municipality and document area.
2. Filter by date/document type.
3. Extract decision/minute/agenda records.
4. Return normalized local-governance dataset.

## Human setup (when needed)
- VOLIS is UI-first; guide user through municipality and filter selection when direct machine endpoint is unavailable.

## Quality checks
- Keep municipality identifiers and document IDs.
- Do not mix draft and final decisions unless explicitly labeled.
