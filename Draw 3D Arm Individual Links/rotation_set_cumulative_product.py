import numpy as np
from planar_rotation_set import planar_rotation_set


def rotation_set_cumulative_product(r_set):
    """
    % Take the cumulative product of a set of rotation matrices
    """

    r_set_c = r_set
    for i in range(1, len(r_set)):
        r_set_c[i] = np.matmul(r_set_c[i - 1], r_set_c[i])
    return r_set


def test_rotate_cum() -> None:
    rotations = planar_rotation_set([0, np.pi, np.pi / 4])
    r_set = rotation_set_cumulative_product(rotations)
    for m in r_set:
        print(m)


if __name__ == "__main__":
    test_rotate_cum()
