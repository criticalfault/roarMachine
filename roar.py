import time
import pygame



pygame.init()

def roar():
    pygame.mixer.music.load('roar.mp3')
    pygame.mixer.music.play()
    time.sleep(10)
    
roar()