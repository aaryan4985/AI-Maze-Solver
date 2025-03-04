import matplotlib.pyplot as plt
import numpy as np

def draw_maze(maze, path=None):
    """Visualizes the maze with walls, a solution path, and start/end markers."""
    rows, cols = maze.shape
    fig, ax = plt.subplots(figsize=(cols, rows))

    # Draw walls and open paths
    for r in range(rows):
        for c in range(cols):
            color = "black" if maze[r, c] == 1 else "white"
            ax.add_patch(plt.Rectangle((c, rows - r - 1), 1, 1, color=color, edgecolor="gray"))

    # Draw solution path if available
    if path:
        for (r, c) in path:
            ax.add_patch(plt.Rectangle((c + 0.2, rows - r - 1 + 0.2), 0.6, 0.6, color="red"))

        # Mark start and end points
        start, end = path[0], path[-1]
        ax.add_patch(plt.Circle((start[1] + 0.5, rows - start[0] - 0.5), 0.3, color="green", label="Start"))
        ax.add_patch(plt.Circle((end[1] + 0.5, rows - end[0] - 0.5), 0.3, color="blue", label="End"))

    # Formatting
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect("equal")

    # Legend
    plt.legend(["Start", "End", "Path"], loc="upper right")

    plt.show()
