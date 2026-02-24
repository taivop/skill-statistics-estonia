---
name: plant-protection-supervision
description: Use Agriculture and Food Board plant protection pages for supervision context, compliance requirements, and extractable official outputs.
---

# Plant Protection Supervision

## Use when
- You need official plant protection supervision and compliance context.
- You need structured extraction of plant protection oversight materials.

## Avoid when
- You need only high-level environmental indicators.

## Inputs
- Topic scope, period, and regulated activity type.

## Outputs
- Structured plant protection supervision references and findings fields.

## Primary endpoints
- Plant protection: https://pta.agri.ee/en/plants/plant-protection

## Workflow
1. Identify relevant plant protection supervision content.
2. Extract requirements, checks, and outcomes fields.
3. Normalize category labels.
4. Return structured output and caveats.

## Human setup (when needed)
- If key details are in linked docs/forms, guide user through retrieval and continue from those files.

## Quality checks
- Distinguish requirement text from observed outcomes.
- Keep legal references associated with each item.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://pta.agri.ee/en/plants/plant-protection (HTTP 200, text/html;, file links detected: 8)

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
