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
