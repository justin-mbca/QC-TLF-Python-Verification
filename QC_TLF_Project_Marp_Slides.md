---
marp: true
---

# QC TLF Python Project

---

## Project Overview
- Deterministic, reproducible QC Tables, Listings, and Figures (TLFs)
- CDISC SDTM and ADaM datasets
- Independent verification against SAS-generated TLFs

---

## Key Requirements
- Input: SDTM/ADaM CSV/XPT
- Output: QC TLFs (CSV, Excel, PNG)
- Strict SAP/SAS logic
- pandas, numpy, matplotlib
- No randomization
- Explicit documentation
- SAS-matching: missing values, sorting, rounding, precision

---

## Workflow Steps
1. Load Data
2. Apply Population Filters
3. Apply Derivation Logic
4. Generate TLFs
5. Export Output
6. Generate Listings

---

## Sample Python Code
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# ...existing code...
```

---

## Sample Outputs
- table1_age_by_treatment.csv
- listing1_subject_safety.csv
- figure1_age_histogram.png

---

## ChatGPT Enterprise for QC
- Used for code generation, review, and validation
- Cell-by-cell comparison with SAS TLFs
- Rapid prototyping and documentation
- Ensured SAP/SAS alignment

---

## Marp Usage
- Add `marp: true` in front-matter
- Write slides in Markdown
- Preview and export to PPTX/PDF in VS Code

---

## Thank You!
Questions?
