---
name: patent-and-trademark-registers
description: Use Estonian Patent Office sources for patents, trademarks, and industrial property register context and structured public-record extraction.
---

# Patent and Trademark Registers

## Use when
- You need official industrial property register context.
- You need structured extraction of patent/trademark public records.

## Avoid when
- You need non-official commercial IP datasets.

## Inputs
- IP type, identifier, owner/applicant, and period.

## Outputs
- Structured IP register outputs with official references.

## Primary endpoints
- Patent Office portal: https://www.patendiamet.ee/en

## Workflow
1. Locate relevant register/search route for IP type.
2. Extract public fields and status data.
3. Normalize status and classification fields.
4. Return structured dataset with provenance.

## Human setup (when needed)
- If search/export is portal-driven, guide user through lookup and continue from provided outputs.

## Quality checks
- Preserve official application/registration identifiers.
- Keep register status definitions attached.
