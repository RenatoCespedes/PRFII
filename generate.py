from routes import *
import random
from file_util import *
import numpy as np

#Generate IDS


lines = []
with open('../extra_feature/pre_procesado/' + target_path + '/FC_label.txt') as f :
    lines = f.readlines()

print(len(lines))


random.seed(337)
test_fold01 = []
test_fold02 = []
test_fold03 = []
test_fold04 = []
test_fold05 = []

for x in range( len(lines) ) :
    
    compare = random.random()
    
    if compare > 0.8 : 
        test_fold01.append( str(x) )
    elif compare > 0.6 : 
        test_fold02.append( str(x) )
    elif compare > 0.4 : 
        test_fold03.append( str(x) )
    elif compare > 0.2 : 
        test_fold04.append( str(x) )        
    else:
        test_fold05.append( str(x) )

def generar_data( list_all, list_test, path ) :

    random.seed(3372)
    
    train = []
    dev = []
    test = []

    for index in range( len(list_all) ) :

        compare = random.random()

        if str(index) not in list_test:
            train.append( str(index) )
        else:
            if compare > 0.70 : 
                dev.append( str(index) )
            else:
                test.append( str(index) )

    with open(path, 'w') as f :
        f.write( ' '.join(train) + '\n')
        f.write( ' '.join(dev) + '\n')
        f.write( ' '.join(test) + '\n')

    print(len(train))
    print(len(dev))
    print(len(test))

#Creacion de 5 Folders

create_folder('../extra_feature/pre_procesado/'+target_path+'/audio_set01')
create_folder('../extra_feature/pre_procesado/'+target_path+'/audio_set02')
create_folder('../extra_feature/pre_procesado/'+target_path+'/audio_set03')
create_folder('../extra_feature/pre_procesado/'+target_path+'/audio_set04')
create_folder('../extra_feature/pre_procesado/'+target_path+'/audio_set05')

#generacion de entrenamiento de los IDs

generar_data(lines,test_fold01,path_set01)
generar_data(lines,test_fold02,path_set02)
generar_data(lines,test_fold03,path_set03)
generar_data(lines,test_fold04,path_set04)
generar_data(lines,test_fold05,path_set05)


#SET01





target_sequence = '../extra_feature/pre_procesado/' + target_path + '/' + target_name_1 + '/' + target_name_1 + '.txt'
target_path_name = '../extra_feature/pre_procesado/' + target_path + '/' + target_name_1 + '/'

train_ids = [] 
dev_ids = [] 
test_ids = [] 
with open( target_sequence ) as f:
    lines = f.readlines()
    train_ids = [ int(x) for x in lines[0].strip().split(' ')]
    dev_ids =  [ int(x) for x in lines[1].strip().split(' ')]
    test_ids = [ int(x) for x in lines[2].strip().split(' ')]

print(len(train_ids))
print(len(dev_ids))
print(len(test_ids))


#MFCC

train_audio_mfcc = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), train_ids  )
dev_audio_mfcc  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), dev_ids  )
test_audio_mfcc  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), test_ids  )

np.save( target_path_name + 'train_audio_mfcc.npy', train_audio_mfcc)
np.save( target_path_name + 'dev_audio_mfcc.npy', dev_audio_mfcc)
np.save( target_path_name + 'test_audio_mfcc.npy', test_audio_mfcc)


#Prosodic

train_audio_prosody = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), train_ids  )
dev_audio_prosody  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), dev_ids  )
test_audio_prosody  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), test_ids  )

np.save( target_path_name + 'train_audio_prosody.npy', train_audio_prosody)
np.save( target_path_name + 'dev_audio_prosody.npy', dev_audio_prosody)
np.save( target_path_name + 'test_audio_prosody.npy', test_audio_prosody)

#Sequencia N
seqN_npy = []
with open('../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA_sequenceN.txt') as f :
    seqN = [ int(x.strip()) for x in f.readlines() ]
    seqN_npy = np.asarray(seqN)
    
train_seqN = extract_data_with_ids( seqN_npy, train_ids  )
dev_seqN  = extract_data_with_ids( seqN_npy, dev_ids  )
test_seqN = extract_data_with_ids( seqN_npy, test_ids  )

np.save( target_path_name + 'train_seqN.npy', train_seqN)
np.save( target_path_name + 'dev_seqN.npy', dev_seqN)
np.save( target_path_name + 'test_seqN.npy', test_seqN)


# label
label_npy = []
with open('../extra_feature/pre_procesado/' + target_path + '/FC_label.txt') as f :
    label = [ int(x.strip()) for x in f.readlines() ]
    label_npy = np.asarray(label)

train_label = extract_data_with_ids( label_npy, train_ids  )
dev_label  = extract_data_with_ids( label_npy, dev_ids  )
test_label = extract_data_with_ids( label_npy, test_ids  )

np.save( target_path_name + 'train_label.npy', train_label)
np.save( target_path_name + 'dev_label.npy', dev_label)
np.save( target_path_name + 'test_label.npy', test_label)




#SET 02
target_sequence = '../extra_feature/pre_procesado/' + target_path + '/' + target_name_2 + '/' + target_name_2 + '.txt'
target_path_name = '../extra_feature/pre_procesado/' + target_path + '/' + target_name_2 + '/'

train_ids = [] 
dev_ids = [] 
test_ids = [] 
with open( target_sequence ) as f:
    lines = f.readlines()
    train_ids = [ int(x) for x in lines[0].strip().split(' ')]
    dev_ids =  [ int(x) for x in lines[1].strip().split(' ')]
    test_ids = [ int(x) for x in lines[2].strip().split(' ')]

print(len(train_ids))
print(len(dev_ids))
print(len(test_ids))


# MFCC
train_audio_mfcc = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), train_ids  )
dev_audio_mfcc  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), dev_ids  )
test_audio_mfcc  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), test_ids  )

np.save( target_path_name + 'train_audio_mfcc.npy', train_audio_mfcc)
np.save( target_path_name + 'dev_audio_mfcc.npy', dev_audio_mfcc)
np.save( target_path_name + 'test_audio_mfcc.npy', test_audio_mfcc)


# prosody
train_audio_prosody = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), train_ids  )
dev_audio_prosody  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), dev_ids  )
test_audio_prosody  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), test_ids  )

np.save( target_path_name + 'train_audio_prosody.npy', train_audio_prosody)
np.save( target_path_name + 'dev_audio_prosody.npy', dev_audio_prosody)
np.save( target_path_name + 'test_audio_prosody.npy', test_audio_prosody)





# sequenceN
seqN_npy = []
with open('../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA_sequenceN.txt') as f :
    seqN = [ int(x.strip()) for x in f.readlines() ]
    seqN_npy = np.asarray(seqN)
    
train_seqN = extract_data_with_ids( seqN_npy, train_ids  )
dev_seqN  = extract_data_with_ids( seqN_npy, dev_ids  )
test_seqN = extract_data_with_ids( seqN_npy, test_ids  )

np.save( target_path_name + 'train_seqN.npy', train_seqN)
np.save( target_path_name + 'dev_seqN.npy', dev_seqN)
np.save( target_path_name + 'test_seqN.npy', test_seqN)


# label
label_npy = []
with open('../extra_feature/pre_procesado/' + target_path + '/FC_label.txt') as f :
    label = [ int(x.strip()) for x in f.readlines() ]
    label_npy = np.asarray(label)

train_label = extract_data_with_ids( label_npy, train_ids  )
dev_label  = extract_data_with_ids( label_npy, dev_ids  )
test_label = extract_data_with_ids( label_npy, test_ids  )

np.save( target_path_name + 'train_label.npy', train_label)
np.save( target_path_name + 'dev_label.npy', dev_label)
np.save( target_path_name + 'test_label.npy', test_label)




#SET 03

target_sequence = '../extra_feature/pre_procesado/' + target_path + '/' + target_name_3 + '/' + target_name_3 + '.txt'
target_path_name = '../extra_feature/pre_procesado/' + target_path + '/' + target_name_3 + '/'

train_ids = [] 
dev_ids = [] 
test_ids = [] 
with open( target_sequence ) as f:
    lines = f.readlines()
    train_ids = [ int(x) for x in lines[0].strip().split(' ')]
    dev_ids =  [ int(x) for x in lines[1].strip().split(' ')]
    test_ids = [ int(x) for x in lines[2].strip().split(' ')]

print(len(train_ids))
print(len(dev_ids))
print(len(test_ids))


# MFCC
train_audio_mfcc = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), train_ids  )
dev_audio_mfcc  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), dev_ids  )
test_audio_mfcc  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), test_ids  )

np.save( target_path_name + 'train_audio_mfcc.npy', train_audio_mfcc)
np.save( target_path_name + 'dev_audio_mfcc.npy', dev_audio_mfcc)
np.save( target_path_name + 'test_audio_mfcc.npy', test_audio_mfcc)


# prosody
train_audio_prosody = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), train_ids  )
dev_audio_prosody  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), dev_ids  )
test_audio_prosody  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), test_ids  )

np.save( target_path_name + 'train_audio_prosody.npy', train_audio_prosody)
np.save( target_path_name + 'dev_audio_prosody.npy', dev_audio_prosody)
np.save( target_path_name + 'test_audio_prosody.npy', test_audio_prosody)




# sequenceN
seqN_npy = []
with open('../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA_sequenceN.txt') as f :
    seqN = [ int(x.strip()) for x in f.readlines() ]
    seqN_npy = np.asarray(seqN)
    
train_seqN = extract_data_with_ids( seqN_npy, train_ids  )
dev_seqN  = extract_data_with_ids( seqN_npy, dev_ids  )
test_seqN = extract_data_with_ids( seqN_npy, test_ids  )

np.save( target_path_name + 'train_seqN.npy', train_seqN)
np.save( target_path_name + 'dev_seqN.npy', dev_seqN)
np.save( target_path_name + 'test_seqN.npy', test_seqN)


# label
label_npy = []
with open('../extra_feature/pre_procesado/' + target_path + '/FC_label.txt') as f :
    label = [ int(x.strip()) for x in f.readlines() ]
    label_npy = np.asarray(label)

train_label = extract_data_with_ids( label_npy, train_ids  )
dev_label  = extract_data_with_ids( label_npy, dev_ids  )
test_label = extract_data_with_ids( label_npy, test_ids  )

np.save( target_path_name + 'train_label.npy', train_label)
np.save( target_path_name + 'dev_label.npy', dev_label)
np.save( target_path_name + 'test_label.npy', test_label)




#SET 04


target_sequence = '../extra_feature/pre_procesado/' + target_path + '/' + target_name_4 + '/' + target_name_4 + '.txt'
target_path_name = '../extra_feature/pre_procesado/' + target_path + '/' + target_name_4 + '/'

train_ids = [] 
dev_ids = [] 
test_ids = [] 
with open( target_sequence ) as f:
    lines = f.readlines()
    train_ids = [ int(x) for x in lines[0].strip().split(' ')]
    dev_ids =  [ int(x) for x in lines[1].strip().split(' ')]
    test_ids = [ int(x) for x in lines[2].strip().split(' ')]

print(len(train_ids))
print(len(dev_ids))
print(len(test_ids))


# MFCC
train_audio_mfcc = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), train_ids  )
dev_audio_mfcc  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), dev_ids  )
test_audio_mfcc  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), test_ids  )

np.save( target_path_name + 'train_audio_mfcc.npy', train_audio_mfcc)
np.save( target_path_name + 'dev_audio_mfcc.npy', dev_audio_mfcc)
np.save( target_path_name + 'test_audio_mfcc.npy', test_audio_mfcc)


# prosody
train_audio_prosody = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), train_ids  )
dev_audio_prosody  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), dev_ids  )
test_audio_prosody  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), test_ids  )

np.save( target_path_name + 'train_audio_prosody.npy', train_audio_prosody)
np.save( target_path_name + 'dev_audio_prosody.npy', dev_audio_prosody)
np.save( target_path_name + 'test_audio_prosody.npy', test_audio_prosody)




# sequenceN
seqN_npy = []
with open('../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA_sequenceN.txt') as f :
    seqN = [ int(x.strip()) for x in f.readlines() ]
    seqN_npy = np.asarray(seqN)
    
train_seqN = extract_data_with_ids( seqN_npy, train_ids  )
dev_seqN  = extract_data_with_ids( seqN_npy, dev_ids  )
test_seqN = extract_data_with_ids( seqN_npy, test_ids  )

np.save( target_path_name + 'train_seqN.npy', train_seqN)
np.save( target_path_name + 'dev_seqN.npy', dev_seqN)
np.save( target_path_name + 'test_seqN.npy', test_seqN)


# label
label_npy = []
with open('../extra_feature/pre_procesado/' + target_path + '/FC_label.txt') as f :
    label = [ int(x.strip()) for x in f.readlines() ]
    label_npy = np.asarray(label)

train_label = extract_data_with_ids( label_npy, train_ids  )
dev_label  = extract_data_with_ids( label_npy, dev_ids  )
test_label = extract_data_with_ids( label_npy, test_ids  )

np.save( target_path_name + 'train_label.npy', train_label)
np.save( target_path_name + 'dev_label.npy', dev_label)
np.save( target_path_name + 'test_label.npy', test_label)



#set 05

target_sequence = '../extra_feature/pre_procesado/' + target_path + '/' + target_name_5 + '/' + target_name_5 + '.txt'
target_path_name = '../extra_feature/pre_procesado/' + target_path + '/' + target_name_5 + '/'

train_ids = [] 
dev_ids = [] 
test_ids = [] 
with open( target_sequence ) as f:
    lines = f.readlines()
    train_ids = [ int(x) for x in lines[0].strip().split(' ')]
    dev_ids =  [ int(x) for x in lines[1].strip().split(' ')]
    test_ids = [ int(x) for x in lines[2].strip().split(' ')]

print(len(train_ids))
print(len(dev_ids))
print(len(test_ids))


# MFCC
train_audio_mfcc = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), train_ids  )
dev_audio_mfcc  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), dev_ids  )
test_audio_mfcc  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA.npy' ), test_ids  )

np.save( target_path_name + 'train_audio_mfcc.npy', train_audio_mfcc)
np.save( target_path_name + 'dev_audio_mfcc.npy', dev_audio_mfcc)
np.save( target_path_name + 'test_audio_mfcc.npy', test_audio_mfcc)


# prosody
train_audio_prosody = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), train_ids  )
dev_audio_prosody  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), dev_ids  )
test_audio_prosody  = extract_data_with_ids( np.load( '../extra_feature/pre_procesado/' + target_path + '/FC_prodosy.npy' ), test_ids  )

np.save( target_path_name + 'train_audio_prosody.npy', train_audio_prosody)
np.save( target_path_name + 'dev_audio_prosody.npy', dev_audio_prosody)
np.save( target_path_name + 'test_audio_prosody.npy', test_audio_prosody)




# sequenceN
seqN_npy = []
with open('../extra_feature/pre_procesado/' + target_path + '/FC_MFCC12EDA_sequenceN.txt') as f :
    seqN = [ int(x.strip()) for x in f.readlines() ]
    seqN_npy = np.asarray(seqN)
    
train_seqN = extract_data_with_ids( seqN_npy, train_ids  )
dev_seqN  = extract_data_with_ids( seqN_npy, dev_ids  )
test_seqN = extract_data_with_ids( seqN_npy, test_ids  )

np.save( target_path_name + 'train_seqN.npy', train_seqN)
np.save( target_path_name + 'dev_seqN.npy', dev_seqN)
np.save( target_path_name + 'test_seqN.npy', test_seqN)


# label
label_npy = []
with open('../extra_feature/pre_procesado/' + target_path + '/FC_label.txt') as f :
    label = [ int(x.strip()) for x in f.readlines() ]
    label_npy = np.asarray(label)

train_label = extract_data_with_ids( label_npy, train_ids  )
dev_label  = extract_data_with_ids( label_npy, dev_ids  )
test_label = extract_data_with_ids( label_npy, test_ids  )

np.save( target_path_name + 'train_label.npy', train_label)
np.save( target_path_name + 'dev_label.npy', dev_label)
np.save( target_path_name + 'test_label.npy', test_label)

