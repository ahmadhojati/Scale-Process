#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def readtiff_(arg_tif, arg_wind, resolution, min_, max_, S):
    """
    This function reads the wind data and tif image of the snow depth or vegetation.

    Parameters:
    - arg_tif (str): The name of the image.
    - arg_wind (str): The wind data file in CSV format.
    - resolution (float): Image resolution.
    - min_ (float): The minimum value to plot.
    - max_ (float): The maximum value for plotting.
    - S (int): If S == 1, it saves the plot.

    Returns:
    - imarray (numpy.ndarray): Array representation of the image.
    - resolution (float): Image resolution.
    - wind (pandas.DataFrame): Wind data.
    """
    # Reading the image
    im = Image.open('{}.tif'.format(arg_tif))

    # Converting the tiff file to an array
    imarray = np.array(im)

    # Filter the noise
    imarray = np.where(imarray < 0, imarray - imarray, imarray)
    imarray = np.nan_to_num(imarray)
    imarray = np.where(imarray > 1000000, imarray - imarray, imarray)

    # Plotting the file and save it
    plt.figure(figsize=(10, 10))
    plt.imshow(imarray, vmin=min_, vmax=max_)
    plt.colorbar()
    if S == 1:
        plt.savefig('{}.png'.format(arg_tif), dpi=300)
    plt.show()

    # Read the wind data
    wind = pd.read_csv('{}.csv'.format(arg_wind))
    
    return imarray, resolution, wind

