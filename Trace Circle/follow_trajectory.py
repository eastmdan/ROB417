import numpy as np
import numdifftools as nd


# not done
def follow_trajectory(t, alpha, j, shape_to_draw):
    """
    % Find the set of 'alpha_dot' joint velocities at a time 't' and current
    % joint angles 'alpha' that will make the end of an arm whose Jacobian
    % function is 'J' follow the shape described by the function 'shape to
    % draw'.
    """

    jacobian_shape = nd.Jacobian(shape_to_draw)
    v = jacobian_shape(t).flatten()

    alpha_dot, _, _, _ = np.linalg.lstsq(j(alpha), v, rcond=None)

    return alpha_dot, v


def test_follow_trajectory():
    def shape_to_draw(time):
        return np.array([time, time ** 2, time ** 3]).ravel()

    def j_array(a): return np.array([[a[0], 0, 0],
                                     [0, a[1], 0],
                                     [0, 0, 1]])

    t = 1
    alpha = np.array([2, 3, 0])

    alpha_dot, v = follow_trajectory(t, alpha, j_array, shape_to_draw)
    print("alpha_dot:\n", alpha_dot)
    print("v:\n", v)


if __name__ == "__main__":
    test_follow_trajectory()
