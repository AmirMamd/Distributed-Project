import socket
from _thread import *
from player import Player
import pickle
import pygame
import threading


LISTENER_LIMIT = 4
active_clients = []  # List of all currently connected users
HOST = "127.0.0.1"
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as e:
    str(e)

s.listen(LISTENER_LIMIT)
print("Waiting for a connection, Server Started")


pos = [(1000*0.2,600*0.8),(1000*0.3,600*0.8),(1000*0.4,600*0.8),(1000*0.5,600*0.8)]
carImg = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car.png')
carImg1 = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car1.png')
carImg2 = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car2.png')
carImg3 = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car3.png')
Images=[".\\Car Racing Game using Pygame\\img\\car.png",".\\Car Racing Game using Pygame\\img\\car1.png",".\\Car Racing Game using Pygame\\img\\car2.png",".\\Car Racing Game using Pygame\\img\\car3.png"]
ids=[]
indices=[]

def threaded_client(conn, player):
    global currentPlayer
    print("id of current player =",player)  #player holds the id of the current player
    print("CurrentPlayer",currentPlayer)
    conn.send(pickle.dumps(str(pos[player])))
    reply = ""
    while True:
        try:
            # data = pickle.decode_long(conn.recv(2048))
            data = pickle.loads(conn.recv(2048))
            if(data=="quit"):
                print("da5al fel quit")
                currentPlayer-=1
                break

            # if(data=="GameOver"):
            #     continue

            if(data=="0" or data=="1" or data=="2" or data=="3"): #Data holds the ID of the player who is quitting
                print("ids.index(data)",ids.index(int(data)))
                indices.append(ids.index(int(data)))
                continue


            print("dataaaaa",data)
            if(data!="GameOver"):
                pos[player] = data

            if not data:
                print("Disconnected")
                break
            elif(data!="GameOver"):
                if player == 0:
                    reply = pos[ids[0]]
                    print("reply 0",reply)
                elif(player==1):
                    reply = pos[ids[1]]
                    print("reply 1", reply)
                elif(player==2):
                    reply = pos[ids[2]]
                    print("reply 2", reply)
                else:
                    reply = pos[ids[3]]
                    print("reply", reply)

            print("Received: ", data)
            print("Sending : ", reply)
            print(pos)
            conn.sendall(pickle.dumps(reply))
        except:
            print("da5al fel except")
            break

    if(data!="GameOver"):
        print(currentPlayer,"currentPlayer")
        print("Lost connection")
        conn.close()

currentPlayer=0
while True:

    conn, addr = s.accept()
    print("Connected to:", addr)
    if(currentPlayer < 4):
        print(" abl el if   indices[0]",indices,"ids",ids)
        if(len(indices)>0):
            print("indices[0]", indices[0], "indices=",indices)
            ids[indices[0]]=indices[0]
            conn.send(pickle.dumps(str(indices[0])))
            start_new_thread(threaded_client, (conn, indices[0]))
            indices.pop(0)
            print("indices[0]", indices, "ids=", ids)
        else:
            ids.append(currentPlayer)
            conn.send(pickle.dumps(str(currentPlayer)))
            start_new_thread(threaded_client, (conn, currentPlayer))
            print("ids be current player 3ady")
        currentPlayer += 1

