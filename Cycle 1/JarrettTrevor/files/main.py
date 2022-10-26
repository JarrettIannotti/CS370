import pygame
from Player import Player

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

fileList = ["ex1.txt", "ex2.txt"]
try:
    # using with we don't need to close the file it handles that for us
    with open(fileList[0]) as file:
        contents = file.read()
        # we would pass the entire file contents to the player when its loaded so each player
        # holds its own file contents
        robot1 = Player(contents)
# if the file doesn't exist it prints and error and exits the program
except FileNotFoundError:
    print("THE FILE IS NOT FOUND")
    exit()

try:
    # using with we don't need to close the file it handles that for us
    with open(fileList[1]) as file:
        contents = file.read()
        # we would pass the entire file contents to the player when its loaded so each player
        # holds its own file contents
        robot2 = Player(contents)
# if the file doesn't exist it prints and error and exits the program
except FileNotFoundError:
    print("THE FILE IS NOT FOUND")
    exit()


# Example file reading
# This would go in main window or spawner or wherever we handle that
# playerList would just be a list of file paths we are loading from
# playerList = ["ex1.txt", "ex2.txt"]
# robotsList = [robot1, robot2]
# i = 0
# for filePath in playerList:
#     try:
#         # using with we don't need to close the file it handles that for us
#         with open(filePath) as file:
#             contents = file.read()
#             # we would pass the entire file contents to the player when its loaded so each player
#             # holds its own file contents
#             robotsList[i] = Player(contents)
#             i += 1
#     # if the file doesn't exist it prints and error and exits the program
#     except FileNotFoundError:
#         print("THE FILE IS NOT FOUND")
#         exit()
# Example file reading ends here



player_group = pygame.sprite.Group()
player_group.add(robot1)
player_group.add(robot2)

bullet_group = pygame.sprite.Group()


print(robot1.getFileContent())
print(robot2.getFileContent())
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
    robot1.move(move_x * 5, move_y * 5)


    if keys[pygame.K_SPACE]:
        bullet = robot1.create_bullet(mouse_x, mouse_y)
        bullet_group.add(bullet)

    if robot1.center[0] <= 0:
        robot1.center[0] = 0
    elif robot1.center[0] >= 750:
        robot1.center[0] = 750
    if robot1.center[1] <= 0:
        robot1.center[1] = 0
    elif robot1.center[1] >= 550:
        robot1.center[1] = 550

    screen.fill(color=(192, 192, 192))
    robot1.draw(screen)
    bullet_group.draw(screen)
    bullet_group.update()
    pygame.display.flip()

