from __future__ import division, print_function

import pygame

from Level import Level
from rendering import Renderer, MapRenderer

class Game(object):
    def __init__(
        self,
        player_name='Player',
        level=None,
        renderer=None,
    ):
        self.player_name = player_name
        self.player_pos = (0, 0)
        self.player_dir = (0, 1)
        pygame.init()
        if level is None:
            self.level = self.generate_level()
        else:
            selv.level = level
        if renderer is not None:
            self.renderer = renderer

    def _move_player(self, vector):
        dx, dy = vector
        x, y = self.player_pos
        self.player_pos = (x + dx, y+dy)

    def generate_level(self):
        return Level()

    def main_loop(self):
        done = False
        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONUP:
                    print('hej')

            if hasattr(self, 'renderer'):
                self.renderer.render(self.level)
            clock.tick(60)
        
        pygame.quit()


if __name__ == '__main__':
    game = Game(renderer=MapRenderer())
    game.main_loop()
