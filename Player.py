import pygame
from Bullet import Bullet
from landmine import Landmine
import random
import pygame.freetype


pygame.init()

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
        self.position = pygame.math.Vector2(self.center[0], self.center[1])
        self.direction = pygame.math.Vector2(10,0)
        self.movement()

    def update(self, screen,color, x, y):
        self.basic_health(screen, color, x, y)
#

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position += self.direction
        if keys[pygame.K_s]:
            self.position -= self.direction
        if keys[pygame.K_a]:
            self.direction.rotate_ip(-1000)
        if keys[pygame.K_d]:
            self.direction.rotate_ip(1000)
        self.robot_angle = self.direction.angle_to((20, 20))
        self.rotated_robot = pygame.transform.rotate(self.image, self.robot_angle)


    def move(self,x, y):
        self.center[0] += x
        self.center[1] += y


        self.rect.x = self.center[0]
        self.rect.y = self.center[1]

        pass

    def draw(self, surf):

        surf.blit(self.rotated_robot, self.rotated_robot.get_rect(center=(round(self.position.x), round(self.position.y))))

    def create_bullet(self, angle):
        return Bullet(self.center[0]+32, self.center[1]+32, angle)

    def create_landmine(self,color,angle):
        return Landmine(self.center[0]+32, self.center[1]+32, color,angle)

    # def ImHit(self):  # Method for getting hit
    #     self.health = - 10
    #     self.kill()
    def kill(self):

            pygame.sprite.Sprite.kill(self)

    def lose_health(self, amount):
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0



    def basic_health(self, screen, color, x, y):
        pygame.draw.rect(screen, color, (x, y, self.current_health/self.health_ratio, 25))
        pygame.draw.rect(screen, (255, 255, 255), (x, y, self.health_bar_length, 25), 4)

