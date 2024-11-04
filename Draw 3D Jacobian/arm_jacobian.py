import numpy as np
from copy import deepcopy

from threeD_robot_arm_endpoints import threeD_robot_arm_endpoints
from vector_set_difference import vector_set_difference
from threeD_joint_axis_set import threeD_joint_axis_set
from vector_set_rotate import vector_set_rotate


def arm_jacobian(link_vectors, joint_angles, joint_axes, link_number):
    """
    % Construct a Jacobian for a chain of links as a function of the link
    % vectors, the joint angles, joint axes, and the number of the link whose
    % endpoint is the location where the Jacobian is evaluated
    """
    (link_ends, _, R_links, _,
     link_end_set, link_end_set_with_base) = threeD_robot_arm_endpoints(link_vectors, joint_angles, joint_axes)

    v_diff = vector_set_difference(link_end_set[link_number - 1], link_end_set_with_base)

    joint_axis_vectors = threeD_joint_axis_set(joint_axes)

    joint_axis_vectors_r = vector_set_rotate(joint_axis_vectors, R_links)

    j = np.zeros((3, len(joint_angles)))

    for i in range(link_number):
        j[:, i] = np.cross(joint_axis_vectors_r[i].reshape(1, 3), v_diff[i].reshape(1, 3))

    return (j, link_ends, link_end_set, link_end_set_with_base, v_diff,
            joint_axis_vectors, joint_axis_vectors_r, R_links)


def test_arm_jacobian():
    link_vectors = [np.array(([1], [0], [0])), np.array(([0.5], [0], [0])), np.array(([0.5], [0], [0]))]
    joint_angles = np.array(([0.4], [-0.5], [0.25])) * np.pi
    joint_axes = ['z', 'z', 'z']
    link_number = 3
    arm_jacobian(link_vectors, joint_angles, joint_axes, link_number)


if __name__ == "__main__":
    test_arm_jacobian()
