import h5py
import numpy as np
# from numpy. import fft
import json
import numpy.fft

FREQ = 256
START_C1 = 21189
START_C2 = START_C1 + FREQ * (20 * 60 + 10)
START_L1 = 34532
START_L2 = START_L1 + FREQ * (20 * 60 + 10)
START_BUFFER = FREQ * 20
END_BUFFER = FREQ * 10
BLINK_DELAY = FREQ * 10
SAMPLE_LENGTH = FREQ * 120

playlist_file = open("playlist.json", "r")
playlist = json.load(playlist_file)

h5dataCD = h5py.File("data/Test_Charles_droite_Test_Charles_droite_04-mars2016.h5", "r")
h5dataCG = h5py.File("data/Test_Charles_gauche_Test_Charles_gauche_04-mars2016.h5", "r")
h5dataLD = h5py.File("data/Test_Louis_droite_Test_Louis_droite_04-mars2016.h5", "r")
h5dataLG = h5py.File("data/Test_Louis_Test_Louis_gauche_04-mars2016.h5", "r")


playlist1 = {
    'sung': [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    'rythmic': [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    'charles likes': [0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    'louis likes': [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
}
playlist2 = {
    'sung': [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    'rythmic': [0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    'charles likes': [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    'louis likes': [1, 0, 1, 0, 1, 1, 1, 0, 0, 0]
}

features1 = [None] * 10
features2 = [None] * 10
for i in range(10):
    features1[i] = {
        'sung': playlist1["sung"][i],
        'rythmic': playlist1["rythmic"][i],
        'charles likes': playlist1["charles likes"][i],
        'louis likes': playlist1["louis likes"][i]
    }
    features2[i] = {
        'sung': playlist2["sung"][i],
        'rythmic': playlist2["rythmic"][i],
        'charles likes': playlist2["charles likes"][i],
        'louis likes': playlist2["louis likes"][i]
    }


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


def crop_sample(sample, start_time, end_time):
    cropped_sample = {}
    for signal in sample:
        cropped_sample[signal] = sample[signal][int(start_time * FREQ):int(end_time * FREQ)]
    return(cropped_sample)


def cut_sample(sample, length):
    samples = []
    for i in range(int(len(sample['T8']) / (FREQ * length))):
        samples.append(crop_sample(sample, i * length, (i + 1) * length))
    return(samples)


enrL1 = get_array(h5dataLD, h5dataLG, START_L1)
enrL2 = get_array(h5dataLD, h5dataLG, START_L2)
enrC1 = get_array(h5dataCD, h5dataCG, START_C1)
enrC2 = get_array(h5dataCD, h5dataCG, START_C2)
