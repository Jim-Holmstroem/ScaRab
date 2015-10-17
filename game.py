from __future__ import division, print_function

import pygame

from rendering import Renderer

class Game(object):
    def __init__(
        self,
        player_name='Player'
    ):
        self.player_name = player_name
        pygame.init()
        self.renderer = Renderer()

    def main_loop(self):
        done = False
        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONUP:
                    print('hej')

            self.renderer.render()
            clock.tick(60)
        
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.main_loop()
