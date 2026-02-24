---
name: ombudsman-opinions
description: Query Chancellor of Justice annual reports and opinion materials for constitutional and rights oversight context in Estonia.
---

# Ombudsman Opinions and Reports

## Use when
- You need oversight/rights interpretation context from the Chancellor of Justice.
- You need annual reports and initiative outputs.

## Avoid when
- You need court judgments rather than ombudsman materials.

## Inputs
- Topic keywords, rights area, and period.

## Outputs
- Report/opinion references with metadata and links.

## Primary endpoint
- Annual reports: https://www.oiguskantsler.ee/en/opinions-and-initiatives/annual-reports

## Workflow
1. Collect report/opinion entries by period and topic.
2. Extract publication metadata and links.
3. Summarize relevant oversight themes.
4. Return structured source list.

## Human setup (when needed)
- If specific subpages are language-dependent, walk user through switching language/filtering and continue from shared URLs.

## Quality checks
- Distinguish formal reports from explanatory news posts.
- Preserve exact publication year/date.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.oiguskantsler.ee/en/opinions-and-initiatives/annual-reports (HTTP 200, text/html;, file links detected: 24)

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
