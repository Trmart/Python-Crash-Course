
import pygame

class Ship():
    
    def __init__(self,screen):
        """init ship and starting position"""
        
        self.screen = screen 

        #load in ship image and get its rectangle 
        self.image = pygame.image.load("images/ship.bmp") #loads our ship image into image var
        self.rect = self.image.get_rect() #makes our image a rectangle object
        self.screen_rect = screen.get_rect() # makes our screen object a rectangle

        #start each new ship at the bottom center of teh screen
        self.rect.centerx = self.screen_rect.centerx # centers the ship on the screen 
        self.rect.bottom = self.screen_rect.bottom #orients ship at the bottom of the screen
    
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image,self.rect) 