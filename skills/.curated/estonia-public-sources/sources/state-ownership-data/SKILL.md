---
name: state-ownership-data
description: Query official state-stakeholding and state-ownership policy pages for governance, ownership structure, and state-enterprise context.
---

# State Ownership Data

## Use when
- You need state stakeholding and ownership-governance context.
- You need official source references for state-enterprise ownership.

## Avoid when
- You need company-level financial statements only.

## Inputs
- Enterprise scope, sector, and analysis period.

## Outputs
- Structured ownership-governance dataset and source notes.

## Primary endpoints
- State assets/stakeholdings: https://www.fin.ee/en/public-procurement-state-aid-and-assets/state-assets/state-stakeholdings

## Workflow
1. Retrieve state-stakeholding references and linked materials.
2. Extract enterprise, ownership-share, and governance fields where published.
3. Normalize organization names and ownership categories.
4. Return ownership map with confidence notes.

## Human setup (when needed)
- If core details are spread across linked documents/annexes, guide the user through opening/downloading them and continue from those files.

## Quality checks
- Distinguish direct vs indirect state ownership.
- Record publication date for each extracted source.

## Limitations
- A single machine-readable central register may not be publicly exposed from this entry page; use linked official materials as primary evidence.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.fin.ee/en/public-procurement-state-aid-and-assets/state-assets/state-stakeholdings (HTTP 200, text/html;, file links detected: 2)

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
