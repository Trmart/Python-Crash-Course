import pygame #pygame add game functionality 
import sys #we use system to exit the game window when a player quits

def game_functions():
    """creates a function to poll game events"""
    """responds to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
def update_screen(ai_settings,screen,ship):
    
    #redraws and fills screen with bg_color during each pass through loop 
    screen.fill(ai_settings.bg_color)
    
    #draw our ship object 
    ship.blitme()