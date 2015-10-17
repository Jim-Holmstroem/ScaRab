from __future__ import division, print_function

import pygame

from Level import Level
from rendering import Renderer

class Game(object):
    def __init__(
        self,
        player_name='Player',
        level=None,
        render=False,
    ):
        self.player_name = player_name
        pygame.init()
        if level is None:
            self.level = self.generate_level()
        else:
            selv.level = level
        if render:
            self.renderer = Renderer()

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
                self.renderer.render()
            clock.tick(60)
        
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.main_loop()
