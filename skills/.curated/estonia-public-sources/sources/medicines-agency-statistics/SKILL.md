---
name: medicines-agency-statistics
description: Use State Agency of Medicines statistical yearbooks for medicines market, pharmacy, and regulatory activity indicators.
---

# Medicines Agency Statistics

## Use when
- You need medicines/pharmacy statistics from the medicines agency.
- You need annual regulatory/market context indicators.

## Avoid when
- You need individual medicine record lookup only.

## Inputs
- Year range and thematic section.

## Outputs
- Structured yearbook indicators and trend tables.

## Primary endpoints
- Statistical yearbooks: https://www.ravimiamet.ee/en/statistics/statistical-yearbooks

## Workflow
1. Retrieve yearbook(s) for selected years.
2. Extract relevant indicator tables.
3. Normalize category labels across editions.
4. Return dataset and definitions metadata.

## Human setup (when needed)
- If content is PDF-based, guide user through file retrieval and continue from tables.

## Quality checks
- Track edition year and section source.
- Keep supply, utilization, and regulatory indicators distinct.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.ravimiamet.ee/en/statistics/statistical-yearbooks (HTTP 200, text/html;, file links detected: 11)

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
