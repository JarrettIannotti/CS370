import pygame
import button
import sound

#Initalize the pygame
pygame.init()

#Create the screen              width,height
screen = pygame.display.set_mode((800,600))

#----------------Title and Icon---------------
pygame.display.set_caption("A-T Robot")
icon = pygame.image.load("robots01.png")

#load button images
play_img = pygame.image.load('Images/play.png')
quit_img = pygame.image.load('Images/quit.png')

#create button instances
start_button = button.Button(100, 500, play_img)
quit_button = button.Button(450, 500, quit_img)

startBtn_sound = sound.Sound()
quitBtn_sound = sound.Sound()
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill(color=(0, 0, 0))

    #If start button is pressed execute Window.py
    if start_button.draw(screen):
        print('START')
        startBtn_sound.playsound()
        exec(open('Window.py').read())
    #If quit button is pressed close the window
    if quit_button.draw(screen):
        print('QUIT')
        quitBtn_sound.playsound()
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()