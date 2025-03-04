import React, { useState, useEffect } from "react";
import io from "socket.io-client";
import MazeGrid from "./components/MazeGrid";
import Controls from "./components/Controls";

function App() {
  const [maze, setMaze] = useState(null);
  const [solution, setSolution] = useState(null);
  const [solvingSteps, setSolvingSteps] = useState([]);
  const [algorithm, setAlgorithm] = useState("astar");
  const [socket, setSocket] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Setup socket connection
    const newSocket = io("http://localhost:5000");
    setSocket(newSocket);

    // Socket event listeners
    newSocket.on("connect", () => {
      console.log("Connected to WebSocket server");
    });

    newSocket.on("maze_generated", (data) => {
      console.log("Maze generated via WebSocket:", data);

      // If data is an object with a 'maze' property, extract it
      const mazeData = Array.isArray(data)
        ? data
        : data.maze && Array.isArray(data.maze)
        ? data.maze
        : data;

      console.log("Processed maze data:", mazeData);

      setMaze(mazeData);
      setSolvingSteps([]);
      setIsLoading(false);
    });

    // Add listener for solving steps
    newSocket.on("maze_solving_step", (data) => {
      console.log("Maze solving step:", data.step);
      setSolvingSteps((prevSteps) => {
        // Avoid duplicate steps
        const stepExists = prevSteps.some(
          (step) => step[0] === data.step[0] && step[1] === data.step[1]
        );
        return stepExists ? prevSteps : [...prevSteps, data.step];
      });
    });

    newSocket.on("maze_solved", (data) => {
      console.log("Maze solved via WebSocket:", data);
      setSolution(data);
      setIsLoading(false);
    });

    newSocket.on("error", (errorMsg) => {
      console.error("Socket error:", errorMsg);
      setError(errorMsg);
      setIsLoading(false);
    });

    // Cleanup socket on component unmount
    return () => newSocket.disconnect();
  }, []);

  const generateMaze = () => {
    if (socket) {
      console.log("Generating maze...");
      setIsLoading(true);
      setMaze(null);
      setSolution(null);
      setSolvingSteps([]);
      socket.emit("generate_maze");
    }
  };

  const solveMaze = () => {
    if (socket && maze) {
      console.log(`Solving maze with algorithm: ${algorithm}`);
      setIsLoading(true);
      setSolvingSteps([]);
      socket.emit("solve_maze", {
        maze: maze,
        algorithm: algorithm,
      });
    }
  };

  return (
    <div className="container mx-auto p-4 max-w-xl">
      <h1 className="text-2xl font-bold mb-4 text-center">AI Maze Solver</h1>

      <Controls
        algorithm={algorithm}
        setAlgorithm={setAlgorithm}
        generateMaze={generateMaze}
        solveMaze={solveMaze}
        mazeGenerated={!!maze}
        isLoading={isLoading}
      />

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative">
          {error}
        </div>
      )}

      {maze && (
        <div className="mt-4 flex justify-center">
          <MazeGrid
            maze={maze}
            solution={solution}
            solvingSteps={solvingSteps}
          />
        </div>
      )}
    </div>
  );
}

export default App;
