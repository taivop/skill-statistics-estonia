---
name: state-services-catalog
description: Query the state services catalog on eesti.ee to map official public services, responsible bodies, and service-level operational context.
---

# State Services Catalog (eesti.ee)

## Use when
- You need service inventory context for how government serves users.
- You need institution-to-service mapping.

## Avoid when
- You need internal document workflows instead of service listings.

## Inputs
- Service domain, audience, keyword filters.

## Outputs
- Service list with provider and link metadata.

## Primary endpoint
- Services catalog: https://www.eesti.ee/en/services

## Workflow
1. Search/filter service categories.
2. Extract service names, institutions, and service links.
3. Normalize category/service metadata.
4. Return catalog subset for analysis.

## Human setup (when needed)
- If some service details require portal interaction, walk the user through required clicks and continue with captured links.

## Quality checks
- Keep service names and responsible authorities exactly as listed.
- Record retrieval date since service catalog changes over time.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.eesti.ee/en/services (HTTP 200, text/html, file links detected: 0)

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
