# Est-ce que quand c’est chanté le préfrontal est plus activé?
from dataset_generator import *
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np

prefrontal_sung = np.array([])
prefrontal_instru = np.array([])
for i in range(10):
    if features1[i]["sung"] == 1:
        print(i)
        # prefrontal_sung = np.concatenate((prefrontal_sung, enrL1[i]["F4"]), axis=0)
    else:
        print("lol", i)
        # prefrontal_instru = np.concatenate((prefrontal_instru, enrL1[i]["F4"]), axis=0)


# prefrontal_sung = abs(fft(prefrontal_sung))
# prefrontal_instru = abs(fft(prefrontal_instru))
def ffty(y):
    # Number of samplepoints
    N = 600
    # sample spacing
    T = 1.0 / 800.0
    x = np.linspace(0.0, N*T, N)
    yf = fft(y)
    xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
    plt.plot(xf, 2.0/N * np.abs(yf[:N/2]))


plt.figure(1)
# Sung
plt.subplot(521)
ffty(enrL1[0]["F4"])
plt.ylabel("Nekfeu")

plt.subplot(523)
ffty(enrL1[2]["F4"])
plt.ylabel("Patrick Sebastien")

plt.subplot(525)
ffty(enrL1[3]["F4"])
plt.ylabel("Gorillaz")

plt.subplot(527)
ffty(enrL1[4]["F4"])
plt.ylabel("Above n Beyond")

plt.subplot(529)
ffty(enrL1[9]["F4"])
plt.ylabel("Glaciation")
# Instru
plt.subplot(522)
ffty(enrL1[1]["F4"])
plt.ylabel("District7")

plt.subplot(524)
ffty(enrL1[5]["F4"])
plt.ylabel("Victor Wooten")

plt.subplot(526)
ffty(enrL1[6]["F4"])
plt.ylabel("Stravinsky")

plt.subplot(528)
ffty(enrL1[7]["F4"])
plt.ylabel("Symbolic n Avalon")

plt.subplot(520)
ffty(enrL1[8]["F4"])
plt.ylabel("City Lies")

plt.show()
