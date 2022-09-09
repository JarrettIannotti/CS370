import pygame
import random

#Initalize the pygame
pygame.init()

#Create the screen              width,height
screen = pygame.display.set_mode((800,600))


#----------------Title and Icon---------------
pygame.display.set_caption("A-T Robot")
icon = pygame.image.load("robots01.gif")

#player1
player1Img = pygame.image.load("tank.png")
player1X = random.randint(32,768)
player1Y = random.randint(32,568)
print(player1Y, player1X)
#player2

player2Img = pygame.image.load("tank2.png")
player2X = random.randint(32+20, random.randint(32,768))
player2Y = random.randint(32+20, random.randint(32,568))
print(player2Y, player2X)
#player3


def player(playerImage, x, y):
    screen.blit(playerImage, (x,y))


#Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill(color=(0, 0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player(player1Img, player1X, player1Y)
    player(player2Img, player2X, player2Y)
    pygame.display.update()
