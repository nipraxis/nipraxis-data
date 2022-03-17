""" Make camera data from scikit-image
"""
import numpy as np

from skimage.data import camera

camera_data = camera().astype(float)
camera_data = camera_data - camera_data.min()
camera_data = camera_data / camera_data.max()

np.savetxt('camera.txt', camera_data.T.ravel(), fmt="%0.4f")
