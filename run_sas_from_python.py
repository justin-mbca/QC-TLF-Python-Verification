import subprocess
import os

# Path to SAS executable (update if needed)
SAS_EXEC = 'sas'  # or full path, e.g., '/usr/local/bin/sas'

# Run Table 1 Demographics SAS script
table1_script = os.path.join('sas', 'Table1_Demographics.sas')
subprocess.run([SAS_EXEC, table1_script], check=True)

# Run Listing 1 Subject Safety SAS script
listing1_script = os.path.join('sas', 'Listing1_Subject_Safety.sas')
subprocess.run([SAS_EXEC, listing1_script], check=True)

print('SAS scripts executed. Check qc_outputs for SAS-generated CSVs.')