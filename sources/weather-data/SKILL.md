---
name: weather-data
description: Query Estonian Weather Service XML feeds for forecast and observation data usable in time-series and impact analysis.
---

# Estonia Weather Data

## Use when
- You need weather observations or forecast feeds from official service.
- You need weather covariates for demand, transport, or health models.

## Avoid when
- You need climate normals that are not available in feed endpoints.

## Inputs
- Feed type (forecast/observations), stations/locations, period.

## Outputs
- Parsed weather dataset with timestamps and variable schema.

## Primary endpoints
- Forecast XML: https://www.ilmateenistus.ee/ilma_andmed/xml/forecast.php
- Observations XML: https://www.ilmateenistus.ee/ilma_andmed/xml/observations.php

## Workflow
1. Pull required XML feed.
2. Parse timestamps, station/location fields, and numeric variables.
3. Convert units/timezones consistently.
4. Return tidy tabular output.

## Human setup (when needed)
- Usually none.

## Quality checks
- Handle missing station readings safely.
- Document timezone assumptions explicitly.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.ilmateenistus.ee/ilma_andmed/xml/forecast.php (HTTP 200, text/xml;charset=UTF-8, file links detected: 0)
- https://www.ilmateenistus.ee/ilma_andmed/xml/observations.php (HTTP 200, text/xml;, file links detected: 0)

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
