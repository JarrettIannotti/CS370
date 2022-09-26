import pygame
CLOCK = pygame.time.Clock()
class Bullet(pygame.sprite.Sprite):

    def __init__ (self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect(center =(pos_x, pos_y))

    def update(self):
        self.rect.y -= 29



        CLOCK.tick(120)


