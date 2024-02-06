#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

def subimage(image, theta):
    """
    This function rotates the image around the center with the specified angle (in degrees) and crops the image in half.
    Positive theta rotation means counter-clockwise.

    Parameters:
    - image (numpy.ndarray): The image that we want to rotate.
    - theta (float): Rotation angle.

    Returns:
    - rotated_image (numpy.ndarray): Rotated and cropped image.
    """
    # Read the image dimensions
    rows, cols = image.shape

    # The center of the image (half of the image length)
    center = (int(cols / 2), int(rows / 2))

    # Find the transformation matrix and rotate
    matrix = cv2.getRotationMatrix2D(center=center, angle=theta, scale=1)
    rotated_image = cv2.warpAffine(image, matrix, (rows, cols))

    # Crop the transformed image from the center into half
    rotated_image = rotated_image[int(cols / 4):int(cols - cols / 4), int(rows / 4):int(rows - rows / 4)]

    return rotated_image

