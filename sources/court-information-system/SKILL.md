---
name: court-information-system
description: Use court information system references for court-process information flows, system context, and structured extraction of publicly available materials.
---

# Court Information System

## Use when
- You need official court information system context.
- You need structured extraction of public system/process references.

## Avoid when
- You need case-level confidential documents.

## Inputs
- Process topic, court level, and period.

## Outputs
- Structured court-information-system references and outputs.

## Primary endpoints
- Court information system: https://www.rik.ee/en/international/court-information-system

## Workflow
1. Retrieve relevant court-system reference pages/materials.
2. Extract process/system fields and linkage points.
3. Normalize terminology across sources.
4. Return structured outputs and caveats.

## Human setup (when needed)
- If detailed artifacts are in linked docs, guide user through retrieval and continue from provided files.

## Quality checks
- Keep system/process references linked to source URLs.
- Distinguish system description from operational statistics.
