---
name: planning-decisions
description: Query national planning register for spatial planning decisions, planning process stages, and plan document records.
---

# Estonia Planning Decisions

## Use when
- You need plan lifecycle data (initiated, approved, in force, etc.).
- You need planning decision records by municipality/region.

## Avoid when
- You need only base geospatial layers.

## Inputs
- Planning type, location, and date range.

## Outputs
- Planning records with stage/status and document links.

## Primary endpoint
- Planning register: https://www.planeeringud.ee/

## Workflow
1. Search planning records by location/type.
2. Capture plan identifiers, responsible authority, and stages.
3. Extract linked documents and decision references.
4. Return normalized planning-process dataset.

## Human setup (when needed)
- If export is UI-only, guide user through exact filters and export/download actions.

## Quality checks
- Preserve plan IDs and stage timestamps.
- Clearly separate draft/planned vs approved/in-force plans.
