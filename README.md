# Distributed-Project
This project is to make a cars game with database replicas and a chatting feature enabling multiple users to play the game remotely.

Here's a sample `README` file for the provided code:

# Car Racing Game Server

This is a server implementation for a car racing game. It handles multiple client connections using socket programming and supports concurrent gameplay for up to four players.

## Prerequisites

- Python 3.x
- `pygame` library
- `pymongo` library
- `database_test` module

## Usage

1. Ensure that all the prerequisites are installed.
2. Run the `car_racing_game_server.py` script to start the server.
3. The server will listen for client connections on a specified host and port.
4. Players can connect to the server using the appropriate client implementation.
5. The server handles the gameplay logic, including tracking positions, scores, and managing database operations.

## Server Architecture

The server code is divided into several sections:

1. Importing necessary modules: The required modules and libraries are imported, including `socket`, `time`, `_thread`, `pickle`, `pygame`, `re`, `concurrent.futures`, `pymongo`, `database_test`, and `threading`.
2. Server configuration: The server's settings are defined, such as the listener limit, active clients list, host, and port number.
3. Socket setup: The server socket is created and bound to the specified host and port.
4. Listening for connections: The server enters a loop and waits for incoming client connections.
5. Handling client connections: When a client connects, a new thread is created to handle the client's requests and responses concurrently.
6. Gameplay logic: The server receives data from the clients, updates the game state, handles quitted players, and communicates with the database for score updates.
7. Database operations: The server manages interactions with the MongoDB database, such as updating player scores and positions.
8. Main execution: The server continuously listens for connections and starts a new thread for each client.

## Multiplayer Gameplay

- The server supports up to four players.
- Each player connects to the server using the appropriate client implementation.
- Players control cars in a racing game.
- The server manages player positions, scores, and updates the database accordingly.
- Players can quit the game, and their progress will be saved.
- The server sends data to clients about the positions and scores of other players.

## Credits

- This server implementation was created by [Your Name].

Feel free to modify the `README` file to include additional information or customize it according to your needs.

##Drive Link
https://drive.google.com/file/d/1COaFhwmEf8t02h4h63n2Am18yxnvugAl/view?usp=drive_link
