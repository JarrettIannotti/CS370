import pygame
import math
from Sound import Sound

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, angle):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
        self.angle = angle

        self.floating_point_x = pos_x
        self.floating_point_y = pos_y

        velocity = 5
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity

    def update(self):
        self.floating_point_x += self.change_x
        self.floating_point_y += self.change_y

        self.rect.x = self.floating_point_x
        self.rect.y = self.floating_point_y

        if self.rect.bottom < -35:
            self.kill()
        elif self.rect.bottom > 850:
            self.kill()

    def checkCollision(self, player):
        return pygame.sprite.spritecollideany(self, player)
    def removeBullet(self, player):
        if self.checkCollision(player):
            self.kill()





