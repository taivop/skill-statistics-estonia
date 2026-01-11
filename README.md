# Statistics Estonia Skill

A Claude Code skill for accessing and querying Statistics Estonia's official statistical database (Statistikaamet). This skill provides programmatic access to over 1,000 statistical tables through the REST API and fetches comprehensive methodology documentation through the ESMS metadata system.

## What is this?

This is a skill designed for use with Claude Code and AI agents that need to work with Estonian official statistics. It provides two main capabilities:

1. **Query statistical data** - Search, discover, and fetch data from Statistics Estonia's API (andmed.stat.ee)
2. **Fetch methodology documentation** - Access comprehensive ESMS metadata including data collection methods, sources, quality indicators, and statistical processing information

## What does it do?

### Data Querying
- Search for statistical tables by keyword or topic
- Inspect table structure (variables, dimensions, available values)
- Query specific data points or time series
- Get data in JSON, JSON-stat, or CSV formats

### Metadata Access
The included `get_metadata.py` script fetches standardized ESMS (European Statistical System) metadata for any table, including:
- **Contact information** - Who maintains and publishes the data
- **Statistical presentation** - What is being measured, classifications used, concepts
- **Methodology** - How data is collected, validated, and compiled
- **Data sources** - Primary and secondary sources
- **Quality indicators** - Accuracy, reliability, timeliness metrics
- **Related documentation** - News releases, publications, methodology papers
- **Legal framework** - Regulations and mandates governing the statistics

The script provides three output formats:
- **Full HTML** (~55KB) - Complete markup with all attributes
- **Simplified HTML** (~18KB, 66% smaller) - Clean structure without unnecessary attributes
- **Plain text** (~12KB, 77% smaller) - Most readable format for quick review

## How to use it

### Prerequisites
- Python 3.x (standard library only, no dependencies)
- `curl` for API queries (or any HTTP client)

### Quick Start

#### 1. Search for tables
```bash
# Find tables related to "price"
curl -s "https://andmed.stat.ee/api/v1/en/stat?query=price" | python -m json.tool

# Find tables about population
curl -s "https://andmed.stat.ee/api/v1/en/stat?query=population"
```

#### 2. Inspect table structure
```bash
# Get metadata about table IA001 (Consumer Price Index)
curl -s "https://andmed.stat.ee/api/v1/en/stat/IA001" | python -m json.tool
```

This returns the table structure including:
- Available variables and their codes
- Dimension values
- Time periods available
- Table title and description

#### 3. Query specific data
```bash
# Query CPI data for 2023
curl -s -X POST "https://andmed.stat.ee/api/v1/en/stat/IA001" \
  -H "Content-Type: application/json" \
  -d '{
    "query": [
      {
        "code": "Aasta",
        "selection": {
          "filter": "item",
          "values": ["2023"]
        }
      }
    ],
    "response": {
      "format": "json"
    }
  }' | python -m json.tool
```

#### 4. Get comprehensive methodology documentation
```bash
# Get ESMS metadata for Consumer Price Index
python get_metadata.py IA001

# Get simplified HTML (66% smaller, cleaner)
python get_metadata.py IA001 --format simple

# Get plain text (77% smaller, most readable)
python get_metadata.py IA001 --format text
```

The metadata includes 19 standardized ESMS sections covering everything from data collection methodology to quality management frameworks.

## Example Prompts

If you're using this skill with Claude Code or an AI agent, here are some example prompts to get started:

### Data Discovery
- "Search the Statistics Estonia database for tables related to unemployment"
- "Find all available consumer price index tables"
- "What statistical tables are available about education in Estonia?"

### Data Querying
- "Get the latest consumer price index data from Statistics Estonia"
- "Show me the population of Estonia by county for the years 2020-2023"
- "Query table IA001 for CPI data from January to December 2023"

### Methodology & Context
- "Get the ESMS metadata for table RV106 to understand how birth statistics are collected"
- "Show me the methodology documentation for the consumer price index"
- "What are the data sources and quality indicators for unemployment statistics?"

### Combined Workflows
- "Search for GDP tables, get the metadata to understand the methodology, then query the latest annual data"
- "Find wage statistics, check the ESMS metadata for data collection methods, and extract data for 2023"
- "Get consumer price index data and explain how it's calculated based on the metadata"

## Files

- **`get_metadata.py`** - Python script to fetch ESMS metadata for any Statistics Estonia table
- **`SKILL.md`** - Detailed skill documentation for AI agents (workflow, best practices, API reference)
- **`README.md`** - This file (human-friendly documentation)

## API Documentation

- [Statistics Estonia Database](https://andmed.stat.ee/en/stat) - Main web interface
- [API Manual (PDF)](https://andmed.stat.ee/help/api-manual.pdf) - Complete API reference
- [ESMS Metadata System](https://www.stat.ee/en/find-statistics/methodology-and-quality/esms-metadata) - Methodology documentation portal

## Notes

- The API provides data structure and values, but NOT methodology or context
- ESMS metadata provides the full picture: how data is collected, what it represents, and quality indicators
- Some tables share the same ESMS metadata (e.g., all CPI tables reference metadata ID 20407)
- Not all tables have ESMS metadata - the script will warn if unavailable
- Use `--format text` for the most readable and compact metadata output

## Use Cases

This skill is particularly useful for:
- Economic analysis and research
- Policy analysis requiring official statistics
- Data journalism and fact-checking
- Academic research on Estonian society and economy
- Business intelligence and market research
- Understanding statistical methodology and data quality
- Building applications that need official Estonian statistics

## License

This skill is provided as-is for accessing public official statistics from Statistics Estonia. The data itself is published by Statistics Estonia under their terms of use.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
