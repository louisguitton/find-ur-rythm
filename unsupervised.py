# Est-ce que quand c’est chanté le préfrontal est plus activé?
from dataset_generator import *
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import spectrum


FREQ_RANGES = [[0.5, 4], [4, 8], [8, 12], [11, 15], [15, 30], [30, 45]]
labels = ["Delta", "Theta", "Alpha1", "Alpha2", "Beta", "Gamma"]

SIGNALS_TO_ANALYZE = ["T8", "C4", "F4", "T7", "C3", "CZ"]


def get_spectral_intensities(data, ranges=FREQ_RANGES):
    intensities = []
    spectral_data = spectrum.pmtm(data, 2.5, show=False)
    l = len(data)
    for [min, max] in ranges:
        intensities.extend(sum(spectral_data[int(min * l / FREQ):int(max * l / FREQ)]))
    return intensities


def get_all_spectral_intensities(sample, ranges=FREQ_RANGES, signals=SIGNALS_TO_ANALYZE):
    intensities = []
    for signal in signals:
        intensities.extend(get_spectral_intensities(sample[signal], ranges))
    return(intensities)

plt.figure("C2['F4']")
width = 1
# Sung
plt.subplot(521)
plt.bar(np.arange(6), get_spectral_intensities(enrC2[0]["F4"]))
plt.xticks(np.arange(6) + width/2., labels)
plt.yscale('log')
plt.ylabel("Nekfeu")

plt.subplot(523)
plt.bar(np.arange(6), get_spectral_intensities(enrC2[2]["F4"]))
plt.xticks(np.arange(6) + width/2., labels)
plt.yscale('log')
plt.ylabel("Patrick Sebastien")

plt.subplot(525)
plt.bar(np.arange(6), get_spectral_intensities(enrC2[3]["F4"]))
plt.xticks(np.arange(6) + width/2., labels)
plt.yscale('log')
plt.ylabel("Gorillaz")

plt.subplot(527)
plt.bar(np.arange(6), get_spectral_intensities(enrC2[4]["F4"]))
plt.xticks(np.arange(6) + width/2., labels)
plt.yscale('log')
plt.ylabel("Above n Beyond")

plt.subplot(529)
plt.bar(np.arange(6), get_spectral_intensities(enrC2[9]["F4"]))
plt.xticks(np.arange(6) + width/2., labels)
plt.yscale('log')
plt.ylabel("Glaciation")

# Instru
plt.subplot(522)
plt.bar(np.arange(6), get_spectral_intensities(enrC2[1]["F4"]))
plt.xticks(np.arange(6) + width/2., labels)
plt.yscale('log')
plt.ylabel("District7")

plt.subplot(524)
plt.bar(np.arange(6), get_spectral_intensities(enrC2[5]["F4"]))
plt.xticks(np.arange(6) + width/2., labels)
plt.yscale('log')
plt.ylabel("Victor Wooten")

plt.subplot(526)
plt.bar(np.arange(6), get_spectral_intensities(enrC2[6]["F4"]))
plt.xticks(np.arange(6) + width/2., labels)
plt.yscale('log')
plt.ylabel("Stravinsky")

plt.subplot(528)
plt.bar(np.arange(6), get_spectral_intensities(enrC2[7]["F4"]))
plt.xticks(np.arange(6) + width/2., labels)
plt.yscale('log')
plt.ylabel("Symbolic n Avalon")

plt.subplot(520)
plt.bar(np.arange(6), get_spectral_intensities(enrC2[8]["F4"]))
plt.xticks(np.arange(6) + width/2., labels)
plt.yscale('log')
plt.ylabel("City Lies")

plt.show()
# plt.savefig("C2.png")




# prefrontal_sung = np.array([])
# prefrontal_instru = np.array([])
# for i in range(10):
#     if features1[i]["sung"] == 1:
#         print(i)
#         # prefrontal_sung = np.concatenate((prefrontal_sung, enrL1[i]["F4"]), axis=0)
#     else:
#         print("lol", i)
#         # prefrontal_instru = np.concatenate((prefrontal_instru, enrL1[i]["F4"]), axis=0)
# prefrontal_sung = abs(fft(prefrontal_sung))
# prefrontal_instru = abs(fft(prefrontal_instru))

#
# def ffty(y):
#     # len(y)=T*N
#     # de 0 a 40 Hz
#     fmax = 40.0
#     T = 1.0 / (2.0 * fmax)
#     # Number of samplepoints
#     N = len(y)/T
#     print("N ", N)
#     yf = fft(y)
#     print(len(yf))
#     xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
#     print(len(xf))
#     plt.plot(xf, 2.0/N * np.abs(yf[0:N/2]))
#     plt.grid()
#     plt.show()
