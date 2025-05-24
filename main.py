import pygame
import sys
from setting import Settings
from ship import Ship
from bullet import Bullet
from enemy import Enemy

pygame.font.init()  # Initialize fonts


class AlienGame:
    def __init__(self):
        pygame.init()
        self.config = Settings()
        self.screen = pygame.display.set_mode((self.config.screen_width, self.config.screen_height))
        pygame.display.set_caption("Alien Game")
        pygame.display.set_icon(self.config.iconimage)

        # Ship and bullet instances
        self.bullets = pygame.sprite.Group()
        self.ship = Ship(self)

        # Enemies instance
        self.enemies = pygame.sprite.Group()

        # Game state
        self.level = 1 
        self.lives = 100

        # Font for displaying text
        self.main_font = pygame.font.SysFont("timesnewroman", 40)

        # Create the initial fleet of enemies
        self._create_fleet()

    def game_run(self):
        """game loop."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_enemies()
            self._screen_updates()

    def _create_enemy(self, x_position, y_position):
        """Create a single enemy at a specific position."""
        new_enemy = Enemy(self)
        new_enemy.x = x_position
        new_enemy.rect.x = x_position
        new_enemy.rect.y = y_position  
        self.enemies.add(new_enemy)

    def _create_fleet(self):
        """Create a fleet of enemies."""
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size

        # Calculate the number of enemies per row and rows
        available_space_x = self.config.screen_width - (2 * enemy_width)
        number_of_enemies_x = available_space_x // (2 * enemy_width)

        available_space_y = self.config.screen_height - (5 * enemy_height)
        number_of_rows = available_space_y // (2 * enemy_height)

        # Create the fleet
        for row_number in range(number_of_rows):
            for enemy_number in range(number_of_enemies_x):
                x_position = enemy_width + (2 * enemy_width * enemy_number)
                y_position = enemy_height + (2 * enemy_height * row_number)
                self._create_enemy(x_position, y_position)

    def _update_enemies(self):
        """Update the positions of all enemies and handle edge collisions."""
        self._check_fleet_edges()
        self.enemies.update()

        # Check for collisions with the ship or reaching the bottom of the screen
        if pygame.sprite.spritecollideany(self.ship, self.enemies):
            self._ship_hit()

        for enemy in self.enemies.sprites():
            if enemy.rect.bottom >= self.screen.get_height():
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        """Respond if any enemy reaches an edge."""
        for enemy in self.enemies.sprites():
            if enemy.rect.right >= self.screen.get_width() or enemy.rect.left <= 0:
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the fleet and change direction."""
        for enemy in self.enemies.sprites():
            enemy.rect.y += 10
        self.config.fleet_direction *= -1

    def _ship_hit(self):
        """Handle the ship being hit."""
        self.lives -= 1
        self.enemies.empty()
        self.bullets.empty()
        self._create_fleet()
        self.ship.center_ship()

        if self.lives <= 0:
            print("Game Over!")
            sys.exit()

    def _check_events(self):
        """Check for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
                print("Exiting...")
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _fire_bullet(self):
        """Fire a bullet if the limit has not been reached."""
        if len(self.bullets) < self.config.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullet positions and remove bullets off-screen."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for bullet-enemy collisions
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)

        if not self.enemies:
            # Increase level and create a new fleet
            self.level += 1
            self._create_fleet()

    def _screen_updates(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.blit(self.config.bg_color, (0, 0))
        self.config.clock.tick(60)

        # Draw bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw enemies
        self.enemies.draw(self.screen)

        # Draw text
        lives_label = self.main_font.render(f"Lives: {self.lives}", 1, (255, 255, 255))
        level_label = self.main_font.render(f"Level: {self.level}", 1, (255, 255, 255))

        self.screen.blit(lives_label, (10, 10))
        self.screen.blit(level_label, (self.config.screen_width - level_label.get_width() - 10, 10))

        # Draw the ship
        self.ship.blitme()

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienGame()
    ai.game_run()
