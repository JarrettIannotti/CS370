import pygame
from Player import Player
import math

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
image1 = "Images/robot.png"
image2 = "Images/robot2.png"
robots = 2
robot = [0, 0]
dx = []
dy = []
angle = [0, 0]
robot[0] = Player(image1, 50)
robot[1] = Player(image2, 50)
player_group = pygame.sprite.Group()
player_group.add(robot[0])
player_group.add(robot[1])

bullet_group = pygame.sprite.Group()

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
        bullet = robot[0].create_bullet(angle[0])
        bullet_group.add(bullet)
    if keys[pygame.K_g]:
        bullet = robot[1].create_bullet(angle[1])
        bullet_group.add(bullet)

    if pygame.sprite.spritecollideany(robot[1], bullet_group):
        print("IM HIT")

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
    bullet_group.draw(screen)
    bullet_group.update()
    player_group.update()
    pygame.display.flip()

