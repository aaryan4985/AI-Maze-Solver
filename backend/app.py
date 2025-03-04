from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import random
from collections import deque
import heapq
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
socketio = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)

def generate_maze(rows=10, cols=10):
    logger.debug(f"Generating maze of size {rows}x{cols}")
    maze = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = 0  # Start point
    maze[rows-1][cols-1] = 0  # End point
    return maze

# HTTP route for maze generation
@app.route('/generate_maze', methods=['GET'])
def http_generate_maze():
    logger.info("HTTP maze generation requested")
    maze = generate_maze()
    return jsonify({'maze': maze})

# WebSocket event for maze generation
@socketio.on('generate_maze')
def handle_generate_maze():
    logger.info("WebSocket maze generation requested")
    maze = generate_maze()
    logger.debug(f"Generated maze: {maze}")
    emit('maze_generated', {'maze': maze})

# WebSocket event for maze solving
@socketio.on('solve_maze')
def handle_solve_maze(data):
    logger.info(f"Solving maze with algorithm: {data.get('algorithm', 'bfs')}")
    maze = data.get('maze', [])
    algorithm = data.get('algorithm', 'bfs')
    
    solution = []
    if algorithm == 'bfs':
        solution = bfs(maze)
    elif algorithm == 'dfs':
        solution = dfs(maze)
    elif algorithm == 'astar':
        solution = astar(maze)
    
    logger.debug(f"Solution found: {solution}")
    emit('maze_solved', {'solution': solution})

def bfs(maze):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(0, 0, [(0, 0)])])
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c, path = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited:
                queue.append((nr, nc, path + [(nr, nc)]))
                visited.add((nr, nc))
    return []

def dfs(maze):
    rows, cols = len(maze), len(maze[0])
    stack = [(0, 0, [(0, 0)])]
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while stack:
        r, c, path = stack.pop()
        if (r, c) == (rows - 1, cols - 1):
            return path
        if (r, c) not in visited:
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                    stack.append((nr, nc, path + [(nr, nc)]))
    return []

def astar(maze):
    rows, cols = len(maze), len(maze[0])
    start, end = (0, 0), (rows - 1, cols - 1)
    heap = [(0, start, [start])]
    visited = set()
    
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    while heap:
        cost, (r, c), path = heapq.heappop(heap)
        if (r, c) == end:
            return path
        if (r, c) not in visited:
            visited.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                    heapq.heappush(heap, (cost + 1 + heuristic((nr, nc), end), (nr, nc), path + [(nr, nc)]))
    return []

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)