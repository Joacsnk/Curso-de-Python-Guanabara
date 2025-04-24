import pygame
pygame.init() # Usando o pygame para iniciar
pygame.mixer.music.load('songs\shiloy.mp3')
pygame.mixer.music.play() # Tocando...
x = input('\33[33mDigite algo para parar: \33[m')
