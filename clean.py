import pygame
from pygame.sprite import Sprite

pygame.init()
pygame.font.init()

# Game Display
WIDTH, HEIGHT = 440, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
COLOR = (0, 38, 111)
time = pygame.time.Clock()
pygame.display.set_caption("PUTARIA")

# FLAG
runnning = True

# Texts
main_font = pygame.font.SysFont("newtimesroman", 40)
comment = "Lead never follow"

class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 12
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
    
    def draw(self,window):
        """Draws the ship rect to the given window (WIN)"""
        pygame.draw.rect(window, (255, 0, 20), (self.rect))



def drawing_shit():
    """Render text to the screen"""
    letter_label = main_font.render(f"{comment}", 1, (255, 255, 255))
    WIN.blit(letter_label, (90, 50))


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.window = ai_game.window
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_col = (255, 16, 219)
        self.bullet_speed = 6

        self.rect = pygame.Rect(0,0, self.bullet_width, self.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def bullet_update(self):
        self.y -= self.bullet_speed
        self.rect.y = self.y

    def bullet_drawn(self):
        pygame.draw.rect(WIN, self.bullet_col, self.rect)

ship = Ship(180, 340)
bullets = pygame.sprite.Group()

# Game Loop
while runnning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
            #print("Quitting huh? You bitch")
            runnning = False
    
    WIN.fill(COLOR)
    drawing_shit()
    self.ship.draw(WIN)
    
    """Checking keys"""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and ship.rect.x + ship.vel + 50 < WIDTH:
        ship.rect.x += ship.vel
    if keys[pygame.K_LEFT] and ship.rect.x - ship.vel > 0:
        ship.rect.x -= ship.vel
    if keys[pygame.K_UP] and ship.rect.y - ship.vel  > 0:
        ship.rect.y -= ship.vel
    if keys[pygame.K_DOWN] and ship.rect.y + ship.vel + 50 < HEIGHT:
        ship.rect.y += ship.vel
        
    #elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    
    fps = time.tick(30)

    pygame.display.flip()
