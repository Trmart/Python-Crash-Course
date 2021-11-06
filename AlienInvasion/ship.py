
import pygame

class Ship():
    
    def __init__(self,ai_settings,screen):
        """init ship and starting position"""
        
        self.screen = screen 
        self.ai_settings = ai_settings

        #load in ship image and get its rectangle 
        self.image = pygame.image.load("images/ship.bmp") #loads our ship image into image var
        self.rect = self.image.get_rect() #makes our image a rectangle object
        self.screen_rect = screen.get_rect() # makes our screen object a rectangle

        #start each new ship at the bottom center of teh screen
        self.rect.centerx = self.screen_rect.centerx # centers the ship on the screen 
        self.rect.bottom = self.screen_rect.bottom #orients ship at the bottom of the screen

        #creates a decimal value for ships center 
        self.center = float(self.rect.centerx)
        
        #moving flags to allow for continuous movement 
        self.moving_right = False
        self.moving_left = False
    
    def update_ship(self):
        #if the player is holding down the right key and does not go out of bounds
        if(self.moving_right and self.rect.right < self.screen_rect.right): 
            #move to the right 
            self.center +=self.ai_settings.ship_speed_factor 
        #if player is holding down left key and does not go out of bounds
        if(self.moving_left and self.rect.left > 0 ): 
            #move to the left
            self.center -= self.ai_settings.ship_speed_factor 
        
        #update rect object from self.center
        self.rect.centerx = self.center
    
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image,self.rect) 
