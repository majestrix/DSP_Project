import pygame
from gtts import gTTS as tts
import os

class myTTS:
    
    def __init__(self):
        self.path = os.path.dirname(__file__) + "/playback.mp3"
        pygame.mixer.init()

    def playText(self,text):
        sound = tts(text,'en')
        sound.save(self.path)
        soundfile = open(self.path,"r")
        pygame.mixer.music.load(soundfile)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
        soundfile.close()
    
    def close(self):
        os.remove(self.path)
