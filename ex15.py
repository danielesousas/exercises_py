#EXERCÍCIO_15: TOCANDO MP3

import pygame
pygame.init()
pygame.mixer.music.load('ex15.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

#FUNÇÃO DA BIBLIOTECA PYGAME ^3^