from sklearn.ensemble import RandomForestClassifier
from dataset_generator import *
import spectrum
import numpy as np
# import matplotlib.pyplot as plt
# import numpy.fft
# import math
# from scipy import signal

FREQ_RANGES = [[0.5, 4], [4, 8], [8, 12], [11, 15], [15, 30], [30, 45]]
# Delta, Theta, Alpha, Beta, Sigma, Delta

SIGNALS_TO_ANALYZE = ["T8", "C4", "F4", "T7", "C3", "CZ"]


def get_spectral_intensities(data, ranges=FREQ_RANGES):
    intensities = []
    spectral_data = spectrum.pmtm(data, 2.5)
    l = len(data)
    for [min, max] in ranges:
        intensities.extend(sum(spectral_data[int(min * l / FREQ):int(max * l / FREQ)]))
    return intensities


def get_all_spectral_intensities(sample, ranges=FREQ_RANGES, signals=SIGNALS_TO_ANALYZE):
    intensities = []
    for signal in signals:
        intensities.extend(get_spectral_intensities(sample[signal], ranges))
    return(intensities)


def add_samples_to_set(x, y, samples, output):
    for sample in samples:
        x.append(get_all_spectral_intensities(sample))
        y.append(output)


# def get_inputs_from_enr(enr, length):
    # inputs = []
    # for sample in

print("Generating dataset for L1")
xL1 = []
yL1 = []
for i in range(10):
    add_samples_to_set(xL1, yL1, cut_sample(enrL1[i], 5), features1[i]["sung"])

print("Generating dataset for L2")
xL2 = []
yL2 = []
for i in range(10):
    add_samples_to_set(xL2, yL2, cut_sample(enrL2[i], 5), features1[i]["sung"])

print("Learning")
classifier = RandomForestClassifier()
classifier.fit(xL1, yL1)

print(classifier.score(xL2, yL2))
