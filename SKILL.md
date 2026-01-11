---
name: querying-statistics-estonia-api
description: Query the Statistics Estonia API (andmed.stat.ee) to discover tables, inspect metadata, and fetch official statistics; includes access to comprehensive ESMS metadata (methodology, sources, quality documentation); use when you need Estonian statistical datasets or time series.
---

# Statistics Estonia API

## Use when
- Need official statistics or time series from Statistikaamet.
- Need to discover datasets and query data via the API.
- Need methodology, data sources, quality documentation, or collection methods for a statistical table.

## Avoid when
- The data is already stored locally in this repo (use local DB skills first).

## Inputs
- Table ID and variable selections.

## Outputs
- JSON, JSON-stat, or CSV responses from the API.
- ESMS metadata HTML (methodology, sources, quality, classifications, etc.).

## Primary tools
- API base: https://andmed.stat.ee/api/v1
- Metadata script: `get_metadata.py`

## Workflow

### For querying data:
1. Search for a table.
2. Inspect table metadata to get variable codes and values.
3. POST a query with your selections.

### For accessing methodology and context:
1. **IMPORTANT**: Before working with a table, always fetch its ESMS metadata for critical context.
2. Run: `python get_metadata.py TABLE_ID`
3. Review the metadata HTML to understand:
   - Data collection methodology
   - Source data and validation procedures
   - Classification systems used
   - Quality indicators and reliability
   - Related tables and documentation
   - Contact information for questions

## Examples

The `examples` directory is intended for human consumption and shows the outputs of agent runs on a set of prompts. 

### Query data from API
```bash
# Search for tables
curl -s "https://andmed.stat.ee/api/v1/en/stat?query=price"

# Get table structure
curl -s "https://andmed.stat.ee/api/v1/en/stat/IA001"

# Query data
curl -s -X POST "https://andmed.stat.ee/api/v1/en/stat/IA001" \
  -H "Content-Type: application/json" \
  -d '{"query":[{"code":"Time","selection":{"filter":"item","values":["2023"]}}],"response":{"format":"json-stat2"}}'
```

### Get comprehensive metadata (RECOMMENDED)
```bash
# Get ESMS metadata for a table - includes methodology, sources, quality documentation

# Default: Full HTML (~55KB)
python get_metadata.py IA001

# Simplified HTML: 66% smaller (~18KB), clean structure
python get_metadata.py IA001 --format simple

# Plain text: 77% smaller (~12KB), most readable
python get_metadata.py IA001 --format text

# The metadata contains 19 standardized ESMS sections:
# 1. Contact - who maintains this data
# 3. Statistical presentation - what is measured, classifications used
# 10. Accessibility and clarity - related tables, documentation links
# 18. Statistical processing - how data is collected, validated, compiled
# And more: quality management, accuracy, timeliness, coherence, etc.
```

## Best practices
- **Always check metadata first** when working with a new table to understand context, limitations, and methodology.
- The API provides data structure (variables, codes) but NOT methodology or sources.
- ESMS metadata provides the full picture: how data is collected, validated, what it represents, and quality indicators.
- Some tables share the same ESMS metadata (e.g., all CPI tables reference metadata ID 20407).
- **Use `--format text` for fastest reading** (77% smaller), or `--format simple` for cleaner HTML (66% smaller).
