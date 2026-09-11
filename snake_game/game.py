import pygame
import sys
import random
from snake_game.snake import Snake
from snake_game.food import Food, PowerUp
from snake_game.utils import *

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.lifetime = 20

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1

    def draw(self, surface):
        alpha = int((self.lifetime / 20) * 255)
        s = pygame.Surface((4, 4))
        s.set_alpha(alpha)
        s.fill(self.color)
        surface.blit(s, (self.x, self.y))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.powerup = PowerUp()
        self.particles = []
        self.state = "MENU"
        self.high_score = self.load_high_score()
        self.level = 1
        self.obstacles = []
        self.load_level(1)

    def create_particles(self, x, y, color):
        for _ in range(10):
            self.particles.append(Particle(x, y, color))

    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())
        except:
            return 0

    def save_high_score(self):
        with open("highscore.txt", "w") as f:
            f.write(str(self.high_score))

    def load_level(self, level):
        self.obstacles = []
        if level == 2:
            # Simple border obstacles
            for x in range(5, 15):
                self.obstacles.append((x, 5))
                self.obstacles.append((GRID_WIDTH - x, GRID_HEIGHT - 6))
        elif level >= 3:
            # More complex patterns
            for i in range(10):
                self.obstacles.append((10, 10 + i))
                self.obstacles.append((GRID_WIDTH - 11, 10 + i))

    def update(self):
        if self.state == "PLAYING":
            self.snake.update()
            self.powerup.update()

            if not self.snake.alive:
                self.state = "GAMEOVER"
                if self.snake.score > self.high_score:
                    self.high_score = self.snake.score
                    self.save_high_score()

            # Check obstacle collision
            if self.snake.get_head_position() in self.obstacles:
                self.snake.alive = False
                self.state = "GAMEOVER"

            # Check food collision
            if self.snake.get_head_position() == self.food.position:
                self.snake.grow()
                self.create_particles(self.food.position[0] * GRID_SIZE + GRID_SIZE // 2, 
                                     self.food.position[1] * GRID_SIZE + GRID_SIZE // 2, COLOR_FOOD)
                self.food.randomize_position(self.snake.positions)
                
                # Level up logic
                if self.snake.score % 50 == 0:
                    self.level += 1
                    self.snake.speed += 1
                    self.load_level(self.level)

            # Check powerup collision
            if self.powerup.active and self.snake.get_head_position() == self.powerup.position:
                self.snake.score += 30
                self.create_particles(self.powerup.position[0] * GRID_SIZE + GRID_SIZE // 2, 
                                     self.powerup.position[1] * GRID_SIZE + GRID_SIZE // 2, COLOR_POWERUP)
                self.powerup.active = False
                self.powerup.spawn_timer = 0

            # Update particles
            for p in self.particles[:]:
                p.update()
                if p.lifetime <= 0:
                    self.particles.remove(p)

    def draw(self):
        self.screen.fill(COLOR_BG)
        
        # Draw grid
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, COLOR_GRID, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, COLOR_GRID, (0, y), (SCREEN_WIDTH, y))

        if self.state == "MENU":
            draw_text(self.screen, "ADVANCED SNAKE", 64, COLOR_SNAKE_HEAD, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
            draw_text(self.screen, "Press SPACE to Start", 32, COLOR_TEXT, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            draw_text(self.screen, f"High Score: {self.high_score}", 24, COLOR_POWERUP, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
        
        elif self.state == "PLAYING":
            # Draw obstacles
            for obs in self.obstacles:
                r = pygame.Rect((obs[0] * GRID_SIZE, obs[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(self.screen, (100, 100, 120), r, border_radius=3)

            self.food.draw(self.screen)
            self.powerup.draw(self.screen)
            self.snake.draw(self.screen)
            for p in self.particles:
                p.draw(self.screen)
            
            # HUD
            draw_text(self.screen, f"Score: {self.snake.score}", 24, COLOR_TEXT, 10, 10, center=False)
            draw_text(self.screen, f"Level: {self.level}", 24, COLOR_TEXT, SCREEN_WIDTH - 120, 10, center=False)

        elif self.state == "GAMEOVER":
            draw_text(self.screen, "GAME OVER", 64, COLOR_FOOD, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
            draw_text(self.screen, f"Final Score: {self.snake.score}", 32, COLOR_TEXT, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)
            draw_text(self.screen, "Press SPACE to Restart", 24, COLOR_TEXT, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)

        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if self.state == "MENU":
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.state = "PLAYING"
                elif self.state == "PLAYING":
                    self.snake.handle_keys(event)
                elif self.state == "GAMEOVER":
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.snake.reset()
                        self.level = 1
                        self.state = "PLAYING"

            self.update()
            self.draw()
            self.clock.tick(self.snake.speed)
