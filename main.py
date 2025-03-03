from maze import create_maze
from solver import bfs_solve_maze
from visualize import draw_maze

# Define start and end points
start = (1, 1)
end = (3, 3)

# Create the maze
maze = create_maze()

# Solve the maze
solution_path = bfs_solve_maze(maze, start, end)
print("Solution Path:", solution_path)

# Visualize the maze with solution
draw_maze(maze, solution_path)
