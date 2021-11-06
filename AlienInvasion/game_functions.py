from typing import Tuple
import pygame #pygame add game functionality 
import sys #we use system to exit the game window when a player quits

def check_events(ship):
    """creates a function to poll game events"""
    """responds to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

    
def check_keyup_events(event,ship):
    """function that responds to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_keydown_events(event,ship):
    """function that responds to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

def update_screen(ai_settings,screen,ship):
    """updates screen, fills background color, and draws ship game obj"""
    #redraws and fills screen with bg_color during each pass through loop 
    screen.fill(ai_settings.bg_color)
    
    #draw our ship object 
    ship.blitme()