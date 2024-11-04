import numpy as np


def ry(phi):
    # Rotation matrix about the y-axis
    r = np.array([[np.cos(phi), 0, np.sin(phi)],
                  [0, 1, 0],
                  [-1 * np.sin(phi), 0, np.cos(phi)]])
    return r
