import pygame
import math
from Sound import Sound

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, targetx, targety):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
        self.tar_x = targetx
        self.tar_y = targety

        self.floating_point_x = pos_x
        self.floating_point_y = pos_y

        x_diff = self.tar_x - pos_x
        y_diff = self.tar_y - pos_y
        angle = math.atan2(y_diff, x_diff)

        velocity = 5
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity



    def update(self):
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x

        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)



