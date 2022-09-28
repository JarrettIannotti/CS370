import pygame
import random

#This is andrews update

#Initalize the pygame
pygame.init()

#Create the screen              width,height
screen = pygame.display.set_mode((800,600))

#----------------Title and Icon---------------
pygame.display.set_caption("A-T Robot")

#player1
player1Img = pygame.image.load("Images/robot.png")
player1X = random.randint(32,768)
player1Y = random.randint(32,568)
playerChangeX = 0
#player2

#player2Img = pygame.image.load("Images/tank2.png")
#player2X = random.randint(32+20, random.randint(32,768))
#player2Y = random.randint(32+20, random.randint(32,568))
#print(player2Y, player2X)
#player3


def player(playerImage, x, y):
    screen.blit(playerImage, (x, y))

velocity = 5
clock = pygame.time.Clock()

#Game Loop
running = True
while running:

    clock.tick(60)
    # RGB - Red, Green, Blue
    screen.fill(color=(192, 192, 192))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChangeX = -5
            if event.key == pygame.K_RIGHT:
                playerChangeX = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChangeX = 0


        # Checking for boundaries of spaceship so it doesn't  go out of bounds
    player1X += playerChangeX

    if player1X <= 0:
        player1X = 0
    if player1X >= 736:
        playerX = 736

    player(player1Img, player1X, player1Y)
    pygame.display.update()