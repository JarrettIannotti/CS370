import pygame
import random

#Initalize the pygame
pygame.init()

#Create the screen              width,height
screen = pygame.display.set_mode((800,600))


#----------------Title and Icon---------------
pygame.display.set_caption("A-T Robot")
icon = pygame.image.load("robots01.gif")

#player
player1Img = pygame.image.load("tank.png")
player1X = random.randint(32,768)
player1Y = random.randint(32,668)

def player(x, y):
    screen.blit(player1Img, (x,y))

#Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill(color=(0, 0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player(player1X, player1Y)
    pygame.display.update()
