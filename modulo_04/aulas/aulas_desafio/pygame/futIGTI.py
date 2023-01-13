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

player1_moveup = False
player1_movedown = False
player2_moveup = False
player2_movedown = False

ball_dir_x = -3
ball_dir_y = 1
max_down = height_field - height_player

def move_player1():
    global player1_y

    if player1_moveup:
        player1_y -= 5
    else:
        player1_y += 0
        
    if player1_movedown:
        player1_y += 5
    else:
        player1_y += 0
        
    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= max_down:
        player1_y = max_down
        
def move_player2():
    global player2_y
    player2_y = ball_y
    
    if player2_y <= 0:
        player2_y = 0
    elif player2_y >= max_down:
        player2_y = max_down

def move_ball():
    global ball_x
    global ball_y
    global ball_dir_x
    global ball_dir_y
    
    ball_x += ball_dir_x
    ball_y += ball_dir_y
    
    if ball_x < (width_player*2) - 23:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_dir_x *= -1
    
    if ball_x > width_field - (2*width_player):
        if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_dir_x *= -1   
    
    if ball_y > 685:
        ball_dir_y *= -1
    elif ball_y <= 0:
        ball_dir_y *= -1
        
    
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
                player1_moveup = True
            if events.key == pygame.K_s:
                player1_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_moveup = False
            if events.key == pygame.K_s:
                player1_movedown = False
            
    drawn()
    move_ball()
    move_player1()
    move_player2()
    pygame.display.update()