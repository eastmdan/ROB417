import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt

from build_links import build_links
from place_links import place_links
from threeD_draw_links import threeD_draw_links
from threeD_robot_arm_endpoints import threeD_robot_arm_endpoints
from threeD_robot_arm_links import threeD_robot_arm_links
from threeD_joint_axis_set import threeD_joint_axis_set
from vector_set_rotate import vector_set_rotate


def draw_3D_arm_individual_links():
    # Draw the arm as a set of lines, one per link

    link_vectors = [np.array(([1], [0], [0])), np.array(([1], [0], [0])), np.array(([0], [0], [0.5]))]

    joint_angles = np.array(([(2 * np.pi) / 5], [-np.pi / 4], [np.pi / 4]))

    joint_axes = ['z', 'y', 'x']

    link_colors = ['r', 'g', 'b']

    link_set, _, r_links, _, _, _, _, _ = threeD_robot_arm_links(deepcopy(link_vectors), deepcopy(joint_angles), deepcopy(joint_axes))

    joint_axis_vectors = threeD_joint_axis_set(deepcopy(joint_axes))

    joint_axis_vectors_r = vector_set_rotate(deepcopy(joint_axis_vectors), deepcopy(r_links))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    threeD_draw_links(link_set, link_colors, ax)

    ax.view_init(elev=20, azim=30)

    ax.set_box_aspect([1, 1, 1])

    _, _, _, _, _, link_end_set_with_base = threeD_robot_arm_endpoints(deepcopy(link_vectors), deepcopy(joint_angles), deepcopy(joint_axes))
    joint_axis_links = build_links(deepcopy(joint_axis_vectors_r))
    # joint_axis_links == links_in_world
    # link_end_set_with_base
    # link end set with base should be vertical columnar vectors (list of)
    # instead, is 3x4 matrix
    # currently is iterating over every row of link_end_set_with_base
    # needs to... ignore the last column of link_end_set with base?
    # what to do with zero vector...
    link_end_set_with_base = [col.reshape(3, 1) for col in link_end_set_with_base.T]
    l3_joints = place_links(joint_axis_links, link_end_set_with_base)

    l3 = []
    for i in range(len(l3_joints)):
        l3.append(ax.plot(xs = l3_joints[i][0, :], ys = l3_joints[i][1, :], zs= l3_joints[i][2, :],
                          marker='o', linestyle='--', color=link_colors[i]))

    plt.show()


if __name__ == "__main__":
    draw_3D_arm_individual_links()
