# QC-TLF Python Verification

## Project Overview
This project generates deterministic, reproducible QC Tables, Listings, and Figures (TLFs) from CDISC SDTM and ADaM datasets for independent verification against SAS-generated TLFs. It is designed for cell-by-cell comparison in clinical trial programming QC, not for regulatory submission.

## Key Features
- Input: SDTM and ADaM datasets (CSV/XPT)
- Output: QC TLFs (CSV, Excel, PNG)
- Strict SAP/SAS logic adherence
- Tools: pandas, numpy, matplotlib
- Deterministic, reproducible results
- Explicit documentation of dataset/variable names, population flags, analysis parameters, grouping, ordering
- Handles missing values, sorting, rounding, decimal precision

## Project Structure
1. Load Data
2. Apply Population Filters
3. Apply Derivation Logic
4. Generate TLFs
5. Export Output
6. Generate Listings

## Sample Outputs
- `qc_outputs/table1_age_by_treatment.csv`: Summary statistics for AGE by treatment arm
- `qc_outputs/listing1_subject_safety.csv`: Subject-level listing for Safety population
- `qc_outputs/figure1_age_histogram.png`: Histogram of AGE by treatment arm

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/justin-mbca/QC-TLF-Python-Verification.git
   ```
2. Install Python dependencies:
   ```bash
   pip install pandas numpy matplotlib
   ```
3. Place your SDTM and ADaM datasets in the appropriate folders (`sdtm/`, `adam/`).
4. Run the main script:
   ```bash
   python TLF.py
   ```

## Usage
- Modify the scripts as needed to match your SAP and SAS logic.
- Outputs will be generated in the `qc_outputs/` folder.
- Compare outputs with SAS-generated TLFs for QC.

## Calling SAS from Python
- Use Python’s `subprocess` module for local SAS execution.
- Use `saspy` for remote SAS server or SAS Viya integration.
- See `run_sas_from_python.py` for examples.

## Marp Slides
- Project slides are available in markdown files and exported PPTX.
- See `QC_TLF_Project_Marp_Slides_Detailed.md` and `QC_TLF_Project_Marp_Slides_Detailed.pptx`.

## Contact
For questions or contributions, please open an issue or contact the repository owner.
