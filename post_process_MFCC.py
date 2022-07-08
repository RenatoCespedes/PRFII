import csv
# import _pickle as cPickle
import numpy as np


lines = []
with open('../extra_feature/pre_procesado/MFCC12EDA.csv') as f:
    csv_reader = csv.reader(f)
    lines = [x for x in csv_reader]

print(len(lines))

print('conversion line ')
list_lines=[]
for x in lines:
    list_lines.append(x[0])

print('conversion line split')

list_new=[]
for p in list_lines:
    list_new.append(p.split(';'))
# lines = [x[0] for x in lines]

# lines = [x.split(';') for x in lines]
print('conversion line float')

list_new_float=[]
for x in list_new_float:
    for i in x[1:]:
        list_new_float.append(float(i))

# float_lines = [ [float(i) for i in x[1:]] for x in lines ]


chunk_index = []
for i, line in enumerate(list_new_float):
    if line[0] == 0:
        chunk_index.append(i)

no_index_float_linex = []#  remove first two columns
for x in list_new:
    no_index_float_linex.append(x[2:])

list_MFCC = []

for i in xrange( len(chunk_index) ):
    
    if i == len(chunk_index) -1:        # last case
        list_MFCC.append( no_index_float_linex[ chunk_index[i]: ] )
    else :
        list_MFCC.append( no_index_float_linex[ chunk_index[i]:chunk_index[i+1] ] )



stat = [ ]
for x in list_MFCC:
    stat.append( len(x) )
    
print(np.mean(stat))
print(np.std(stat))
print(np.max(stat))
print(np.min(stat))


np.save('../extra_feature/pre_procesado/processed_MFCC12EDA_sequenceN.npy', np.asarray(stat))


with open('../extra_feature/pre_procesado/processed_MFCC12EDA_sequenceN.txt', 'w') as f:
    for data in stat:
        f.write( str(data) + '\n' )

np_MFCC = np.zeros( [10039, 750, 39], dtype=np.float)
np.shape(np_MFCC)


for i in xrange( len(list_MFCC) ):
    
    if len( list_MFCC[i] ) > 750:
        np_MFCC[i][:] = list_MFCC[i][:750]
    else:
        np_MFCC[i][:len(list_MFCC[i])] = list_MFCC[i][:]

np.save('../extra_feature/pre_procesado/processed_MFCC12EDA.npy', np_MFCC)