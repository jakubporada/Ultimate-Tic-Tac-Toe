from board import Board

class Game:

    def __init__(self, ultimate=False, max=False):
        self.board = Board(ultimate=ultimate, max=max)

    def render_board(self, surface):
        self.board.render(surface)