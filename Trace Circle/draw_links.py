import matplotlib.pyplot as plt
import numpy as np


def draw_links(link_set, link_colors, ax):
    # Draw a set of lines for a link structure into a specified axis
    lines = []

    for i, link in enumerate(link_set):
        line, = ax.plot(link[0], link[1], marker="o", color=link_colors[i])
        lines.append(line)

    return lines


def test_draw_links():
    # unfinished, reference threeD_draw_links to test.
    link_vectors = [
        np.array(([1], [0])),
        np.array(([1], [0]))
    ]
    joint_angles = np.array(([np.pi / 4], [-np.pi / 2], [1]))
    #link_set = planar_robot_arm_links(link_vectors, joint_angles)
    #draw_links()


if __name__ == "__main__":
    test_draw_links()

"""
link_vectors = {[1;0],[1;0]};
joint_angles = [pi/4; -pi/2];
link_set = planar_robot_arm_links(link_vectors,joint_angles);
ax = create_axes(317);

link_colors = {'r',[0.5 0.5 0.5]};

l = draw_links(link_set,link_colors,ax)
"""