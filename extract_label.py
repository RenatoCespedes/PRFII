import csv
import os
import sys
import numpy as np
from file_util import *
from routes import *

os.system('rm ' + out_file_Label)
list_category = ['ang','hap','sad','neu','fru',
                'exc','fea','sur','dis','oth','xxx']


category = {}
for c_type in list_category:
    # print(c_type)
    if c_type in category:
    # if category.has_key(c_type):
        print("next")
    else:
        category[c_type] = len(category)

# print(category)



def find_category(lines):
    is_target = True
    
    id = ''
    c_label = ''
    list_ret = []
    
    for line in lines:
        if is_target == True:
            
            try:
                id       = line.split('\t')[1].strip()  #  extract ID
                # print(id)
                c_label  = line.split('\t')[2].strip()  #  extract category
                # print(c_label)
                # print( "wss",not category.has_key(c_label))
                if c_label not in category:
                    
                    print("ERROR nokey" + c_label)
                    sys.exit()
                
                list_ret.append( [id, c_label] )
                # print(list_ret,'\n')
                is_target = False

            except:
                print("ERROR " + line)
                sys.exit()
        
        else:
            if line == '\n':
                is_target = True
        
    return list_ret



def extract_labels( list_in_file, out_file ) :
    id = ''
    lines = []
    list_ret = []
    
    for in_file in list_in_file:
        # print("extracting labels from " + in_file)
        with open(in_file, 'r') as f:
            lines = f.readlines()
            lines = lines[2:]                           # remove head
            list_ret = find_category(lines)
        list_ret = sorted(list_ret)                   # sort based on first element
    
        with open(out_file, 'a') as f:
            csv_writer = csv.writer( f )
            csv_writer.writerows( list_ret )                   









list_files = []
list_avoid_dir = ['Attribute', 'Categorical', 'Self-evaluation']

for x in range(5):
    sess_name = 'Session' + str(x+1)

    path = '../IEMOCAP_full_release/' + sess_name + '/dialog/EmoEvaluation/'
    # print("search")
    file_search(path, list_files, list_avoid_dir)
    # print("search done")
    list_files = sorted(list_files)
    

    print(sess_name + ", #sum files: " + str(len(list_files)))
    # print(list_files,'\n')


extract_labels(list_files, out_file_Label)