---
name: statistics-api
description: Query Statistics Estonia datasets and metadata via andmed.stat.ee API; use for official Estonian indicators, time series, and table-level methodology context.
---

# Statistics Estonia API

## Use when
- You need official national statistics from Statistics Estonia.
- You need machine-readable table data (JSON/JSON-stat/CSV).
- You need ESMS methodology and quality metadata before analysis.

## Avoid when
- The task is discovery across many institutions (use `open-data`).

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

## Access reality
- Public access type: API or structured endpoint access.
- Verification run: 2026-02-24.
- https://andmed.stat.ee/en/stat (HTTP 200, text/html;, file links detected: 0)
- https://andmed.stat.ee/api/v1 (HTTP 404, text/html, file links detected: 0)

## Request contract
- Use the listed primary endpoints as authoritative entry points.
- If API/query parameters are only visible in-browser, preserve exact request URL, params, and headers in output metadata.
- If endpoint is UI-only, document click path and extraction method used.

## Output schema expectations
- Keep at least: source URL, retrieval timestamp, publication/update date (if available), title/record label, and extracted governance-relevant fields.
- Preserve original field names when present in downloadable/API output.

## Limits and caveats
- Confirm whether data is open-download, UI-only, or authenticated before claiming full access.
- Separate narrative/guidance text from measurable records.

## Verification hooks
- Validate endpoint reachability and content type before extraction.
- Validate that each extracted claim is linked to a concrete source URL.
