import socket
from _thread import *
import pickle
import pygame


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
flagx=-1

def threaded_client(conn, player):
    global currentPlayer,flagx
    print("id of current player =",player)  #player holds the id of the current player
    print("CurrentPlayer",currentPlayer)
    # conn.send(pickle.dumps(str(pos[player])))
    reply = []
    flag=0
    flag1=0
    while True:
        try:
            # data = pickle.decode_long(conn.recv(2048))
            data = pickle.loads(conn.recv(2048))
            for u in range(len(reply)):
                if (flagx == reply[u]):
                    reply.pop(u)
                    reply.pop((u - 1))
                    flagx=-1

            if(data=="quit"):
                conn.send(pickle.dumps("Quitted"))
                currentPlayer-=1
                break

            if(data=="0" or data=="1" or data=="2" or data=="3"): #Data holds the ID of the player who is quitting
                print("ids.index(data)",ids.index(int(data)))
                indices.append(ids.index(int(data)))
                flagx=int(data)
                conn.send(pickle.dumps(reply))
                continue


            print("dataaaaa",data)
            if(data!="GameOver"):
                pos[player] = data

            if not data:
                print("Disconnected")
                break
            elif(data!="GameOver"):
                for i in range(len(ids)):
                    for j in range(len(indices)):
                        if(ids[i]==indices[j] or ids[i]==int(player)):
                            flag=1
                            break

                    if(flag==0 and i!=int(player)):
                        print("i=",i,"ids=",ids, "int player",int(player))
                        for k in range(len(reply)):
                            if(k%2==1 and i==reply[k]):
                                flag1=1
                                reply[k-1]=pos[i]
                                print("replyyyy men 3'er flag 1", reply)
                        if(flag1==0):
                            reply.append(pos[i]) #here reply holds the position of the cars that are in game excluding the current player
                            reply.append(i)
                            print("replyyyy b flag 1", reply)
                    flag=0
                    flag1=0


            print("Received: ", data)
            print("Sending : ", reply)
            print(pos)
            # if(data!="quit"):
            conn.sendall(pickle.dumps(reply))
            print("mirnaaaaaaaa")
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
        conn.send(pickle.dumps(indices))
        currentPlayer+=1
