---
name: state-port-register
description: Use state port register sources for official port registry information and maritime infrastructure governance context.
---

# State Port Register

## Use when
- You need official state port registry context and records.
- You need structured port-level governance metadata.

## Avoid when
- You need ship-level register entries only.

## Inputs
- Port name, region, and record scope.

## Outputs
- Structured port registry extract and metadata.

## Primary endpoints
- State port register context: https://www.transpordiamet.ee/en/roads-waterways-airspace/ports/state-port-register
- State port register system: https://www.sadamaregister.ee/

## Workflow
1. Identify applicable port register entry/listing (policy page or `sadamaregister.ee`).
2. Extract core port fields and statuses.
3. Normalize port naming and location fields.
4. Return structured registry dataset.

## Human setup (when needed)
- If the register requires interactive search/export, guide user through exact actions and continue from provided results.

## Quality checks
- Preserve official port identifiers where available.
- Record data retrieval date and source endpoint.
