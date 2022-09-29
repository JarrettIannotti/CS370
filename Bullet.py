import pygame
from Sound import Sound
CLOCK = pygame.time.Clock()
class Bullet(pygame.sprite.Sprite):

    #Constructor
    def __init__ (self, pos_x, pos_y, bearing):
        super().__init__()
        self.x = pos_x
        self.y= pos_y
        self.rect = self.image.get_rect(center =(self.x, self.y))
        self.bearing = bearing


    def update(self):
        self.rect.y -= 29

    def shoot(self, ):

