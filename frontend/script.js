// script.js

// Connect to the Socket.io server
const socket = io('http://localhost:5000'); // Replace with your backend URL

// Get HTML elements
const playButton = document.getElementById('play-button');
const pauseButton = document.getElementById('pause-button');
const prevButton = document.getElementById('prev-button');
const nextButton = document.getElementById('next-button');
const thumbnail = document.getElementById('thumbnail');

// Event listeners
playButton.addEventListener('click', () => {
    // Emit play song event
    socket.emit('play_song', { query: 'your_song_query' }); // Replace with actual song query
});

pauseButton.addEventListener('click', () => {
    // Emit pause song event
    socket.emit('pause_song');
});

prevButton.addEventListener('click', () => {
    // Emit previous song event
    socket.emit('previous_song');
});

nextButton.addEventListener('click', () => {
    // Emit next song event
    socket.emit('next_song');
});

// Listen for song updates
socket.on('song_update', (data) => {
    // Update the thumbnail and song information
    document.getElementById('song-title').textContent = data.title;
    document.getElementById('song-artist').textContent = data.artist;
    thumbnail.src = data.thumbnail;
});
