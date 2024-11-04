import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy


def draw_vectors_at_point(p, v, ax):
    """
    % Draw the columns of V as arrows based at point p, in axis ax
    """
    for i in range(len(v)):
        ax.quiver(p[0], p[1], p[2], v[i][0], v[i][1], v[i][2], arrow_length_ratio=0.1)


def test_draw_vectors_at_point():
    p = np.array(([1], [1], [1]))
    v = [np.array(([1], [0], [0])),
         np.array(([0], [1], [0])),
         np.array(([0], [0], [1]))]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([0.8, 2.2])
    ax.set_ylim([0.8, 2.2])
    ax.set_zlim([0.8, 2.2])
    draw_vectors_at_point(p, v, ax)
    plt.show()


if __name__ == "__main__":
    test_draw_vectors_at_point()



"""
function q = draw_vectors_at_point(p,V,ax)
% Draw the columns of V as arrows based at point p, in axis ax
%
% Inputs:
%
%   p: a 3x1 vector designating the location of the vectors
%   V: a 3xn matrix, each column of which is a 3x1 vector that should be
%       drawn at point p
%   ax: the axis in which to draw the vectors
%
% Output:
%
%   q: a cell array of handles to the quiver objects for the drawn arrows

    % First use hold(ax,'on') so that when we call quiver, it does not
    % delete the plot
    hold(ax, 'on');

    % Now create an empty cell array named 'q' with one row and as many columns as V
    [~, column] = size(V);
    q = cell(1, column);

    % Loop over the columns of V

        % Use quiver3 to plot an arrow at p, with vector components taken
        % as the first three rows of the (idx)th column of V. Store the
        % output as the (idx)th element of q
    for i = 1:column
        q{i} = quiver3(ax, p(1), p(2), p(3), V(1,i), V(2, i), V(3,i));
    end



    % Use hold(ax,'off') to return the axis to its normal behavior
    hold(ax,'off');

end
"""