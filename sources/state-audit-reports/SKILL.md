---
name: state-audit-reports
description: Query National Audit Office publications and audits to extract findings on public-sector performance and governance operations.
---

# State Audit Reports

## Use when
- You need independent audit findings about government operations.
- You need audit-level evidence for policy/governance analysis.

## Avoid when
- You need primary operational logs rather than audit conclusions.

## Inputs
- Audit topic, institution, period, and type.

## Outputs
- Audit list with findings metadata and links.

## Primary endpoint
- Audit list: https://www.riigikontroll.ee/en/audits

## Workflow
1. Filter audits by topic/type/date.
2. Extract title, institution, publication date, and report link.
3. Capture key findings/recommendations if needed.
4. Return structured audit evidence table.

## Human setup (when needed)
- If report documents require manual download, guide user through retrieval and continue from files.

## Quality checks
- Separate audit reports from press/news items.
- Keep publication date and audit type fields explicit.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.riigikontroll.ee/en/audits (HTTP 200, text/html;, file links detected: 1)

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
