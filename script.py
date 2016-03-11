import h5py
import numpy as np
import matplotlib.pyplot as plt


f = h5py.File("data/Test_Louis_Test_Louis_gauche_04-mars2016.h5", "r")

for name in f:
    print(name)

dset = f['signal_0/sig']
print(dset)
print(dset.shape)
# print dset.type

# frequence d'echantillonage en Hz
freq = 250
length_acquisition = dset.shape[0] / (freq*60)  # in minutes
print("the acquisition is ", length_acquisition, " minutes long")

plt.plot(dset)
plt.ylabel('Louis Gauche')
plt.show()
