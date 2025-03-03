import numpy as np

def create_maze():
    maze = np.array([
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ])
    return maze

if __name__ == "__main__":
    maze = create_maze()
    print(maze)
