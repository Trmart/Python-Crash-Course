import sys
import pygame

def run_game():
    #init game and create our screen obj
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Alien Invasion')

    #define background color 
    bg_color = (230,230,230)

    #start the main game loop
    while True:
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #fill screen with bg_color
        screen.fill(bg_color)

        #make the most recently drawn screen visible
        pygame.display.flip()

def main():
   
    run_game()

if(__name__=='__main__'):
    main()

