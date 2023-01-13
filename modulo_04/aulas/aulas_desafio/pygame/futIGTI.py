# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:50:46 2023

@author: Kamila
"""

import pygame

pygame.init()

window = pygame.display.set_mode([1132, 768])
window_title = pygame.display.set_caption('Fute IGTI')

field = pygame.image.load('assets/field.png') # largura = 1132 / altura = 768
player1 = pygame.image.load('assets/player1.png') # largura = 104 / altura = 226
player2 = pygame.image.load('assets/player2.png') # largura = 104 / altura = 226
ball = pygame.image.load('assets/ball.png') # largura = 50 / altura = 50

ball_x = 541 # ponto inicial X => (larguraF-larguraB)/2
ball_y = 344 # ponto inicial Y => ((alturaF/2) - larguraB) + 10

def move_ball():
    global ball_x
    global ball_y
    
    ball_x += 1

def drawn():
    window.blit(field, (0, 0))
    window.blit(player1, (104, 280)) # (larguraP1, (alturaF/2) - larguraP1)
    window.blit(player2, (924, 280)) # (larguraF - (2*larguraP2), (alturaF/2) - larguraP2)
    window.blit(ball, (ball_x, ball_y))

loop = True

while loop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            
    drawn()
    move_ball()
    pygame.display.update()