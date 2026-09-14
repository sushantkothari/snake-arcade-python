import pygame
import random
from snake_game.utils import *

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = COLOR_FOOD
        self.randomize_position([])

    def randomize_position(self, snake_positions):
        while True:
            self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if self.position not in snake_positions:
                break

    def draw(self, surface):
        r = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r.inflate(-4, -4), border_radius=10)
        # Add a small shine effect
        pygame.draw.circle(surface, (255, 200, 200), (r.centerx - 3, r.centery - 3), 2)

class PowerUp(Food):
    def __init__(self):
        super().__init__()
        self.color = COLOR_POWERUP
        self.active = False
        self.spawn_timer = 0

    def update(self):
        if not self.active:
            self.spawn_timer += 1
            if self.spawn_timer > 100: # Random chance to spawn
                if random.random() < 0.05:
                    self.active = True
                    self.spawn_timer = 0
        else:
            self.spawn_timer += 1
            if self.spawn_timer > 50: # Despawn after some time
                self.active = False
                self.spawn_timer = 0

    def draw(self, surface):
        if self.active:
            r = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            # Pulsing effect
            pulse = (pygame.time.get_ticks() // 200) % 2
            size_diff = -2 if pulse == 0 else -6
            pygame.draw.rect(surface, self.color, r.inflate(size_diff, size_diff), border_radius=5)
