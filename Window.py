import pygame


#Initalize the pygame
pygame.init()

#Create the screen              width,height
screen = pygame.display.set_mode(800,600)


#----------------Title and Icon---------------
pygame.display.set_caption("A-T Robot")
icon = pygame.image.load("robots01.gif")


#Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill(color=(0, 0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False