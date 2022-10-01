import pygame
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, color, Xcoord, Ycoord, health):  # Set by game initializer, initiates a player object
        self.color = color
        self.Xcoord = Xcoord
        self.Ycoord = Ycoord
        self.health = health
        # might need more settings/config. Also this init could handle sprites or it can be a seperate file?

    def ImHit(self):  # Method for getting hit
        self.health = - 10

    def Movement(self, angle):  # Moves Player
        self.Xcoord += math.cos(angle)
        self.Ycoord += math.sin(angle)
        # Need to add collision detection

    # Example movement begins here

    # The "command" dict will verify the user typed the right command and then call the proper function. The key will
    # be the command and the function call is the value We can nest multiple dicts within the same one so we can
    # check for proper syntax later. (see "Something else" key)
    commands = {
        "NOP": nop,
        "ADD": add,
        "Something else": {
            "Testing": "Second dict value"
        }
    }

    def nop(self):
        print("YO")

    def add(self, a, b):
        print("Currently in add")
        c = a + b
        print(c)

    def readLine(self, command):
        # We would change "NOP" and "ADD" to command this is just an example
        if commands.__contains__("NOP"):
            commands["NOP"]()
        elif commands.__contains__("ADD"):
            commands["ADD"](1, 2)
        elif commands["Something else"].__contains__("Testing"):
            print("YOO")

    # End example movement
# Add these all to a group eventually with all_sprites_list = pygame.sprite.Group()
# Then all_sprites_list.add(object_) ON https://www.geeksforgeeks.org/pygame-creating-sprites/
# https://stackoverflow.com/questions/61088785/pygame-trying-to-understand-the-sprite-class
