# QC TLF Generation Template
# Author: Senior Clinical Statistical Programmer
# Purpose: Deterministic, reproducible QC Tables, Listings, and Figures (TLFs)
#          from CDISC SDTM and ADaM datasets for independent verification against SAS-generated TLFs

# Requirements:
# - Input: SDTM/ADaM XPT or CSV files
# - Output: QC TLFs (CSV/Excel/PNG)
# - Logic strictly follows SAP and SAS TLFs
# - Uses pandas, numpy, matplotlib (no seaborn)
# - No randomization; deterministic results
# - Explicit documentation of dataset/variable names, population flags, analysis parameters, grouping, ordering
# - Matches SAS: missing value handling, sorting, rounding, decimal precision
# - Structured: Load data, Apply population filters, Derivation logic, Generate TLF, Export output
# - Numeric outputs suitable for cell-by-cell comparison

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# -----------------------------
# Section 1: Load Data
# -----------------------------
ADSL_PATH = 'adam/adsl.csv'  # ADaM Subject-Level dataset (CSV for testing)
DM_PATH = 'sdtm/dm.csv'      # SDTM Demographics dataset (CSV for testing)

def load_adam_adsl(path):
    if path.lower().endswith('.xpt'):
        return pd.read_sas(path, format='xport', encoding='utf-8')
    else:
        return pd.read_csv(path, encoding='utf-8')

def load_sdtm_dm(path):
    if path.lower().endswith('.xpt'):
        return pd.read_sas(path, format='xport', encoding='utf-8')
    else:
        return pd.read_csv(path, encoding='utf-8')

adsl = load_adam_adsl(ADSL_PATH)
dm = load_sdtm_dm(DM_PATH)

# -----------------------------
# Section 2: Apply Population Filters
# -----------------------------
safety_pop = adsl[adsl['SAFFL'] == 'Y'].copy()

# -----------------------------
# Section 3: Apply Derivation Logic
# -----------------------------
def derive_age_category(df, age_var='AGE'):
    return np.where(df[age_var] < 65, '<65', '>=65')

safety_pop['AGECAT'] = derive_age_category(safety_pop)
group_var = 'TRT01A'

# -----------------------------
# Section 4: Generate TLF
# -----------------------------
def summarize_age_by_treatment(df, group_var, age_var='AGE'):
    summary = df.groupby(group_var)[age_var].agg([
        ('N', lambda x: x.notna().sum()),
        ('Mean', lambda x: round(np.mean(x.dropna()), 1)),
        ('SD', lambda x: round(np.std(x.dropna(), ddof=1), 2)),
        ('Min', lambda x: round(np.min(x.dropna()), 1)),
        ('Max', lambda x: round(np.max(x.dropna()), 1)),
    ])
    summary = summary.reset_index()
    return summary

age_summary = summarize_age_by_treatment(safety_pop, group_var)

# -----------------------------
# Section 5: Export Output
# -----------------------------
OUTPUT_DIR = 'qc_outputs'
os.makedirs(OUTPUT_DIR, exist_ok=True)
age_summary.to_csv(os.path.join(OUTPUT_DIR, 'table1_age_by_treatment.csv'), index=False, float_format='%.1f')

def plot_age_histogram(df, group_var, age_var='AGE', output_path=None):
    groups = df[group_var].unique()
    plt.figure(figsize=(8, 6))
    for grp in sorted(groups):
        grp_data = df[df[group_var] == grp][age_var].dropna()
        plt.hist(grp_data, bins=10, alpha=0.6, label=str(grp), edgecolor='black')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Histogram of Age by Treatment Arm')
    plt.legend()
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=300)
    plt.close()

plot_age_histogram(safety_pop, group_var, output_path=os.path.join(OUTPUT_DIR, 'figure1_age_histogram.png'))

# -----------------------------
# Section 6: Generate Listing
# -----------------------------
listing_vars = ['USUBJID', 'AGE', 'SEX', 'RACE', 'TRT01A', 'SAFFL', 'ITTFL', 'PPSFL']
listing_df = pd.merge(safety_pop, dm, on='USUBJID', how='left')
listing_df = listing_df[listing_vars]
listing_df = listing_df.sort_values(by='USUBJID')
listing_df.to_csv(os.path.join(OUTPUT_DIR, 'listing1_subject_safety.csv'), index=False)