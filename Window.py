import pygame
<<<<<<< HEAD

=======
import random

#This is andrews update
>>>>>>> 1d40443f8197424235592ddbf1d2c67b1fa64587

#Initalize the pygame
pygame.init()

#Create the screen              width,height
<<<<<<< HEAD
screen = pygame.display.set_mode(800,600)
=======
screen = pygame.display.set_mode((800,600))
>>>>>>> 1d40443f8197424235592ddbf1d2c67b1fa64587


#----------------Title and Icon---------------
pygame.display.set_caption("A-T Robot")
<<<<<<< HEAD
icon = pygame.image.load("robots01.gif")
=======
icon = pygame.image.load("robots01.png")

#player1
player1Img = pygame.image.load("Images/tank.png")
player1X = random.randint(32,768)
player1Y = random.randint(32,568)
playerChangeX = 0
print(player1Y, player1X)
#player2

player2Img = pygame.image.load("Images/tank2.png")
player2X = random.randint(32+20, random.randint(32,768))
player2Y = random.randint(32+20, random.randint(32,568))
print(player2Y, player2X)
#player3


def player(playerImage, x, y):
    screen.blit(playerImage, (x,y))

#Move Forward
def move_forward(y):
    y = 5
    return y

#Move backward
def move_backward(y):
    y = -5
    return y

#Move left
def move_left(x):
    x = -5
    return x
# move right
def move_right(x):
    x = 5
    return x
>>>>>>> 1d40443f8197424235592ddbf1d2c67b1fa64587


#Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill(color=(0, 0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
<<<<<<< HEAD
            running = False
=======
            running = False
        # if keystroke is pressed check wheather its right or left
        if event.type == pygame.KEYDOWN:
            print("A key stroked is pressed")
            if event.key == pygame.K_LEFT:
                move_left(playerChangeX)
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                move_right(playerChangeX)
                print("Right arrow is pressed")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystoke has been released")
                playerChangeX = 0

        # Checking for boundaries of spaceship so it doesn't  go out of bounds
        player1X += playerChangeX

        if player1X <= 0:
            player1X = 0
        elif player1X >= 736:
            playerX = 736
        player(player1Img, player1X, player1Y)
        player(player2Img, player2X, player2Y)
        pygame.display.update()
>>>>>>> 1d40443f8197424235592ddbf1d2c67b1fa64587
