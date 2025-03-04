import React from 'react';

const MazeGrid = ({ maze, solution, solvingSteps }) => {
  // Check if maze is an array
  if (!maze || !Array.isArray(maze)) {
    return <div>Invalid maze data</div>;
  }

  return (
    <div className="flex flex-col border border-gray-300">
      {maze.map((row, rowIndex) => (
        <div key={rowIndex} className="flex">
          {row.map((cell, colIndex) => {
            // Determine cell color based on cell value and state
            let cellClass = "w-6 h-6 border border-gray-300";

            if (cell === 1) {
              // Wall
              cellClass += " bg-black";
            } else {
              // Open path
              cellClass += " bg-white";
            }

            // Highlight start and end points
            if (rowIndex === 0 && colIndex === 0) {
              cellClass += " bg-green-600";
            }
            if (rowIndex === maze.length - 1 && colIndex === maze[0].length - 1) {
              cellClass += " bg-red-600";
            }

            // Highlight solving steps
            if (solvingSteps && solvingSteps.some(
              ([y, x]) => y === rowIndex && x === colIndex
            )) {
              cellClass += " bg-blue-300";
            }

            // Highlight solution path
            if (solution && solution.solution && solution.solution.some(
              ([y, x]) => y === rowIndex && x === colIndex
            )) {
              cellClass += " bg-green-500";
            }

            return (
              <div 
                key={`${rowIndex}-${colIndex}`}
                className={cellClass}
              />
            );
          })}
        </div>
      ))}
    </div>
  );
};

export default MazeGrid;