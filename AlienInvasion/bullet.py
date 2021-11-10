import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullet class to allow instances of bullet objects in game"""
    """We will fire these bullets from our ship object"""
    def __init__(self,ai_settings,screen,ship):
        """create a bullet at the ships location"""
        #inherit __init__ from Sprite class
        super().__init__()
        self.screen =screen

        """spawn bullet at (0,0) then correct position to ship position"""
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_highth)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the bullets position as a float, for easier manipulation
        self.y = float(self.rect.y)

        #init bullet color and bullet speed with ai_settings
        self.bullet_color = ai_settings.bullet_color
        self.bullet_speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """function to update bullets location after fired from ship"""
        #move the bullet up the screen by subtracting bullet speed
        self.y -= self.bullet_speed_factor
        #then set the bullet rect to self
        self.rect.y = self.y

    def draw_bullet(self):
        """function draws the bullet to the screen"""
        #uses pygame draw module and call rect to draw bullet to screen
        pygame.draw.rect(self.screen,self.bullet_color,self.rect)