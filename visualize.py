import matplotlib.pyplot as plt
import numpy as np

def draw_maze(maze, path=None, start=None, end=None):
    rows, cols = maze.shape
    fig, ax = plt.subplots(figsize=(cols, rows))  # Adjust figure size based on maze dimensions

    # Define colors
    cmap = {0: "white", 1: "black"}  # Open paths = white, Walls = black
    path_color = "red"
    start_color = "green"
    end_color = "blue"

    # Draw maze
    for r in range(rows):
        for c in range(cols):
            color = cmap[maze[r, c]]
            ax.add_patch(plt.Rectangle((c, rows - r - 1), 1, 1, color=color))

    # Draw path
    if path:
        for (r, c) in path:
            ax.add_patch(plt.Rectangle((c + 0.25, rows - r - 1 + 0.25), 0.5, 0.5, color=path_color))

    # Draw start and end points
    if start:
        ax.add_patch(plt.Rectangle((start[1], rows - start[0] - 1), 1, 1, color=start_color, alpha=0.7))
    if end:
        ax.add_patch(plt.Rectangle((end[1], rows - end[0] - 1), 1, 1, color=end_color, alpha=0.7))

    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim([0, cols])
    ax.set_ylim([0, rows])

    plt.show()
