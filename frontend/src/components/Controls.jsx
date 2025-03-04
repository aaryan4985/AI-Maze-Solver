import React from 'react';

const Controls = ({ 
  algorithm, 
  setAlgorithm, 
  generateMaze, 
  solveMaze, 
  mazeGenerated,
  isLoading
}) => {
  const algorithms = ['bfs', 'dfs', 'astar'];

  return (
    <div className="flex flex-col sm:flex-row space-y-2 sm:space-y-0 space-x-0 sm:space-x-4 mb-4">
      <select 
        value={algorithm}
        onChange={(e) => setAlgorithm(e.target.value)}
        className="px-2 py-1 border rounded w-full sm:w-auto"
        disabled={isLoading}
      >
        {algorithms.map((algo) => (
          <option key={algo} value={algo}>
            {algo.toUpperCase()}
          </option>
        ))}
      </select>

      <button 
        onClick={generateMaze}
        disabled={isLoading}
        className={`w-full sm:w-auto px-4 py-2 rounded ${
          isLoading 
            ? 'bg-gray-300 text-gray-500 cursor-not-allowed' 
            : 'bg-blue-500 text-white hover:bg-blue-600'
        }`}
      >
        {isLoading ? 'Generating...' : 'Generate Maze'}
      </button>

      <button 
        onClick={solveMaze}
        disabled={!mazeGenerated || isLoading}
        className={`w-full sm:w-auto px-4 py-2 rounded ${
          mazeGenerated && !isLoading
            ? 'bg-green-500 text-white hover:bg-green-600' 
            : 'bg-gray-300 text-gray-500 cursor-not-allowed'
        }`}
      >
        {isLoading ? 'Solving...' : 'Solve Maze'}
      </button>
    </div>
  );
};

export default Controls;