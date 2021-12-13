import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_functions import check_events, update_screen,update_bullets

def run_game():
    #init game and create our screen obj
    pygame.init() #initializes game 
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #creates our screen object and sets window dimensions (x,y) 
    pygame.display.set_caption('Alien Invasion') #sets a caption for our window title bar

    #creates an instance of our ship class 
    ship = Ship(ai_settings,screen)

    #creates a group, functioning like a list, to manage bullets fired
    bullets = Group()

    #start the main game loop
    while True:
        #watch for keyboard and mouse events, calls game function class
        check_events(ai_settings,screen,ship,bullets)
        #checks to see if play is holding down movement keys, updates ship position
        ship.update_ship()
        #update bullet position if in bullets
        update_bullets(bullets)
        #update screen 
        update_screen(ai_settings,screen,ship,bullets)

        #make the most recently drawn screen visible
        pygame.display.flip()

def main():
   
    run_game()

if(__name__=='__main__'):
    main()

