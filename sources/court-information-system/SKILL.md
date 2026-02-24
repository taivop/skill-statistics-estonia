---
name: court-information-system
description: Use court information system references for court-process information flows, system context, and structured extraction of publicly available materials.
---

# Court Information System

## Use when
- You need official court information system context.
- You need structured extraction of public system/process references.

## Avoid when
- You need case-level confidential documents.

## Inputs
- Process topic, court level, and period.

## Outputs
- Structured court-information-system references and outputs.

## Primary endpoints
- Court information system: https://www.rik.ee/en/international/court-information-system

## Workflow
1. Retrieve relevant court-system reference pages/materials.
2. Extract process/system fields and linkage points.
3. Normalize terminology across sources.
4. Return structured outputs and caveats.

## Human setup (when needed)
- If detailed artifacts are in linked docs, guide user through retrieval and continue from provided files.

## Quality checks
- Keep system/process references linked to source URLs.
- Distinguish system description from operational statistics.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.rik.ee/en/international/court-information-system (HTTP 200, text/html;, file links detected: 0)

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
