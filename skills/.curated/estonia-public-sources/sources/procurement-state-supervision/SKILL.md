---
name: procurement-state-supervision
description: Use Ministry of Finance procurement state supervision pages for supervisory actions, compliance findings, and oversight process context.
---

# Procurement State Supervision

## Use when
- You need procurement supervision process and oversight context.
- You need structured extraction of supervision findings/actions.

## Avoid when
- You need procurement market analytics only.

## Inputs
- Supervision topic, period, and authority scope.

## Outputs
- Structured supervision references, actions, and findings.

## Primary endpoints
- State supervision: https://www.fin.ee/en/public-procurement-state-aid-and-assets/public-procurement-policy/state-supervision

## Workflow
1. Retrieve supervision-related publications/materials.
2. Extract action/finding details and dates.
3. Normalize supervisory action taxonomy.
4. Return structured outputs with citations.

## Human setup (when needed)
- If materials are PDF-based, guide user through retrieval and continue from extracted content.

## Quality checks
- Keep dates and reference IDs for each action.
- Separate policy guidance from actual supervisory findings.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.fin.ee/en/public-procurement-state-aid-and-assets/public-procurement-policy/state-supervision (HTTP 200, text/html;, file links detected: 1)

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
