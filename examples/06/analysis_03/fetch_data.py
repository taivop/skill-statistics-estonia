#!/usr/bin/env python3
"""
Fetch retail sector data from Statistics Estonia API
Tables:
- KM00338: Retail Sales Volume Index (quarterly)
- KM0061: Retail sales by economic activity and commodity group
"""

import json
import urllib.request
import pathlib

BASE_URL = "https://andmed.stat.ee/api/v1/en/stat"
OUT_DIR = pathlib.Path(__file__).parent


def fetch_json(url, payload=None):
    """Fetch JSON data from API."""
    if payload is None:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode("utf-8"))
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode("utf-8"))


def get_structure(table_id):
    """Get table structure to understand available dimensions."""
    return fetch_json(f"{BASE_URL}/{table_id}")


# Fetch KM00338 - Retail Sales Volume Index (quarterly)
print("Fetching KM00338 structure...")
km00338_structure = get_structure("KM00338")

# Save structure for reference
with open(OUT_DIR / "km00338_structure.json", "w") as f:
    json.dump(km00338_structure, f, indent=2, ensure_ascii=False)

print("Variables in KM00338:")
for var in km00338_structure["variables"]:
    print(f"  {var['code']}: {var['text']} ({len(var['values'])} values)")
    if len(var['values']) <= 10:
        print(f"    Values: {var['values']}")

# Fetch all retail sales volume index data (full time series)
print("\nFetching KM00338 data (full time series)...")
km00338_query = {
    "query": [],  # Get all data
    "response": {"format": "json-stat2"}
}

km00338_data = fetch_json(f"{BASE_URL}/KM00338", km00338_query)

with open(OUT_DIR / "km00338_retail_sales_index.json", "w") as f:
    json.dump(km00338_data, f, indent=2, ensure_ascii=False)

print(f"Saved KM00338 data: {len(km00338_data.get('value', []))} values")

# Fetch KM0061 - Retail sales by economic activity and commodity group
print("\nFetching KM0061 structure...")
try:
    km0061_structure = get_structure("KM0061")

    with open(OUT_DIR / "km0061_structure.json", "w") as f:
        json.dump(km0061_structure, f, indent=2, ensure_ascii=False)

    print("Variables in KM0061:")
    for var in km0061_structure["variables"]:
        print(f"  {var['code']}: {var['text']} ({len(var['values'])} values)")

    # Fetch commodity group data
    print("\nFetching KM0061 data...")
    km0061_query = {
        "query": [],  # Get all data
        "response": {"format": "json-stat2"}
    }

    km0061_data = fetch_json(f"{BASE_URL}/KM0061", km0061_query)

    with open(OUT_DIR / "km0061_retail_by_commodity.json", "w") as f:
        json.dump(km0061_data, f, indent=2, ensure_ascii=False)

    print(f"Saved KM0061 data: {len(km0061_data.get('value', []))} values")

except Exception as e:
    print(f"Note: Could not fetch KM0061: {e}")
    print("Will proceed with KM00338 data only.")

print("\nData fetch complete!")
