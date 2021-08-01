# Faça um programa em python que abra e reproduza o áudio de um arquivo mp3. #

import pygame
pygame.mixer.init()
pygame.mixer.music.load('tz.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
