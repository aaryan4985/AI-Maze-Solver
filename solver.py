from collections import deque

def bfs_solve_maze(maze, start, end):
    rows, cols = maze.shape
    queue = deque([(*start, [])])  # (row, col, path)
    visited = set()

    while queue:
        r, c, path = queue.popleft()
        
        if (r, c) == end:
            return path + [(r, c)]  # Return full path
        
        if (r, c) in visited:
            continue
        visited.add((r, c))

        # Explore all 4 possible directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr, nc] == 0:
                queue.append((nr, nc, path + [(r, c)]))

    return None  # No path found
