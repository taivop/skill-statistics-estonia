---
name: ship-registers
description: Use official Estonian ship register sources for vessel registration and maritime registry governance context.
---

# Ship Registers

## Use when
- You need official vessel registration context.
- You need ship-register fields for compliance/governance analysis.

## Avoid when
- You need port infrastructure records only.

## Inputs
- Vessel identifier, register type, and period.

## Outputs
- Structured vessel register extract and status fields.

## Primary endpoints
- Estonian ship registers: https://www.transpordiamet.ee/en/vehicle-ship-airplane/ships/estonian-ship-registers

## Workflow
1. Determine relevant ship register type.
2. Extract available vessel registration fields.
3. Normalize vessel and status identifiers.
4. Return structured dataset with provenance.

## Human setup (when needed)
- If register browsing/export is manual-only, guide user through the process and continue from supplied results.

## Quality checks
- Keep register type explicit in outputs.
- Separate active registration from historical/inactive states.
