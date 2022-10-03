import pygame
from Bullet import Bullet
import random

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/robot.png")
        self.rect = self.image.get_rect()
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.center = [self.x, self.y]

    def move(self, x, y):
        self.center[0] += x
        self.center[1] += y

    def draw(self, surf):
        surf.blit(self.image, self.center)

    def create_bullet(self, pos_x, pos_y):
        return Bullet(self.center[0]+32, self.center[1]+15, pos_x, pos_y)