from __future__ import division, print_function

import numpy as np

from abc import ABCMeta, abstractmethod

import pygame


class Renderer(object):
    __metaclass__ = ABCMeta

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    def __init__(self):
        size = (700, 600)  # Could be calculated from board size
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('ScaRab')

    @abstractmethod
    def render(self, level):
        pass


class PlayerViewRenderer(Renderer):
    def render(self, level):
        self.screen.fill(self.RED)
        pygame.display.flip()


class MapRenderer(Renderer):
    def render(self, level):
        node_width=40
        self.screen.fill(self.WHITE)
        pygame.draw.lines(
            self.screen,
            self.BLACK,
            True,
            [(40,40),
             (node_width*level.size[0]+40,40),
             (node_width*level.size[0]+40, node_width*level.size[1]+40),
             (40,node_width*level.size[1]+40)
             ],
            10
        )
        for (y, x), node in np.ndenumerate(level.nodes):
            print(node.walls.keys())
            for direction in node.walls.keys():
                if direction == (1, 0):
                    start_pos = (x, y+1)
                    end_pos = (x+1, y+1)
                elif direction == (-1, 0):
                    start_pos = (x, y)
                    end_pos = (x+1, y)
                elif direction == (0, 1):
                    start_pos = (x+1, y)
                    end_pos = (x+1, y+1)
                elif direction == (0, -1):
                    start_pos = (x, y)
                    end_pos = (x, y+1)
                start_pix = tuple(40+node_width * np.array(start_pos))
                end_pix = tuple(40+node_width * np.array(end_pos))
                print(start_pix,end_pix)
                pygame.draw.line(
                    self.screen,
                    self.BLACK,
                    start_pix,
                    end_pix,
                    10
                )
        pygame.display.flip()
