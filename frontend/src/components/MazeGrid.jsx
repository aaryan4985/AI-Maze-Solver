import React from 'react';

const MazeGrid = ({ maze, solution }) => {
  // Check if maze is an array
  if (!maze || !Array.isArray(maze)) {
    return <div>Invalid maze data</div>;
  }

  return (
    <div className="flex flex-col border border-gray-300">
      {maze.map((row, rowIndex) => (
        <div key={rowIndex} className="flex">
          {row.map((cell, colIndex) => {
            // Determine cell color based on cell value
            const cellColor = cell === 1 
              ? 'bg-black' // Wall
              : 'bg-white'; // Path

            // Check if cell is part of solution path
            const isSolutionPath = solution && solution.path && solution.path.some(
              ([y, x]) => y === rowIndex && x === colIndex
            );

            return (
              <div 
                key={`${rowIndex}-${colIndex}`}
                className={`w-6 h-6 border border-gray-300 
                  ${cellColor} 
                  ${isSolutionPath ? 'bg-green-500 bg-opacity-50' : ''}`}
              />
            );
          })}
        </div>
      ))}
    </div>
  );
};

export default MazeGrid;