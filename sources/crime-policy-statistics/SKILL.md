---
name: crime-policy-statistics
description: Use criminal policy statistics and studies portal for crime trends, victimization studies, and justice-policy evidence.
---

# Crime Policy Statistics

## Use when
- You need official crime-policy statistics and research outputs.
- You need crime trend context linked to policy analysis.

## Avoid when
- You need real-time police incident feeds.

## Inputs
- Topic area, period, and study/statistics scope.

## Outputs
- Structured indicators/study metadata and trend extracts.

## Primary endpoints
- Statistics and studies: https://www.kriminaalpoliitika.ee/et/statistika-ja-uuringud/statistika-ja-uuringud

## Workflow
1. Locate relevant statistical series or study output.
2. Extract periodized metrics and definitions.
3. Normalize categories across publications.
4. Return structured output with methodology notes.

## Human setup (when needed)
- If data is embedded in reports, walk user through report retrieval and continue from extracted tables.

## Quality checks
- Keep source methodology references with indicators.
- Separate survey-based and administrative indicators.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.kriminaalpoliitika.ee/et/statistika-ja-uuringud/statistika-ja-uuringud (HTTP 200, text/html;, file links detected: 0)

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
