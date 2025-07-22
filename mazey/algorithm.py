import pygame
import heapq
from mazey.constants import BLUE, YELLOW

class Dijkstra:
    def __init__(self, grid, start, end, draw_fn, win):
        self.grid = grid
        self.start = start
        self.end = end
        self.draw = draw_fn
        self.win = win

        # Distance from start to all cell as infinity
        self.distances = {cell : float('inf') for row in grid for cell in row}
        self.distances[start] = 0

        # For reconstructing the shortest path
        self.came_from = {}

        # Priority queue
        self.open_set = []

        # Tie breaker in heap to avoid comparing cells directly
        self.count = 0

        # Push start node into the PQ
        heapq.heappush(self.open_set, (0, self.count, start))
        self.visited = set()
    
    def run(self):
        while self.open_set:
            # pop cell with the lowest distance
            current = heapq.heappop(self.open_set)[2]

            if current in self.visited:
                continue
            self.visited.add(current)

            # if we reached end , reconstruct the path and stop
            if current == self.end:
                self.reconstruct_path()
                return True

            for neighbour in self.get_neighbours(current):
                temp_dist = self.distances[current] + 1
                if temp_dist < self.distances[neighbour]:
                    # update current distance if shorter
                    self.distances[neighbour] = temp_dist
                    self.came_from[neighbour] = current
                    self.count += 1
                    heapq.heappush(self.open_set, (temp_dist, self.count, neighbour))

            # set visited nodes as blue
            if current != self.start and current != self.end:
                current.color = BLUE
            
            self.draw(self.win, self.grid)
            pygame.time.wait(20)

        return False

    
    def reconstruct_path(self):
        # backtracking end to start 
        current = self.end
        shortest_path_length = []
        while current in self.came_from:
            current = self.came_from[current]
            if current != self.start:
                current.color = YELLOW # drawing shortest path
                shortest_path_length.append(current)
            self.draw(self.win, self.grid)
            pygame.time.wait(30)
        print(f"Shortest path length : {len(shortest_path_length)}")
    
    def get_neighbours(self, cell):
        neighbours = []
        row, col = cell.row, cell.col

        if row > 0 and not self.grid[row - 1][col].is_wall:
            # up
            neighbours.append(self.grid[row - 1][col])
        if row < len(self.grid) - 1 and not self.grid[row + 1][col].is_wall:
            # down
            neighbours.append(self.grid[row + 1][col])
        if col > 0 and not self.grid[row][col - 1].is_wall: 
            # left
            neighbours.append(self.grid[row][col - 1])
        if col < len(self.grid[0]) - 1 and not self.grid[row][col + 1].is_wall:
            # right
            neighbours.append(self.grid[row][col + 1])
        
        return neighbours