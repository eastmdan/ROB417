import numpy as np


def planar_rotation_set(joint_angles):
    """
    % Generate a set of planar rotation matrices corresponding to the angles in
    % the input vector
    """
    return np.around([r_planar(x) for x in joint_angles], 5)


def r_planar(alpha):
    # % Planar rotation matrix
    r = np.array((np.cos(alpha), -np.sin(alpha), np.sin(alpha), np.cos(alpha))).reshape((-1, 2))
    return r


def test_r_planar() -> None:
    rot_mat = r_planar(np.pi / 4)
    print(rot_mat)


def test_planar_rotation_set() -> None:
    s = planar_rotation_set([0, np.pi, np.pi / 4])
    print(s)


if __name__ == "__main__":
    #test_r_planar()
    test_planar_rotation_set()
