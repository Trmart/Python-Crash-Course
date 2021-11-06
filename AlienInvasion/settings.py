"""settings class module to store and allow import of settings for game"""

class Settings():
    """this is the created settings class told hold game settings"""
    """this will store window size, and color"""
    def __init__(self): #constructor for our settings class
        self.screen_width = 1200 
        self.screen_height = 800
        self.bg_color = (230,230,230) #light grey/off white (Red,Green,Blue) 
        self.ship_speed_factor = 1.5 
#Red = (255,0,0) Green = (0,255,0) Blue = (0,0,255)