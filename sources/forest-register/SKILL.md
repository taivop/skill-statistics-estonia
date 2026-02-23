---
name: forest-register
description: Use official forest register for forestry records, forest-unit context, and governance-relevant registry extraction.
---

# Forest Register

## Use when
- You need official forestry register records or metadata.
- You need forest-unit level context for governance/environment workflows.

## Avoid when
- You only need general environmental indicators.

## Inputs
- Forest area/unit identifier, location scope, and period.

## Outputs
- Structured forest register extract with provenance.

## Primary endpoints
- Forest register: https://register.metsad.ee/

## Workflow
1. Identify lookup mode and target forest unit/area.
2. Extract available registry attributes.
3. Normalize location and classification fields.
4. Return structured dataset and caveats.

## Human setup (when needed)
- If interactive map/portal controls block direct extraction, guide user through export/copy steps and continue from provided files.

## Quality checks
- Preserve official unit identifiers and classes.
- Record retrieval date and source view.
