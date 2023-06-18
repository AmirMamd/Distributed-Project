import socket
from _thread import *
import pickle
import pygame
import re
import concurrent.futures
from database_test import *
import threading
LISTENER_LIMIT = 4
active_clients = []  # List of all currently connected users
HOST = ""
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT=7777
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as e:
    str(e)

s.listen(LISTENER_LIMIT)
print("Waiting for a connection, Server Started")
pool = concurrent.futures.ThreadPoolExecutor(max_workers=1)
executor0 = concurrent.futures.ThreadPoolExecutor(max_workers=100)
executor1 = concurrent.futures.ThreadPoolExecutor(max_workers=100)
executor2 = concurrent.futures.ThreadPoolExecutor(max_workers=100)
executor3 = concurrent.futures.ThreadPoolExecutor(max_workers=100)
executors=[executor0,executor1,executor2,executor3]
users=[]
ips=[]
quitted=[]
scores=[0,0,0,0]
pos = [(1000*0.2,''),(1000*0.3,''),(1000*0.4,''),(1000*0.5,'')]
carImg = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car.png')
carImg1 = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car1.png')
carImg2 = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car2.png')
carImg3 = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car3.png')
Images=[".\\Car Racing Game using Pygame\\img\\car.png",".\\Car Racing Game using Pygame\\img\\car1.png",".\\Car Racing Game using Pygame\\img\\car2.png",".\\Car Racing Game using Pygame\\img\\car3.png"]
ids=[]
indices=[]
flagx=-1
counter=0
olduserflag=0


def threaded_client(conn, player):
    global currentPlayer,flagx,counter,pos ,user_id,user_name , user_position ,user_score,olduserflag

    reply = []
    flag=0
    flag1=0
    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            if(flagx!=-1):
                for u in range(len(reply)):
                    if (flagx == reply[u]):
                        reply.pop(u+1)
                        reply.pop(u)
                        reply.pop(u - 1)
                        counter+=1
                        if(counter==currentPlayer):
                            flagx=-1
                        conn.send(pickle.dumps(reply))
                        break

                conn.send(pickle.dumps(reply))

            if(data=="quit"):
                conn.send(pickle.dumps("Quitted"))
                currentPlayer-=1
                break

            if(data=="0" or data=="1" or data=="2" or data=="3"): #Data holds the ID of the player who is quitting
                indices.append(ids.index(int(data)))
                flagx=int(data)
                conn.send(pickle.dumps(reply))

                db = threading.Thread(target=DB,args=(data,  pos[player][1], scores[player], pos[player][0],1,None,0))

                db.start()
                continue

            s = re.split(r'[(,)]', str(data))
            if(data!="GameOver" and len(s)>1 and len(s)!=3  and data!="update db"):
                pos[player] = data

            if not data:
                print("Disconnected")
                break
            elif(data!="GameOver"):
                if(len(s)==1  and data!="update db"):
                    scores[player]=int(data)
                if (len(s) == 3  and data!="update db"):
                    if(olduserflag==1):
                        scores[user_id] = user_score
                        pos[user_id]=(user_position,user_name)
                        olduserflag=0
                    users.append(s[1])
                    pos[player]=(pos[player][0],s[1])
                for i in range(len(ids)):
                    for j in range(len(indices)):
                        if(ids[i]==indices[j] or ids[i]==int(player)):
                            flag=1
                            break

                    if(flag==0 and i!=int(player)):

                        for k in range(len(reply)):
                            if(k%3==1 and i==reply[k]):
                                flag1=1
                                reply[k-1]=pos[i]
                                reply[k+1]=scores[i]
                        if(flag1==0):
                            reply.append(pos[i]) #here reply holds the position of the cars that are in game excluding the current player
                            reply.append(i)
                            reply.append(scores[i])

                    if (data == "update db"):

                        executors[int(ids[player])].submit(DB,ids[player],  pos[player][1], scores[player], pos[player][0],0,indices,0)
                    flag=0
                    flag1=0



            conn.sendall(pickle.dumps(reply))


        except:
            address = re.split(r'[(,)]', str(addr))
            quitted.append((address[1],player,pos[player][1]))
            currentPlayer-=1
            break

    if(data!="GameOver"):
        conn.close()

currentPlayer=0
while True:
    flagg=0
    global user_id,user_name , user_position ,user_score
    conn, addr = s.accept()
    print("Connected to:", addr)
    address1 = re.split(r'[(,)]', str(addr))
    if address1[1] not in ips:
        ips.append(address1[1])
    if(currentPlayer < 4):
        for item in quitted:
            if item[0] in ips:
                result = pool.submit(DB, None, item[2], None, None, 2, None, 1)

                result1 = result.result()
                ids[item[1]] = item[1]
                if (result1 != None):
                    user_id =result1['_id']
                    user_name = result1['name']
                    user_position = result1['position']
                    user_score = result1['score']
                    olduserflag=1
                    conn.send(pickle.dumps((item[1],user_position,user_score)))
                flagg=1
                start_new_thread(threaded_client, (conn, item[1]))
                quitted.pop()
                break

        if(len(indices)>0):
            ids[indices[0]]=indices[0]
            conn.send(pickle.dumps(str(indices[0])))
            start_new_thread(threaded_client, (conn, indices[0]))
            indices.pop(0)
        elif(flagg==0):
            ids.append(currentPlayer)
            conn.send(pickle.dumps(str(currentPlayer)))
            start_new_thread(threaded_client, (conn, currentPlayer))
        conn.send(pickle.dumps(indices))
        currentPlayer+=1
        flagg=0