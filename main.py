import pygame
import sys

from const import *
from game import Game

class Main:

    def __init__(self):
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        self.screen.fill(BG_COLOR)
        pygame.display.set_caption("ULTIMATE TIC TAC TOE")
        self.game = Game(ultimate=True, max=False)

    def mainloop(self):

        screen = self.screen
        game = self.game
        game.render_board(screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.mainloop()