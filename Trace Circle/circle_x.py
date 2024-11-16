import numpy as np


def circle_x(t):
    """
    % Generate points on a unit circle in the y-z plane, wrapping in the
    % clockwise (negative) direction around the x-axis, such that the
    % range of t=[0 1] corresponds to one full cycle of the circle, and
    % the initial point is at [0;0;1]
    """
    t = np.atleast_1d(t).flatten()

    xyz = np.zeros((3, len(t)))
    for i, j in enumerate(t):
        xyz[1, i] = round(np.sin(2 * np.pi * j), 4)
        xyz[2, i] = round(np.cos(2 * np.pi * j), 4)

    return xyz


def test_circle_x():
    # Column input
    t_column = np.array([[0.125], [0.25], [0.375], [0.5]])
    xyz_from_column = circle_x(t_column)
    print(xyz_from_column)

    # Row input
    t_row = np.array([0.625, 0.75, 0.875, 1])
    xyz_from_row = circle_x(t_row)
    print(xyz_from_row)


if __name__ == "__main__":
    test_circle_x()
