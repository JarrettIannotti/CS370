import winsound
import random

class Sound():

    def __init__(self):
        self.freq = random.randint(500, 1500)
        print('Setting frequency of ', self.freq)

    def playsound(self):
        print('playing sound')
        winsound.Beep(self.freq, 100)

