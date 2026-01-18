#!/usr/bin/env python3
"""
Analysis 4: Food Price Inflation Drivers in Estonia
Examines Estonia's food price inflation trends, drivers, and comparison to EU
"""

import json
import math
import urllib.request
from itertools import product
from datetime import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10

BASE_URL = "https://andmed.stat.ee/api/v1/en/stat"


def fetch_json(url, payload=None):
    """Fetch JSON data from API"""
    if payload is None:
        with urllib.request.urlopen(url, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def _expand_values(values, total_size):
    """Expand sparse value dictionary to full array"""
    if isinstance(values, dict):
        expanded = [None] * total_size
        for key, value in values.items():
            expanded[int(key)] = value
        return expanded
    return values


def jsonstat_to_dataframe(data):
    """Convert JSON-stat format to pandas DataFrame"""
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


def fetch_cpi_data():
    """Fetch CPI data from IA02 table (monthly, by commodity group)"""
    print("Fetching CPI data from IA02...")

    # Query for years 2020-2025, all commodity groups, all months
    query = {
        "query": [
            {"code": "Aasta", "selection": {"filter": "item",
                "values": ["2020", "2021", "2022", "2023", "2024", "2025"]}},
            {"code": "Kaubagrupp", "selection": {"filter": "all", "values": ["*"]}},
            {"code": "Kuu", "selection": {"filter": "all", "values": ["*"]}}
        ],
        "response": {"format": "json-stat2"}
    }

    data = fetch_json(f"{BASE_URL}/IA02", query)

    # Save raw response
    with open('cpi_monthly_raw.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Convert to dataframe
    df = jsonstat_to_dataframe(data)

    # Create date column
    df['date'] = pd.to_datetime(df['Aasta'] + '-' + df['Kuu'].map({
        'January': '01', 'February': '02', 'March': '03', 'April': '04',
        'May': '05', 'June': '06', 'July': '07', 'August': '08',
        'September': '09', 'October': '10', 'November': '11', 'December': '12'
    }) + '-01')

    df = df.rename(columns={'Kaubagrupp': 'commodity_group', 'value': 'index'})
    df = df[['date', 'commodity_group', 'index']]
    df = df.sort_values('date')

    return df


def calculate_inflation_rates(df):
    """Calculate year-over-year inflation rates"""
    df = df.copy()
    df = df.sort_values(['commodity_group', 'date'])

    # Calculate YoY inflation rate
    df['inflation_yoy'] = df.groupby('commodity_group')['index'].pct_change(periods=12) * 100

    # Calculate month-over-month
    df['inflation_mom'] = df.groupby('commodity_group')['index'].pct_change() * 100

    return df


def create_eu_comparison_data():
    """
    Create ESTIMATED EU comparison data interpolated from ECB literature reference points.

    IMPORTANT: This is NOT actual Eurostat HICP data. Values are interpolated
    from ECB (2024) reported reference points:
    - Peak: ~15% (March 2023)
    - January 2024: 5.7%

    For rigorous analysis, actual Eurostat HICP food category data should be used.
    This estimated line is provided for illustrative purposes only.
    """
    dates = pd.date_range('2020-01-01', '2025-12-01', freq='MS')

    # Estonia actual trend (will be replaced with real data)
    # EU average based on ECB literature
    eu_inflation = []

    for date in dates:
        if date < pd.Timestamp('2021-06-01'):
            # Pre-inflation period
            inflation = np.random.normal(2.5, 0.3)
        elif date < pd.Timestamp('2022-03-01'):
            # Rising inflation
            months_since = (date - pd.Timestamp('2021-06-01')).days / 30
            inflation = 2.5 + (8.0 - 2.5) * (months_since / 9)
        elif date < pd.Timestamp('2023-03-01'):
            # Peak inflation period
            months_since = (date - pd.Timestamp('2022-03-01')).days / 30
            inflation = 8.0 + (15.0 - 8.0) * (months_since / 12)
        elif date < pd.Timestamp('2024-01-01'):
            # Declining from peak
            months_since = (date - pd.Timestamp('2023-03-01')).days / 30
            inflation = 15.0 - (15.0 - 5.7) * (months_since / 10)
        else:
            # Continued decline
            months_since = (date - pd.Timestamp('2024-01-01')).days / 30
            inflation = max(2.0, 5.7 - (5.7 - 2.5) * (months_since / 24))

        eu_inflation.append(inflation)

    eu_df = pd.DataFrame({
        'date': dates,
        'eu_food_inflation': eu_inflation
    })

    return eu_df


def main():
    """Main analysis workflow"""

    # 1. Fetch CPI data
    cpi_df = fetch_cpi_data()
    print(f"Fetched {len(cpi_df)} CPI data points")

    # 2. Calculate inflation rates
    cpi_df = calculate_inflation_rates(cpi_df)

    # 3. Save processed data
    cpi_df.to_csv('cpi_monthly_processed.csv', index=False)
    print("Saved cpi_monthly_processed.csv")

    # 4. Extract food-specific data
    food_df = cpi_df[cpi_df['commodity_group'] == 'Food and non-alcoholic beverages'].copy()
    total_df = cpi_df[cpi_df['commodity_group'] == 'Total'].copy()

    # 5. Create EU comparison data
    eu_df = create_eu_comparison_data()

    # 6. Merge for comparison
    comparison_df = food_df[['date', 'inflation_yoy']].merge(
        eu_df, on='date', how='left'
    )
    comparison_df = comparison_df.rename(columns={'inflation_yoy': 'estonia_food_inflation'})

    # 7. Create visualizations
    print("Creating visualizations...")

    # Visualization 1: Food inflation trend over time
    fig, ax = plt.subplots(figsize=(16, 8))

    ax.plot(food_df['date'], food_df['inflation_yoy'],
            linewidth=2.5, marker='o', markersize=4,
            label='Estonia Food Inflation', color='#d62728')
    ax.plot(total_df['date'], total_df['inflation_yoy'],
            linewidth=2, linestyle='--', alpha=0.7,
            label='Estonia Overall CPI', color='#1f77b4')

    ax.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
    ax.axvline(x=pd.Timestamp('2022-02-24'), color='black',
               linestyle=':', alpha=0.5, linewidth=2)
    ax.text(pd.Timestamp('2022-02-24'), ax.get_ylim()[1] * 0.95,
            'Ukraine War', rotation=0, ha='left', fontsize=10)

    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.set_ylabel('Year-over-Year Inflation (%)', fontsize=12, fontweight='bold')
    ax.set_title('Estonia: Food Price Inflation vs Overall CPI (2020-2025)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper left', fontsize=11)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('food_inflation_trend.png', dpi=300, bbox_inches='tight')
    print("Saved food_inflation_trend.png")
    plt.close()

    # Visualization 2: Estonia vs EU comparison
    fig, ax = plt.subplots(figsize=(16, 8))

    valid_comparison = comparison_df.dropna()
    ax.plot(valid_comparison['date'], valid_comparison['estonia_food_inflation'],
            linewidth=2.5, marker='o', markersize=5,
            label='Estonia', color='#0072CE')
    ax.plot(valid_comparison['date'], valid_comparison['eu_food_inflation'],
            linewidth=2.5, marker='s', markersize=5, linestyle='--',
            label='EU Average (ESTIMATED from ECB 2024 - not actual Eurostat data)', color='#FDB913')

    # Mark key events
    ax.axvline(x=pd.Timestamp('2022-02-24'), color='black',
               linestyle=':', alpha=0.5, linewidth=2)
    ax.text(pd.Timestamp('2022-02-24'), ax.get_ylim()[1] * 0.95,
            'Ukraine War', rotation=0, ha='left', fontsize=10)

    # Mark peak inflation
    if len(valid_comparison) > 0:
        peak_estonia = valid_comparison.loc[valid_comparison['estonia_food_inflation'].idxmax()]
        ax.plot(peak_estonia['date'], peak_estonia['estonia_food_inflation'],
                'r*', markersize=20, label=f'Estonia Peak: {peak_estonia["estonia_food_inflation"]:.1f}%')

    ax.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.set_ylabel('Food Price Inflation YoY (%)', fontsize=12, fontweight='bold')
    ax.set_title('Food Price Inflation: Estonia vs EU Average (2020-2025)\n(EU line is ESTIMATED from ECB reference points, not actual Eurostat data)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper left', fontsize=11)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('estonia_vs_eu_comparison.png', dpi=300, bbox_inches='tight')
    print("Saved estonia_vs_eu_comparison.png")
    plt.close()

    # Visualization 3: Commodity group comparison
    fig, ax = plt.subplots(figsize=(16, 10))

    # Select key commodity groups
    key_groups = [
        'Total',
        'Food and non-alcoholic beverages',
        'Housing',
        'Transport',
        'Recreation, entertainment'
    ]

    colors = ['#1f77b4', '#d62728', '#2ca02c', '#ff7f0e', '#9467bd']

    for group, color in zip(key_groups, colors):
        group_df = cpi_df[cpi_df['commodity_group'] == group]
        ax.plot(group_df['date'], group_df['inflation_yoy'],
                linewidth=2, marker='o', markersize=3,
                label=group, color=color, alpha=0.8)

    ax.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
    ax.axvline(x=pd.Timestamp('2022-02-24'), color='black',
               linestyle=':', alpha=0.5, linewidth=2)
    ax.text(pd.Timestamp('2022-02-24'), ax.get_ylim()[1] * 0.95,
            'Ukraine War', rotation=0, ha='left', fontsize=10)

    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.set_ylabel('Year-over-Year Inflation (%)', fontsize=12, fontweight='bold')
    ax.set_title('Estonia: Inflation by Commodity Group (2020-2025)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('commodity_group_comparison.png', dpi=300, bbox_inches='tight')
    print("Saved commodity_group_comparison.png")
    plt.close()

    # Print summary statistics
    print("\n" + "="*60)
    print("FOOD INFLATION SUMMARY STATISTICS")
    print("="*60)

    recent_food = food_df[food_df['date'] >= '2020-01-01'].copy()
    if len(recent_food) > 0:
        print(f"\nFood Inflation (2020-2025):")
        print(f"  Mean: {recent_food['inflation_yoy'].mean():.2f}%")
        print(f"  Median: {recent_food['inflation_yoy'].median():.2f}%")
        print(f"  Max: {recent_food['inflation_yoy'].max():.2f}% ({recent_food.loc[recent_food['inflation_yoy'].idxmax(), 'date'].strftime('%B %Y')})")
        print(f"  Min: {recent_food['inflation_yoy'].min():.2f}% ({recent_food.loc[recent_food['inflation_yoy'].idxmin(), 'date'].strftime('%B %Y')})")
        print(f"  Std Dev: {recent_food['inflation_yoy'].std():.2f}%")

        # Latest value
        latest = recent_food.iloc[-1]
        print(f"\nLatest (as of {latest['date'].strftime('%B %Y')}):")
        print(f"  Food Inflation: {latest['inflation_yoy']:.2f}%")

    # Compare 2022-2023 period
    crisis_food = food_df[(food_df['date'] >= '2022-01-01') &
                          (food_df['date'] <= '2023-12-31')].copy()
    if len(crisis_food) > 0:
        print(f"\nCrisis Period (2022-2023):")
        print(f"  Average Food Inflation: {crisis_food['inflation_yoy'].mean():.2f}%")
        print(f"  Peak: {crisis_food['inflation_yoy'].max():.2f}%")

    print("\n" + "="*60)
    print("Analysis complete!")
    print("="*60)


if __name__ == '__main__':
    main()
