# mazey/grid_manager.py
import pygame
from mazey.constants import CELL_SIZE, WHITE, GREY, BLACK, ROWS, WIDTH
from mazey.cell_manager import Cell

class Grid:
    def __init__(self):
        self.grid = self.make_grid()

    def make_grid(self):
        grid = []
        for row in range(ROWS):
            grid.append([])
            for col in range(ROWS):
                cell = Cell(row, col)
                grid[row].append(cell)
        return grid
    
    def draw_grid_lines(self, win):
        for i in range(ROWS):
            pygame.draw.line(win, GREY, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))
            pygame.draw.line(win, GREY, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH))
    
    def draw(self, win, grid):
        win.fill(WHITE)
        for row in grid:
            for cell in row:
                cell.draw(win)
        
        self.draw_grid_lines(win)
        pygame.display.update()