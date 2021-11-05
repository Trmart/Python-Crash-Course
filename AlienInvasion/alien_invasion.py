import pygame
from settings import Settings
from ship import Ship
from game_functions import game_functions, update_screen

def run_game():
    #init game and create our screen obj
    pygame.init() #initializes game 
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #creates our screen object and sets window dimensions (x,y) 
    pygame.display.set_caption('Alien Invasion') #sets a caption for our window title bar

    #creates an instance of our ship class 
    ship = Ship(screen)

    #start the main game loop
    while True:
        #watch for keyboard and mouse events, calls game function class
        game_functions()

        #update screen 
        update_screen(ai_settings,screen,ship)

        #make the most recently drawn screen visible
        pygame.display.flip()

def main():
   
    run_game()

if(__name__=='__main__'):
    main()

