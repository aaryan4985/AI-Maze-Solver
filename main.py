import argparse
from maze import create_maze
from solver import bfs_solve_maze, astar_solve_maze
from visualize import draw_maze

def main(rows, cols, algorithm):
    start = (1, 1)
    end = (rows - 2, cols - 2)

    maze = create_maze(rows, cols)

    if algorithm == "bfs":
        solution_path = bfs_solve_maze(maze, start, end)
    elif algorithm == "astar":
        solution_path = astar_solve_maze(maze, start, end)
    else:
        raise ValueError("Invalid algorithm! Choose 'bfs' or 'astar'.")

    print("Solution Path:", solution_path)
    draw_maze(maze, solution_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=5, help="Number of rows in the maze")
    parser.add_argument("--cols", type=int, default=5, help="Number of columns in the maze")
    parser.add_argument("--algorithm", type=str, default="bfs", choices=["bfs", "astar"], help="Algorithm to solve the maze")

    args = parser.parse_args()
    main(args.rows, args.cols, args.algorithm)
