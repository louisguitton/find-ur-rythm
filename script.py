import h5py
import numpy as np

f = h5py.File("data/Test_Louis_Test_Louis_gauche_04-mars2016.h5", "r")

for name in f:
    print name

dset = f['signal_0/sig']
print dset
print dset.shape
# print dset.type
