################################
#     Training             
################################
CAL_ACCURACY_FROM = 0
MAX_EARLY_STOP_COUNT = 7
EPOCH_PER_VALID_FREQ = 0.3

DATA_TRAIN_MFCC            = 'train_audio_mfcc.npy'
DATA_TRAIN_MFCC_SEQN  = 'train_seqN.npy'
DATA_TRAIN_PROSODY      = 'train_audio_prosody.npy'
DATA_TRAIN_LABEL           = 'train_label.npy'



DATA_DEV_MFCC              = 'dev_audio_mfcc.npy'
DATA_DEV_MFCC_SEQN    = 'dev_seqN.npy'
DATA_DEV_PROSODY        = 'dev_audio_prosody.npy'
DATA_DEV_LABEL             = 'dev_label.npy'



DATA_TEST_MFCC            = 'test_audio_mfcc.npy'
DATA_TEST_MFCC_SEQN  = 'test_seqN.npy'
DATA_TEST_PROSODY      = 'test_audio_prosody.npy'
DATA_TEST_LABEL           = 'test_label.npy'





################################
#     Audio
################################
N_CATEGORY = 4
N_AUDIO_MFCC = 39
N_AUDIO_PROSODY= 35
N_SEQ_MAX = 750                 # max 1,000 (MSP case only)



################################
#     ETC
################################
IS_LOGGING = True