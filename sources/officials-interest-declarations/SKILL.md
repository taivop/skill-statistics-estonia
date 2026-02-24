---
name: officials-interest-declarations
description: Query official guidance and registry-access context for Estonian public officials' interest declarations and anti-corruption disclosure workflows.
---

# Officials' Interest Declarations

## Use when
- You need official process/context for interests declaration workflows.
- You need to locate declaration-related public records and controls.

## Avoid when
- You need unrelated party-finance reporting.

## Inputs
- Official role scope, institution scope, and period.

## Outputs
- Declaration workflow map and available public-record outputs.

## Primary endpoints
- Declaration guidance and registry access instructions: https://www.korruptsioon.ee/et/juhendid-kkk/huvide-deklareerimine/juhised-deklareerimiseks
- Public process explanation: https://www.eesti.ee/eraisik/en/article/working-and-labor-relations/working/annual-declaration-of-interests

## Workflow
1. Identify applicable declaration process and competent authority.
2. Determine what is publicly accessible vs restricted.
3. Extract available public declaration/control information.
4. Return evidence-backed summary with access limitations.

## Human setup (when needed)
- If registry access requires institutional rights or authenticated login, explicitly walk the user through access-request steps and proceed using any public outputs they can provide.

## Quality checks
- Separate legal/procedural guidance from actual declaration records.
- Mark access-controlled elements clearly.

## Limitations
- Full declaration registers may require role-based access and are not always openly queryable end-to-end.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.korruptsioon.ee/et/juhendid-kkk/huvide-deklareerimine/juhised-deklareerimiseks (HTTP 200, text/html;, file links detected: 6)
- https://www.eesti.ee/eraisik/en/article/working-and-labor-relations/working/annual-declaration-of-interests (HTTP 200, text/html, file links detected: 0)

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
