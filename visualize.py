import matplotlib.pyplot as plt

def draw_maze(maze, path=None):
    rows, cols = maze.shape
    fig, ax = plt.subplots(figsize=(5, 5))

    # Draw walls
    for r in range(rows):
        for c in range(cols):
            if maze[r, c] == 1:
                ax.add_patch(plt.Rectangle((c, rows - r - 1), 1, 1, color="black"))

    # Draw path if available
    if path:
        for (r, c) in path:
            ax.add_patch(plt.Rectangle((c + 0.2, rows - r - 1 + 0.2), 0.6, 0.6, color="red"))

    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()
