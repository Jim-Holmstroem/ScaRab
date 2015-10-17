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
        draw_indices = np.array([
            [(200, 200), (300, 200)],
            [(200, 300), (300, 300)]
        ])
        self.screen.fill(self.RED)
        for (x, y), node in np.ndenumerate(level.nodes):
            for dx, dy in node.openings.keys():
                pygame.draw.line(
                    self.screen,
                    self.BLACK,
                    draw_indices[x][y],
                    draw_indices[x+dx][y+dy],
                    10
                )
            pygame.draw.circle(
                self.screen,
                node.color,
                draw_indices[x][y],
                15
            )

        pygame.display.flip()
