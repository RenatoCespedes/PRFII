import csv
import os
import sys
import numpy as np
from file_util import *


lines = []
with open('../extra_feature/pre_procesado/prosodic.csv') as f:
    csv_reader = csv.reader(f)
    lines = [x for x in csv_reader]


# lines=[xline.replace(';',',') for xline in lines]
# lines=lines[0].replace(';',',') 
for line in lines:
    print(line)
    break


np_prosody = np.zeros( [10039, 35], dtype=float)
print(np.shape(np_prosody))


for i in range( len(np_prosody) ):
    np_prosody[i] = lines[i]


np.save('../extra_feature/pre_procesado/processed_prosody.npy', np_prosody)