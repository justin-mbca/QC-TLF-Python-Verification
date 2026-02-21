/* Table 1: Demographics by Treatment Arm (SAS) */
libname adam './adam';

proc means data=adam.adsl n mean std min max;
  class TRT01A;
  var AGE;
  where SAFFL = 'Y';
run;

proc export data=adam.adsl outfile='../qc_outputs/table1_age_by_treatment_sas.csv' dbms=csv replace;
  where SAFFL = 'Y';
run;
