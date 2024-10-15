import numpy as np

from rotation_set_cumulative_product import rotation_set_cumulative_product
from threeD_rotation_set import threeD_rotation_set
from vector_set_cumulative_sum import vector_set_cumulative_sum
from vector_set_rotate import vector_set_rotate


def threeD_robot_arm_endpoints(link_vectors, joint_angles, joint_axes):
    """
    % Take a set of link vectors and joint angles, and return a matrix whose
    % columns are the endpoints of all of the links (including the point that
    % is the first end of the first link, which should be placed at the
    % origin).
    """
    r_joints = threeD_rotation_set(joint_angles, joint_axes)

    r_links = rotation_set_cumulative_product(r_joints)

    link_vectors_in_world = vector_set_rotate(link_vectors, r_links)

    link_end_set = vector_set_cumulative_sum(link_vectors_in_world)


    link_end_set_with_base = np.hstack((np.zeros((3, 1)), np.hstack(link_end_set)))


    link_ends = np.asarray(link_end_set_with_base)

    return (
        link_ends,
        r_joints,
        r_links,
        link_vectors_in_world,
        link_end_set,
        link_end_set_with_base
    )


def test_robot_arm_endpoints():
    link_vectors = [
        np.array(([1], [0], [0])),
        np.array(([1], [0], [0])),
    ]
    joint_angles = np.array(([np.pi / 4], [-np.pi / 2]))
    joint_axes = np.array(["x", "z"])
    link_ends, _, _, _, _, _ = threeD_robot_arm_endpoints(link_vectors, joint_angles, joint_axes)
    for link in link_ends:
        print(link)


if __name__ == "__main__":
    test_robot_arm_endpoints()
