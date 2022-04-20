import pygame
import time

pygame.init()
pygame.mixer.init()

def play_audio(file_name):
    print("----- AUDIO : Audio being played... -----\n")
    pygame.mixer.music.load("/home/pi/Smart_Door_Lock/sound/"+file_name+".mp3")
    pygame.mixer.music.play()
    time.sleep(3)
