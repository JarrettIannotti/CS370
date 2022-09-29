import pygame
import random


class Player(object):

    def __init__(self):
        self.image = pygame.image.load("Images/robot.png")
        self.x = random.randint(32, 768)
        self.y = random.randint(32, 568)
        self.center = [self.x, self.y]
        self.change_x = 0
        self.change_y = 0

    def move(self, x, y):
        self.center[0] += x
        self.center[1] += y

    def draw(self, surf):
        surf.blit(self.image, self.center)


class Game(object):

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.robot = Player()

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            move_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
            move_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
            self.robot.move(move_x * 5, move_y * 5)

            if self.robot.center[0] <-16:
                self.robot.center[0] = 0
            if self.robot.center[0] > 780:
                self.robot.center[0] = 736

            self.screen.fill(color=(192, 192, 192))
            self.robot.draw(self.screen)
            pygame.display.update()
g = Game()
g.run()

# Initalize the pygame
# pygame.init()
#
# # ----------------Title and Icon---------------
# pygame.display.set_caption("A-T Robot")
#
# # player1
# # player1Img = pygame.image.load("Images/robot.png")
# # player1X = random.randint(32, 768)
# # player1Y = random.randint(32, 568)
# # playerChangeX = 0
# # playerChangeY = 0
#
#
# def player(playerImage, x, y):
#     screen.blit(playerImage, (x, y))
#
#
# velocity = 5
# clock = pygame.time.Clock()
#
# # Game Loop
# running = True
# while running:
#
#     clock.tick(60)
#     # RGB - Red, Green, Blue
#     screen.fill(color=(192, 192, 192))
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 playerChangeX = -5
#             if event.key == pygame.K_RIGHT:
#                 playerChangeX = 5
#             if event.key == pygame.K_UP:
#                 playerChangeY = -5
#             if event.key == pygame.K_DOWN:
#                 playerChangeY = 5
#
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
#                 playerChangeX = 0
#                 playerChangeY = 0
#
#         if player1X <= 0:
#             player1X = 0
#         elif player1X >= 736:
#             player1X = 736
#         if player1Y <= 0:
#             player1Y = 0
#         elif player1Y >= 568:
#             player1Y = 568
#
#         # Checking for boundaries of spaceship so it doesn't  go out of bounds
#     player1X += playerChangeX
#     player1Y += playerChangeY
#
#     player(player1Img, player1X, player1Y)
#     pygame.display.update()
