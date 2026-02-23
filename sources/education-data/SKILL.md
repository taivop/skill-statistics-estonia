---
name: education-data
description: Query HaridusSilm education indicators for school system, outcomes, staffing, and regional education analysis in Estonia.
---

# Estonia Education Data (HaridusSilm)

## Use when
- You need education-system indicators by level, region, or institution.
- You need dashboard data exports for analysis.

## Avoid when
- You need student-level data (not public).

## Inputs
- Topic, education level, geography, and period.

## Outputs
- Education indicator extracts and metadata notes.

## Primary endpoint
- Portal: https://www.haridussilm.ee/ee/avaleht

## Workflow
1. Navigate to relevant indicator view.
2. Apply filters and choose comparable slices.
3. Export available table data.
4. Normalize field names and period keys.

## Human setup (when needed)
- If data is only exportable via UI interactions, walk the user through precise filter and export steps.

## Quality checks
- Confirm definitions (e.g., completion vs participation).
- Check whether figures represent school year or calendar year.
