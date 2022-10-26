import pygame
import random
from Bullet import Bullet
from pygame import mixer
#Initalize the pygame
pygame.init()
bulletSound = pygame.mixer.Sound("Machine-Gun-Automatic-Fire-A-www.fesliyanstudios.com.mp3")

#Create the screen              width,height
screen = pygame.display.set_mode((800,600))


#----------------Title and Icon---------------
pygame.display.set_caption("A-T Robot")
icon = pygame.image.load("robots01.png")

#player
player1Img = pygame.image.load("Images/tank.png")
player1X = random.randint(32,768)
player1Y = random.randint(32,568)
player1Rect = player1Img.get_rect() # this makes a rectangle around player1Img

#Rectangle that goes around the mouse
mouseRect = pygame.Rect(0, 0, 50, 50)

def player(rect):
    screen.blit(player1Img, rect)

def something():
    pass

def create_bullet():
    return Bullet(player1X+15,player1Y)


bullet_group = pygame.sprite.Group()
#Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill(color=(0, 0, 0))
    #test


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    # World boundary - Makes sure the robot doesn't leave the game window
    if player1X <= 0:
        player1X = 0
    elif player1X >= 768:
        player1X = 768
    if player1Y <= 0:
        player1Y = 0
    elif player1Y >= 568:
        player1Y = 568
        
    # Makes the center of mouseRect the center of your mouses current position
    mouseRect.center = pygame.mouse.get_pos()
    
    # Keeping the rectangle on player1
    player1Rect.x = player1X
    player1Rect.y = player1Y
    # Passes the rect which has x,y coordinates to blit the player onto the screen
    player(player1Rect)
    
    # Checks if player1 collides with the mouse rect and if it does draws a rect around the player
    if player1Rect.colliderect(mouseRect):
        pygame.draw.rect(screen, (255, 0, 0), player1Rect, 4)
        bullet_group.add(create_bullet())
        bulletSound.play(-1)
    else:
        bulletSound.stop()
    # Draws the rectangle around the mouse

    bullet_group.draw(screen)
    bullet_group.update()
    pygame.draw.rect(screen, (0, 255, 0), mouseRect, 4)
    pygame.display.update()
