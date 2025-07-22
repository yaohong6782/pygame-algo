# mazey/main.py
import pygame
import sys

from mazey.grid_manager import Grid
from mazey.constants import WIDTH, CELL_SIZE, ROWS, WINDOW_HEIGHT
from mazey.algorithm import Dijkstra

def get_clicked_pos(pos):
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col

def draw_legend(win):
    font = pygame.font.SysFont("arial", 20)
    instructions  = [
        "Left Click: Draw Wall",
        "Right Click: Set Start/End",
        "S: Start Dijkstra",
        "C: Clear Grid"
    ]
    for i, text in enumerate(instructions):
        label = font.render(text, True, (255, 255, 255))
        win.blit(label, (10, WIDTH + 10 + i * 22))  # Adjust vertical spacing

def main():
    print("Game starting")
    pygame.init()

    WIN = pygame.display.set_mode((WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Mazey - Maze Solver")

    grid_obj = Grid()

    start_cell = None
    end_cell = None

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # Left click - add wall
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)
                cell = grid_obj.grid[row][col]
                if not cell.is_start and not cell.is_end:
                    cell.make_wall()

            if pygame.mouse.get_pressed()[2]:  # Right click - remove wall
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)
                cell = grid_obj.grid[row][col]

                if start_cell is None and not cell.is_end:
                    cell.make_start()
                    start_cell = cell
                elif end_cell is None and not cell.is_start:
                    cell.make_end()
                    end_cell = cell
                elif cell == start_cell:
                    cell.reset()
                    start_cell = None
                elif cell == end_cell:
                    cell.reset()
                    end_cell = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s  and start_cell and end_cell:
                    print("Starting Dijkstra")
                    algo  = Dijkstra(grid_obj.grid, start_cell, end_cell, grid_obj.draw, WIN)
                    algo.run()

                if event.key == pygame.K_c:
                    print("Clearing board")
                    start_cell = None
                    end_cell = None
                    grid_obj = Grid()
                    grid = grid_obj.grid
        
        WIN.fill((0,0,0))
        grid_obj.draw(WIN, grid_obj.grid)
        draw_legend(WIN)
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()