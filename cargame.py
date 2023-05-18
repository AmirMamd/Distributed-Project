import pygame
import re
from network import Network
import random
from time import sleep



class CarRacing:
    def __init__(self):
        pygame.init()
        self.display_width = 1000
        self.display_height = 600
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None
        # self.const=310
        self.initialize(0)

    def initialize(self,x):
        pos1 = [(1000*0.2,600*0.8),(1000*0.3,600*0.8),(1000*0.4,600*0.8),(1000*0.5,600*0.8)]
        self.crashed = False
        if(x==0):
            global n,p1,x1,v
            n = Network()
            p1 = n.getP()
            v=[]
            print("p11111", p1)
            n.send(pos1[int(p1)])
            x=str(pos1[int(p1)])
            s = re.split(r'[(,]', x)
            x1=float(s[1])

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

    def car(self, car_x_coordinate, car_y_coordinate, id):
        print("car_x_coordinate",car_x_coordinate, "id",id)
        self.gameDisplay.blit(self.Images[int(id)], (car_x_coordinate, car_y_coordinate))

    def racing_window(self):
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Car Dodge')

        self.run_car()

    def run_car(self):
        global v
        # v = n.send((self.car_x_coordinate, self.car_y_coordinate))
        while not self.crashed:
            v = n.send((self.car_x_coordinate, self.car_y_coordinate))
            # n.send((self.car_x_coordinate, self.car_y_coordinate))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # print("p1=",p1)
                    # v = n.send((self.car_x_coordinate, self.car_y_coordinate))
                    n.send(p1)
                    n.send("quit")
                    self.crashed = True

                if (event.type == pygame.KEYDOWN):
                    print("v=",v)
                    if (event.key == pygame.K_LEFT):
                        self.car_x_coordinate -= 50
                        v=n.send((self.car_x_coordinate, self.car_y_coordinate))
                        print("aloooo vvvvv",v)
                        print ("CAR X COORDINATES: %s" % self.car_x_coordinate)
                    if (event.key == pygame.K_RIGHT):
                        self.car_x_coordinate += 50
                        v = n.send((self.car_x_coordinate, self.car_y_coordinate))
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
            self.car(self.car_x_coordinate, self.car_y_coordinate, self.id)


            for a in range(len(v)):
                if(a%2==0):
                    print("a=",a)
                    s = re.split(r'[(,)]', str(v[a]) )
                    print("V[x]=",v[a])
                    print("v[1]",v[1])
                    x1 = float(s[1])
                    print("x1=",x1)
                    self.id=(v[a+1])
                    self.car(x1, self.car_y_coordinate,self.id)

            self.highscore(self.count)
            self.count += 1
            if (self.count % 100 == 0):
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
        car_racing.racing_window()

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
        font = pygame.font.SysFont("arial", 20)
        text = font.render("Score : " + str(count), True, self.white)
        self.gameDisplay.blit(text, (0, 0))

    def display_credit(self):
        font = pygame.font.SysFont("lucidaconsole", 14)
        text = font.render("Thanks for playing!", True, self.white)
        self.gameDisplay.blit(text, (600, 520))

if __name__ == '__main__':
    car_racing = CarRacing()
    car_racing.racing_window()
