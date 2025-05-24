import pygame

class Ship:
    def __init__(self, ai_game):
        self.x_position = 0
        self.y_position = 0

        self.screen = ai_game.screen # Acess the game screen
        self.screen_rect = ai_game.screen.get_rect()
        self.config = ai_game.config # acess the settings instance
        
        # Resizes the image and places it midbottom
        self.image = self.config.resize_image()
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
       
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def ship_movement(self):
        """Captures all the keys and makes the ship move to all sides"""
        keys = pygame.key.get_pressed()

    
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.config.ship_speed
            #print("Ship moved to the right")
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.config.ship_speed
            #print("Ship moved to the left")
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.top -= self.config.ship_speed
            #print("Ship moved upwards!")
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.bottom += self.config.ship_speed
            #print("Ship moved downwards!")

        
        elif keys[pygame.K_BACKSPACE]:
            if not hasattr(pygame, 'backspace_pressed'):
                pygame.backspace_pressed = True
                print("Working, nothing to see here kiddo")
        else:
            if hasattr(pygame, 'backspace_pressed'):
                del pygame.backspace_pressed
        
        
    def ship_constrain(self):
        """Maintains the ship inside the screen's border"""
        """-------------------------Sideways-----------------------------------"""
        self.rect.right = min(self.rect.right, self.screen_rect.right)
        self.rect.left = max(self.rect.left, self.screen_rect.left)
        """------------------------Top/Bottom----------------------------------"""
        # Ensures that self.rect.bottom doesn't exceed self.screen_rect.bottom boundaries
        self.rect.bottom = min(self.rect.bottom, self.screen_rect.bottom) # MIN() returns the smallest value
        self.rect.top = max(self.rect.top, self.screen_rect.top) 
    
    def update(self):
        """Updates the ship state"""
        self.ship_movement()
        self.ship_constrain()
    
    def center_ship(self):
        self.x_position = self.config.screen_width // 2
        self.y_position = self.config.screen_height - 50
