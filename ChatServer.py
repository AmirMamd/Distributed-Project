import socket
import threading
import pickle

LISTENER_LIMIT = 4
HOST = "127.0.0.1"
chat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# PORT=6666

PORT = 7777


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((HOST, PORT))
except socket.error as e:
    str(e)

s.listen(LISTENER_LIMIT)




print("Waiting for a connection, Server Started")

server_socket = None
clients = []
chat_room = "Chat Room"

def threaded_client(conn, currentplayer):
    clients.append(conn)
    username=conn.recv(1024).decode("utf-8")

    conn.sendall(username.encode())

    send_message(conn, f"Welcome to the {chat_room}, {username}!")

    while True:
        try:
            message = conn.recv(1024).decode("utf-8")
            if message:
                print(f"Received message from {username}: {message}")
                broadcast_message(f"{username}: {message}", sender_socket=conn)
            else:
                clients.remove(conn)
                conn.close()
                # currentplayer-=1
                broadcast_message(f"{username} has left the {chat_room}")
                break
        except ConnectionResetError:
            clients.remove(conn)
            conn.close()
            broadcast_message(f"{username} has left the {chat_room}")
            break

def broadcast_message(message, sender_socket=None):
    for client in clients:
        client.sendall(message.encode())

def send_message(client_socket, message):
    client_socket.sendall(message.encode())

currentPlayer = 0
while True:

    conn, addr = s.accept()
    print("Connected to:", addr)
    print("Accepted connection from", addr[0] + ":" + str(addr[1]))
    threading.Thread(target=threaded_client, args=(conn, currentPlayer)).start()
