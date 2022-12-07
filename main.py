from tkinter import Button
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import pygame
from pygame import mixer
from Player import Player
import math
import time
from Sound import Sound
from button import Button

import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()




screen = pygame.display.set_mode((1400, 900))
BG = pygame.image.load(resource_path("assets/Background.jpg"))
#----------------------------------------------
clock = pygame.time.Clock()
previous_time = pygame.time.get_ticks()
image1 = resource_path("Images/robot.png")
image2 = resource_path("Images/robot2.png")
timer = 5
robots = 2
robot = [0, 0]
dx = []
dy = []
angle = [0, 0]
landmine_angle = [0,0]
bullet_group = [0, 0]
bullet = [0, 0]

landmine_group = [0, 0]
landmine = [0,0]

robot[0] = Player(image1, 50)
robot[1] = Player(image2, 50)
#font
font = pygame.font.Font(None, 40)
text = font.render("Health", False, "Red")

#options - for the side
#Escape
escape = pygame.image.load(resource_path("Images/escape.png"))
Escfont = pygame.font.Font(None, 30)
Esctext = Escfont.render("Press ESC to exit the game", False, "White")
#audio
audio = pygame.image.load(resource_path("Images/mute (1).png"))
audiofont = pygame.font.Font(None, 30)
auidotext = audiofont.render("Press M to mute", False, "White")

# #Player Sprite Group
# player_group = pygame.sprite.Group()
# player_group.add(robot[0])
# player_group.add(robot[1])
# circle = pygame.image.load("Images/circle.png")
# bullet_group[0] = pygame.sprite.Group()
# bullet_group[1] = pygame.sprite.Group()
#
#
# health = 10
# sound = Sound()
def winScreen(Players):
    while True:
        screen.blit(BG, (0, 0))
        # Start playing the song

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # ------------------------  Back Button -----------------------
        OPTIONS_BACK = Button(image=None, pos=(700, 460),
                              text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        OPTIONS_BACK.changeColor(MENU_MOUSE_POS)
        OPTIONS_BACK.update(screen)
        UPLOAD_TEXT = get_font(75).render(f"{Players} won", True, "Yellow")
        UPLOAD_RECT = UPLOAD_TEXT.get_rect(center=(700, 300))
        screen.blit(UPLOAD_TEXT, UPLOAD_RECT)

        # -------------------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(MENU_MOUSE_POS):
                   main_menu()
        pygame.display.update()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font(resource_path("assets/font.ttf"), size)

def get_text_box(active, color_active, color_passive, input_rect, base_font, user_text):
    if active:
        color = color_active
    else:
        color = color_passive
    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, 'black')
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width() + 10)
    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()
    # clock.tick(60) means that for every second at most
    # 60 frames should be passed.
    clock.tick(60)


def play():
    # Player Sprite Group
    player_group = pygame.sprite.GroupSingle(robot[0])
    player_group1 = pygame.sprite.GroupSingle(robot[1])
    # player_group.add(robot[0])
    # player_group.add(robot[1])
    circle = pygame.image.load(resource_path("Images/circle.png"))
    #bullet group
    bullet_group[0] = pygame.sprite.Group()
    bullet_group[1] = pygame.sprite.Group()
    #landmine group

    landmine_group[0] = pygame.sprite.Group()
    landmine_group[1] = pygame.sprite.Group()



    previous_time = pygame.time.get_ticks()
    health = 10
    sound = Sound()

    running = True

    while running:

        screen.blit(BG, (0, 0))
        #---------------------------------------------
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("black")

        clock.tick(60)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()





        for i in range(0, robots):
            dx.insert(i, robot[i].center[0])

        for i in range(0, robots):
            dy.insert(i, robot[i].center[1])

        angle.insert(0, math.atan2((dy[1] - dy[0]), (dx[1] - dx[0])))
        angle.insert(1, math.atan2((dy[0] - dy[1]), (dx[0] - dx[1])))

        landmine_angle.insert(0, math.atan2((dy[1] - dy[0]), (dx[1] - dx[0])))
        landmine_angle.insert(0, math.atan2((dy[0] - dy[1]), (dx[0] - dx[1])))

        #Robot 1 move
        move_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        move_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        robot[0].move(move_x * 5, move_y * 5)

        #robot 2 move
        move_x1 = keys[pygame.K_d] - keys[pygame.K_a]
        move_y1 = keys[pygame.K_s] - keys[pygame.K_w]
        robot[1].move(move_x1*5, move_y1*5)
#-------------------------------------------------------------------------------------------------
        #robot1 landmine
        if keys[pygame.K_t]:                              #red
            landmine.insert(0,robot[0].create_landmine((255,0,0),angle[0]))
            landmine_group[0].add(landmine[0])

        #robot 1  firing
        if keys[pygame.K_f]:
            current_time = pygame.time.get_ticks()
            if current_time - previous_time > 500:
                previous_time = current_time
                bullet.insert(0, robot[0].create_bullet(angle[0]))
                bullet_group[0].add(bullet[0])
                sound.playsound()

        circle_coordinate_robot1 = list(robot[1].rect.center)
        circle_coordinate_robot2 = list(robot[0].rect.center)
        # Collision- Robot2
        if pygame.sprite.spritecollide(robot[1], bullet_group[0], True, pygame.sprite.collide_circle):
            print("ROBOT 2 HIT")
            screen.blit(circle, (circle_coordinate_robot1[0] - 25, circle_coordinate_robot1[1] - 25))

            # screen.fill("Red")
            pygame.display.update()
            robot[0].health -= 1
            player_group1.sprite.lose_health(20)
        print(robot[0].health)

        if pygame.sprite.spritecollide(robot[1], landmine_group[0], True, pygame.sprite.collide_circle):
            print("Robot 2 got hit by the landmine")
            screen.blit(circle, (circle_coordinate_robot1[0]-25, circle_coordinate_robot1[1] -25))
            pygame.display.update()
            robot[0].health -=1
            player_group1.sprite.lose_health(30)
        print(robot[0].health)

        #robot 2 landmine
        if keys[pygame.K_m]:  # red
            landmine.insert(0, robot[1].create_landmine((255,255,0), angle[1]))
            landmine_group[1].add(landmine[1])

        #---------------------- robot 2 firing -----------------------------------------


        if keys[pygame.K_g]:
            current_time = pygame.time.get_ticks()
            if current_time - previous_time > 500:
                previous_time = current_time
                bullet.insert(1, robot[1].create_bullet(angle[1]))
                bullet_group[1].add(bullet[1])
                sound.playsound()
        # Collision - Robot 1
        if pygame.sprite.spritecollide(robot[0], bullet_group[1], True, pygame.sprite.collide_circle):
            print("ROBOT 1 HIT")
            # screen.fill("Blue")
            screen.blit(circle, (circle_coordinate_robot2[0] - 25, circle_coordinate_robot2[1] - 25))
            pygame.display.update()
            player_group.sprite.lose_health(30)
#---------------------------------------------------------------------------------------
        if pygame.sprite.spritecollide(robot[0], landmine_group[1], True, pygame.sprite.collide_circle):
            print("Robot 1 got hit by the landmine")
            screen.blit(circle, (circle_coordinate_robot2[1]-25, circle_coordinate_robot2[1] -25))
            pygame.display.update()
            robot[0].health -=1
            player_group1.sprite.lose_health(30)
        print(robot[0].health)

        if robot[0].current_health <= 0:

            robot[0].kill()
            winScreen("Player 1 ")

        if robot[1].current_health <=0:
            robot[1].kill()
            winScreen("Player 2")


        print(robot[0].current_health)

        if robot[0].center[0] <= 0:
            robot[0].center[0] = 0
        elif robot[0].center[0] >= 836:
            robot[0].center[0] = 836
        if robot[0].center[1] <= 0:
            robot[0].center[1] = 0
        elif robot[0].center[1] >= 836:
            robot[0].center[1] = 836

        screen.fill(color=(0, 0, 0))

        player_group.draw(screen)
        player_group1.draw(screen)
        bullet_group[0].draw(screen)
        bullet_group[0].update()
        bullet_group[1].draw(screen)
        bullet_group[1].update()

        #land mine
        landmine_group[0].draw(screen)
        landmine_group[0].update()

        player_group1.update(screen, "Red", 1020, 60)
        player_group.update(screen, "Blue", 1020, 100)

        # Health font
        screen.blit(text, (1020, 20))

        # Render Esc Option on to the game window
        # Escape
        screen.blit(escape, (1020, 500))
        screen.blit(Esctext, (1060, 502))
        # audio
        screen.blit(audio, (1020, 540))
        screen.blit(auidotext, (1060, 542))

        # border
        grey = (128, 128, 128)  # white
        white = (255, 255, 255)

        # game border for the player
        pygame.draw.rect(screen, grey, (0, 0, 1000, 900), 8)  # width=3
        pygame.draw.rect(screen, white, (8, 8, 984, 884), 3)

        # border for the status
        pygame.draw.rect(screen, grey, (1000, 0, 800, 900), 8)
        # draw line
        # border for the options
        pygame.draw.line(screen, white, (1008, 395), (1400, 395), 3)  # white line for depth effect for the grey border
        pygame.draw.line(screen, grey, (1000, 400), (1400, 400), 8)
        pygame.draw.line(screen, white, (1008, 408), (1008, 890), 3)  # white line for depth effect for the grey border
        pygame.draw.line(screen, white, (1008, 406), (1400, 406), 3)

        pygame.display.flip()

def options():
    clock = pygame.time.Clock()

    # --------------------Player name changes ----------------------
    #basic font for user typed
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    player1_text = ''
    player2_text = ''
    player3_text = ''
    player4_text = ''
    # Create rectangle
    input_rect = pygame.Rect(200, 200, 140, 32)
    player1_text_rect = pygame.Rect(400, 200, 150, 20)
    # color active stores color(White) which will get active when input box is clicked by user
    color_active = pygame.Color('White')
    # color_passive store color(chartreuse4)which is color of input box
    color_passive = pygame.Color('grey')
    color = color_passive
    # --------------------------------------------------------------
    active = False
    while True:

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("Black")

        # OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "White")
        # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        # screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        #------------------------  Back Button -----------------------
        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)
        #-------------------------------------------------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                    player1_text = player1_text[:-1]
                    player2_text = player2_text[:-1]
                    player3_text = player3_text[:-1]
                    player4_text = player4_text[:-1]
                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode
                    player1_text += event.unicode
                # it will set background color of screen
            # screen.fill((255, 255, 255))
        get_text_box(active, color_active, color_passive, input_rect, base_font, player1_text)
        #=====================  NEED TO WORK ON IT BUT, NOT NOW - FIX THE PLAYER MOVEMENT THEN WORK ON THIS  =========================
        pygame.display.update()
# To open file directory
def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.py')])
   if file:
      content = file.read()
      file.close()
      print("%d characters in this file" % len(content))


def main_menu():
    while True:
        screen.blit(BG, (0, 0))
        # Start playing the song

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(75).render("AT-Robot", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(700, 100))

        PLAY_BUTTON = Button(image=pygame.image.load(resource_path("assets/Play Rect.png")), pos=(300, 800),
                             text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load(resource_path("assets/Play Rect.png")), pos=(700, 800),
                                text_input="OPTION", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(resource_path("assets/Quit Rect.png")), pos=(1100, 800),
                             text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        #Player button to browse assembly file
        UPLOAD_TEXT = get_font(20).render("Upload your code here", True, "White")
        UPLOAD_RECT = UPLOAD_TEXT.get_rect(center=(700, 300))
        screen.blit(UPLOAD_TEXT, UPLOAD_RECT)
        PLAYER_FILE1 = Button(image=pygame.image.load(resource_path("assets/Play Rect1.png")), pos=(500, 400),
                             text_input="PLAYER1", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        PLAYER_FILE2 = Button(image=pygame.image.load(resource_path("assets/Play Rect1.png")), pos=(900, 400),
                              text_input="PLAYER2", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        PLAYER_FILE3 = Button(image=pygame.image.load(resource_path("assets/Play Rect1.png")), pos=(500, 500),
                              text_input="PLAYER3", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        PLAYER_FILE4 = Button(image=pygame.image.load(resource_path("assets/Play Rect1.png")), pos=(900, 500),
                              text_input="PLAYER4", font=get_font(30), base_color="#d7fcd4", hovering_color="White")


        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, PLAYER_FILE1, PLAYER_FILE2, PLAYER_FILE3, PLAYER_FILE4]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAYER_FILE1.checkForInput(MENU_MOUSE_POS):
                    open_file()
                if PLAYER_FILE2.checkForInput(MENU_MOUSE_POS):
                    open_file()
                if PLAYER_FILE3.checkForInput(MENU_MOUSE_POS):
                    open_file()
                if PLAYER_FILE4.checkForInput(MENU_MOUSE_POS):
                    open_file()
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                # border


        grey = (128, 128, 128)  # white
        white = (255, 255, 255)

        # game border for the player
        pygame.draw.rect(screen, grey, (0, 0, 1400, 900), 8)  # width=3
        pygame.draw.rect(screen, white, (8, 8, 1384, 884), 3)

        # Border for the button
        pygame.draw.rect(screen, grey, (300, 200, 800,400 ), 15) #Grey border
        pygame.draw.rect(screen, white, (315, 215, 775, 375), 4) #white border
        pygame.display.flip()
        pygame.display.update()


main_menu()
        # print(len(bullet_group[1]))
# # Starting the mixer
#
# mixer.init()
#
# # Loading the song
# mixer.music.load("assets/POL-guilty-one-short.wav")
#
# # Setting the volume
# mixer.music.set_volume(0.7)
# mixer.music.play()