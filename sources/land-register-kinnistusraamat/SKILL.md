---
name: land-register-kinnistusraamat
description: Query Estonia Land Register (Kinnistusraamat) public views for property rights records, legal encumbrance context, and ownership-history tracing.
---

# Land Register (Kinnistusraamat)

## Use when
- You need official land register extracts or record metadata.
- You need ownership-right and encumbrance context for a property.

## Avoid when
- You only need cadastral geometry layers (use geospatial/cadaster skills).

## Inputs
- Property address, cadastral identifier, or registry reference.

## Outputs
- Land-register record extract with source timestamps.
- Structured ownership/encumbrance fields for analysis.

## Primary endpoints
- Main portal: https://kinnistusraamat.rik.ee/
- Immovables portal context: https://www.rik.ee/en/e-land-register/immovables-portal
- E-land register XML service context: https://www.rik.ee/en/e-land-register/e-land-register-portal/xml-service

## Workflow
1. Identify search key (address, cadastral unit, or registry code).
2. Retrieve available public record views and document-level metadata.
3. If relevant, use immovables/XML service routes to improve extraction consistency.
4. Normalize party names, rights, and encumbrance categories.
5. Return a structured extract with legal-context caveats.

## Human setup (when needed)
- If lookup requires interactive captcha, session validation, or paid document retrieval, guide the user step-by-step through the portal and continue from files/screenshots they provide.

## Quality checks
- Keep registry identifiers exactly as published.
- Separate factual register fields from interpretation.

## Limitations
- Some detailed records may require authenticated or paid access.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://kinnistusraamat.rik.ee/ (HTTP 200, text/html;, file links detected: 0)
- https://www.rik.ee/en/e-land-register/immovables-portal (HTTP 200, text/html;, file links detected: 2)
- https://www.rik.ee/en/e-land-register/e-land-register-portal/xml-service (HTTP 200, text/html;, file links detected: 1)

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
