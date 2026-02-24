---
name: supreme-court-judgments
description: Query Estonian Supreme Court judgment publications for case-law context that shapes governance and administrative practice.
---

# Supreme Court Judgments

## Use when
- You need Supreme Court case-law references.
- You need jurisprudence context for administrative/governance questions.

## Avoid when
- You need lower-court bulk proceedings without Supreme Court focus.

## Inputs
- Case topic, chamber/type, date range, keywords.

## Outputs
- Judgment list with metadata and links.

## Primary endpoint
- Judgments page (ET): https://www.riigikohus.ee/et/lahendid

## Workflow
1. Search/filter judgments by topic/date.
2. Extract case references and dates.
3. Capture decision summaries or linked full text.
4. Return legal-context dataset.

## Human setup (when needed)
- If filtering is UI-only or Estonian-only, provide exact user steps to locate target judgments and continue from shared links.

## Quality checks
- Preserve case number and date format.
- Do not infer holdings beyond published text.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.riigikohus.ee/et/lahendid (HTTP 200, text/html;, file links detected: 7)

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
