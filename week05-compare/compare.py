"""Week 5: compare valid reaction times in conditions A and B.

Run from the week05-compare folder: python compare.py
Requires matplotlib: python -m pip install matplotlib
"""
import csv
from pathlib import Path
from statistics import mean

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
CSV_FILE = HERE / 'week05-results.csv'
values = {'A': [], 'B': []}

with CSV_FILE.open(newline='', encoding='utf-8-sig') as file:
    for row in csv.DictReader(file):
        condition = row['condition'].strip().upper()
        if condition not in values:
            continue
        try:
            rt = float(row['rt'])
            correct = int(float(row['correct'])) == 1
            practice = int(float(row['practice'])) == 1
            anticipation = int(float(row['anticipation'])) == 1
        except (ValueError, TypeError) as exc:
            raise ValueError(f'Invalid CSV row: {row}') from exc
        if not practice and correct and not anticipation and 150 <= rt <= 2500:
            values[condition].append(rt)

a, b = values['A'], values['B']
if not a or not b:
    raise SystemExit('Need at least one valid trial in both conditions.')

mean_a, mean_b = mean(a), mean(b)
difference = mean_b - mean_a

# Observed-range overlap: percent of B trials whose RT lies between
# the minimum and maximum observed valid A reaction times (inclusive).
# This is one explicit overlap measure; use a different one if your
# instructor specifies a particular definition.
overlap_count = sum(min(a) <= rt <= max(a) for rt in b)
overlap_pct = 100 * overlap_count / len(b)

print(f'Condition A: n={len(a)}, mean={mean_a:.2f} ms')
print(f'Condition B: n={len(b)}, mean={mean_b:.2f} ms')
print(f'Difference (B - A): {difference:+.2f} ms')
print(f'Overlap (B trials within A observed range): {overlap_pct:.1f}% '
      f'({overlap_count}/{len(b)})')
print(f'A observed range: {min(a):.0f}–{max(a):.0f} ms')

fig, ax = plt.subplots(figsize=(8, 5))
ax.boxplot([a, b], tick_labels=['A: Simple RT', 'B: Choice RT'],
           showmeans=True, meanline=True)
ax.set_ylabel('Reaction time (ms)')
ax.set_title('Week 5: Reaction-time comparison')
ax.grid(axis='y', alpha=0.25)
fig.text(0.5, 0.01,
         f'Means: A {mean_a:.1f} ms | B {mean_b:.1f} ms | B−A {difference:+.1f} ms',
         ha='center', fontsize=9)
fig.tight_layout(rect=[0, 0.04, 1, 1])
output = HERE / 'compare.png'
fig.savefig(output, dpi=180)
plt.close(fig)
print(f'Saved: {output.name}')
