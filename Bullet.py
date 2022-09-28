import pygame
import sound
CLOCK = pygame.time.Clock()
class Bullet(pygame.sprite.Sprite):

    #Constructor
    def __init__ (self, pos_x, pos_y, bearing):
        super().__init__()
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect(center =(pos_x, pos_y))
        self.bearing = bearing

    def update(self):
        self.rect.y -= 29

    def shoot(self, ):



        CLOCK.tick(120)