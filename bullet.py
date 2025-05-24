import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        """Create a bullet object at the ship current position"""
        self.screen = ai_game.screen
        self.config = ai_game.config
        self.color = ai_game.config.bullet_color

        """Create a bullet rect at (0,0) then set current position"""
        self.rect = pygame.Rect(0,0, self.config.bullet_width, self.config.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop # puts the bullet rect slightly above the ship rect
        # midright for change the bullet orietation to right edge of the ship

        self.y = float(self.rect.y) # self.x
        
    def update(self):
        """update the bullet's position on the screen"""
        # change to self.x and increase to change the bullet orietation
        self.y -= self.config.bullet_speed
        self.rect.y = self.y

        #if self.rect.left > self.screen.get_rect().right:
         #   self.kill()

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

