---
name: legislation-workflow-eis
description: Track Estonian draft legislation workflow in EIS, including coordination status, document versions, and stakeholder input history.
---

# Estonia Legislation Workflow (EIS)

## Use when
- You need operational status of draft legal acts in inter-ministerial coordination.
- You need chronology of proposals, versions, and comments.

## Avoid when
- You need only final enacted law text (use Riigi Teataja legal-acts skill).

## Inputs
- Draft title, keyword, ministry, or registry identifier.

## Outputs
- Timeline of workflow steps and current status.
- Linked documents and responsible institution context.

## Primary endpoint
- EIS portal: https://eelnoud.valitsus.ee/main/main

## Workflow
1. Search draft by title/keyword/ministry.
2. Open draft card and capture identifiers and latest status.
3. Extract milestone timeline (submission, coordination, revisions, approval path).
4. Return concise status summary with direct source links.

## Human setup (when needed)
- If search results are only available via interactive UI, guide the user step-by-step to open the correct draft card and share the URL; continue from that URL.

## Quality checks
- Separate current draft status from historical status.
- Keep timestamps and institution names exactly as published.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://eelnoud.valitsus.ee/main/main (HTTP 200, text/html;charset=UTF-8, file links detected: 0)

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
