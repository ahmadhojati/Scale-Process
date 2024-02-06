#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from scipy.signal import find_peaks

def peak_diff(im, resolution, direction):
    """
    This function finds the peaks farther than 1m from each other per each row and column of the image.

    Parameters:
    - im (numpy.ndarray): Input image.
    - resolution (float): The image resolution.
    - direction (str): Direction of analysis - 'N' for North-South or 'E' for East-West.

    Returns:
    - d (list): Distances between peaks at a specific direction.
    """
    d = []

    for i in range(0, len(im)):
        # For each column
        if direction == 'N':
            peaks, _ = find_peaks(im[:, i], height=np.mean(im[:, i]), distance=1, width=1)
            d0 = np.diff(peaks) * resolution
            d.append(d0)

        # For each row
        elif direction == 'E':
            peaks, _ = find_peaks(im[i, :], height=np.mean(im[i, :]), distance=1, width=1)
            d0 = np.diff(peaks) * resolution
            d.append(d0)

    return d

