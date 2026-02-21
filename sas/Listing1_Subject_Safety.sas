/* Listing 1: Subject-level listing for Safety population (SAS) */
libname adam './adam';

proc print data=adam.adsl;
  where SAFFL = 'Y';
  var USUBJID AGE SEX RACE TRT01A SAFFL ITTFL PPSFL;
run;

proc export data=adam.adsl outfile='../qc_outputs/listing1_subject_safety_sas.csv' dbms=csv replace;
  where SAFFL = 'Y';
run;
