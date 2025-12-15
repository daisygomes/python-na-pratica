# Tocando uma música
import pygame
pygame.init()
pygame.mixer.music.load('exer22.mp3')
pygame.mixer.music.play()
pygame.event.wait()