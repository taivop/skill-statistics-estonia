---
name: cyber-incidents-cert-ee
description: Query CERT-EE public incident-handling and cyber situation resources for operational cybersecurity governance context.
---

# CERT-EE Incident Context

## Use when
- You need public cybersecurity incident and response context.
- You need national cyber governance operational references.

## Avoid when
- You need confidential incident data not publicly released.

## Inputs
- Topic, incident type, period.

## Outputs
- Public CERT-EE references, advisories, and incident-context records.

## Primary endpoint
- CERT-EE section: https://www.ria.ee/en/cyber-security/handling-cyber-incidents-cert-ee

## Workflow
1. Locate relevant CERT-EE pages and advisories.
2. Extract publication dates, incident categories, and guidance links.
3. Normalize into timeline/context dataset.
4. Return references with caveats on public scope.

## Human setup (when needed)
- If incident details are only in downloadable advisories, guide user to fetch files and continue from them.

## Quality checks
- Distinguish incidents, advisories, and procedural guidance.
- Record publication date and source URL for each item.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.ria.ee/en/cyber-security/handling-cyber-incidents-cert-ee (HTTP 200, text/html;, file links detected: 1)

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
