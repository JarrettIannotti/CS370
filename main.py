import pygame
from Player import Player
import math
import time
from Sound import Sound
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
image1 = "Images/robot.png"
image2 = "Images/robot2.png"
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



#Player Sprite Group
player_group = pygame.sprite.Group()
player_group.add(robot[0])
player_group.add(robot[1])
circle = pygame.image.load("Images/circle.png")
bullet_group[0] = pygame.sprite.Group()
bullet_group[1] = pygame.sprite.Group()

previous_time = pygame.time.get_ticks()
health = 10
sound= Sound()
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

    keys = pygame.key.get_pressed()
    move_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    move_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
    robot[0].move(move_x * 5, move_y * 5)

    if keys[pygame.K_f]:
        current_time = pygame.time.get_ticks()
        if current_time - previous_time > 500:
            previous_time = current_time
            bullet.insert(0, robot[0].create_bullet(angle[0]))
            bullet_group[0].add(bullet[0])
            sound.playsound()


    circle_coordinate_robot1 = list(robot[1].rect.center)
    circle_coordinate_robot2 = list(robot[0].rect.center)
    #Collision- Robot2
    if pygame.sprite.spritecollide(robot[1], bullet_group[0], True, pygame.sprite.collide_circle):
        print("ROBOT 2 HIT")
        screen.blit(circle, (circle_coordinate_robot1[0]-25, circle_coordinate_robot1[1]-25))

        # screen.fill("Red")
        pygame.display.update()
        health -= 1
    print(health)





    if keys[pygame.K_g]:
        current_time = pygame.time.get_ticks()
        if current_time - previous_time > 500:
            previous_time = current_time
            bullet.insert(1, robot[1].create_bullet(angle[1]))
            bullet_group[1].add(bullet[1])
            sound.playsound()
    #Collision - Robot 1
    if pygame.sprite.spritecollide(robot[0], bullet_group[1], True, pygame.sprite.collide_circle):
        print("ROBOT 1 HIT")
        # screen.fill("Blue")
        screen.blit(circle, (circle_coordinate_robot2[0] - 25, circle_coordinate_robot2[1] - 25))
        pygame.display.update()







    if robot[0].center[0] <= 0:
        robot[0].center[0] = 0
    elif robot[0].center[0] >= 750:
        robot[0].center[0] = 750
    if robot[0].center[1] <= 0:
        robot[0].center[1] = 0
    elif robot[0].center[1] >= 550:
        robot[0].center[1] = 550

    screen.fill(color=(192, 192, 192))

    player_group.draw(screen)
    bullet_group[0].draw(screen)
    bullet_group[0].update()
    bullet_group[1].draw(screen)
    bullet_group[1].update()
    player_group.update()
    pygame.display.flip()
    #print(len(bullet_group[1]))

