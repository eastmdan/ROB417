import matplotlib.pyplot as plt
import numpy as np

from threeD_robot_arm_links import threeD_robot_arm_links
from draw_links import draw_links


# not done
def threeD_update_links(lines, link_set):
    # Update the drawings of a set of lines for a link structure

    for i, line in enumerate(lines):
        #print(line, i)
        line.set_xdata(link_set[i][0])
        line.set_ydata(link_set[i][1])
        line.set_3d_properties(link_set[i][2])

    return lines


def test_threeD_update_links():
    link_vectors = [np.array([[1], [0], [0]]), np.array([[1], [0], [0]]), np.array([[0], [0], [1]])]
    joint_angles = np.array([[np.pi / 4], [-np.pi / 2], [1]])
    joint_axes = ['x', 'y', 'z']
    link_set, _, _, _, _, _, _, _ = threeD_robot_arm_links(link_vectors, joint_angles, joint_axes)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    link_colors = ['red', 'gray', 'black']

    lines = draw_links(link_set, link_colors, ax)

    ax.view_init(elev=20, azim=30)

    link_set, _, _, _, _, _, _, _ = threeD_robot_arm_links(link_vectors, joint_angles + 1, joint_axes)

    threeD_update_links(lines, link_set)

    ax.set_xlim([0, 2])
    ax.set_ylim([-1.5, 0])
    ax.set_zlim([-1, 1])

    plt.show()


if __name__ == "__main__":
    test_threeD_update_links()
