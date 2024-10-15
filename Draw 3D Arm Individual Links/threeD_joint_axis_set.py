import numpy as np


def threeD_joint_axis_set(joint_axes):
    # Generate a set of unit vectors along specified x, y, or z axes

    joint_axis_vectors = []
    for i, axes in enumerate(joint_axes):
        if axes == 'x':
            joint_axis_vectors.append(np.array(([1], [0], [0])))
        elif axes == 'y':
            joint_axis_vectors.append(np.array(([0], [1], [0])))
        elif axes == 'z':
            joint_axis_vectors.append(np.array(([0], [0], [1])))
        else:
            raise ValueError(f"{axes} is not a known joint axis")

    return joint_axis_vectors


def test_joint_axis_set():
    s = threeD_joint_axis_set(["x", "y", "z"])
    for i in s:
        print(i)


if __name__ == "__main__":
    test_joint_axis_set()
