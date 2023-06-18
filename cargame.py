import time
import pygame
import re
import threading
import chat
from network import Network
import random
from time import sleep
import pygame_gui
import sys
from chat import ChatClientGUI
import tkinter as tk
# from database_test import Database
class CarRacing:
    def __init__(self):
        pygame.init()
        self.display_width = 1000
        self.display_height = 600
        self.black = (0, 0, 0)
        # Create an instance of ChatClientGUI
        # self.ScoreArray=[(0,''),(0,''),(0,''),(0,'')]
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None
        # self.WIDTH, self.HEIGHT = 1000, 600
        # self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # self.manager = pygame_gui.UIManager((1000, 600))
        #
        # self.text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((150, 275), (600, 50)),
        #                                                       manager=self.manager,
        #                                                       object_id='#main_text_entry')
        # # self.const=310
        # self.get_user_name(self.clock, self.manager, self.SCREEN, self.WIDTH, self.HEIGHT)
        self.initialize(0)

    def show_user_name(self,user_name,SCREEN,WIDTH,HEIGHT,clock):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            SCREEN.fill("white")

            new_text = pygame.font.SysFont("bahnschrift", 100).render(f"Hello, {user_name}", True, "black")
            new_text_rect = new_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            SCREEN.blit(new_text, new_text_rect)

            clock.tick(60)

            pygame.display.update()

            sleep(1)
            break
        #self.initialize(0)
    def get_user_name(self,clock,manager,SCREEN,WIDTH,HEIGHT):
        global n, user
        flag=0
        while True:

            UI_REFRESH_RATE = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                        event.ui_object_id == '#main_text_entry'):
                    user=event.text

                    self.show_user_name(event.text,SCREEN,WIDTH,HEIGHT,clock)
                    flag=1
                    break

                manager.process_events(event)

            manager.update(UI_REFRESH_RATE)

            SCREEN.fill("white")

            manager.draw_ui(SCREEN)

            # pygame.display.update()
            new_text = pygame.font.SysFont("bahnschrift", 50).render(f"Enter username", True, "black")
            new_text_rect = new_text.get_rect(center=(WIDTH / 4, HEIGHT / 4))
            SCREEN.blit(new_text, new_text_rect)
            # clock.tick(60)
            pygame.display.update()
            if(flag==1):
                break


    def initialize(self,x):
        global olduser, oldscore
        # pygame.display.update()
        pos1 = [(1000*0.2,600*0.8),(1000*0.3,600*0.8),(1000*0.4,600*0.8),(1000*0.5,600*0.8)]
        self.crashed = False
        if(x==0):
            global n, p1, x1, v,user
            n = Network()
            self.WIDTH, self.HEIGHT = 1000, 600
            self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            pygame.display.set_caption("car dodge")

            self.manager = pygame_gui.UIManager((1000, 600))

            self.text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((150, 275), (600, 50)),
                                                                  manager=self.manager,
                                                                  object_id='#main_text_entry')

            self.clock = pygame.time.Clock()
            self.get_user_name(self.clock, self.manager, self.SCREEN, self.WIDTH, self.HEIGHT)
            p2 = n.getP()
            print(p2)
            n.send("(" + user + ")")
            # p1=p2
            olduser=0
            if(p2!='0' and p2!='1' and p2!='2' and p2!='3'):
                # p2= re.split(r'[(,)]', p2)
                # print(p2[1])
                # n.send(pos1[int(p1)])
                print("bena3mel p2")
                p1=p2[0]
                oldscore=p2[2]
                x1 = p2[1]
                olduser=1

            else:
                p1=p2
                # n.send("(" + user + ")")
                n.send(pos1[int(p1)])
                x = str(pos1[int(p1)])
                s = re.split(r'[(,]', x)
                x1 = float(s[1])
            v=[]
            print("p11111", p1)
            # n.send("(" + user + ")")
            # n.send(pos1[int(p1)])
            # x=str(pos1[int(p1)])
            # s = re.split(r'[(,]', x)
            # x1=float(s[1])
        self.carImg = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car.png')
        self.carImg1 = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car1.png')
        self.carImg2 = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car2.png')
        self.carImg3 = pygame.image.load('.\\Car Racing Game using Pygame\\img\\car3.png')
        self.Images=[self.carImg,self.carImg1,self.carImg2,self.carImg3]

        self.car_x_coordinate = float(x1)
        self.car_y_coordinate = (self.display_height * 0.8)
        self.id=0
        self.car_width = 49

        # enemy_car
        self.enemy_car = pygame.image.load('.\\Car Racing Game using Pygame\\img\\enemy_car_1.png')
        self.enemy_car_startx = random.randrange(310, 450)
        self.enemy_car_starty = -600
        self.enemy_car_speed = 5
        self.enemy_car_width = 49
        self.enemy_car_height = 100

        # Background
        self.bgImg = pygame.image.load(".\\Car Racing Game using Pygame\\img\\back_ground.jpg")
        self.bg_x1 = (self.display_width /3) - (360/1.5)
        self.bg_x2 = (self.display_width / 3) - (360/1.5)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 3
        self.count = 0

    def car(self, car_x_coordinate, car_y_coordinate, id,a):
        global v,user
        print("kerkerker",user)
        print("car_x_coordinate",car_x_coordinate, "id",id)
        self.gameDisplay.blit(self.Images[int(id)], (car_x_coordinate, car_y_coordinate))
        for rep in range(len(v)):
            if(rep==a and a!=-1):
                print("gena hena awii", v)
                self.gameDisplay.blit(pygame.font.SysFont("arial", 20).render((str(v[rep][1])), True, self.white),(car_x_coordinate, car_y_coordinate + self.enemy_car_height))


        # self.gameDisplay.blit(pygame.font.SysFont("arial", 20).render(user), True, self.white), (0,countt))

    def racing_window(self,k):
        # Create a new thread for running the Tkinter GUI
        if(k==0):
            gui_thread = threading.Thread(target=self.rootStart).start()
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Car Dodge')
        self.run_car()

    def rootStart(self):
        root = tk.Tk()
        global user
        client_gui = ChatClientGUI(root)
        client_gui.Username(user)
        root.mainloop()

    def run_car(self):

        global v,user,gui_thread,olduser, oldscore
        # self.root.mainloop()
        # v = n.send((self.car_x_coordinate, self.car_y_coordinate))
        while not self.crashed:
            # root = tk.Tk()
            # client_gui = ChatClientGUI(root, user)
            # root.mainloop()
            v = n.send((self.car_x_coordinate, user))
            # n.send((self.car_x_coordinate, self.car_y_coordinate))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # print("p1=",p1)
                    # v = n.send((self.car_x_coordinate, self.car_y_coordinate))
                    n.send(str(p1))
                    n.send("quit")
                    self.crashed = True
                    # event_quit.set()
                    #
                    # sys.exit()




                if (event.type == pygame.KEYDOWN):
                    print("v=",v)
                    if (event.key == pygame.K_LEFT):
                        self.car_x_coordinate -= 50
                        v=n.send((self.car_x_coordinate, user))
                        print("aloooo vvvvv",v)
                        print ("CAR X COORDINATES: %s" % self.car_x_coordinate)
                    if (event.key == pygame.K_RIGHT):
                        self.car_x_coordinate += 50
                        v = n.send((self.car_x_coordinate, user))
                        print("aloooo vvvvv",v)
                        print ("CAR X COORDINATES: %s" % self.car_x_coordinate)
                    print ("x: {x}, y: {y}".format(x=self.car_x_coordinate, y=self.car_y_coordinate))
            self.gameDisplay.fill(self.black)
            self.back_ground_raod()

            self.run_enemy_car(self.enemy_car_startx, self.enemy_car_starty)
            self.enemy_car_starty += self.enemy_car_speed

            if self.enemy_car_starty > self.display_height:
                self.enemy_car_starty = 0 - self.enemy_car_height
                self.enemy_car_startx = random.randrange(310, 450)
            print("v fo2 5ales=", v)

            self.id = p1
            self.car(self.car_x_coordinate, self.car_y_coordinate, self.id,-1)
            self.gameDisplay.blit(pygame.font.SysFont("arial", 20).render((user), True, self.white), (self.car_x_coordinate,self.car_y_coordinate+self.enemy_car_height))


            for a in range(len(v)):
                if(a%3==0):
                    print("a=",a)
                    s = re.split(r'[(,)]', str(v[a]) )
                    print("V[x]=",v[a])
                    print("v[1]",v[1])
                    x1 = float(s[1])
                    print("x1=",x1)
                    self.id=(v[a+1])
                    self.car(x1, self.car_y_coordinate,self.id,a)

            if(olduser==1):
                self.count=self.count+oldscore
                # score=self.count+oldscore
                self.highscore(self.count)
                self.count += 1
                olduser=0
            else:
                self.highscore(self.count)
                self.count += 1
            if (self.count % 100 == 0):
                n.send(self.count)
                self.enemy_car_speed += 1
                self.bg_speed += 1
            if self.car_y_coordinate < self.enemy_car_starty + self.enemy_car_height:
                if self.car_x_coordinate > self.enemy_car_startx and self.car_x_coordinate < self.enemy_car_startx + self.enemy_car_width or self.car_x_coordinate + self.car_width > self.enemy_car_startx and self.car_x_coordinate + self.car_width < self.enemy_car_startx + self.enemy_car_width:
                    # self.crashed = True
                    n.send("GameOver")
                    self.display_message("Game Over !!!")


            if self.car_x_coordinate < 150 or self.car_x_coordinate > 550:
                # self.crashed = True
                n.send("GameOver")
                self.display_message("Game Over !!!")

            pygame.display.update()
            self.clock.tick(60)


    def display_message(self, msg):
        font = pygame.font.SysFont("comicsansms", 72, True)
        text = font.render(msg, True, (255, 255, 255))
        self.gameDisplay.blit(text, (400 - text.get_width() // 2, 240 - text.get_height() // 2))
        self.display_credit()
        pygame.display.update()
        self.clock.tick(60)
        sleep(1)
        car_racing.initialize(1)
        car_racing.racing_window(1)

    def back_ground_raod(self):
        self.gameDisplay.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        self.gameDisplay.blit(self.bgImg, (self.bg_x2, self.bg_y2))

        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.display_height:
            self.bg_y1 = -600

        if self.bg_y2 >= self.display_height:
            self.bg_y2 = -600

    def run_enemy_car(self, thingx, thingy):
        self.gameDisplay.blit(self.enemy_car, (thingx, thingy))

    def highscore(self, count):
        ScoreArray = [(0, ''), (0, ''), (0, ''), (0, '')]
        print("bos ba2a score array",ScoreArray)
        global v,user
        print("v gowa highscore=",v)
        font = pygame.font.SysFont("arial", 20)
        ScoreArray[0] = (int(count), str(user))
        # if (int(count) % 100 == 0 and count!=0):
        if (int(count) % 100 == 0):
            n.send("update db")
        # if (int(count) % 100 == 0):
        #     db = threading.Thread(target=Database, args=((self.car_x_coordinate, user, p1, int(count)), v))
        #     db.daemon = True
        #     db.start()
        #     del db
        # text = font.render("Score of player "+ user +": " + str(count), True, self.white)
        # self.gameDisplay.blit(text, (0, 0))
        p=0
        for l in range (len(v)):
            if (l % 3 == 0):
                p+=1
                ScoreArray[p] = (int(v[l + 2]), str(v[l][1]))
        print("ScoreArray",ScoreArray)


        sorted_array = sorted(ScoreArray, key=lambda x: x[0],reverse=True)
        print("sorted_array",sorted_array)

        # for x in range (len(sorted_array)):
        #     for b in range (len(v))

        countt = 0
        for rep in range(len(sorted_array)):
            if( str(sorted_array[rep][1])!=''):
                self.gameDisplay.blit(font.render("Score of player " + str(sorted_array[rep][1]) + ": " + str(sorted_array[rep][0]), True, self.white),(0, countt))
            countt += 20

    def display_credit(self):
        font = pygame.font.SysFont("lucidaconsole", 14)
        text = font.render("Thanks for playing!", True, self.white)
        self.gameDisplay.blit(text, (600, 520))

if __name__ == '__main__':
    car_racing = CarRacing()
    gameThread= threading.Thread(target=car_racing.racing_window(0)).start()
    # car_racing.racing_window()