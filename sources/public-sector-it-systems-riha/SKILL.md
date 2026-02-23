---
name: public-sector-it-systems-riha
description: Query RIHA information-systems registry for official metadata about Estonian public-sector IT systems, owners, and integration context.
---

# Public-Sector IT Systems (RIHA)

## Use when
- You need official registry metadata on state information systems.
- You need system-owner and interoperability context.

## Avoid when
- You need runtime operational logs rather than registry metadata.

## Inputs
- System keywords, institution, domain.

## Outputs
- RIHA system metadata list with links.

## Primary endpoint
- Search page: https://riha.eesti.ee/riha/main/infSystem/search

## Workflow
1. Search systems by institution/topic.
2. Extract system name, owner, purpose, and status metadata.
3. Capture links to related documentation where available.
4. Return normalized catalog table.

## Human setup (when needed)
- If detailed records require manual expansion, guide user through selecting records and sharing links/screenshots.

## Quality checks
- Preserve unique system IDs and owner fields.
- Separate active vs historical/deprecated records.
