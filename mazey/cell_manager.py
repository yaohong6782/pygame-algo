from mazey.constants import CELL_SIZE, WHITE, GREY, BLACK, GREEN,  RED
import pygame

class Cell:
    def __init__(self,row, col):
        self.row =  row
        self.col = col
        self.x = col * CELL_SIZE
        self.y = row * CELL_SIZE
        self.color = WHITE
        self.is_wall = False
        self.is_start = False
        self.is_end = False

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, CELL_SIZE, CELL_SIZE))

    def make_start(self):
        self.color = GREEN
        self.is_start = True
    
    def make_end(self):
        self.color = RED
        self.is_end = True

    def make_wall(self):
        if not self.is_start and not self.is_end:
            self.color = BLACK
            self.is_wall = True
    
    def reset(self):
        self.color = WHITE
        self.is_wall = False
        self.is_start = False
        self.is_end = False