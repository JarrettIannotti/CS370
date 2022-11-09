from tkinter import Button

import pygame
from Player import Player
import math
import time
from Sound import Sound
import sys
pygame.init()
screen = pygame.display.set_mode((1400, 900))
clock = pygame.time.Clock()
image1 = "Images/robot.png"
image2 = "Images/robot.png"
timer = 5
robots = 2
robot = [0, 0]
dx = []
dy = []
angle = [0, 0]
bullet_group = [0, 0]
bullet = [0, 0]

robot[0] = Player(image1, 50)
robot[1] = Player(image2, 50)

#font
font = pygame.font.Font(None, 40)
text = font.render("Health", False, "Red")

#options - for the side
#Escape
escape = pygame.image.load("Images/escape.png")
Escfont = pygame.font.Font(None, 30)
Esctext = Escfont.render("Press ESC to exit the game", False, "White")
#audio
audio = pygame.image.load("Images/mute (1).png")
audiofont = pygame.font.Font(None, 30)
auidotext = audiofont.render("Press M to mute", False, "White")

#Player Sprite Group
player_group = pygame.sprite.Group()
player_group.add(robot[0])
player_group.add(robot[1])
circle = pygame.image.load("Images/circle.png")
bullet_group[0] = pygame.sprite.Group()
bullet_group[1] = pygame.sprite.Group()

previous_time = pygame.time.get_ticks()
health = 10
sound = Sound()
running = True


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(0, robots):
        dx.insert(i, robot[i].center[0])

    for i in range(0, robots):
        dy.insert(i, robot[i].center[1])

    angle.insert(0, math.atan2((dy[1] - dy[0]), (dx[1] - dx[0])))
    angle.insert(1, math.atan2((dy[0] - dy[1]), (dx[0] - dx[1])))

    #------robot[0] movement with streering -----
    clock.tick(60)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        robot[0].position += robot[0].direction
    if keys[pygame.K_s]:
        robot[0].position -= robot[0].direction
    if keys[pygame.K_a]:
        robot[0].direction.rotate_ip(-1)
    if keys[pygame.K_d]:
        robot[0].direction.rotate_ip(1)
    robot[0].robot_angle = robot[0].direction.angle_to((1, 0))
    robot[0].rotated_robot = pygame.transform.rotate(robot[0].image, robot[0].robot_angle)



    # --------------------------

   # move_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    #move_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]

    #robot[0].move(move_x, move_y)

    #---Firing ----
    if keys[pygame.K_f]:
        current_time = pygame.time.get_ticks()
        if current_time - previous_time > 500:
            previous_time = current_time
            bullet.insert(0, robot[0].create_bullet(angle[0]))
            bullet_group[0].add(bullet[0])
            sound.playsound()

    circle_coordinate_robot1 = list(robot[1].rect.center)
    circle_coordinate_robot2 = list(robot[0].rect.center)
    # Collision- Robot2
    if pygame.sprite.spritecollide(robot[1], bullet_group[0], True, pygame.sprite.collide_circle):
        print("ROBOT 2 HIT")
        screen.blit(circle, (circle_coordinate_robot1[0] - 25, circle_coordinate_robot1[1] - 25))

        # screen.fill("Red")
        pygame.display.update()
        robot[0].health -= 1
        #player_group.sprite.get_health(20)
    print(robot[0].health)

    if keys[pygame.K_g]:
        current_time = pygame.time.get_ticks()
        if current_time - previous_time > 500:
            previous_time = current_time
            bullet.insert(1, robot[1].create_bullet(angle[1]))
            bullet_group[1].add(bullet[1])
            sound.playsound()
    # Collision - Robot 1
    if pygame.sprite.spritecollide(robot[0], bullet_group[1], True, pygame.sprite.collide_circle):
        print("ROBOT 1 HIT")
        # screen.fill("Blue")
        screen.blit(circle, (circle_coordinate_robot2[0] - 25, circle_coordinate_robot2[1] - 25))
        pygame.display.update()
       # player_group.sprite.get_health(30)

    print(robot[0].current_health)

    if robot[0].center[0] <= 0:
        robot[0].center[0] = 0
    elif robot[0].center[0] >= 836:
        robot[0].center[0] = 836
    if robot[0].center[1] <= 0:
        robot[0].center[1] = 0
    elif robot[0].center[1] >= 836:
        robot[0].center[1] = 836
#
    screen.fill(color=(0, 0, 0))

    robot[0].draw(screen)
    robot[1].draw(screen)
    #screen.blit(robot[0].rotated_robot, robot[0].rotated_robot.get_rect(center=(round(robot[0].position.x), round(robot[0].position.y))))
    # player_group1.draw(screen)
    bullet_group[0].draw(screen)
    bullet_group[0].update()
    bullet_group[1].draw(screen)
    bullet_group[1].update()

    player_group.update(screen, "Red", 1020, 60)
    player_group.update(screen, "Blue", 1020, 100)

    #Health font
    screen.blit(text, (1020, 20))

    #Render Esc Option on to the game window
    #Escape
    screen.blit(escape, (1020,500 ))
    screen.blit(Esctext, (1060, 502))
    #audio
    screen.blit(audio, (1020, 540))
    screen.blit(auidotext, (1060, 542))

    #border
    grey =(128, 128, 128) # white
    white=(255, 255, 255)

    #game border for the player
    pygame.draw.rect(screen, grey, (0, 0, 1000,900), 8) # width=3
    pygame.draw.rect(screen, white, (8, 8, 984, 884), 3)

    #border for the status
    pygame.draw.rect(screen, grey,(1000,0, 800, 900 ), 8)
    #draw line
    # border for the options
    pygame.draw.line(screen,white,(1008,395), (1400, 395),3) #white line for depth effect for the grey border
    pygame.draw.line(screen, grey, (1000,400), (1400,400), 8)
    pygame.draw.line(screen, white, (1008, 408), (1008, 890),3)# white line for depth effect for the grey border
    pygame.draw.line(screen, white, (1008, 406), (1400, 406),3)
    # screen.blit(rotated_robot, rotated_robot.get_rect(center=(round(robot[0].position.x), round(robot[0].position.y))))

    pygame.display.flip()






    #print(len(bullet_group[1]))

