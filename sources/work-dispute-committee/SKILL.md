---
name: work-dispute-committee
description: Use Labour Inspectorate work dispute committee pages for labor-dispute procedure, filing workflow, and decision context.
---

# Work Dispute Committee

## Use when
- You need official labor dispute committee procedures and decision workflow context.
- You need structured extraction of public committee materials.

## Avoid when
- You need private dispute files not publicly released.

## Inputs
- Dispute category, period, and procedural stage.

## Outputs
- Structured process references and available decision outputs.

## Primary endpoints
- Work dispute committee: https://www.tooinspektsioon.ee/en/work-dispute-committee

## Workflow
1. Identify relevant committee procedure and document paths.
2. Extract deadlines, stages, and available outputs.
3. Normalize procedure vocabulary.
4. Return structured guidance/output references.

## Human setup (when needed)
- If decision materials require manual retrieval, guide the user through steps and continue from provided documents.

## Quality checks
- Distinguish binding decision text from guidance.
- Preserve official timelines and stage labels.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.tooinspektsioon.ee/en/work-dispute-committee (HTTP 200, text/html;, file links detected: 1)

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
