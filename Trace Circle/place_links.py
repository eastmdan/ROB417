import numpy as np
from copy import deepcopy


def place_links(links_in_world, link_end_set_with_base):
    """
    % Use the locations of the ends of a set of links to place the
    % start-and-end matrices for the links
    """
    link_set = deepcopy(links_in_world)
    for i, (world_link, link_end) in enumerate(zip(links_in_world, link_end_set_with_base)):
        link_set[i] = link_end + world_link
    return link_set


def test_place_links() -> None:
    links_in_world = [np.array(([0, 0], [0, 1])), np.array(([0, 2], [0, 1]))]
    link_end_set_with_base = [
        np.array(([0], [0])),
        np.array(([0], [1])),
        np.array(([2], [2])),
    ]

    link_set = place_links(links_in_world, link_end_set_with_base)
    for link in link_set:
        print(link)


if __name__ == "__main__":
    test_place_links()
