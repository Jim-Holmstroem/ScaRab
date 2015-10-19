from __future__ import division, print_function

import numpy as np
import random
from rendering import Renderer

class Node(object):
    def __init__(self, color=Renderer.BLACK):
        self.color = color
        self.openings = {}
        self.walls = {}

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
    
    def set_inner_walls(self):
        for index,node in np.ndenumerate(self.nodes):
            array_index=np.array(index)
            for direction in [(1,0),(-1,0),(0,1),(0,-1)]:
                if all(array_index+direction<=(0,0)) and all(array_index+direction<self.nodes.shape):
                    neighbor_index = tuple(array_index+direction)
                    node.walls[direction]=self.nodes[neighbor_index]
    
    def make_random_connection(self,node):
        wall_directions = node.walls.keys()
        random.shuffle(wall_directions)
        for direction in wall_directions:
            if not node.walls[direction].openings:
                make_pairwise_connection(node.coord,node.walls[direction].coord)
                make_random_connection(node.neighbors[direction])

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
