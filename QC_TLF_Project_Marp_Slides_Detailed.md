---
marp: true
---

# QC TLF Python Project

---

## Project Overview
- Goal: Generate deterministic, reproducible QC Tables, Listings, and Figures (TLFs) from CDISC SDTM and ADaM datasets for independent verification against SAS-generated TLFs.
- Context: Used for cell-by-cell comparison in clinical trial programming QC, not for regulatory submission.

---

## Key Requirements
- Input: SDTM and ADaM datasets (CSV/XPT)
- Output: QC TLFs (CSV, Excel, PNG)
- Logic: Strictly follows Statistical Analysis Plan (SAP) and SAS TLFs
- Tools: pandas, numpy, matplotlib (no seaborn)
- Determinism: No randomization; reproducible results
- Documentation: Explicit dataset/variable names, population flags, analysis parameters, grouping, ordering
- SAS Matching: Handles missing values, sorting, rounding, decimal precision

---

## Project Structure
1. Load Data
2. Apply Population Filters
3. Apply Derivation Logic
4. Generate TLFs
5. Export Output
6. Generate Listings

---

## Sample Code (Python)
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# ...existing code...
```
- Modular, well-documented, and SAP/SAS-aligned

---

## Sample Outputs
- table1_age_by_treatment.csv: Summary statistics for AGE by treatment arm
- listing1_subject_safety.csv: Subject-level listing for Safety population
- figure1_age_histogram.png: Histogram of AGE by treatment arm

---

## Testing & Validation
- Created sample CSV files for ADaM and SDTM
- Ran script to generate QC outputs
- Verified outputs for cell-by-cell comparison with SAS

---

## Prompt Used for Code Generation & ChatGPT Enterprise
- Prompt Example:
  > Generate deterministic, reproducible Python code to create QC Tables, Listings, and Figures (TLFs) from CDISC SDTM and ADaM datasets for independent verification against SAS-generated TLFs. Follow SAP and SAS logic, use pandas/numpy/matplotlib, document dataset/variable names, population flags, analysis parameters, grouping, ordering, and match SAS behavior for missing values, sorting, rounding, and decimal precision. Structure code into clear sections: Load data, Apply population filters, Apply derivation logic, Generate TLF, Export output. Output numeric values for cell-by-cell comparison.
- ChatGPT Enterprise Use:
  - Used ChatGPT Enterprise to generate, review, and validate Python code for QC TLFs.
  - Compared Python-generated outputs against SAS TLFs for cell-by-cell QC.
  - Leveraged AI for rapid prototyping, documentation, and deterministic logic.
  - Ensured strict adherence to SAP and SAS requirements.

---

## How ChatGPT Enterprise Supports Validation
- Code Review: Reviews Python and SAS code for logic, structure, and SAP/SAS alignment.
- Logic Comparison: Compares Python and SAS TLF generation logic for equivalence.
- Output Validation: Assists in cell-by-cell comparison of Python and SAS outputs (CSV, Excel, PNG).
- Documentation & Transparency: Generates clear documentation for QC workflow, code, and validation steps.
- Rapid Prototyping: Quickly generates and tests new QC logic or TLFs for SAP changes.

---

## Interview Talking Points
- Demonstrated end-to-end QC TLF workflow in Python
- Matched SAS logic for clinical trial QC
- Automated, reproducible, and transparent process
- Used ChatGPT Enterprise for code generation and QC
- Ready for extension to additional TLFs or listings

---

## Next Steps
- Add more TLFs/listings per SAP
- Integrate Excel export or PowerPoint automation if needed
- Adapt for other clinical trial datasets

---

## Marp Usage
- Add `marp: true` in front-matter
- Write slides in Markdown
- Preview and export to PPTX/PDF in VS Code

---

## Thank You!
Questions?
