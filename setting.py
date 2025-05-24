import pygame
from enemy import Enemy
class Settings:
    def __init__(self):
        """Game Settings"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = self.resize_background()
        self.iconimage = pygame.image.load('graphics/alienicon.png')
        self.ship_speed = 30
        self.clock = pygame.time.Clock()
        
        """Bullet Settings"""
        self.bullet_speed = 12
        self.bullet_width = 4   # switch height and width values to change bullet orietation
        self.bullet_height = 15
        self.bullet_color = (255, 128, 0)
        self.bullets_allowed = 10 # Limits how many bullets you can shoot at a time

        """Enemy Settings"""
        self.enemy_speed = 1.0
        self.fleet_direction = -1



    def resize_image(self):
        """Resize the ship image"""
        img = pygame.image.load('graphics/2dship.png')
        return pygame.transform.scale(img, (130, 60))
    
    def resize_background(self):

        imge = pygame.image.load('graphics/atmosphere.jpg')
        return pygame.transform.scale(imge, (800, 600))
    
    def resize_enemy(self):
        img = pygame.image.load('graphics/ship.bmp')
        
        rotated_img = pygame.transform.rotate(img, 180)

        resized = pygame.transform.scale(rotated_img, (80, 40))

        return resized

