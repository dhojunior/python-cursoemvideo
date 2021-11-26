'''import Play_mp3
#Importante colcar o arquivo dentro da pasta de projetos
Play_mp3.play(r'ex021.mp3') #Difícil essa Hein!'''

import pygame
pygame.init()
pygame.mixer.music.load('Feriadonacional.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('CURTE O SOM PIVETE')#Precisa do input pra funcionar certinho


