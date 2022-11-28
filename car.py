import pygame
import math
from Bullet import Bullet
import random
import pygame.freetype

class CarSprite( pygame.sprite.Sprite ):
    """ Car Sprite with basic acceleration, turning, braking and reverse """

    def __init__( self, car_image, x, y, rotations=360 ):
        """ A car Sprite which pre-rotates up to <rotations> lots of
            angled versions of the image.  Depending on the sprite's
            heading-direction, the correctly angled image is chosen.
            The base car-image should be pointing North/Up.          """
        pygame.sprite.Sprite.__init__(self)
        # Pre-make all the rotated versions
        # This assumes the start-image is pointing up-screen
        # Operation must be done in degrees (not radians)
        self.rot_img   = []
        self.min_angle = ( 360 / rotations )
        for i in range( rotations ):
            # This rotation has to match the angle in radians later
            # So offet the angle (0 degrees = "north") by 90° to be angled 0-radians (so 0 rad is "east")
            rotated_image = pygame.transform.rotozoom( car_image, 360-90-( i*self.min_angle ), 1 )
            self.rot_img.append( rotated_image )
        self.min_angle = math.radians( self.min_angle )   # don't need degrees anymore
        # define the image used
        self.image       = self.rot_img[0]
        self.rect        = self.image.get_rect()
        self.rect.center = ( x, y )
        # movement
        self.reversing = False
        self.heading   = 0                           # pointing right (in radians)
        self.speed     = 0
        self.velocity  = pygame.math.Vector2( 0, 0 )
        self.position  = pygame.math.Vector2( x, y )

    def turn( self, angle_degrees ):
        """ Adjust the angle the car is heading, if this means using a
            different car-image, select that here too """
        ### TODO: car shouldn't be able to turn while not moving
        self.heading += math.radians( angle_degrees )
        # Decide which is the correct image to display
        image_index = int( self.heading / self.min_angle ) % len( self.rot_img )
        # Only update the image if it's changed
        if ( self.image != self.rot_img[ image_index ] ):
            x,y = self.rect.center
            self.image = self.rot_img[ image_index ]
            self.rect  = self.image.get_rect()
            self.rect.center = (x,y)

    def accelerate( self, amount ):
        """ Increase the speed either forward or reverse """
        if ( not self.reversing ):
            self.speed += amount
        else:
            self.speed -= amount

    def brake( self ):
        """ Slow the car by half """
        self.speed /= 2
        if ( abs( self.speed ) < 0.1 ):
            self.speed = 0

    def reverse( self ):
        """ Change forward/reverse, reset any speed to 0 """
        self.speed     = 0
        self.reversing = not self.reversing

    def update( self ):
        """ Sprite update function, calcualtes any new position """
        self.velocity.from_polar( ( self.speed, math.degrees( self.heading ) ) )
        self.position += self.velocity
        self.rect.center = ( round(self.position[0]), round(self.position[1] ) )

    # def draw(self, surf):
    #
    #     surf.blit(self.rotated_robot, self.rotated_robot.get_rect(center=(round(self.position.x), round(self.position.y))))

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
