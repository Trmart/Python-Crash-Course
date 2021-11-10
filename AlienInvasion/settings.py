"""settings class module to store and allow import of settings for game"""



class Settings():
    """this is the created settings class told hold game settings"""
    """this will store window size, and color"""
    def __init__(self): #constructor for our settings class
        self.screen_width = 1200 
        self.screen_height = 800
        #Red = (255,0,0) Green = (0,255,0) Blue = (0,0,255)
        self.bg_color = (230,230,230) 
        self.ship_speed_factor = 1.5 

        #Bullet Class Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_highth = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
