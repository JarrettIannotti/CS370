import winsound
import random
import pygame

class Sound():
    pygame.mixer.init()
    def __init__(self):
        self.freq = random.randint(500, 1500)
        print('Setting frequency of ', self.freq)

    def playsound(self):
        print('playing sound')
        crash_sound = pygame.mixer.Sound("gutfire.mp3")
        crash_sound.play()
