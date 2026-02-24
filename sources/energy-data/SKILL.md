---
name: energy-data
description: Query Elering dashboard API for Estonia electricity and system data, including market and balance time series.
---

# Estonia Energy Data (Elering)

## Use when
- You need near-real-time electricity system and market series.
- You need energy context for macro, climate, or operations analysis.

## Avoid when
- You need only annual energy aggregates from statistical yearbooks.

## Inputs
- Start/end timestamps (ISO UTC).
- Data family (price, system balance, production/consumption).

## Outputs
- Time-series JSON extract with harmonized timestamps.

## Primary endpoints
- Dashboard: https://dashboard.elering.ee/
- NPS price API: `https://dashboard.elering.ee/api/nps/price?start=...&end=...`
- System with plan API: `https://dashboard.elering.ee/api/system/with-plan?start=...&end=...`

## Workflow
1. Choose relevant endpoint and set UTC time window.
2. Fetch JSON and parse the `data` object by region/series.
3. Convert timestamps consistently and document timezone handling.
4. Return cleaned series and missing-data notes.

## Human setup (when needed)
- Usually none.

## Quality checks
- Validate interval consistency (e.g., 15-minute or hourly).
- Flag daylight-saving boundaries and missing points.

## Access reality
- Public access type: API or structured endpoint access.
- Verification run: 2026-02-24.
- https://dashboard.elering.ee/ (HTTP 200, text/html, file links detected: 0)
- https://dashboard.elering.ee/api/nps/price?start=...&end=...` (HTTP 400, application/json, file links detected: 0)
- https://dashboard.elering.ee/api/system/with-plan?start=...&end=...` (HTTP 400, application/json, file links detected: 0)

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
