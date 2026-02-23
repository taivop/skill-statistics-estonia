---
name: querying-state-services-catalog
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
