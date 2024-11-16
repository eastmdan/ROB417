import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from circle_x import circle_x
from arm_jacobian import arm_jacobian
from follow_trajectory import follow_trajectory
from threeD_robot_arm_links import threeD_robot_arm_links
from threeD_draw_links import threeD_draw_links
from threeD_robot_arm_endpoints import threeD_robot_arm_endpoints
from threeD_update_links import threeD_update_links


# not done
def trace_circle():
    """
    % Make an animated plot of a robot arm tracing a circle in the yz plane
    """

    link_vectors = [np.array(([1], [0], [0])),
                    np.array(([1], [0], [0])),
                    np.array(([0.75], [0], [0]))]

    joint_axes = ['z', 'y', 'y']

    def shape_to_draw(time): return (circle_x(time) * (1 / 2)).ravel()

    def jacobian(b):
        j, _, _ = arm_jacobian(link_vectors, b, joint_axes, len(link_vectors))  # b.reshape(3, 1)
        return j

    def joint_velocity(time, a):
        alpha_dot, _ = follow_trajectory(time, a, jacobian, shape_to_draw)
        return alpha_dot

    t = [0, 1]
    a_start = np.array([0, np.pi / 4, -np.pi / 2])
    sol = solve_ivp(joint_velocity, t, a_start, t_eval=np.linspace(0, 1, 100))
    alpha = sol.y

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    link_colors = ['r', 'g', 'b']

    link_set, _, _, _, _, _, _, _ = threeD_robot_arm_links(link_vectors, a_start, joint_axes)

    l = threeD_draw_links(link_set, link_colors, ax)

    alpha_col = alpha.shape[1]
    p = np.zeros((3, alpha_col))
    link_end_set_with_base = []

    for i in range(alpha_col):
        _, _, _, _, _, link_end_base = threeD_robot_arm_endpoints(link_vectors, alpha[:, i], joint_axes)
        link_end_set_with_base.append(link_end_base)

        for j in range(alpha.shape[0]):
            p[j, i] = link_end_set_with_base[i][-1][j]

    l_trace, = ax.plot(p[0, :], p[1, :], p[2, :])

    ax.view_init(azim=-140, elev=20)

    ax.set_box_aspect([1, 1, 1])

    ax.set_autoscale_on(False)

    link_set_history = []
    for i in range(alpha_col):
        link_set, _, _, _, _, _, _, _ = threeD_robot_arm_links(link_vectors, alpha[:, i], joint_axes)
        l = threeD_update_links(l, link_set)
        plt.pause(0.01)
        link_set_history.append(link_set)

    plt.show()

    return (link_vectors,
            joint_axes,
            shape_to_draw,
            jacobian,
            joint_velocity,
            t,
            a_start,
            sol,
            alpha,
            ax,
            link_colors,
            link_set,
            l,
            p,
            l_trace,
            link_set_history)


if __name__ == "__main__":
    trace_circle()
