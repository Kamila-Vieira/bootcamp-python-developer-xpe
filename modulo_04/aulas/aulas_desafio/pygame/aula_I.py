# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:50:46 2023

@author: Kamila
"""

import pygame

pygame.init()

window = pygame.display.set_mode([1132, 768])
window_title = pygame.display.set_caption('Fute IGTI')

field = pygame.image.load('assets/field.png')
window.blit(field, (0, 0))

loop = True

while loop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    pygame.display.update()