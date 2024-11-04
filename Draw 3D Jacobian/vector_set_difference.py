import numpy as np
from copy import deepcopy


def vector_set_difference(v, v_set):
    """
    % Find the vector difference v - v_set (the vector pointing to v from each
    % element of v_set).
    """
    v_diff = deepcopy(v_set)

    for i in range(0, len(v_set)):
        v_diff[i] = v - v_set[i]
    return v_diff


def test_vector_set_difference():
    v_set = [np.array(([1], [0])), np.array(([0], [1]))]
    v_single = np.array(([2], [2]))
    v_diff = vector_set_difference(v_single, v_set)
    for v in v_diff:
        print(v)


if __name__ == "__main__":
    test_vector_set_difference()
