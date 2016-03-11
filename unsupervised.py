# Est-ce que quand c’est chanté le préfrontal est plus activé?
from dataset_generator import *
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np

prefrontal_sung = np.array([])
prefrontal_instru = np.array([])
for i in range(10):
    if features1[i]["sung"] == 1:
        prefrontal_sung = np.concatenate((prefrontal_sung, enrL1[i]["F4"]), axis=0)
    else:
        prefrontal_instru = np.concatenate((prefrontal_instru, enrL1[i]["F4"]), axis=0)


# prefrontal_sung = abs(fft(prefrontal_sung))
# prefrontal_instru = abs(fft(prefrontal_instru))

# plt.figure(1)
# plt.subplot(211)
# plt.plot(prefrontal_sung)
#
# plt.subplot(212)
# plt.plot(prefrontal_instru)
# plt.show()

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = prefrontal_sung
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
y2 = prefrontal_instru
yf2 = fft(y2)

plt.figure(1)
plt.subplot(521)
plt.plot(xf, 2.0/N * np.abs(yf[:N/2]))
plt.subplot(522)
plt.plot(xf, 2.0/N * np.abs(yf2[:N/2]))
plt.show()
