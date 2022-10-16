import pygame
from Bullet import Bullet
import random

class Player(pygame.sprite.Sprite):

    def __init__(self, image, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.radius = 32
        # self.circle = pygame.draw.circle(self.image, "Red", self.rect.center, self.radius)
        self.x = random.randint(64, 736)
        self.y = random.randint(64, 536)
        self.center = [self.x, self.y]
        self.health = health
        self.rect.x = self.center[0]
        self.rect.y = self.center[1]


    def move(self, x, y):
        self.center[0] += x
        self.center[1] += y

        self.rect.x = self.center[0]
        self.rect.y = self.center[1]

    def draw(self, surf):
        surf.blit(self.image, self.center)

    def create_bullet(self, angle):
        return Bullet(self.center[0]+32, self.center[1]+32, angle)

    def ImHit(self):  # Method for getting hit
        self.health = - 10
        self.kill()
