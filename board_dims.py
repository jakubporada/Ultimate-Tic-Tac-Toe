from const import *

class BoardDims:

    def __init__(self, size, xcor, ycor):
        self.size = size
        self.sqsize = size // ROWS
        self.xcor = xcor
        self.ycor = ycor