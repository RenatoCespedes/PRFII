import numpy as np
#Rutas de configuracion de la aplicacion

#Etiquetas 
out_file_Label='../extra_feature/pre_procesado/labels.csv'

#MFCC Features
OPENSMILE_CONFIG_PATH_M= '../extra_feature/config_opensmile/MFCC12_E_D_A.conf'
out_file_M='../extra_feature/pre_procesado/MFCC12EDA.csv'



#Prosodic Features
OPENSMILE_CONFIG_PATH_P= '../extra_feature/config_opensmile/prosodic.conf'
out_file_P='../extra_feature/pre_procesado/prosodic.csv'


#Emobase Features
OPENSMILE_CONFIG_PATH_E= '../extra_feature/config_opensmile/emobase.conf'
out_file_E='../extra_feature/pre_procesado/emobase.csv'

#----Global functions-------

def extract_data_with_ids( npy_data, ids ) :
    npy_data_select = npy_data[ids][:][:]
    print(np.shape(npy_data_select))
    return npy_data_select

#-----------CATEGORIAS----------------
target_path = 'four_category'
target_name_1='audio_set01'
target_name_2='audio_set02'
target_name_3='audio_set03'
target_name_4='audio_set04'
target_name_5='audio_set05'

#--------------------GLOBAL VARIABLES----------------
full_label = []
with open('../extra_feature/pre_procesado/processed_label.txt') as f:
    full_label = f.readlines()
full_label = [ x.strip() for x in full_label]

#---------------------train_test--------------------
path_set01='../extra_feature/pre_procesado/' + target_path + '/audio_set01/audio_set01.txt'
path_set02='../extra_feature/pre_procesado/' + target_path + '/audio_set02/audio_set02.txt'
path_set03='../extra_feature/pre_procesado/' + target_path + '/audio_set03/audio_set03.txt'
path_set04='../extra_feature/pre_procesado/' + target_path + '/audio_set04/audio_set04.txt'
path_set05='../extra_feature/pre_procesado/' + target_path + '/audio_set05/audio_set05.txt'
