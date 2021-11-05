# 12-1. Blue Sky: Make a Pygame window with a blue background.
import pygame
import sys

def main():
    
    screen = pygame.display.set_mode((1200,800))
    screen.fill(pygame.Color('blue'))
    
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                sys.exit()
        screen.fill(pygame.Color('blue'))
        pygame.display.flip()


if(__name__ == '__main__'):
    main()