const http = require('http');
const express = require('express');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

const reviews = [];

io.on('connection', (socket) => {
  // Handle incoming review data from React Native app
  socket.on('submitReview', (data) => {
    reviews.push(data);
    // Log the received review to the server console
    console.log('Received Review:', data);

    // Broadcast the updated review list to all connected clients
    io.emit('updatedReviews', reviews);
  });
});

server.listen(3000, () => {
  console.log('WebSocket server is running on port 3000');
});
