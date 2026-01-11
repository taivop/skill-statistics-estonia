#!/usr/bin/env python3
"""
Create cumulative salary distribution chart comparing men vs women
Data source: Statistics Estonia PA623 table
"""

import json
import matplotlib.pyplot as plt
import numpy as np

# Load data
with open('examples/01/data.json', 'r') as f:
    data = json.load(f)

# Extract values - data is organized as [D1_M, D1_F, D2_M, D2_F, ...]
values = data['value']

# Parse the data: deciles vary fastest in the first dimension
# Structure: 9 deciles x 2 sexes
males_earnings = []
females_earnings = []

for i in range(9):  # 9 deciles
    idx = i * 2  # Each decile has 2 values (M, F)
    males_earnings.append(values[idx])
    females_earnings.append(values[idx + 1])

# Cumulative percentages for deciles (10%, 20%, ..., 90%)
percentiles = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# Create the chart
plt.figure(figsize=(12, 7))

# Plot cumulative distributions
plt.plot(males_earnings, percentiles, 'o-', linewidth=2.5, markersize=8,
         label='Males', color='#2E86AB', alpha=0.8)
plt.plot(females_earnings, percentiles, 's-', linewidth=2.5, markersize=8,
         label='Females', color='#A23B72', alpha=0.8)

# Add grid
plt.grid(True, alpha=0.3, linestyle='--')

# Labels and title
plt.xlabel('Gross Hourly Earnings (EUR)', fontsize=12, fontweight='bold')
plt.ylabel('Cumulative Percentage (%)', fontsize=12, fontweight='bold')
plt.title('Cumulative Salary Distribution: Males vs Females\nEstonia, October 2022',
          fontsize=14, fontweight='bold', pad=20)

# Legend
plt.legend(fontsize=11, loc='lower right', framealpha=0.95)

# Add median line
median_idx = 4  # 5th decile (50th percentile)
plt.axhline(y=50, color='gray', linestyle=':', alpha=0.5, linewidth=1.5)
plt.text(males_earnings[median_idx] + 0.3, 52,
         f'Median M: €{males_earnings[median_idx]:.2f}',
         fontsize=9, color='#2E86AB')
plt.text(females_earnings[median_idx] + 0.3, 48,
         f'Median F: €{females_earnings[median_idx]:.2f}',
         fontsize=9, color='#A23B72')

# Format axes
plt.xlim(4, 22)
plt.ylim(0, 100)

# Add source note
plt.figtext(0.99, 0.01, 'Source: Statistics Estonia (PA623)',
            ha='right', fontsize=8, style='italic', color='gray')

plt.tight_layout()
plt.savefig('examples/01/cumulative_distribution.png', dpi=300, bbox_inches='tight')
print("Chart saved to examples/01/cumulative_distribution.png")

# Print summary statistics
print("\n=== Summary Statistics (EUR/hour) ===")
print(f"\nMales:")
print(f"  10th percentile (D1): €{males_earnings[0]:.2f}")
print(f"  Median (D5):          €{males_earnings[4]:.2f}")
print(f"  90th percentile (D9): €{males_earnings[8]:.2f}")
print(f"\nFemales:")
print(f"  10th percentile (D1): €{females_earnings[0]:.2f}")
print(f"  Median (D5):          €{females_earnings[4]:.2f}")
print(f"  90th percentile (D9): €{females_earnings[8]:.2f}")

# Calculate gender pay gap
gaps = [(m - f) / m * 100 for m, f in zip(males_earnings, females_earnings)]
print(f"\n=== Gender Pay Gap by Decile ===")
for i, (pct, gap, m, f) in enumerate(zip(percentiles, gaps, males_earnings, females_earnings)):
    print(f"  D{i+1} ({int(pct)}th percentile): {gap:.1f}% (M: €{m:.2f}, F: €{f:.2f})")
