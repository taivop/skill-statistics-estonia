---
name: construction-register
description: Use Estonia construction register (EHR) public data views for permits, building records, and construction-related operational events.
---

# Estonia Construction Register (EHR)

## Use when
- You need building permit/construction operation records.
- You need location/project-level construction administrative data.

## Avoid when
- You need only aggregated construction statistics.

## Inputs
- Address/parcel, municipality, permit type, date range.

## Outputs
- Construction-register records with permit/status metadata.

## Primary endpoint
- EHR: https://www.ehr.ee/en

## Workflow
1. Locate relevant EHR public search area.
2. Apply location/permit/date filters.
3. Extract permit/project records and status fields.
4. Return standardized construction operations dataset.

## Human setup (when needed)
- If EHR requires interactive map/form navigation, walk user through exact search steps and ask them to share resulting URLs or exported files.

## Quality checks
- Keep unique register IDs and address references.
- Distinguish planned, approved, and completed states.
