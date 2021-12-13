import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Alien class to create alien objects"""
    def __init__(self,ai_settings,screen):
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings
        #load in alien image and set rect attributes
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        #start each new alien at teh top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #store the aliens exact position 
        self.x= float(self.rect.x)

    def blitme(self):
        """draw alien at its current position"""
        self.screen.blit(self.image,self.rect)