import pygame
from Player import Player

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
robot = Player()
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
player_group.add(robot)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    keys = pygame.key.get_pressed()
    move_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    move_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
    robot.move(move_x * 5, move_y * 5)
    robot_bullet = robot.create_bullet(mouse_x, mouse_y)

    if keys[pygame.K_f]:
        robot_bullet.update()
        bullet_group.add(robot_bullet)

    if robot.center[0] <= 0:
        robot.center[0] = 0
    elif robot.center[0] >= 750:
        robot.center[0] = 750
    if robot.center[1] <= 0:
        robot.center[1] = 0
    elif robot.center[1] >= 550:
        robot.center[1] = 550

    screen.fill(color=(192, 192, 192))
    robot.draw(screen)
    bullet_group.draw(screen)
    bullet_group.update()
    pygame.display.flip()