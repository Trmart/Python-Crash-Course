# 12-3. Rocket: Make a game that begins with a rocket in the center of the
# screen. Allow the player to move the rocket up, down, left, or right using the
# four arrow keys. Make sure the rocket never moves beyond any edge of the
# screen.
import pygame
import sys

def main():
    """main"""
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    screen.fill(pygame.Color('grey'))
    
    pygame.display.set_caption('Rocket Game Practice')
    rocket = pygame.image.load('ship.bmp')
    rocket_rect = rocket.get_rect()
    screen_rect = screen.get_rect()
    rocket_rect.centerx = screen_rect.centerx
    rocket_rect.centery = screen_rect.centery
    moving = False
    while True:
       
        screen.fill(pygame.Color('grey'))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_RIGHT and rocket_rect.right < screen_rect.right:
                    rocket_rect.centerx += 1
                if event.key == pygame.K_LEFT and rocket_rect.left > 0:
                    rocket_rect.centerx -= 1
                if event.key == pygame.K_UP and rocket_rect.centery > 0:
                    rocket_rect.centery -= 1
                if event.key == pygame.K_DOWN and rocket_rect.centery > 0:
                    rocket_rect.centery += 1
                
        screen.blit(rocket,rocket_rect)
        pygame.display.flip()
    
if(__name__=='__main__'):
    main()


