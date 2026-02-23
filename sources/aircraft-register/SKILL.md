---
name: aircraft-register
description: Use official aircraft register pages for aircraft registration status and aviation registry context.
---

# Aircraft Register

## Use when
- You need official aircraft registration context.
- You need structured extraction of aircraft register fields.

## Avoid when
- You need air-incident reporting analytics (use aviation occurrence skill).

## Inputs
- Aircraft identifier, registration, or date scope.

## Outputs
- Structured aircraft registry records and status metadata.

## Primary endpoints
- Aircraft register context: https://www.transpordiamet.ee/en/vehicle-ship-airplane/aircraft-registration/aircraft-register

## Workflow
1. Locate register access path and search fields.
2. Extract registration/status fields.
3. Normalize aircraft identifier formats.
4. Return structured dataset with source references.

## Human setup (when needed)
- If registry lookup requires manual portal interaction, guide user through steps and continue from exported/copied output.

## Quality checks
- Keep official registration identifiers unchanged.
- Separate current status from historical notes.
