---
name: public-finance-data
description: Analyze Estonian state finance transparency data from RiigiRaha for budget, spending, and public-sector financial overviews.
---

# Estonia Public Finance Data (RiigiRaha)

## Use when
- You need budget and expenditure transparency data.
- You need ministry/program-level public finance context.

## Avoid when
- You need tax administration microdata (use EMTA-oriented skill).

## Inputs
- Institution/program scope and period.

## Outputs
- Finance dataset extract and metric definitions used.

## Primary endpoint
- Portal: https://riigiraha.fin.ee/

## Workflow
1. Identify target dashboard section and metric definition.
2. Export available table view to machine-readable format.
3. Standardize codes, units, and period labels.
4. Return extract with clear interpretation notes.

## Human setup (when needed)
- RiigiRaha is UI-heavy; if direct API is unavailable, walk the user through exact export clicks and continue from the downloaded file.

## Quality checks
- Distinguish budgeted vs executed values.
- Preserve institution hierarchy codes when present.
