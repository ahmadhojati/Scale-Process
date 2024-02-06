#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from scipy import signal

def psd_(imarray, direction):
    """
    This function computes the power spectral density (psd) for East-West and North-South directions.

    Parameters:
    - imarray (numpy.ndarray): Image array file.
    - direction (str): 'N' for North-South and 'E' for East-West direction.

    Returns:
    - psd_normalized (numpy.ndarray): Normalized power spectral density.
    - freqs (numpy.ndarray): Frequencies.
    """
    psd0 = np.zeros(int(len(imarray) / 2) + 1)

    if direction == 'N':
        for i in range(0, len(imarray)):
            freqs, psd = signal.welch(imarray[:, i], nperseg=len(imarray))
            psd0 = psd + psd0
    elif direction == 'E':
        for j in range(0, len(imarray)):
            freqs, psd = signal.welch(imarray[j, :], nperseg=len(imarray))
            psd0 = psd + psd0

    psd_normalized = psd0 / len(imarray)

    return psd_normalized, freqs

