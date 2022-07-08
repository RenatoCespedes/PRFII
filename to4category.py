from routes import *
import csv
from file_util import *
import numpy as np

#IDS

tmp_ids = []
with open('../extra_feature/pre_procesado/labels.csv') as f:
    csv_reader = csv.reader(f)
    tmp_ids = [x for x in csv_reader]
    # print(tmp_ids)
    tmp_ids = [x[0] for x in tmp_ids if x!=[]]


with open('../extra_feature/pre_procesado/ordered_ids.txt', 'w') as f:
    for _id in tmp_ids:
        f.write(_id+'\n')

data = []
with open('../extra_feature/pre_procesado/ordered_ids.txt') as f:
    data = f.readlines()




create_folder('../extra_feature/pre_procesado/'+target_path)

with open('../extra_feature/pre_procesado/' + target_path + '/FC_ordered_ids.txt', 'w') as f:
    for i, label in enumerate(full_label):
        if label != '-1':
            f.write( data[i] )


#Etiquetas


data = []
with open('../extra_feature/pre_procesado/processed_label.txt') as f:
    data = f.readlines()


with open('../extra_feature/pre_procesado/' + target_path + '/FC_label.txt', 'w') as f:
    for i, label in enumerate(full_label):
        if label != '-1':            
            f.write( data[i] )

#Sequence MFCC

data = []

with open('../extra_feature/pre_procesado/processed_MFCC12EDA_sequenceN.txt') as f:
    data = f.readlines()

with open('../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA_sequenceN.txt', 'w') as f:
    for i, label in enumerate(full_label):
        if label != '-1':
            f.write( data[i] )

#Prosodic 


data = np.load('../extra_feature/pre_procesado/processed_prosody.npy')
np.shape(data)

total_num = 5531
new_data = np.zeros([5531, 35], dtype=np.float)


index = 0
for i, label in enumerate(full_label):
    if label != '-1':
        new_data[index] = data[i]
        index += 1

np.save('../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy', new_data)

#MFCC



data = np.load('../extra_feature/pre_procesado/processed_MFCC12EDA.npy')
np.shape(data)

total_num = 5531
new_data = np.zeros([5531, 750, 39], dtype=np.float)

index = 0
for i, label in enumerate(full_label):
    if label != '-1':
        new_data[index] = data[i]
        index += 1

np.save('../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy', new_data)

#