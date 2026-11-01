"""Recompute the monograph's reported statistics from the numbers it prints beside them.

The inputs are copied from Tables 1, 4 and 5 of the full manuscript as submitted (the 101-page PDF dated
2026-10-31). Each block prints what the table's own numbers give next to what the table reports.
Needs numpy and scipy. Output as of 2026-11-01: checks/check_tables.out.txt
"""
import math
import numpy as np
from scipy import stats

print("Table 5: Arm 1 (consistency null step) vs Arm 2 (mean of 30 random null steps), 5 seeds")
arm1 = np.array([78.00, 81.00, 75.00, 79.00, 77.00])
rand = np.array([63.87, 65.73, 61.40, 64.90, 62.80])
d = arm1 - rand
sd = d.std(ddof=1)
se = sd / math.sqrt(5)
t = d.mean() / se
print(f"  from the table: d = {np.round(d, 2)}, mean {d.mean():.4f}, s_d {sd:.4f}, SE {se:.4f}, t(4) {t:.2f}, "
      f"two-sided p {2 * stats.t.sf(t, 4):.3g}")
print(f"  as reported:    mean 14.2600, s_d 0.7021, SE 0.3140, t(4) 45.4140, p 7.108e-06")
print(f"  p for the reported t(4) = 45.414: two-sided {2 * stats.t.sf(45.414, 4):.4g}, one-sided {stats.t.sf(45.414, 4):.4g}")

print("\nTable 5: lawful-recall non-inferiority (margin -2.0 pp), as reported: d -0.20, 95% CI [-0.8841, +0.4841], "
      "t_NI 7.3485, p 8.891e-04")
half = 0.6841
se_ci = half / stats.t.ppf(0.975, 4)
print(f"  SE implied by the CI: {se_ci:.5f}  ->  t_NI {(-0.20 + 2.0) / se_ci:.4f}")
se_t = 1.8 / 7.3485
print(f"  SE implied by t_NI:   {se_t:.5f}  ->  CI half-width {se_t * stats.t.ppf(0.975, 4):.4f}")
print(f"  p for t_NI = 7.3485, one-sided: {stats.t.sf(7.3485, 4):.4g}")

print("\nTable 1: advantage I_R as mean +/- sd over N = 15 paired runs (a paired t-test has df = 14)")
for name, m, s, p_rep in [("physics", 21.80, 1.54, 1.12e-16), ("ARC", 23.53, 0.67, 2.14e-22), ("STRIPS", 23.91, 0.54, 7.82e-24)]:
    tt = m / (s / math.sqrt(15))
    print(f"  {name:8s} t(14) = {tt:7.1f}, two-sided p = {2 * stats.t.sf(tt, 14):.3g}   (reported p = {p_rep:.3g})")

print("\nTable 4: regression t-statistics with df = 92")
for name, tt, p_rep in [("S_param", 1.08, 0.2829), ("I_HSIC", 1.39, 0.1679), ("lambda_2", 0.57, 0.5699), ("Rank_ctrl", 0.84, 0.4031),
                         ("H_graph", -1.71, 0.0906), ("D_eff", -1.12, 0.2657), ("INCD", -5.59, 2.18e-07)]:
    print(f"  {name:9s} t = {tt:5.2f}: two-sided p = {2 * stats.t.sf(abs(tt), 92):.4g}   (reported {p_rep:.4g})")
r2 = 0.7410
f = (r2 / 7) / ((1 - r2) / 92)
print(f"  F from R^2 = 0.741: {f:.2f} (reported 37.60), p = {stats.f.sf(37.60, 7, 92):.3g} (reported 1.34e-23)")
