from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import numpy as np
from solver import bfs_solve_maze, dfs_solve_maze, astar_solve_maze

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def create_maze(rows=10, cols=10):
    maze = np.ones((rows, cols), dtype=int)
    maze[1:-1, 1:-1] = np.random.choice([0, 1], size=(rows-2, cols-2), p=[0.7, 0.3])
    maze[1, 1] = 0
    maze[-2, -2] = 0
    return maze.tolist()

@app.route("/generate_maze", methods=["GET"])
def generate_maze():
    rows = int(request.args.get("rows", 10))
    cols = int(request.args.get("cols", 10))
    maze = create_maze(rows, cols)
    return jsonify({"maze": maze})

@socketio.on("solve_maze")
def solve_maze(data):
    maze = np.array(data["maze"])
    algorithm = data["algorithm"]
    start, end = (1, 1), (maze.shape[0] - 2, maze.shape[1] - 2)
    
    solver = {
        "bfs": bfs_solve_maze,
        "dfs": dfs_solve_maze,
        "astar": astar_solve_maze
    }.get(algorithm, bfs_solve_maze)
    
    for step in solver(maze, start, end, emit):
        socketio.sleep(0.1)
    
    emit("solution_complete")

if __name__ == "__main__":
    socketio.run(app, debug=True)
