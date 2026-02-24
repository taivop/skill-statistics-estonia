---
name: drone-operator-registration
description: Use Transport Administration drone operator registration sources for UAS registration workflow and compliance context extraction.
---

# Drone Operator Registration

## Use when
- You need official drone operator registration workflow context.
- You need structured extraction of registration/compliance requirements.

## Avoid when
- You need aircraft register data for manned aviation.

## Inputs
- Operator type, operation category, and period.

## Outputs
- Structured registration requirements and process outputs.

## Primary endpoints
- Operator registration: https://www.transpordiamet.ee/en/aviation-and-aviation-safety/flying-drones-estonia/operator-registration

## Workflow
1. Identify applicable operator registration path.
2. Extract required steps, conditions, and outputs.
3. Normalize operation category terminology.
4. Return structured process map and references.

## Human setup (when needed)
- If registration must be completed in e-services, guide user through steps and continue from provided results.

## Quality checks
- Keep operation category definitions with requirements.
- Separate legal requirements from explanatory guidance.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.transpordiamet.ee/en/aviation-and-aviation-safety/flying-drones-estonia/operator-registration (HTTP 200, text/html;, file links detected: 1)

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
