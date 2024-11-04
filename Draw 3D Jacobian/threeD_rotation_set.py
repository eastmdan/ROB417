import numpy as np
from rx import rx
from ry import ry
from rz import rz


def threeD_rotation_set(joint_angles, joint_axes):
    """
    % Generate a set of planar rotation matrices corresponding to the angles
    % and axes in the input vector
    """
    r_set = []
    joint_angles = np.asarray(joint_angles, dtype=float)
    for angle, axis in zip(joint_angles, joint_axes):
        if axis == "x":
            r_set.append(rx(float(angle)))
        elif axis == "y":
            r_set.append(ry(float(angle)))
        elif axis == "z":
            r_set.append(rz(float(angle)))
        else:
            raise ValueError(f"{axis} is not a known joint axis")
    return [np.around(np.asarray(r, dtype=float), 5) for r in r_set]


def test_rotate():
    r_set = threeD_rotation_set([0, np.pi, np.pi / 4], ["x", "y", "z"])
    for i in r_set:
        print(i)


if __name__ == "__main__":
    test_rotate()
