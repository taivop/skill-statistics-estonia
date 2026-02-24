---
name: health-welfare-open-data
description: Use TEHIK open-data listings to locate health and welfare administrative datasets and route them into analysis workflows.
---

# Estonia Health/Welfare Open Data (TEHIK)

## Use when
- You need administrative health or welfare datasets listed by TEHIK.
- You need source routing from catalog to downloadable datasets.

## Avoid when
- You need only TAI statistical tables.

## Inputs
- Topic and needed granularity.

## Outputs
- Curated dataset shortlist and direct access links.

## Primary endpoint
- TEHIK open data page: https://teabekeskus.tehik.ee/et/avaandmed

## Workflow
1. Identify relevant TEHIK-listed datasets.
2. Follow through to actual file/API endpoints.
3. Assess metadata completeness and update cadence.
4. Return recommended primary dataset and backup options.

## Human setup (when needed)
- If the catalog links to portals requiring manual interaction, give exact click path and request the final file or URL.

## Quality checks
- Check legal/privacy notes on each dataset.
- Verify that aggregation level matches the user request.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://teabekeskus.tehik.ee/et/avaandmed (HTTP 200, text/html;, file links detected: 1)

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
