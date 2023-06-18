import socket
import threading
import pickle

LISTENER_LIMIT = 4
HOST = "127.0.0.1"
chat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# PORT=8000
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Bind the server socket to a specific address and port
# server_socket.bind((HOST, PORT))
#
#
# # Listen for incoming connections
# server_socket.listen(2)
# server_socket.close()
# chat_socket.connect((HOST, 8000))
# # Send data to the target server
# message = "Hello from Server 2!"
# chat_socket.send(message.encode())
# PORT = int(chat_socket.recv(4096).decode())
PORT=6666
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((HOST, PORT))
except socket.error as e:
    str(e)

s.listen(LISTENER_LIMIT)


# Connect to the target server


# while True:
    # Accept a client connection
    # client_socket, addr = server_socket.accept()
    # print("Accepted connection from", addr[0] + ":" + str(addr[1]))
    #
    # # Receive data from the client
    # data = client_socket.recv(4096).decode()
    # print("dataaaa", data)
    # if data == "Hello from Server 1!":
    #     print("[Received from Client Server]:", data)
    #     client_socket.send("3000".encode())
# chat_socket.close()


print("Waiting for a connection, Server Started")

server_socket = None
clients = []
chat_room = "Chat Room"

def threaded_client(conn, currentplayer):
    clients.append(conn)
    username=conn.recv(1024).decode("utf-8")

    # data = s.recv(4096).decode()
    # if(data=="username"):
    #     flag=1

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
            # currentplayer-=1
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
    # client_socket, addr = server_socket.accept()
    print("Accepted connection from", addr[0] + ":" + str(addr[1]))
    # Receive data from the client
    # data = client_socket.recv(4096).decode()
    # print("dataaaa", data)
    # if currentPlayer < 4:
    threading.Thread(target=threaded_client, args=(conn, currentPlayer)).start()
        # currentPlayer += 1
    # client_socket.send("3000".encode())
    # if data == "Hello from Server 1!":
    #     print("[Received from Client Server]:", data)

    # if currentPlayer < 4:
    #     threading.Thread(target=threaded_client, args=(conn, currentPlayer)).start()
    #     currentPlayer += 1