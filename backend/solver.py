from collections import deque
import heapq
import time

def bfs_solve_maze(maze, start, end, socketio=None):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = set([start])
    path_steps = []

    while queue:
        current, path = queue.popleft()
        
        if current == end:
            return path

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + dr, current[1] + dc
            
            if (0 <= nr < rows and 0 <= nc < cols and 
                maze[nr][nc] == 0 and (nr, nc) not in visited):
                new_path = path + [(nr, nc)]
                queue.append(((nr, nc), new_path))
                visited.add((nr, nc))
                
                # Emit step if socketio is provided
                if socketio:
                    socketio.emit('maze_solving_step', {'step': (nr, nc)})
                    time.sleep(0.1)  # Add a small delay to visualize steps

    return []

def dfs_solve_maze(maze, start, end, socketio=None):
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set([start])

    while stack:
        current, path = stack.pop()
        
        if current == end:
            return path

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + dr, current[1] + dc
            
            if (0 <= nr < rows and 0 <= nc < cols and 
                maze[nr][nc] == 0 and (nr, nc) not in visited):
                new_path = path + [(nr, nc)]
                stack.append(((nr, nc), new_path))
                visited.add((nr, nc))
                
                # Emit step if socketio is provided
                if socketio:
                    socketio.emit('maze_solving_step', {'step': (nr, nc)})
                    time.sleep(0.1)  # Add a small delay to visualize steps

    return []

def astar_solve_maze(maze, start, end, socketio=None):
    rows, cols = len(maze), len(maze[0])
    
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    open_set = [(0, start, [start])]
    visited = set([start])

    while open_set:
        _, current, path = heapq.heappop(open_set)
        
        if current == end:
            return path

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + dr, current[1] + dc
            
            if (0 <= nr < rows and 0 <= nc < cols and 
                maze[nr][nc] == 0 and (nr, nc) not in visited):
                
                new_path = path + [(nr, nc)]
                priority = len(new_path) + heuristic((nr, nc), end)
                
                heapq.heappush(open_set, (priority, (nr, nc), new_path))
                visited.add((nr, nc))
                
                # Emit step if socketio is provided
                if socketio:
                    socketio.emit('maze_solving_step', {'step': (nr, nc)})
                    time.sleep(0.1)  # Add a small delay to visualize steps

    return []