import numpy as np

def create_maze(rows=5, cols=5):
    """
    Creates a random maze with given dimensions.
    0 = Open path, 1 = Wall
    Ensures start (1,1) and end (rows-2, cols-2) are open.
    """
    maze = np.random.choice([0, 1], size=(rows, cols), p=[0.7, 0.3])  # 70% open paths, 30% walls

    # Ensure borders are walls
    maze[0, :] = maze[-1, :] = 1
    maze[:, 0] = maze[:, -1] = 1

    # Ensure start and end are open
    start, end = (1, 1), (rows - 2, cols - 2)
    maze[start] = maze[end] = 0

    return maze
