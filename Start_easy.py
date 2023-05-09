import pygame
from pygame import mixer
import random
import math
import time
import tkinter as tk
import sqlite3

  
#screen:    
pygame.init() 
display_width = 800    
display_height = 600      
screen = pygame.display.set_mode((800, 600))   
pygame.display.set_caption('Space Invaders')     
iconShip = pygame.image.load('iconShip.png').convert()    
pygame.display.set_icon(iconShip)
font = pygame.font.Font('freesansbold.ttf', 32)

def limit_line():
    pygame.draw.line(screen, red, (0, -30), (800, -30), 2)
    
    
        
#Player ship: 
playerShipImg = pygame.image.load('playerShip.png').convert()   
ship_x = 382   
ship_y = 500

def playerShip(x, y):   
    screen.blit(playerShipImg, (x, y))


#Lives:
lives = 10
lives_x = 10
lives_y = 10

def lives_count():
    disp_lives = font.render("Lives: " + str(lives), True, white)
    screen.blit(disp_lives, (10, 10))
    

#Game Over:

def game_over(lives):
    disp_gameOver = font.render("GAME OVER", True, red)
    if lives <= 0:
        screen.blit(disp_gameOver, (300, 280))
        for i in range(no_of_enemies):
            enemy_y[i] = -500
    

#Score:
points = 0

def score():
    disp_score = font.render("Score: " + str(points), True, white)
    screen.blit(disp_score, (620, 10))

b = open('highscore.txt','r')

def updScore(points):
    a = open('highscore.txt','w')
    c = open('email.txt','r')
    a.write(str(points))
    

#Colissions:
def collided(x1, y1, x2, y2):
    distance = math.sqrt(pow((x1 - x2),2) + pow((y1 - y2),2))
    if distance < 32:
        return True
    else:
        return False




    
    
#Bullet:
bulletImg = pygame.image.load('B33.png').convert()
bull_firing = False
bull_speed = 0
bull_x = 0
bull_y = 0
no_of_bull = 0

def bulletDisp(x, y):
    if bull_firing:
        screen.blit(bulletImg, (x, y))
    
 
  
#Enemy: 
enemies = ['E1.png','E2.png','E3.png','E4.png'] 
enemyImg = []
enemyRect = []
enemy_x = [] 
enemy_y = [] 
enemy_y_change = [] 
no_of_enemies = 7
enemy_num = []
init_speed = 0.05
enemy_speed = init_speed
##random.randrange(82,683,100)
##random.randrange(-360,-36,36)

for i in range(no_of_enemies): 
    if len(enemy_x) > 0:
        enemy_x.append(random.randrange(82,683,100)) 
        enemy_y.append(random.randrange(-360,-36,36)) 
        enemy_y_change.append(0) 
        enemyImg.append(pygame.image.load(enemies[random.randint(0,3)]).convert())

        while enemy_x[-1] in enemy_x[:-1]: 
            enemy_x[i] = random.randrange(82,683,100)         
                 
    else: 
        enemy_x.append(random.randrange(82,683,100)) 
        enemy_y.append(random.randrange(-360,-36,36)) 
        enemy_y_change.append(0) 
        enemyImg.append(pygame.image.load(enemies[random.randint(0,3)]).convert())
##        enemyRect.append(pygame.Rect(enemy_x[i], enemy_y[i], 36, 36))
         
def enemyShip(x, y, i): 
    screen.blit(enemyImg[i], (x, y))

def enemyRectDraw(i):
    pygame.draw.rect(screen, white, enemyRect[i])



#problems:
numbers = [0,1,2,3,4,5,6,7,8,9]
num_list = []
operators = ['*','+','-']
div = ('/')
num_entered = []

for i in range(no_of_enemies):
    num_list.append(numbers[random.randint(0,9)])

def playerNum(x, y):
    a = str(num_entered[-1])
    disp_num = font.render(a, True, white)
    screen.blit(disp_num, (x, y))

def genNumber(x, y, i):
    a = str(num_list[i])
    disp_num = font.render(a, True, white)
    screen.blit(disp_num, (x, y))

def genEquation(x, y, i):
    a = (str(num_list[i]) + operators[random.randint(0,2)] + str(num_list[random.randint(0,9)]))
    disp_equation = font.render(a, True, white)
    screen.blit(disp_equation, (x, y))

def genDiv(x, y):
    a = (str(num_list[random.randint(0,9)]) + div + str(num_list[random.randint(0,9)]))
    disp_div = font.render(a, True, white)
    screen.blit(disp_div, (x, y))



  
    
#colours:   
black = (0,0,0)    
white = (255,255,255)   
red = (255,0,0)    
green = (0,255,0)    
blue = (0,0,255)   
  
   
clock = pygame.time.Clock()   
running = True   
    
#main:   
while running:     
##    screen.fill((10,20,40))
    screen.fill(black)
    for event in pygame.event.get(): 
  
        #FPS: 
        clock.tick(60) 
##        print(event) 
         
        if event.type == pygame.QUIT:    

            running = False 
  
        if event.type == pygame.KEYDOWN:  
  
            #player movement:  
            if event.key == pygame.K_RIGHT:   
                if ship_x < 682: 
                    ship_x += 100 
                else:   
                    ship_x += 0                      
            if event.key == pygame.K_LEFT:   
                if ship_x > 82: 
                    ship_x -= 100
                else:   
                    ship_x -= 0  
            if event.key == pygame.K_UP:   
                if ship_y >= 350:   
                    ship_y -= 60                      
                else:   
                    ship_y -= 0  
            if event.key == pygame.K_DOWN:   
                if ship_y <= 470:

                    ship_y += 60                      
                else:   
                    ship_y -= 0


    #bullet:
            if event.key == pygame.K_0:
                num_entered.append(0)
                bull_effect = mixer.Sound('laser.wav')
                bull_effect.play()
                no_of_bull += 1
                bull_x = (ship_x + 10)
                bull_y = (ship_y - 14)
                bull_speed = 0
            if event.key == pygame.K_1:
                num_entered.append(1)
                bull_effect = mixer.Sound('laser.wav')
                bull_effect.play()
                no_of_bull += 1
                bull_x = (ship_x + 10)
                bull_y = (ship_y - 14)
                bull_speed = 0
            if event.key == pygame.K_2:
                num_entered.append(2)
                bull_effect = mixer.Sound('laser.wav')
                bull_effect.play()
                no_of_bull += 1
                bull_x = (ship_x + 10)
                bull_y = (ship_y - 14)
                bull_speed = 0
            if event.key == pygame.K_3:
                num_entered.append(3)
                bull_effect = mixer.Sound('laser.wav')
                bull_effect.play()
                no_of_bull += 1
                bull_x = (ship_x + 10)
                bull_y = (ship_y - 14)
                bull_speed = 0
            if event.key == pygame.K_4:
                num_entered.append(4)
                bull_effect = mixer.Sound('laser.wav')
                bull_effect.play()
                no_of_bull += 1
                bull_x = (ship_x + 10)
                bull_y = (ship_y - 14)
                bull_speed = 0
            if event.key == pygame.K_5:
                num_entered.append(5)
                bull_effect = mixer.Sound('laser.wav')
                bull_effect.play()
                no_of_bull += 1
                bull_x = (ship_x + 10)
                bull_y = (ship_y - 14)
                bull_speed = 0
            if event.key == pygame.K_6:
                num_entered.append(6)
                bull_effect = mixer.Sound('laser.wav')
                bull_effect.play()
                no_of_bull += 1
                bull_x = (ship_x + 10)
                bull_y = (ship_y - 14)
                bull_speed = 0
            if event.key == pygame.K_7:
                num_entered.append(7)
                bull_effect = mixer.Sound('laser.wav')
                bull_effect.play()
                no_of_bull += 1
                bull_x = (ship_x + 10)
                bull_y = (ship_y - 14)
                bull_speed = 0
            if event.key == pygame.K_8:
                num_entered.append(8)
                bull_effect = mixer.Sound('laser.wav')
                bull_effect.play()
                no_of_bull += 1
                bull_x = (ship_x + 10)
                bull_y = (ship_y - 14)
                bull_speed = 0
            if event.key == pygame.K_9:
                num_entered.append(9)
                bull_effect = mixer.Sound('laser.wav')
                bull_effect.play()
                no_of_bull += 1
                bull_x = (ship_x + 10)
                bull_y = (ship_y - 14)
                bull_speed = 0

            
    if bull_y >= -27:
        bull_firing = True
        bull_speed -= 0.01
        bull_y += bull_speed
    else:
        bull_firing = False
        bull_y = -1000
        
    bulletDisp(bull_x, bull_y)

                   
        
        
    #enemy movement:
    for i in range(no_of_enemies):
                
        if enemy_y[i] < 565:
            if points == 0:
                enemy_y_change[i] = init_speed
            else:
                enemy_y_change[i] = enemy_speed
            enemy_y[i] += enemy_y_change[i]
              

            
        else:
            lives -= 1
            collision_effect = mixer.Sound('explosion.wav')
            collision_effect.play()
            enemy_y_change[i] = 0
            enemy_y[i] = (random.randrange(-360,-36,36)) 
            enemyImg[i] = (pygame.image.load(enemies[random.randint(0,3)]).convert())
            num_list[i] = (numbers[random.randint(0,9)])

            

        enemyShip(enemy_x[i], enemy_y[i], i)
        enemy_num.append(genNumber((enemy_x[i] + 10), (enemy_y[i] + 36), i))
        enemy_num[i]
        



    #collisions:
    for i in range(no_of_enemies):
        bull_collision = collided(enemy_x[i], enemy_y[i], bull_x, bull_y)
        if len(num_entered) > 0:
            if num_entered[-1] == (num_list[i]):
                if bull_collision:
                    enemy_speed += 0.005
                    num_list[i] = (numbers[random.randint(0,9)])
                    collision_effect = mixer.Sound('explosion.wav')
                    collision_effect.play()
                    num_entered = []
                    points += 1
                    print (enemy_y_change)
                    bull_y = -1000
                    enemy_y[i] = (random.randrange(-360,-36,36)) 
                    enemy_y_change[i] = 0 
                    enemyImg[i] = (pygame.image.load(enemies[random.randint(0,3)]).convert())
                    
        ship_collision =  collided(enemy_x[i], (enemy_y[i] +31), ship_x, ship_y)
        if ship_collision:
            collision_effect = mixer.Sound('explosion.wav')
            collision_effect.play()
            lives -= 1
            enemy_y[i] = (random.randrange(-360,-36,36)) 
            enemy_y_change[i] = 0 
            enemyImg[i] = (pygame.image.load(enemies[random.randint(0,3)]).convert())

        line_collision = collided(bull_x, -30, bull_x, bull_y)
        if line_collision:
            num_entered = []

    con = sqlite3.connect('playerdata.db')
    cur = con.cursor()
    for row in cur.execute("Select * from record"):
        cur.execute("""UPDATE record SET highscore = '%s'""" % (points))
    con.commit()

##    print(num_entered)
    if len(num_entered) > 0:
        playerNum((ship_x + 10), (ship_y + 36))
    score()
    updScore(points)
    game_over(lives)
    lives_count()
    limit_line()
    playerShip(ship_x, ship_y)
    pygame.display.update()

pygame.quit()
quit()
import Menu.py
