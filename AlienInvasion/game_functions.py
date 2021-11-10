from typing import Tuple
import pygame #pygame add game functionality 
import sys #we use system to exit the game window when a player quits
from bullet import Bullet


def check_events(ai_settings,screen,ship,bullets):
    """creates a function to poll game events"""
    """responds to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

    
def check_keyup_events(event,ship):
    """function that responds to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """function that responds to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
      fire_bullet(ai_settings,screen,ship,bullets)

def update_screen(ai_settings,screen,ship,bullets):
    """updates screen, fills background color, and draws ship game obj"""
    #redraws and fills screen with bg_color during each pass through loop 
    screen.fill(ai_settings.bg_color)
    
    #draw our ship object 
    ship.blitme()

    #draw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
def update_bullets(bullets):
    """update position of bullets and deletes old ones"""
    bullets.update()

    #delete old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings,screen,ship,bullets):
    """function to fire bullet if limit not yet reached"""
    #check for number of bullets in our bullets Group()
    #if the numb of bullets in bullets Group < allowed_bullets
    if len(bullets) < ai_settings.bullets_allowed:
        #create a new bullet
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)