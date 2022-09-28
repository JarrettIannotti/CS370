import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self,color,Xcoord,Ycoord,health):
        self.color = color
        self.Xcoord = Xcoord
        self.Ycoord = Ycoord
        self.health = 100

    def ImHit(self):
        health =- 10

    def Movement(self,angle):
        Xcoord += cos(angle)
        Ycoord += sin(angle)

# Add these all to a group eventually with all_sprites_list = pygame.sprite.Group()
# Then all_sprites_list.add(object_) ON https://www.geeksforgeeks.org/pygame-creating-sprites/
#https://stackoverflow.com/questions/61088785/pygame-trying-to-understand-the-sprite-class