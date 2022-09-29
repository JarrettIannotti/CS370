import pygame
from math import *
from Sound import Sound

class Bullet(pygame.sprite.Sprite):

    def __init(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 50))
        self.image.fill(255, 255, 255)
        self.rect = self.image.get_rect(center = (x, y))

    def update(self):
        self.rect.y += 5



