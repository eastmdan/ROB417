import numpy as np


def build_links(link_vectors):
    """
    % Take a set of link vectors and augment each with a zero vector representing
    % the base of the link
    """

    link_set = []
    for link in link_vectors:
        #print(link)
        row = np.hstack((np.zeros(link.size).reshape(-1, 1), link))
        link_set.append(row)
    return link_set


def test_links():
    link_vectors = [
        np.array((1, 0)).reshape((-1, 1)),
        np.array((0, 1)).reshape((-1, 1)),
        np.array((0, 2, 1)).reshape((-1, 1)),
    ]
    link_vectors_2 = [np.array(([1], [0])), np.array(([1], [0])), np.array(([0], [2], [1]))]
    link_set = build_links(link_vectors)
    for link in link_set:
        print(link)


if __name__ == "__main__":
    test_links()
