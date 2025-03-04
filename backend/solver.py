#backend\solver.py
from collections import deque
import heapq

def bfs_solve_maze(maze, start, end, emit=None):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set()
    came_from = {}
    
    while queue:
        current = queue.popleft()
        if current == end:
            break

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited:
                queue.append((nr, nc))
                visited.add((nr, nc))
                came_from[(nr, nc)] = current
                if emit:
                    emit("maze_step", {"cell": (nr, nc)}, broadcast=True)

    path = []
    curr = end
    while curr in came_from:
        path.append(curr)
        curr = came_from[curr]
    return path[::-1]

def dfs_solve_maze(maze, start, end, emit=None):
    rows, cols = len(maze), len(maze[0])
    stack = [start]
    visited = set()
    came_from = {}

    while stack:
        current = stack.pop()
        if current == end:
            break

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited:
                stack.append((nr, nc))
                visited.add((nr, nc))
                came_from[(nr, nc)] = current
                if emit:
                    emit("maze_step", {"cell": (nr, nc)}, broadcast=True)

    path = []
    curr = end
    while curr in came_from:
        path.append(curr)
        curr = came_from[curr]
    return path[::-1]

def astar_solve_maze(maze, start, end, emit=None):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: abs(start[0] - end[0]) + abs(start[1] - end[1])}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            break

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                tentative_g = g_score[current] + 1
                if (nr, nc) not in g_score or tentative_g < g_score[(nr, nc)]:
                    came_from[(nr, nc)] = current
                    g_score[(nr, nc)] = tentative_g
                    f_score[(nr, nc)] = tentative_g + abs(nr - end[0]) + abs(nc - end[1])
                    heapq.heappush(open_set, (f_score[(nr, nc)], (nr, nc)))
                    if emit:
                        emit("maze_step", {"cell": (nr, nc)}, broadcast=True)

    path = []
    curr = end
    while curr in came_from:
        path.append(curr)
        curr = came_from[curr]
    return path[::-1]
