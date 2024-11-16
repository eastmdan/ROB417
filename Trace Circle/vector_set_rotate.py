import numpy as np
from copy import deepcopy
from planar_rotation_set import planar_rotation_set


def vector_set_rotate(v_set, r_set):
    """
    % Rotate a set of vectors specified in local coordinates by a set of
    % rotation matrices that specifies the orientations of the frames in which
    % the vectors are defined.
    """
    v_set_r = deepcopy(v_set)
    for i, (vector, rotation) in enumerate(zip(v_set, r_set)):
        v_set_r[i] = np.dot(rotation, vector)
    return v_set_r


def test_vsr():
    v_set = [np.array(([1], [0])), np.array(([0], [1])), np.array(([10], [15]))]
    # v_set = np.array(([[1], [0]], [[0], [1]], [[10], [15]]))
    r_set = planar_rotation_set(np.array((-1, 1, 2)) * np.pi / 4)
    v_set_r = vector_set_rotate(v_set, r_set)
    for s in v_set_r:
        print(s)


if __name__ == "__main__":
    test_vsr()
