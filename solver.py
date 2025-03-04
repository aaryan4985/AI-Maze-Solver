from collections import deque
import heapq
import numpy as np

def bfs_solve_maze(maze, start, end):
    """Solves the maze using Breadth-First Search (BFS)."""
    rows, cols = maze.shape
    queue = deque([(start, [])])  # (current_position, path)
    visited = set()

    while queue:
        (r, c), path = queue.popleft()
        
        if (r, c) == end:
            return path + [(r, c)]  # Return full path
        
        if (r, c) in visited:
            continue
        visited.add((r, c))

        # Explore neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr, nc] == 0:
                queue.append(((nr, nc), path + [(r, c)]))

    return None  # No path found

def heuristic(a, b):
    """Heuristic function for A* (Manhattan Distance)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_solve_maze(maze, start, end):
    """Solves the maze using A* algorithm."""
    rows, cols = maze.shape
    open_set = [(0, start, [])]  # (cost, current_position, path)
    heapq.heapify(open_set)
    visited = set()
    g_costs = {start: 0}  # Cost from start node

    while open_set:
        _, (r, c), path = heapq.heappop(open_set)

        if (r, c) == end:
            return path + [(r, c)]  # Return full path

        if (r, c) in visited:
            continue
        visited.add((r, c))

        # Explore neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr, nc] == 0:
                new_g = g_costs[(r, c)] + 1
                if (nr, nc) not in g_costs or new_g < g_costs[(nr, nc)]:
                    g_costs[(nr, nc)] = new_g
                    f_cost = new_g + heuristic((nr, nc), end)
                    heapq.heappush(open_set, (f_cost, (nr, nc), path + [(r, c)]))

    return None  # No path found
