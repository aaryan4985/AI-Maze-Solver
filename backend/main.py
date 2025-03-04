import argparse
from maze import create_maze
from solver import bfs_solve_maze, astar_solve_maze
from visualize import draw_maze

def main(rows, cols, algorithm):
    """
    Main function to run the maze solver with chosen parameters.
    """
    start, end = (1, 1), (rows - 2, cols - 2)
    maze = create_maze(rows, cols)

    if algorithm == "bfs":
        solution_path = bfs_solve_maze(maze, start, end)
        algo_used = "BFS"
    elif algorithm == "astar":
        solution_path = astar_solve_maze(maze, start, end)
        algo_used = "A*"
    else:
        print("❌ Invalid algorithm choice! Defaulting to BFS.")
        solution_path = bfs_solve_maze(maze, start, end)
        algo_used = "BFS"

    if solution_path:
        print(f"\n✅ Solution Found using {algo_used}: {solution_path}")
        draw_maze(maze, solution_path, start, end)
    else:
        print("\n❌ No Path Found!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Maze Solver with BFS or A*")
    parser.add_argument("--rows", type=int, default=5, help="Number of rows in the maze")
    parser.add_argument("--cols", type=int, default=5, help="Number of columns in the maze")
    parser.add_argument("--algorithm", choices=["bfs", "astar"], default="bfs", help="Maze solving algorithm")

    args = parser.parse_args()
    main(args.rows, args.cols, args.algorithm)
