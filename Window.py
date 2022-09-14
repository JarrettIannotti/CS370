import pygame
import random
import time
import math

#Initalize the pygame
pygame.init()

#Create the screen              width,height
screen = pygame.display.set_mode((800,600))

#----------------Title and Icon---------------
pygame.display.set_caption("A-T Robot")
icon = pygame.image.load("robots01.gif")

#File init and read to text array
fileObj = open("ROBOT.txt", "r") #opens the file in read mode
text = fileObj.read().splitlines() #puts the file into an array
fileObj.close()

#player
player1Img = pygame.image.load("tank.png")
player1X = random.randint(32,768)
player1Y = random.randint(32,568)
player1Rect = player1Img.get_rect() # this makes a rectangle around player1Img
flag = 4
#Rectangle that goes around the mouse
mouseRect = pygame.Rect(0, 0, 50, 50)
angle = 0
velocity = 12       #pixels the bots move per loop cycle
count = 0           #Array position for cycling through text file
o = 0
def player(rect):
    screen.blit(player1Img, rect)
#Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill(color=(0, 0, 0))
   
# Track player location then find the time for command
    num = " "
#   for i in text:
#       if i.isdigit():
#           num = i

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

    # Move then wait a few seconds


#   if "forward" in text[count]:           #Array position needs to by cycled
#       while (i < 5):
#           i += 1
#           player1X += velocity
#           time.sleep(.005)
#           if player1X >= 768:
#               player1X = 768

#   if "back" in text[count]:
#       while (i < 3):
#           i += 1
#           player1X -= velocity
#           time.sleep(.005)
#           if player1X <= 0:
#               player1X = 0

#   if "up" in text[count]:
#       while (i < 3):
#           i += 1
#           player1Y -= velocity
#           time.sleep(.005)
#           if player1Y >= 0:
#               player1Y = 0

#   if "down" in text[count]:
#       while (i < 3):
#           i = count + 1
#           player1Y -= velocity
#           pygame.time.delay(.005)
#           if player1Y >= 768:
#               player1Y = 768


    if "rotate" in text[count]:
        res = ""
        #res = [int(i) for i in text[count].split() if i.isdigit()]
        for char in text[count]:
            if char.isdigit():
                res += char

        angle = (int(res) * (3.14159 / 180))
        print(angle)


    if "throttle" in text[count]:
        player1Y -= (math.cos(angle) * velocity)
        player1X += (math.sin(angle) * velocity)
        time.sleep(.05)

#    if "sleep" in text[count]:


    count += 1

    if "!" in text[count]:
        count = 0



    # Keeping the rectangle on player1
    player1Rect.x = player1X
    player1Rect.y = player1Y
    # Passes the rect which has x,y coordinates to blit the player onto the screen
    player(player1Rect)

    # Checks if player1 collides with the mouse rect and if it does a rect around the player
    if player1Rect.colliderect(mouseRect):
        pygame.draw.rect(screen, (255, 0, 0), player1Rect, 4)

    # Draws the rectangle around the mouse
    pygame.draw.rect(screen, (0, 255, 0), mouseRect, 4)
    
    pygame.display.update()