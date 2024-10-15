import matplotlib.pyplot as plt
import numpy as np


from threeD_robot_arm_links import threeD_robot_arm_links


def threeD_draw_links(link_set, link_colors, ax):
    # Draw a set of lines for a link structure into a specified axis.

    for i, link in enumerate(link_set):
        ax.plot(link[0], link[1], link[2], marker="o", color=link_colors[i])


def test_3d_draw_links() -> None:
    link_vectors = [
        np.array(([1], [0], [0])),
        np.array(([0], [1], [0])),
        np.array(([1], [0], [1])),
    ]
    joint_angles = np.array(([np.pi / 4], [-np.pi / 2], [1]))
    joint_axes = np.array(["x", "y", "z"])
    link_set, _, _, _, _, _, _, _ = threeD_robot_arm_links(link_vectors, joint_angles, joint_axes)
    link_colors = ["r", "g", "b"]
    fig, ax = plt.subplots(1, 1)
    threeD_draw_links(link_set, link_colors, ax)
    #fig.savefig("out.jpg")
    plt.show()


if __name__ == "__main__":
    test_3d_draw_links()
