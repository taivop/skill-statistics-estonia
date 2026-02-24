---
name: animal-keeper-registering
description: Use Agriculture and Food Board animal keeper registration sources for registry workflow context and extractable official outputs.
---

# Animal Keeper Registering

## Use when
- You need official animal-keeper registration workflow context.
- You need structured extraction from publicly available registration materials.

## Avoid when
- You need detailed confidential farm-level records.

## Access reality
- Public access type: process/guidance content with links to services.
- Public machine-readable register dumps are not the main access mode on this page.

## Inputs
- Registration topic, species scope, and period.

## Outputs
- Structured registration process/output references and fields.

## Primary endpoints
- Main page: https://pta.agri.ee/en/animals/registering-keeper-animals
- Linked PRIA portal (service flow): http://www.pria.ee/et/ePRIA
- Linked agriculture portal (service flow): https://portaal.agri.ee/epm-portal-ng/esileht.html

## Retrieval workflow
1. Open registration page and extract official requirements, process steps, and authority references.
2. Identify whether requested information is publicly visible or requires authenticated service access.
3. Extract publicly available identifiers, forms, and declared process outputs.
4. If authenticated outputs are required, switch to human-guided retrieval and continue from user-provided files.

## Request contract
- No open API contract is documented for public keeper-level register extraction on this source page.
- Treat as workflow/procedure extraction unless user provides authenticated exports.

## Output schema expectations
- Keep at least:
  - process step
  - required actor (keeper, authority, service)
  - required documents/inputs
  - resulting official output/status
  - source URL and date metadata

## Limits and caveats
- Some linked systems are login-based.
- Public page is process-oriented, not a bulk public register endpoint.
- Keep confidentiality boundaries explicit.

## Verification hooks
- Verify each extracted process requirement is backed by a source URL.
- Verify distinction between publicly visible guidance and authenticated registry outputs.

## Quality checks
- Keep authoritative identifiers where provided.
- Distinguish guidance content from register outputs.
