import pygame
from Player import Player

pygame.init()
clock = pygame.time.Clock()



# ------robot[0] movement with streering -----
clock.tick(60)
image1 = "Images/robot.png"
robot = Player(image1, 50)

def movement(robot):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        robot.position += robot[0].direction
    if keys[pygame.K_s]:
        robot.position -= robot[0].direction
    if keys[pygame.K_a]:
        robot.direction.rotate_ip(-1)
    if keys[pygame.K_d]:
        robot.direction.rotate_ip(1)
    robot_angle = robot.direction.angle_to((1, 0))
    rotated_robot = pygame.transform.rotate(robot.image, robot_angle)
    return rotated_robot

# --------------------------