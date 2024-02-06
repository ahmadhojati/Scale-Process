#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import collections
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


def dist_plot_(imarray, resolution, direction, arg, S):
    """
    This function generates a distribution plot of peak distances.

    Parameters:
    - imarray (numpy.ndarray): Input image.
    - resolution (float): The image resolution.
    - direction (str): Direction of analysis - 'N' for North-South or 'E' for East-West.
    - arg (tuple): The title for the plot and the input image file name for saving.
    - S (int): If S==1 it saves the plot.
    """
    # Peak distances at North-South or East-West direction
    lst = peak_diff(imarray, resolution, direction)

    # Convert the distances to a list of distances for the distribution plot
    d = []
    for l in range(0, len(lst)):
        d += lst[l].tolist()

    # Initial figure
    plt.figure(figsize=(12, 6))

    # Count the elements and store as dictionary values
    ctr = collections.Counter(d)
    cnt, val = ctr.values(), ctr.keys()

    # Plot Distance versus frequency of its happening
    plt.plot(list(val), list(cnt) / np.sum(list(cnt)) * 100, 'r^', markersize=8)
    plt.xlabel('Distance (m)', fontsize=15)
    plt.ylabel('Frequency(%)', fontsize=15)
    plt.title('{}'.format(arg[0]), fontsize=15)

    # Save the plot
    if S == 1:
        plt.savefig('Peak_distance_distribution_{}.png'.format(arg[1]), dpi=300)

    # Print the median distance between the peaks at North-South direction
    print('Median peak distance = {} m'.format(np.median(d)))

