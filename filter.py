from dataset_generator import *
from scipy.signal import filter_design, filtfilt


# Eliminate the electrical interference noise (50 Hz) using notch filter.
def filter_50Hz(sample):
    # Chebyshev notch filter centered on 50Hz
    nyquist = FREQ / 2.
    b, a = filter_design.iirfilter(3, (49. / nyquist, 51. / nyquist), rs=10, ftype='cheby2')
    sample_50Hz = filtfilt(b, a, sample)
    return(sample - sample_50Hz)
