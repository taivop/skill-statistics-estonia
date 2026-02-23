#!/usr/bin/env python3
"""
Fetch and process Statistics Estonia data for:
- Crude birth rate (RV030)
- Live births by educational level of mother (RV144 + RV144U)
Outputs:
- JSON responses
- CSV datasets
- PNG chart
"""

import json
import math
import pathlib
import urllib.request
from itertools import product

import matplotlib.pyplot as plt
import pandas as pd

BASE_URL = "https://andmed.stat.ee/api/v1/en/stat"
OUT_DIR = pathlib.Path("examples/05")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def fetch_json(url, payload=None):
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
    return fetch_json(f"{BASE_URL}/{table_id}")


def _expand_values(values, total_size):
    if isinstance(values, dict):
        expanded = [None] * total_size
        for key, value in values.items():
            expanded[int(key)] = value
        return expanded
    return values


def jsonstat_to_dataframe(data):
    if "id" in data and "size" in data:
        dims = data["id"]
        sizes = data["size"]
    else:
        dims = data["dimension"]["id"]
        sizes = data["dimension"]["size"]
    values = _expand_values(data["value"], math.prod(sizes))

    dim_codes = {}
    dim_labels = {}

    for dim in dims:
        cat = data["dimension"][dim]["category"]
        idx = cat["index"]
        if isinstance(idx, dict):
            codes = [None] * len(idx)
            for code, pos in idx.items():
                codes[pos] = code
        else:
            codes = list(idx)
        labels = cat.get("label", {})
        label_list = [labels.get(code, code) for code in codes]
        dim_codes[dim] = codes
        dim_labels[dim] = label_list

    multipliers = []
    running = 1
    for size in reversed(sizes):
        multipliers.insert(0, running)
        running *= size

    records = []
    for idxs in product(*[range(size) for size in sizes]):
        flat_index = sum(idx * mult for idx, mult in zip(idxs, multipliers))
        value = values[flat_index]
        if value is None:
            continue
        record = {dim: dim_labels[dim][idx] for dim, idx in zip(dims, idxs)}
        record["value"] = value
        records.append(record)

    return pd.DataFrame(records)


# --- Fetch birth rate data (RV030) ---
rv030_structure = get_structure("RV030")
rv030_years = [
    y for y in rv030_structure["variables"][0]["values"] if 2005 <= int(y) <= 2024
]

rv030_query = {
    "query": [
        {"code": "Aasta", "selection": {"filter": "item", "values": rv030_years}},
        {"code": "Näitaja", "selection": {"filter": "item", "values": ["4"]}},
    ],
    "response": {"format": "json-stat2"},
}

rv030_data = fetch_json(f"{BASE_URL}/RV030", rv030_query)
(OUT_DIR / "rv030_birth_rate.json").write_text(
    json.dumps(rv030_data, ensure_ascii=True, indent=2),
    encoding="utf-8",
)

rv030_df = jsonstat_to_dataframe(rv030_data)
rv030_df["Year"] = rv030_df["Aasta"].astype(int)
rv030_df = rv030_df.rename(columns={"value": "Crude_birth_rate"})
rv030_df = rv030_df[["Year", "Crude_birth_rate"]].sort_values("Year")


# --- Fetch maternal education data (RV144 + RV144U) ---

def fetch_births_by_education(table_id, start_year, end_year, out_name):
    structure = get_structure(table_id)
    var_map = {var["code"]: var for var in structure["variables"]}

    years = [
        y for y in var_map["Aasta"]["values"] if start_year <= int(y) <= end_year
    ]
    counties = var_map["Maakond"]["values"]
    age_total = [var_map["Ema vanus"]["values"][0]]
    edu_values = var_map["Ema haridustase"]["values"][1:]

    query = {
        "query": [
            {"code": "Aasta", "selection": {"filter": "item", "values": years}},
            {
                "code": "Maakond",
                "selection": {"filter": "item", "values": counties},
            },
            {"code": "Ema vanus", "selection": {"filter": "item", "values": age_total}},
            {
                "code": "Ema haridustase",
                "selection": {"filter": "item", "values": edu_values},
            },
        ],
        "response": {"format": "json-stat2"},
    }

    data = fetch_json(f"{BASE_URL}/{table_id}", query)
    (OUT_DIR / out_name).write_text(
        json.dumps(data, ensure_ascii=True, indent=2),
        encoding="utf-8",
    )

    df = jsonstat_to_dataframe(data)
    df["Year"] = df["Aasta"].astype(int)
    df = df.rename(
        columns={
            "Ema haridustase": "Education",
            "Maakond": "County",
            "Ema vanus": "Age_group",
            "value": "Births",
        }
    )
    return df


rv144_df = fetch_births_by_education("RV144", 2005, 2016, "rv144_births_2005_2016.json")
rv144u_df = fetch_births_by_education("RV144U", 2017, 2024, "rv144u_births_2017_2024.json")

births_df = pd.concat([rv144_df, rv144u_df], ignore_index=True)

# Aggregate across counties to national totals
births_edu = (
    births_df.groupby(["Year", "Education"], as_index=False)["Births"].sum()
)

births_edu.to_csv(OUT_DIR / "births_by_maternal_education.csv", index=False)

# Compute average education index (exclude unknown from weighting)
edu_weights = {
    "Primary or basic education": 1,
    "Secondary education": 2,
    "Higher education": 3,
}
unknown_label = "Educational level unknown"

records = []
for year, group in births_edu.groupby("Year"):
    total_all = group["Births"].sum()
    known = group[group["Education"].isin(edu_weights)]
    total_known = known["Births"].sum()
    weighted = (known["Births"] * known["Education"].map(edu_weights)).sum()
    avg_index = weighted / total_known if total_known else None
    unknown_births = group.loc[group["Education"] == unknown_label, "Births"].sum()
    unknown_share = unknown_births / total_all if total_all else None
    records.append(
        {
            "Year": year,
            "Avg_maternal_edu_index": avg_index,
            "Unknown_education_share": unknown_share,
        }
    )

edu_index_df = pd.DataFrame(records).sort_values("Year")

# Merge with birth rate data
combined_df = pd.merge(rv030_df, edu_index_df, on="Year", how="inner").sort_values("Year")
combined_df.to_csv(OUT_DIR / "birth_rate_and_maternal_education.csv", index=False)

# --- Visualization ---
plt.style.use("seaborn-v0_8-whitegrid")
fig, ax1 = plt.subplots(figsize=(12, 7))

ax1.plot(
    combined_df["Year"],
    combined_df["Crude_birth_rate"],
    color="#1f77b4",
    linewidth=2.5,
    marker="o",
    label="Crude birth rate (per 1,000)",
)
ax1.set_xlabel("Year")
ax1.set_ylabel("Crude birth rate (per 1,000)", color="#1f77b4")
ax1.tick_params(axis="y", labelcolor="#1f77b4")

ax2 = ax1.twinx()
ax2.plot(
    combined_df["Year"],
    combined_df["Avg_maternal_edu_index"],
    color="#d62728",
    linewidth=2.5,
    marker="s",
    label="Average maternal education index",
)
ax2.set_ylabel("Average maternal education index (1=basic, 3=higher)", color="#d62728")
ax2.tick_params(axis="y", labelcolor="#d62728")

ax1.set_title(
    "Estonia: Crude Birth Rate and Average Maternal Education Index (2005–2024)",
    fontsize=14,
    fontweight="bold",
)

# Build a combined legend
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper right")

fig.tight_layout()
chart_path = OUT_DIR / "birth_rate_vs_maternal_education.png"
plt.savefig(chart_path, dpi=300, bbox_inches="tight")

print(f"Saved chart to {chart_path}")
