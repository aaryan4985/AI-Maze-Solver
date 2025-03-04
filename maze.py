import numpy as np
import random

def create_maze(rows=5, cols=5):
    # Initialize maze with walls (1)
    maze = np.ones((rows, cols), dtype=int)

    # Create a simple randomized path
    def carve_path(r, c):
        maze[r, c] = 0  # Mark as open path
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dr, dc in directions:
            nr, nc = r + dr * 2, c + dc * 2
            if 1 <= nr < rows - 1 and 1 <= nc < cols - 1 and maze[nr, nc] == 1:
                maze[r + dr, c + dc] = 0  # Carve adjacent path
                carve_path(nr, nc)

    # Start carving from (1,1)
    carve_path(1, 1)
    
    # Ensure start and end are open
    maze[1, 1] = 0
    maze[rows - 2, cols - 2] = 0
    
    return maze

if __name__ == "__main__":
    maze = create_maze(7, 7)
    print(maze)
