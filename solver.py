from collections import deque
import heapq
import numpy as np

def bfs_solve_maze(maze, start, end):
    """
    Solves the maze using Breadth-First Search (BFS).
    Returns the shortest path from start to end, or None if no path exists.
    """
    rows, cols = maze.shape
    queue = deque([(start, [])])  # (current position, path taken)
    visited = set()

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == end:
            return path + [(r, c)]  # Return completed path

        if (r, c) in visited:
            continue
        visited.add((r, c))

        # Possible moves: Up, Down, Left, Right
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr, nc] == 0:
                queue.append(((nr, nc), path + [(r, c)]))

    return None  # No valid path found

def heuristic(a, b):
    """ Heuristic function for A* (Manhattan distance). """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_solve_maze(maze, start, end):
    """
    Solves the maze using the A* (A-star) algorithm.
    Returns the shortest path from start to end, or None if no path exists.
    """
    rows, cols = maze.shape
    open_set = [(0, start, [])]  # (cost, position, path)
    heapq.heapify(open_set)
    visited = set()

    while open_set:
        cost, (r, c), path = heapq.heappop(open_set)

        if (r, c) == end:
            return path + [(r, c)]  # Return full path

        if (r, c) in visited:
            continue
        visited.add((r, c))

        # Possible moves: Up, Down, Left, Right
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr, nc] == 0:
                new_cost = cost + 1 + heuristic((nr, nc), end)
                heapq.heappush(open_set, (new_cost, (nr, nc), path + [(r, c)]))

    return None  # No valid path found
