---
name: communicable-disease-bulletins
description: Use Health Board communicable disease bulletins for outbreak, surveillance, and public-health operations indicators.
---

# Communicable Disease Bulletins

## Use when
- You need infectious disease surveillance bulletins and trend indicators.
- You need official public-health operational context.

## Avoid when
- You need healthcare financing indicators.

## Inputs
- Disease group, period, and geographic scope.

## Outputs
- Structured bulletin-derived disease indicators and metadata.

## Primary endpoints
- Bulletins: https://www.terviseamet.ee/en/communicable-diseases/statistics/communicable-disease-bulletins

## Workflow
1. Retrieve relevant bulletin files/pages.
2. Extract disease indicators by period/location.
3. Normalize disease names and units.
4. Return structured dataset with bulletin references.

## Human setup (when needed)
- If indicators are only in downloadable bulletins, guide user through retrieval and continue from files.

## Quality checks
- Keep disease taxonomy and case definitions with values.
- Distinguish provisional from finalized counts.
