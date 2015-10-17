from __future__ import division, print_function
import numpy as np

class Node(object):
    def __init__(self):
        self.openings = []

    def __repr__(self):
        if len(self.openings) == 0:
            repr_string = 'empty'
        else:
            vectors = zip(*self.openings)[1]
            repr_string = str(vectors)
        return repr_string

class Level(object):
    def __init__(self):
        self.nodes = np.array([[Node(),Node()],[Node(),Node()]])
        self._make_connections()

    def _make_connections(self):
        self._make_pairwise_connection(
            (0, 1),
            (1, 1)
        )

    def _make_pairwise_connection(
        self,
        coord1,
        coord2
    ):
        node1 = self.nodes[coord1]
        node2 = self.nodes[coord2]
        vector = np.array(coord1) - np.array(coord2)

        node1.openings.append((node2, -vector))
        node2.openings.append((node1, vector))
        import ipdb; ipdb.set_trace()

    def display_level(self):
        print(self.nodes)
