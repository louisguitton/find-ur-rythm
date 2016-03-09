import h5py
import numpy as np
import matplotlib.pyplot as plt


f = h5py.File("data/Test_Louis_Test_Louis_gauche_04-mars2016.h5", "r")

for name in f:
    print name

dset = f['signal_0/sig']
print dset
print dset.shape
# print dset.type
plt.plot(dset)
plt.ylabel('Louis Gauche')
plt.show()

# frequence d'echantillonage en Hz
freq = 250
length_acquisition = dset.shape / (freq*60)  # in minutes
print length_acquisition
