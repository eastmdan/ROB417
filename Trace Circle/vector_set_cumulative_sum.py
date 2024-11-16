import numpy as np
from copy import deepcopy

def vector_set_cumulative_sum(v_set):
    """
    % Take the cumulative sum of a set of vectors.
    """
    v_set = deepcopy(v_set)
    for i in range(1, len(v_set)):
        v_set[i] = v_set[i - 1] + v_set[i]
    return v_set


def test_cumulative_sum():
    v_set = [np.array(([1], [0])), np.array(([0], [1])), np.array(([12], [30]))]
    v_set_cumulative = vector_set_cumulative_sum(v_set)
    for v in v_set_cumulative:
        print(v)


if __name__ == "__main__":
    test_cumulative_sum()
