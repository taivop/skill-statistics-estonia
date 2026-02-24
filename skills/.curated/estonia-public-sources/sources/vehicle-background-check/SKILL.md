---
name: vehicle-background-check
description: Use official vehicle background check service for vehicle registry status context and public vehicle record validation.
---

# Vehicle Background Check

## Use when
- You need public vehicle registry status checks.
- You need vehicle background validation from official transport services.

## Avoid when
- You need private owner-level data not publicly exposed.

## Inputs
- Vehicle identifier(s) supported by service.

## Outputs
- Structured vehicle status/background results.

## Primary endpoints
- Vehicle background check: https://eteenindus.mnt.ee/public/soidukTaustakontroll.jsf?lang=en

## Workflow
1. Validate supported search identifier.
2. Run check and capture returned fields.
3. Normalize status/technical fields.
4. Return structured output with query timestamp.

## Human setup (when needed)
- If captcha/session controls appear, guide user through form submission and continue from returned output.

## Quality checks
- Preserve original registry status labels.
- Keep query timestamp and identifier used.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://eteenindus.mnt.ee/public/soidukTaustakontroll.jsf?lang=en (HTTP 200, text/html;charset=UTF-8, file links detected: 0)

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
