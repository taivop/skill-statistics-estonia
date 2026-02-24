---
name: labour-inspectorate-enforcement
description: Use Labour Inspectorate enforcement/proceedings pages for supervision actions, procedural steps, and compliance outcomes.
---

# Labour Inspectorate Enforcement

## Use when
- You need supervision/enforcement process context from the Labour Inspectorate.
- You need structured extraction of proceedings-related outputs.

## Avoid when
- You only need aggregate labour market statistics.

## Inputs
- Enforcement topic, period, and action type.

## Outputs
- Structured enforcement/proceedings records and summaries.

## Primary endpoints
- Proceedings page: https://www.tooinspektsioon.ee/jarelevalve/menetlustoimingud

## Workflow
1. Identify relevant enforcement action pages/documents.
2. Extract action type, dates, and outcomes.
3. Normalize enforcement taxonomy.
4. Return structured dataset with procedural caveats.

## Human setup (when needed)
- If source evidence is PDF/document based, guide user through obtaining files and continue from them.

## Quality checks
- Distinguish guidance text from actual enforcement outcomes.
- Keep action dates and references where available.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.tooinspektsioon.ee/jarelevalve/menetlustoimingud (HTTP 200, text/html;, file links detected: 1)

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
