---
name: querying-statistics-estonia-api
description: Query Statistics Estonia datasets and metadata via andmed.stat.ee API; use for official Estonian indicators, time series, and table-level methodology context.
---

# Statistics Estonia API

## Use when
- You need official national statistics from Statistics Estonia.
- You need machine-readable table data (JSON/JSON-stat/CSV).
- You need ESMS methodology and quality metadata before analysis.

## Avoid when
- The task is discovery across many institutions (use `discovering-estonia-open-data`).

## Inputs
- Topic keywords or known table ID.
- Time period, dimensions, and output format.

## Outputs
- Queried dataset extract.
- Metadata summary with caveats.

## Primary endpoints
- Portal: https://andmed.stat.ee/en/stat
- API base: https://andmed.stat.ee/api/v1
- Local helper script: `get_metadata.py`

## Workflow
1. Discover table IDs by topic.
2. Open table structure and valid dimension codes.
3. Fetch ESMS metadata first (`python get_metadata.py TABLE_ID --format text`).
4. Submit API query and validate returned dimensions and units.
5. Return data plus a short caveat summary from ESMS metadata.

## Human setup (when needed)
- Usually none.
- If the service is temporarily unavailable, tell the user the exact table ID and query payload to retry later.

## Quality checks
- Confirm unit, seasonal adjustment, and reference period.
- Confirm whether the chosen table is index, absolute value, or rate.
