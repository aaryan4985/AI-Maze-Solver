import React, { useState, useEffect } from "react";
import socket from "./socket";

const SocketProvider = ({ children }) => {
  const [isConnected, setIsConnected] = useState(false);

  useEffect(() => {
    socket.on('connect', () => {
      setIsConnected(true);
      console.log('Connected to WebSocket');
    });

    socket.on('connect_error', (error) => {
      setIsConnected(false);
      console.error('Connection Error:', error);
    });

    socket.on('disconnect', () => {
      setIsConnected(false);
      console.log('Disconnected from WebSocket');
    });

    return () => {
      socket.off('connect');
      socket.off('connect_error');
      socket.off('disconnect');
    };
  }, []);

  if (!isConnected) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-900 text-white">
        Connecting to server...
      </div>
    );
  }

  return children;
};

export default SocketProvider;