from __future__ import division, print_function

import numpy as np
import random
from rendering import Renderer


class Node(object):
    def __init__(self, color=Renderer.BLACK, coords=(None, None)):
        self.color = color
        self.openings = {}
        self.walls = {}
        self.coords = coords

    def __repr__(self):
        arrows = {(1, 0): "v", (-1, 0): "^", (0, 1): ">", (0, -1): "<"}
        repr_string = "N({})".format("".join([arrows[opening] for opening in self.openings.keys()]))
        return repr_string


class Level(object):
    def __init__(self, size=(2, 2)):
        self.nodes = np.empty(size, dtype=object)
        for index, _ in np.ndenumerate(self.nodes):
            self.nodes[index] = Node(coords=index)
        self._set_inner_walls()
        self._make_random_connections(self.nodes[(0, 0)])
    
    def _set_inner_walls(self):
        for index, node in np.ndenumerate(self.nodes):
            array_index = np.array(index)
            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if all(array_index+direction <= (0, 0)) and all(array_index+direction < self.nodes.shape):
                    neighbor_index = tuple(array_index+direction)
                    node.walls[direction] = self.nodes[neighbor_index]
    
    def _make_random_connections(self, node):
        wall_directions = node.walls.keys()
        random.shuffle(wall_directions)
        for direction in wall_directions:
            if not node.walls[direction].openings:
                self._make_pairwise_connection(node.coord, node.walls[direction].coord)
                self._make_random_connections(node.neighbors[direction])

    def _make_connections(self):
        self._make_pairwise_connection(
            (0, 1),
            (1, 1)
        )
        self._make_pairwise_connection(
            (0, 0),
            (0, 1)
        )
        self._make_pairwise_connection(
            (1, 0),
            (1, 1)
        )

    def _make_pairwise_connection(
        self,
        coord1,
        coord2
    ):
        node1 = self.nodes[coord1]
        node2 = self.nodes[coord2]
        vector = tuple(np.array(coord1) - np.array(coord2))
        neg_vector = tuple(np.array(coord2) - np.array(coord1))

        node1.openings[neg_vector] = node2
        node2.openings[vector] = node1
        del node1.walls[neg_vector]
        del node2.walls[vector]

    def display_level(self):
        print(self.nodes)
