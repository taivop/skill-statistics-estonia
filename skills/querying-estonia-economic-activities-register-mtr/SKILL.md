---
name: querying-estonia-economic-activities-register-mtr
description: Query Estonia Economic Activities Register (MTR) for licensed activity records, operator details, and sector-specific authorization context.
---

# Economic Activities Register (MTR)

## Use when
- You need operator/license information from MTR.
- You need activity-authorization context by sector.

## Avoid when
- You only need broad business population snapshots.

## Inputs
- Company identifier, activity class, sector, and time scope.

## Outputs
- MTR activity-license records and normalized fields.

## Primary endpoints
- Register portal: https://mtr.ttja.ee/

## Workflow
1. Select relevant search view in MTR.
2. Filter by entity/activity class/time.
3. Extract registration, status, and authorization details.
4. Return structured table with status semantics.

## Human setup (when needed)
- If export is UI-only, walk the user through exact filters and export actions, then continue from the provided file.

## Quality checks
- Preserve original MTR reference identifiers.
- Distinguish active, suspended, and terminated records.
