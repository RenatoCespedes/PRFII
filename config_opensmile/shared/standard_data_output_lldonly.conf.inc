///////////////////////////////////////////////////////////////////////////////////////
///////// > openSMILE configuration file for data output <           //////////////////
/////////                                                            //////////////////
///////// (c) 2014-2016 audEERING,                                   //////////////////
/////////     All rights reserverd. See file COPYING for details     //////////////////
///////////////////////////////////////////////////////////////////////////////////////


/*
   This file can be included as data output file for standard feature
   extraction configuration files. It provides commandline options
   for the batch extraction GUI, and supports LLD and Functionals (summaries)
   saving.
   It requires the main extrator configuration file to provide the following
   data memory levels:  lld  (including, if available lld_de)
 */

;;;;;;;;; output LLD features to CSV ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

[componentInstances:cComponentManager]
instance[lldcsvsink].type=cCsvSink
;instance[lldhtksink].type=cHtkSink
;instance[lldarffsink].type=cArffSink

[lldcsvsink:cCsvSink]
reader.dmLevel = lld
filename=\cm[csvoutput{MFCC12EDA.csv}:output csv file for LLD, disabled by default ?, only written if filename given]
instanceName=\cm[instname(N){unknown}:instance name]
append = \cm[appendcsv{1}:set to 1 to append to the LLD output csv file, default is not to append]
timestamp = \cm[timestampcsv{1}:set to 0 to suppress timestamp column, default is 1, i.e. to show timestamp in second column] 
number = 0
printHeader = \cm[headercsv{0}:set to 0 to suppress header line with feature names, default is 1, i.e. to show header line]
errorOnNoOutput = 1