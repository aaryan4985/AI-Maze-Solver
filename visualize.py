import matplotlib.pyplot as plt
import numpy as np
import time

def draw_maze(maze, path=None, start=None, end=None, delay=0.2):
    rows, cols = maze.shape
    fig, ax = plt.subplots(figsize=(cols, rows))  # Adjust figure size based on maze dimensions

    # Define colors
    cmap = {0: "white", 1: "black"}  # Open paths = white, Walls = black
    path_color = "red"
    start_color = "green"
    end_color = "blue"

    # Draw initial maze
    ax.clear()
    for r in range(rows):
        for c in range(cols):
            color = cmap[maze[r, c]]
            ax.add_patch(plt.Rectangle((c, rows - r - 1), 1, 1, color=color))

    if start:
        ax.add_patch(plt.Rectangle((start[1], rows - start[0] - 1), 1, 1, color=start_color, alpha=0.7))
    if end:
        ax.add_patch(plt.Rectangle((end[1], rows - end[0] - 1), 1, 1, color=end_color, alpha=0.7))

    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim([0, cols])
    ax.set_ylim([0, rows])

    plt.ion()  # Turn on interactive mode for animation
    plt.show()

    # Animate the path
    if path:
        for (r, c) in path:
            ax.add_patch(plt.Circle((c + 0.5, rows - r - 1 + 0.5), 0.3, color=path_color))  # Moving dot
            plt.pause(delay)  # Pause for animation effect

    plt.ioff()  # Turn off interactive mode
    plt.show()
