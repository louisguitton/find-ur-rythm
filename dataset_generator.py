import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import filter_design, filtfilt

FREQ = 250
START_C1 = 21189
START_C2 = START_C1 + FREQ * (20 * 60 + 10)
START_L1 = 34532
START_L2 = START_L1 + FREQ * (20 * 60 + 10)
START_BUFFER = FREQ * 20
END_BUFFER = FREQ * 10
BLINK_DELAY = FREQ * 10
SAMPLE_LENGTH = FREQ * 120

h5dataCD = h5py.File("data/Test_Charles_droite_Test_Charles_droite_04-mars2016.h5", "r")
h5dataCG = h5py.File("data/Test_Charles_gauche_Test_Charles_gauche_04-mars2016.h5", "r")
h5dataLD = h5py.File("data/Test_Louis_droite_Test_Louis_droite_04-mars2016.h5", "r")
h5dataLG = h5py.File("data/Test_Louis_Test_Louis_gauche_04-mars2016.h5", "r")

def get_array(dataD, dataG, start_enr):
    enr = [None] * 10
    for i in range(10):
        start = start_enr + SAMPLE_LENGTH * i + BLINK_DELAY + START_BUFFER
        end = start_enr + SAMPLE_LENGTH * (i + 1) - END_BUFFER
        enr[i] = {
            'T8': np.array(dataD['signal_0/sig'][start:end]),
            'C4': np.array(dataD['signal_1/sig'][start:end]),
            'F4': np.array(dataD['signal_2/sig'][start:end]),
            'E2': np.array(dataD['signal_3/sig'][start:end]),
            'T7': np.array(dataG['signal_0/sig'][start:end]),
            'C3': np.array(dataG['signal_1/sig'][start:end]),
            'CZ': np.array(dataG['signal_2/sig'][start:end])
        }
    return(enr)

enrL1 = get_array(h5dataLD, h5dataLG, START_L1)
enrL2 = get_array(h5dataLD, h5dataLG, START_L2)
enrC1 = get_array(h5dataCD, h5dataCG, START_C1)
enrC2 = get_array(h5dataCD, h5dataCG, START_C2)

print(len(enrC1[0]['CZ']))
print(len(enrC1[9]['CZ']))
