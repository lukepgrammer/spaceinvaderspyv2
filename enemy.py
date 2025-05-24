import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, aigame):
        super().__init__()
        self.screen = aigame.screen
        self.config = aigame.config

        # Load the enemy image and set its rect attribute
        self.image = self.config.resize_enemy()
        self.rect = self.image.get_rect()

        # Start each enemy at the top-left corner with a small offset
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the enemy's exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the enemy to the right."""
        self.x += self.config.enemy_speed * self.config.fleet_direction
        self.rect.x = self.x
