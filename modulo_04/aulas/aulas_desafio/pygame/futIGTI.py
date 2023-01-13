# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:50:46 2023

@author: Kamila
"""

import pygame

pygame.init()

width_player = 104
height_player = 226

width_ball = 50
height_ball = 50

width_field = 1132
height_field = 768

window = pygame.display.set_mode([width_field, height_field])
window_title = pygame.display.set_caption('Fute IGTI')

field = pygame.image.load('assets/field.png')
player1 = pygame.image.load('assets/player1.png')
player2 = pygame.image.load('assets/player2.png')
ball = pygame.image.load('assets/ball.png')

ball_x = (width_field - width_ball)/2
ball_y = ((height_field/2) - width_ball) + 10
player1_y = (height_field/2) - width_player
player2_y = (height_field/2) - width_player

player_moveup = False
player_movedown = False

def move_player():
    global player1_y
    max_down = height_field - height_player
    
    if player_moveup:
        player1_y -= 5
    else:
        player1_y += 0
        
    if player_movedown:
        player1_y += 5
    else:
        player1_y += 0
        
    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= max_down:
        player1_y = max_down

 
def move_ball():
    global ball_x
    global ball_y
    
    ball_x += 1

def drawn():
    window.blit(field, (0, 0))
    window.blit(player1, (width_player, player1_y))
    window.blit(player2, (width_field - (2*width_player), player2_y))
    window.blit(ball, (ball_x, ball_y))

loop = True

while loop:
    
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player_moveup = True
            if events.key == pygame.K_s:
                player_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player_moveup = False
            if events.key == pygame.K_s:
                player_movedown = False
            
    drawn()
   #move_ball()
    move_player()
    pygame.display.update()