import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self,color,Xcoord,Ycoord,health):      #Set by game initializer, initiates a player object
        self.color = color
        self.Xcoord = Xcoord
        self.Ycoord = Ycoord
        self.health = health
        #might need more settings/config. Also this init could handle sprites or it can be a seperate file?
    def ImHit(self):                                    #Method for getting hit
        self.health =- 10

    def Movement(self,angle):                           #Moves Player
        self.Xcoord += math.cos(angle)
        self.Ycoord += math.sin(angle)
            #Need to add collision detection


# Add these all to a group eventually with all_sprites_list = pygame.sprite.Group()
# Then all_sprites_list.add(object_) ON https://www.geeksforgeeks.org/pygame-creating-sprites/
# https://stackoverflow.com/questions/61088785/pygame-trying-to-understand-the-sprite-class