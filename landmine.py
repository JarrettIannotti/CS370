import pygame
import math


class Landmine(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y,color, angle):
        super().__init__()
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.angle = angle

        self.floating_point_x = pos_x
        self.floating_point_y = pos_y

    def update(self):

        self.rect.x = self.floating_point_x
        self.rect.y = self.floating_point_y

    def removeLandmine(self):
            self.kill()