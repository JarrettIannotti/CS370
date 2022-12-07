import winsound
import random
import pygame

import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Sound():
    pygame.mixer.init()
    def __init__(self):
        self.freq = random.randint(500, 1500)
        print('Setting frequency of ', self.freq)

    def playsound(self):
        print('playing sound')
        crash_sound = pygame.mixer.Sound(resource_path("assets/gunfire.mp3"))
        crash_sound.play()
