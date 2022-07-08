import os
import sys
import csv
from file_util import *
from routes import *


def extract_feature( list_in_file, out_file ) :
    print(out_file)
    
    cnt = 0    
    for in_file in list_in_file:        
        cmd = 'SMILExtract -C ' + OPENSMILE_CONFIG_PATH_P + ' -I ' + in_file + ' -csvoutput ' + out_file + ' -headercsv 0'  
        os.system(cmd)
        
        cnt += 1
        if cnt % 1000 == 0:
            print(str(cnt) + " / " + str( len(list_in_file)))
            sys.stdout.flush()


list_files = []

for x in range(5):
    sess_name = 'Session' + str(x+1)
    path = '../IEMOCAP_full_release/' + sess_name + '/sentences/wav/'
    file_search(path, list_files)
    list_files = sorted(list_files)

    print(sess_name + ", #sum files: " + str(len(list_files)))

extract_feature( list_files, out_file_P )