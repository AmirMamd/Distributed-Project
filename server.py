import socket
from _thread import *
from player import Player
import pickle
import pygame
import threading


LISTENER_LIMIT = 5
active_clients = []  # List of all currently connected users
HOST = "127.0.0.1"
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as e:
    str(e)

s.listen(4)
print("Waiting for a connection, Server Started")


pos = [(1000*0.45,600*0.8),(1000*0.5,600*0.8),(1000*0.55,600*0.8),(1000*0.6,600*0.8)]
carImg = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car.png')
carImg1 = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car1.png')
carImg2 = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car2.png')
carImg3 = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car3.png')
Images=[".\\Car Racing Game using Pygame\\img\\car.png",".\\Car Racing Game using Pygame\\img\\car1.png",".\\Car Racing Game using Pygame\\img\\car2.png",".\\Car Racing Game using Pygame\\img\\car3.png"]


def threaded_client(conn, player):
    global currentPlayer
    print("player",player)
    print("CurrentPlayer",currentPlayer)
    conn.send(pickle.dumps(str(pos[player])))
    reply = ""
    while True:
        try:
            # data = pickle.decode_long(conn.recv(2048))
            data = pickle.loads(conn.recv(2048))
            print("dataaaaa",data)
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                print("elseeee")
                if player == 0:
                    reply = pos[0]
                    print("reply 0",reply)
                elif(player==1):
                    reply = pos[1]
                    print("reply 1", reply)
                elif(player==2):
                    reply = pos[2]
                    print("reply 2", reply)
                else:
                    reply = pos[3]
                    print("reply", reply)

            print("Received: ", data)
            print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            print("")
            break

    print("Lost connection")
    conn.close()

currentPlayer=0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    if(currentPlayer < 4):
        start_new_thread(threaded_client, (conn, currentPlayer))
        currentPlayer += 1

