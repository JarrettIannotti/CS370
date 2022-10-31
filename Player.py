import pygame
from Bullet import Bullet
import random
import pygame.freetype
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
        self.current_health = 300
        self.maximum_health = 300
        self.health_bar_length = 300
        self.health_ratio = self.maximum_health / self.health_bar_length
        self.rect.x = self.center[0]
        self.rect.y = self.center[1]

    def update(self, screen,color, x, y):
        self.basic_health(screen, color, x, y)

    def move(self, x, y):
        self.center[0] += x
        self.center[1] += y

        self.rect.x = self.center[0]
        self.rect.y = self.center[1]

    def draw(self, surf):
        surf.blit(self.image, self.center)

    def create_bullet(self, angle):
        return Bullet(self.center[0]+32, self.center[1]+32, angle)

    # def ImHit(self):  # Method for getting hit
    #     self.health = - 10
    #     self.kill()


    def get_health(self, amount):
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0

    def basic_health(self, screen, color, x, y):
        pygame.draw.rect(screen, color, (x, y, self.current_health/self.health_ratio, 25))
        pygame.draw.rect(screen, (255, 255, 255), (x, y, self.health_bar_length, 25), 4)

