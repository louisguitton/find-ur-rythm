from dataset_generator import *
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np

h5dataLD = h5py.File("data/Test_Louis_droite_Test_Louis_droite_04-mars2016.h5", "r")


# plt.plot(h5dataLD['signal_3/sig'])
plt.plot(enrL2[0]["E2"])
plt.show()
