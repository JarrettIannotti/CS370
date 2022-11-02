import pygame
from Bullet import Bullet
import random
import math


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
        self.current_health = 1000
        self.maximum_health = 1000
        self.health_bar_length = 400
        self.health_ratio = self.maximum_health / self.health_bar_length
        self.rect.x = self.center[0]
        self.rect.y = self.center[1]
        self.position = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(5, 0)

        # Registers
        self.ax = 0
        self.bx = 0
        self.cx = 0
        self.dx = 0

        # Constants
        self.p_throttle = 10
        self.p_steering = 3
        self.p_weapon = 3
        self.p_scanarc = 0
        self.p_scan = 0
        self.p_random = 10

        # this is a dictionary of our registers
        self.registers = {
            "ax": self.ax,
            "bx": self.bx,
            "cx": self.cx,
            "dx": self.dx,
        }
        # this is a dictionary for constants
        self.constants = {
            "p_scanarc": self.p_scanarc,
            "p_throttle": self.p_throttle,
            "p_steering": self.p_steering,
            "p_scan": self.p_scan,
            "p_weapon": self.p_weapon,
            "p_random": self.p_random,
        }

        # This is a dictionary of commands, functions go here
        self.commands = {
            "mov": self.mov,
            "opo": self.opo,
            "ipo": self.ipo,
            "mod": self.mod,
            "neg": self.neg,
        }

    ##########################################################################################
    ### ROBOT LOGIC                                                                        ###
    ##########################################################################################

    def update(self, screen, color, x, y):
        self.basic_health(screen, color, x, y)

    def move(self, x, y, screen):
        # self.center[0] += x
        # self.center[1] += y

        #self.direction.rotate_ip(-1)
        self.direction.rotate_ip(4)
        angle = self.direction.angle_to((1, 0))
        rotated_robot = pygame.transform.rotate(self.image, angle)
        self.rect = rotated_robot.get_rect(center = (round(self.position.x), round(self.position.y)))

        #self.center[0] += math.sin(90) * (x/10)
        #self.center[1] += math.cos(90) * (y/10)
        # x = pygame.transform.rotate(self.image, 25)
        # #self.rect = x.get_rect(self.rectx)
        #
        # self.image = pygame.transform.rotate(self.image, self.p_steering)
        # self.angle += self.change_angle
        # self.angle = self.angle % 360
        # self.rect = self.image.get_rect(center=self.rect.center)
        # self.rect.x = self.center[0]
        # self.rect.y = self.center[1]

    def draw(self, surf):
        surf.blit(self.image, self.center)

    def create_bullet(self, angle):
        return Bullet(self.center[0] + 32, self.center[1] + 32, angle)

    # def ImHit(self):  # Method for getting hit
    #     self.health = - 10
    #     self.kill()

    def get_health(self, amount):
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0

    def basic_health(self, screen, color, x, y):
        pygame.draw.rect(screen, color, (x, y, self.current_health / self.health_ratio, 25))
        pygame.draw.rect(screen, (255, 255, 255), (x, y, self.health_bar_length, 25), 4)

    ##########################################################################################
    ### PARSER                                                                             ###
    ##########################################################################################

    def newParseIdea(self, string):
        '''
        string : (Instruction) (Register | Constant) ^ (Constant | Register | INT number)
        '''
        # mov ax 10
        # our ex string is ["mov", "ax", "10"]
        # if the string in the first index is in commands it will go into here
        if string[0] in self.commands:
            # if the string in the first index is "mov" we will move forward assuming the syntax is correct for mov
            if string[0] == "mov":
                self.commands["mov"](string[1], string[2])
            # [OPO N1 N2] Outputs N2 to port N1
            elif string[0] == "opo":
                print("in opo")
                self.commands[string[0]](string[1], string[2])
            elif string[0] == "ipo":
                self.commands[string[0]](string[1], string[2])
            elif string[0] == "mod":
                self.commands[string[0]](string[1], string[2])
            elif string[0] == "neg":
                self.commands[string[0]](string[1])

    # [MOV V N] Sets V = N
    def mov(self, v, n):
        if v in self.registers:
            if n in self.registers:
                self.registers[v] = self.registers[n]
            elif n in self.constants:
                self.registers[v] = self.constants[n]
            elif n.isnumeric():
                self.registers[v] = n
        elif v in self.constants:
            if n in self.registers:
                self.constants[v] = self.registers[n]
            elif n in self.constants:
                self.constants[v] = self.constants[n]
            elif n.isnumeric():
                self.constants[v] = n

    # [OPO N1 N2] Outputs N2 to port N1
    def opo(self, n1, n2):
        if n1 in self.constants:
            if n2 in self.constants:
                self.constants[n1] = self.constants[n2]
                print(f"TEST:{self.constants[n1]}")
            elif n2.isnumeric():
                print(f"TEST:{self.constants[n1]}")
                self.constants[n1] = n2

    # [IPO N V] Inputs number from port N, result into V
    def ipo(self, n, v):
        if n in self.constants:
            if v in self.constants:
                self.constants[v] = self.constants[n]
                print(self.constants[v])
            elif v.isnumeric():
                self.constants[v] = n
            elif v in self.registers:
                self.registers[v] = self.constants[n]

    # [MOD V N] MOD's V & N, result stored in V (modulus)
    def mod(self, v, n):
        if v in self.constants:
            if n in self.constants:
                self.constants[v] = int(self.constants[v]) % int(self.constants[n])
            elif n.isnumeric():
                self.constants[v] = int(self.constants[v]) % int(n)
            elif n in self.registers:
                self.constants[v] = int(self.constants[v]) % int(self.registers[n])
        elif v in self.registers:
            if n in self.constants:
                self.registers[v] = int(self.registers[v]) % int(self.constants[n])
            elif n.isnumeric():
                self.registers[v] = int(self.registers[v]) % int(n)
            elif n in self.registers:
                self.registers[v] = int(self.registers[v]) % int(self.registers[n])

    # [NEG V] Negates V: V = 0-V (aka "two's compliment")
    def neg(self, v):
        if v in self.constants:
            self.constants[v] = int(self.constants[v]) * -1
        if v in self.registers:
            self.registers[v] = int(self.registers[v]) * -1

    def printRegisters(self):
        print("ax: ", self.ax)
        print("bx: ", self.bx)
        print("cx: ", self.cx)
        print("dx: ", self.dx)
# # this is the string we will pass into the function to parse (it is just one example line)
# string = "mov                ax                10"
# # split the string into individual words so that we can figure out each word individually
# # .split also removes white spaces
# stringList = string.split()sdasd
# print(stringList)
#
# # Pass the stringList to new parse idea
# newParseIdea(stringList)
# newParseIdea(["opo", "p_throttle", "p_weapon"])
# print(f"p_throttle: {p_throttle}")
# newParseIdea(["mod", "p_random", "2"])
# print(p_random)
# newParseIdea(["neg", "p_random"])
# print(p_random)
