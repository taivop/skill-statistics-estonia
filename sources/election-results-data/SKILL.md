---
name: election-results-data
description: Analyze Estonian election archive and open election datasets from valimised.ee for turnout, vote shares, and historical election trends.
---

# Estonia Election Results Data

## Use when
- You need historical election results, turnout, or e-voting statistics.
- You need multi-election comparisons.

## Avoid when
- You need parliamentary voting records (use Riigikogu open data skill).

## Inputs
- Election type, years, geography, and metric.

## Outputs
- Election result dataset and harmonized comparison table.

## Primary endpoints
- Main site: https://www.valimised.ee/en
- Elections archive (ET): https://www.valimised.ee/et/toimunud-valimiste-arhiiv
- Election open data (ET): https://www.valimised.ee/et/valimiste-arhiiv/valimiste-avaandmed

## Workflow
1. Choose election type and years from archive/open-data pages.
2. Download available machine-readable files.
3. Harmonize geography and party/candidate naming across years.
4. Return trend-ready dataset with caveats.

## Human setup (when needed)
- If only Estonian-language navigation is available, walk user through the exact ET menu path and what file to download.

## Quality checks
- Keep election-type boundaries separate (EP, parliamentary, local, referendum).
- Track boundary or constituency changes before trend comparisons.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.valimised.ee/en (HTTP 200, text/html;, file links detected: 0)
- https://www.valimised.ee/et/toimunud-valimiste-arhiiv (HTTP 200, text/html;, file links detected: 0)
- https://www.valimised.ee/et/valimiste-arhiiv/valimiste-avaandmed (HTTP 200, text/html;, file links detected: 7)

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
