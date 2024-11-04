import numpy as np


def rz(theta):
    # Rotation matrix about the z-axis
    r = np.array([[np.cos(theta), -1 * np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                  [0, 0, 1]])
    return r
