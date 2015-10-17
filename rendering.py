from __future__ import division, print_function

import pygame

class Renderer(object):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    def __init__(self):
        size = (700, 600)  # Could be calculated from board size
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('ScaRab')

    def render(self):
        self.screen.fill(self.RED)
        pygame.display.flip()
