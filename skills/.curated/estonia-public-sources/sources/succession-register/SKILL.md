---
name: succession-register
description: Use official succession register service context for inheritance-related register workflows and structured output extraction.
---

# Succession Register

## Use when
- You need succession register process/context and available public outputs.
- You need structured extraction of official succession-register evidence.

## Avoid when
- You need confidential case details not publicly available.

## Inputs
- Query scope, allowed identifiers, and legal basis.

## Outputs
- Structured succession-register outputs and constraints notes.

## Primary endpoints
- Succession register: https://www.rik.ee/en/other-services/succession-register

## Workflow
1. Identify permitted lookup/output route.
2. Retrieve accessible record/result details.
3. Normalize identifiers and status fields.
4. Return structured output plus access caveats.

## Human setup (when needed)
- If access requires authenticated workflow, guide user step-by-step and continue from provided result material.

## Quality checks
- Preserve official references and timestamps.
- Separate process guidance from register output.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.rik.ee/en/other-services/succession-register (HTTP 200, text/html;, file links detected: 0)

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
