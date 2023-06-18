import socket
import time
from _thread import *
import pickle
import pygame
import re
import concurrent.futures
from pymongo import MongoClient
from database_test import *
import threading
LISTENER_LIMIT = 4
active_clients = []  # List of all currently connected users
HOST = ""
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT=3030
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
# LostConnectionUsers=[]
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
            print("dataaaaaa",data)
            print("player=", int(player))

            if(flagx!=-1):
                for u in range(len(reply)):
                    if (flagx == reply[u]):
                        print("replyyy foooooo2 abl el pop", reply)
                        reply.pop(u+1)
                        reply.pop(u)
                        reply.pop(u - 1)
                        counter+=1
                        if(counter==currentPlayer):
                            flagx=-1
                        conn.send(pickle.dumps(reply))
                        print("replyyy foooooo2",reply)
                        break

                conn.send(pickle.dumps(reply))

            if(data=="quit"):
                print("quitttt")
                conn.send(pickle.dumps("Quitted"))
                currentPlayer-=1
                break

            if(data=="0" or data=="1" or data=="2" or data=="3"): #Data holds the ID of the player who is quitting
                print("ids.index(data)",ids.index(int(data)))
                indices.append(ids.index(int(data)))
                flagx=int(data)
                conn.send(pickle.dumps(reply))
                print("----------------------------------------------")
                # print(ids)
                # print(users)
                # print(scores)
                # print(ids[player], users[player], scores[player], pos[player][0], 0)
                # dead=False

                db = threading.Thread(target=DB,args=(data,  pos[player][1], scores[player], pos[player][0],1,None,0))

                # db = threading.Thread(target=DB,args=(data,  pos[player][1], scores[player], pos[player][0],1))

                print("player deleted =", pos[player][1])
                print("count threads", threading.active_count())
                db.start()

                # del db
                # users.pop(int(data))
                continue

            print("dataaaaa",data)
            s = re.split(r'[(,)]', str(data))
            if(data!="GameOver" and len(s)>1 and len(s)!=3  and data!="update db"):
                pos[player] = data

            if not data:
                print("Disconnected")
                break
            elif(data!="GameOver"):
                if(len(s)==1  and data!="update db"):
                    scores[player]=int(data)
                    print("scores=",scores)
                if (len(s) == 3  and data!="update db"):
                    if(olduserflag==1):
                        scores[user_id] = user_score
                        pos[user_id]=(user_position,user_name)
                        print("scores====", scores)
                        print("ids====", ids)
                        print("poss====", pos)
                        olduserflag=0
                    # if s[1] in LostConnectionUsers:
                    # result = pool.submit(DB,ids[player], s[1], scores[player], pos[player][0], 2,None,1)
                    # # LostConnectionUsers.pop(s[1])
                    # # print("lost conn", LostConnectionUsers)
                    # print("++++++++++++++++++++++++++++++++++++++++")
                    # print("result =",result.result())
                    # result1=result.result()
                    # if(result1!=None):
                    #     # user = {'_id': 0, 'name': 'j', 'position': 200.0, 'score': 2700}
                    #     print("da5al")
                    #     user_id = result1['_id']
                    #     user_name = result1['name']
                    #     user_position = result1['position']
                    #     user_score = result1['score']
                        # ids[quitted[0]] = quitted[0]
                        # quitted.pop(0)
                        # ids.pop(player)
                    # currentPlayer-=1
                    # scores[user_id]=user_score


                    # pos[user_id]=(user_position,user_name)
                    # print("aaa")
                    # print("scores====",scores)
                    # print("ids====", ids)
                    # print("poss====", pos)
                        # ids[player]=user_id
                        #law el user kan mawgod update el pos bel score we position we kol 7aga haterga3 men el database
                        # client_socket.send(s[1].encode())

                    users.append(s[1])
                    pos[player]=(pos[player][0],s[1])
                    print("users=", users)
                    print("possss",pos)
                for i in range(len(ids)):
                    for j in range(len(indices)):
                        if(ids[i]==indices[j] or ids[i]==int(player)):
                            flag=1
                            break

                    if(flag==0 and i!=int(player)):
                        print("i=",i,"ids=",ids, "int player",int(player))
                        for k in range(len(reply)):
                            if(k%3==1 and i==reply[k]):
                                flag1=1
                                reply[k-1]=pos[i]
                                reply[k+1]=scores[i]
                                print("replyyyy men 3'er flag 1", reply)
                        if(flag1==0):
                            reply.append(pos[i]) #here reply holds the position of the cars that are in game excluding the current player
                            reply.append(i)
                            reply.append(scores[i])

                            print("replyyyy b flag 1", reply)
                    # if(data == "update db"):
                    #     print("ray7en ne update aho")
                    #     # time.sleep(1)
                    #     # Database(ids[i], users[i], scores[i], pos[i][0])
                    #     db = threading.Thread(target=Database, args=((ids[i], users[i], scores[i], pos[i][0])))
                    #     db.start()
                    #     # del db
                    #     # conn.send(pickle.dumps(reply))
                    #     del db
                    if (data == "update db"):
                        print("ray7en ne update aho")
                        # time.sleep(1)
                        # Database(ids[i], users[i], scores[i], pos[i][0])
                        print("----------------------------------------------")
                        # print(ids)
                        # print(users)
                        # print(scores)
                        # print("player=",player)
                        # print(ids[player], users[player], scores[player], pos[player][0],0)
                        # dead=False
                        # db = threading.Thread(target=DB, args=(ids[player],  pos[player][1], scores[player], pos[player][0],0)).start()

                        executors[int(ids[player])].submit(DB,ids[player],  pos[player][1], scores[player], pos[player][0],0,indices,0)
                        # print("player=", pos[player][1])
                        print("count threads", threading.active_count())
                        # if(threading.active_count()>150):
                        #     # print(threading.current_thread())
                        #     print("walaaaa")
                        #     # ExFlag = True
                        #     # for exe in range(len(executors)):
                        #     executors[int(ids[player])].shutdown()
                        #     executors[int(ids[player])] = concurrent.futures.ThreadPoolExecutor(max_workers=100)
                        # # if(ExFlag):

                        # executors[int(ids[player])].submit(DB,ids[player],  pos[player][1], scores[player], pos[player][0],0)
                        # print("player=", pos[player][1])
                        # print("count threads", threading.active_count())
                        # if(threading.active_count()>150):
                        #     # print(threading.current_thread())
                        #     print("walaaaa")
                        #     # ExFlag = True
                        #     # for exe in range(len(executors)):
                        #     executors[int(ids[player])].shutdown()
                        #     executors[int(ids[player])] = concurrent.futures.ThreadPoolExecutor(max_workers=100)
                        # if(ExFlag):

                        #     executor = concurrent.futures.ThreadPoolExecutor(max_workers=100)

                        # db.start()
                        # del db
                        # conn.send(pickle.dumps(reply))
                        # del db
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
            address = re.split(r'[(,)]', str(addr))
            print("address", address[1])
            quitted.append((address[1],player,pos[player][1]))
            print("quitted=",quitted)
            # LostConnectionUsers.append(pos[player][1])
            currentPlayer-=1
            break

    if(data!="GameOver"):
        print(currentPlayer,"currentPlayer")
        print("Lost connection")
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
    # print("address", address[2])
    if(currentPlayer < 4):
        print(" abl el if   indices[0]",indices,"ids",ids)
        for item in quitted:
            if item[0] in ips:
                print("item0 and item 1",item[0],item[1],item[2])
                # result = pool.submit(DB, int(ids[item[1]]), None,  None, None, 2, None, 1)
                result = pool.submit(DB, None, item[2], None, None, 2, None, 1)

                result1 = result.result()

                print("resulttt=",result1)
                ids[item[1]] = item[1]
                if (result1 != None):
                    # user = {'_id': 0, 'name': 'j', 'position': 200.0, 'score': 2700}
                    print("da5 al")
                    user_id =result1['_id']
                    user_name = result1['name']
                    user_position = result1['position']
                    user_score = result1['score']
                    olduserflag=1
                    conn.send(pickle.dumps((item[1],user_position,user_score)))
                print("afashna el 5arag")
                flagg=1
                start_new_thread(threaded_client, (conn, item[1]))
                quitted.pop()
                break

        if(len(indices)>0):
            print("indices[0]", indices[0], "indices=",indices)
            ids[indices[0]]=indices[0]
            conn.send(pickle.dumps(str(indices[0])))
            start_new_thread(threaded_client, (conn, indices[0]))
            indices.pop(0)
            print("indices[0]", indices, "ids=", ids)
        elif(flagg==0):
            ids.append(currentPlayer)
            conn.send(pickle.dumps(str(currentPlayer)))
            start_new_thread(threaded_client, (conn, currentPlayer))
            print("ids be current player 3ady")
        conn.send(pickle.dumps(indices))
        currentPlayer+=1
        flagg=0