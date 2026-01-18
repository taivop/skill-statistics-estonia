#!/usr/bin/env python3
"""
Fetch tax revenue and retail sales data from Statistics Estonia API
"""

import json
import urllib.request
import urllib.error


def fetch_url(url, data=None, timeout=30):
    """Fetch URL with optional POST data"""
    try:
        if data:
            data = json.dumps(data).encode('utf-8')
            req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
        else:
            req = urllib.request.Request(url)

        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Error fetching {url}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def save_json(data, filename):
    """Save data to JSON file"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved {filename}")


# Fetch RR027 - Monthly tax revenues (all tax types)
print("Fetching RR027: Monthly tax revenues...")
rr027_query = {
    "query": [
        {
            "code": "Näitaja",
            "selection": {
                "filter": "item",
                "values": ["TAX"]
            }
        },
        {
            "code": "Maksu liik",
            "selection": {
                "filter": "item",
                "values": ["TAX", "VAT", "MOT", "INC", "SS", "EX"]  # Total, VAT, Motor vehicle, Income, Social security, Excise
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
}

tax_data = fetch_url("https://andmed.stat.ee/api/v1/en/stat/RR027", data=rr027_query)
if tax_data:
    save_json(tax_data, "tax_revenues_monthly.json")


# Fetch RR024 - Quarterly tax revenues for comparison
print("Fetching RR024: Quarterly tax revenues...")
rr024_query = {
    "query": [
        {
            "code": "Näitaja",
            "selection": {
                "filter": "item",
                "values": ["TAX"]
            }
        },
        {
            "code": "Maksu liik",
            "selection": {
                "filter": "item",
                "values": ["TAX", "VAT", "MOT", "INC", "SS", "EX"]
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
}

tax_data_q = fetch_url("https://andmed.stat.ee/api/v1/en/stat/RR024", data=rr024_query)
if tax_data_q:
    save_json(tax_data_q, "tax_revenues_quarterly.json")


# Fetch KM00338 - Retail sales volume index
print("Fetching KM00338: Retail sales volume index...")
km00338_query = {
    "query": [
        {
            "code": "Näitaja",
            "selection": {
                "filter": "item",
                "values": ["RETAIL"]
            }
        },
        {
            "code": "Tegevusala",
            "selection": {
                "filter": "item",
                "values": ["G45_47"]
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
}

retail_data = fetch_url("https://andmed.stat.ee/api/v1/en/stat/KM00338", data=km00338_query)
if retail_data:
    save_json(retail_data, "retail_sales.json")


# Fetch KM0061 - Retail sales by commodity (for vehicle sales)
print("Fetching KM0061: Retail sales by commodity...")
km0061_metadata = fetch_url("https://andmed.stat.ee/api/v1/en/stat/KM0061")
if km0061_metadata:
    save_json(km0061_metadata, "km0061_metadata.json")
    print("Got KM0061 metadata - checking for vehicle-related data")


# Fetch CPI data for context
print("Fetching IA021: Consumer Price Index (monthly)...")
ia021_query = {
    "query": [
        {
            "code": "Näitaja",
            "selection": {
                "filter": "item",
                "values": ["1"]  # Change compared to same month of previous year
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
}

cpi_data = fetch_url("https://andmed.stat.ee/api/v1/en/stat/IA021", data=ia021_query)
if cpi_data:
    save_json(cpi_data, "cpi_monthly.json")


print("\nData fetch complete!")
