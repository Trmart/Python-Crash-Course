# 12-2. Game Character: Find a bitmap image of a game character you like or
# convert an image to a bitmap. Make a class that draws the character at the
# center of the screen and match the background color of the image to the back-
# ground color of the screen, or vice versa.
import pygame
import sys

def main():

    screen = pygame.display.set_mode((1200,800))
    screen.fill(pygame.Color('grey'))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(pygame.Color('grey'))
        ship = pygame.image.load('alien.bmp')
        ship_rect = ship.get_rect()
        screen_rect = screen.get_rect()
        ship_rect.centerx = screen_rect.centerx
        ship_rect.bottom = screen_rect.bottom
        screen.blit(ship,ship_rect)

        pygame.display.flip()

if(__name__ == '__main__'):
    main()