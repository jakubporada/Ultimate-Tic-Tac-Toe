import pygame

from const import *
from board_dims import BoardDims

class Board:

    def __init__(self, dims=None, linewidth=15, ultimate=False, max = False):
        self.squares = [ [0, 0, 0] for row in range(ROWS)]
        self.dims = dims

        if not dims:
            self.dims = BoardDims(WIDTH, 0, 0)

        self.linewidth = linewidth
        self.max = max
        
        if ultimate:
            self.create_ultimate()

    def render(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                sqr = self.squares[row][col]
        
        #vertical lines
        pygame.draw.line(surface, LINE_COLOR, (self.dims.sqsize + self.dims.sqsize, self.dims.ycor), (self.dims.sqsize + self.dims.sqsize, self.dims.size), self.linewidth)
        pygame.draw.line(surface, LINE_COLOR, (self.dims.size - self.dims.sqsize, self.dims.ycor), (self.dims.size - self.dims.sqsize, self.dims.size), self.linewidth)

        # horizontal lines
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor, self.dims.sqsize), (self.dims.size, self.dims.sqsize), self.linewidth)
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor, self.dims.size - self.dims.sqsize), (self.dims.size, self.dims.size - self.dims.sqsize), self.linewidth)

    def create_ultimate(self):
        for row in range(ROWS):
            for col in range(COLS):

                size = self.dims.sqsize
                xcor, ycor = self.dims.xcor + (col * self.dims.sqsize), self.dims.ycor + (row * self.dims.sqsize)
                dims = BoardDims(size = size, xcor=xcor, ycor=ycor)
                linewidth = self.linewidth - 7
                ultimate = self.max

                self.squares[row][col] = Board(dims = dims, linewidth = linewidth, ultimate = ultimate, max=False)