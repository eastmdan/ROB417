import numpy as np

from build_links import build_links
from place_links import place_links
from copy import deepcopy
from rotation_set_cumulative_product import rotation_set_cumulative_product
from threeD_rotation_set import threeD_rotation_set
from vector_set_cumulative_sum import vector_set_cumulative_sum
from vector_set_rotate import vector_set_rotate


def threeD_robot_arm_links(link_vectors, joint_angles, joint_axes):
    """
    Take a set of link vectors, joint angles, and joint axes, and return a
    set of matrices for which the columns of each matrix are the endpoints of
    one of the links.
    """

    r_joints = threeD_rotation_set(joint_angles, joint_axes)

    r_links = rotation_set_cumulative_product(r_joints)

    link_set_local = build_links(deepcopy(link_vectors))

    link_vectors_in_world = vector_set_rotate(link_vectors, r_links)

    links_in_world = vector_set_rotate(link_set_local, r_links)

    link_end_set = vector_set_cumulative_sum(link_vectors_in_world)

    link_end_set_with_base = np.hstack((np.zeros((3, 1)), np.hstack(link_end_set)))
    link_end_set_with_base = [col.reshape(3, 1) for col in link_end_set_with_base.T]

    link_set = place_links(links_in_world, link_end_set_with_base)

    return (
        link_set,
        r_joints,
        r_links,
        link_set_local,
        link_vectors_in_world,
        links_in_world,
        link_end_set,
        link_end_set_with_base
    )


def test_3d_arm_links():
    link_vectors = [
        np.array(([1], [0], [0])),
        np.array(([0], [1], [0])),
        np.array(([0], [0], [1])),
    ]
    joint_angles = np.array(([np.pi / 4], [-np.pi / 2], [np.pi / 4]))
    joint_axes = np.array(["x", "y", "z"])
    link_set, _, _, _, _, _, _, _ = threeD_robot_arm_links(link_vectors, joint_angles, joint_axes)
    for link in link_set:
        print(link)


if __name__ == "__main__":
    test_3d_arm_links()
