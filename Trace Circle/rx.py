import numpy as np


def rx(psi):
    # Rotation matrix about the x-axis
    r = np.array([[1, 0, 0],
                  [0, np.cos(psi), -1 * np.sin(psi)],
                  [0, np.sin(psi), np.cos(psi)]])
    return r
