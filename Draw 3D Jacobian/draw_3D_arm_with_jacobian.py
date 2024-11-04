import numpy as np
import matplotlib.pyplot as plt

from arm_jacobian import arm_jacobian
from draw_vectors_at_point import draw_vectors_at_point
from build_links import build_links
from place_links import place_links


def draw_3D_arm_with_jacobian():
    # Make a set of plots (subplots in one axis) that illustrate the
    # relationship between the geometry of the arm and the Jacobians of the
    # links

    link_vectors = [np.array(([1], [0], [0])),
                    np.array(([1], [0], [0])),
                    np.array(([0], [0], [0.5]))]

    joint_angles = np.array(([(2 * np.pi) / 5], [-np.pi / 4], [np.pi / 4]))

    joint_axes = ['z', 'y', 'x']

    j = []
    for i, _ in enumerate(link_vectors):
        (jacobian,
         link_ends,
         link_end_set,
         link_end_set_with_base,
         _, _, joint_axis_vectors_r, _) = arm_jacobian(link_vectors, joint_angles, joint_axes, (i + 1))
        j.append(jacobian)

    cols, _, _ = np.shape(link_vectors)
    fig, axs = plt.subplots(1, cols, subplot_kw={"projection": "3d"}, figsize=(10, 5))

    for i in range(len(axs)):
        axs[i].view_init(azim=-150, elev=30)
        axs[i].plot(link_ends[:, 0], link_ends[:, 1], link_ends[:, 2], marker='o', color='black')

    for i in range(len(axs)):
        # funny reshape to j
        j[i] = [col.reshape(3, 1) for col in j[i].T]
        draw_vectors_at_point(link_end_set[i], j[i], axs[i])

    for i in range(len(axs)):

        for i2 in range(i + 1):
            k = np.hstack((link_end_set_with_base[i2], link_end_set[i]))
            axs[i].plot(k[0, :], k[1, :], k[2, :], linestyle=':')

        joint_axis_links = build_links(joint_axis_vectors_r)
        l3_joints = place_links(joint_axis_links, link_end_set_with_base)

        for i3 in range(i + 1):
            axs[i].plot(l3_joints[i3][0, :], l3_joints[i3][1, :], l3_joints[i3][2, :], linestyle='--')

    plt.show()


if __name__ == "__main__":
    draw_3D_arm_with_jacobian()
