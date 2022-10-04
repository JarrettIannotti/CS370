import pygame
from Bullet import Bullet
import random

class Player(pygame.sprite.Sprite):

    def __init__(self, fileContent):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/robot.png")
        self.rect = self.image.get_rect()
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.center = [self.x, self.y]
        self.fileContent = fileContent

    def move(self, x, y):
        self.center[0] += x
        self.center[1] += y

    def draw(self, surf):
        surf.blit(self.image, self.center)

    def create_bullet(self, pos_x, pos_y):
        return Bullet(self.center[0]+32, self.center[1]+15, pos_x, pos_y)

    def getFileContent(self):
        print(self.fileContent)

# import pygame
# import math
#
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self, color, Xcoord, Ycoord, health):  # Set by game initializer, initiates a player object
#         self.color = color
#         self.Xcoord = Xcoord
#         self.Ycoord = Ycoord
#         self.health = health
#         # might need more settings/config. Also this init could handle sprites or it can be a seperate file?
#
#     def ImHit(self):  # Method for getting hit
#         self.health = - 10
#
#     def Movement(self, angle):  # Moves Player
#         self.Xcoord += math.cos(angle)
#         self.Ycoord += math.sin(angle)
#         # Need to add collision detection
#
#     # Example movement begins here
#
#     # The "command" dict will verify the user typed the right command and then call the proper function. The key will
#     # be the command and the function call is the value We can nest multiple dicts within the same one so we can
#     # check for proper syntax later. (see "Something else" key)
#     commands = {
#         "NOP": nop,
#         "ADD": add,
#         "Something else": {
#             "Testing": "Second dict value"
#         }
#     }
#
#     def nop(self):
#         print("YO")
#
#     def add(self, a, b):
#         print("Currently in add")
#         c = a + b
#         print(c)
#
#     def readLine(self, command):
#         # We would change "NOP" and "ADD" to command this is just an example
#         if commands.__contains__("NOP"):
#             commands["NOP"]()
#         elif commands.__contains__("ADD"):
#             commands["ADD"](1, 2)
#         elif commands["Something else"].__contains__("Testing"):
#             print("YOO")
#         # this would be how it is done
#         if command in commands:
#             'Do the commands'
#
#     # End example movement
#
#     # Example file reading
#     # This would go in main window or spawner or wherever we handle that
#         # playerList would just be a list of file paths we are loading from
#         for filePath in playerList:
#             try:
#                 # using with we don't need to close the file it handles that for us
#                 with open("filename.txt") as file:
#                     contents = file.read()
#                     # we would pass the entire file contents to the player when its loaded so each player
#                     # holds its own file contents
#                     player(color, Xcoord, Ycoord, health, contents)
#             # if the file doesn't exist it prints and error and exits the program
#             except FileNotFoundError:
#                     print("THE FILE IS NOT FOUND")
#                     exit()
#     # Example file reading ends here
#
#
# # Add these all to a group eventually with all_sprites_list = pygame.sprite.Group()
# # Then all_sprites_list.add(object_) ON https://www.geeksforgeeks.org/pygame-creating-sprites/
# https://stackoverflow.com/questions/61088785/pygame-trying-to-understand-the-sprite-class