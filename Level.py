from __future__ import division, print_function

import numpy as np
import random
from rendering import Renderer

class Node(object):
    def __init__(self, color=Renderer.BLACK):
        self.color = color
        self.openings = {}

    def __repr__(self):
        return 'node'

#    def __repr__(self):
#        if len(self.openings) == 0:
#            repr_string = 'empty'
#        else:
#            vectors = self.openings.keys()
#            repr_string = str(vectors)
#        return repr_string

class Level(object):
    def __init__(self):
        self.nodes = np.array([[Node(),Node(Renderer.WHITE)],[Node(),Node()]])
        self._make_connections()
    
    def make_random_connection(self,node):
    wall_directions = node.walls.keys()
    random.shuffle(wall_directions)
    for dir in wall_directions:
        if not node.walls[dir].openings:
            make_pairwise_connection(node.coord,node.walls[dir].coord)
            make_random_connection(node.neighbors[dir])

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


    def display_level(self):
        print(self.nodes)
