---
name: riigiteataja-draft-acts
description: Query Riigi Teataja draft-act search for legal drafting stream monitoring and draft-text retrieval.
---

# Riigi Teataja Draft Acts

## Use when
- You need public draft-act discovery and monitoring.
- You need links between drafts and final legal instruments.

## Avoid when
- You only need enacted/current legal text.

## Inputs
- Draft topic, issuer, date range.

## Outputs
- Draft-act search results with metadata and links.

## Primary endpoint
- Draft search: https://www.riigiteataja.ee/eelnoud/otsing.html

## Workflow
1. Run draft search with focused terms.
2. Capture draft identifiers, dates, and issuing body.
3. Follow links to draft documents and related acts.
4. Return tracking table suitable for updates.

## Human setup (when needed)
- If filters are UI-only, walk user through exact settings and ask for result URL or exported file.

## Quality checks
- Keep draft and enacted references separate.
- Preserve official identifiers and document dates.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.riigiteataja.ee/eelnoud/otsing.html (HTTP 200, text/html;charset=utf-8, file links detected: 0)

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
