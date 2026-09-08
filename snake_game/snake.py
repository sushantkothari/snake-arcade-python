import pygame
from snake_game.utils import *

class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.length = 3
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.score = 0
        self.growing = False
        self.speed = 10
        self.alive = True

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        self.direction = self.next_direction
        cur = self.get_head_position()
        x, y = self.direction
        new = (cur[0] + x, cur[1] + y)

        # Collision with walls
        if new[0] < 0 or new[0] >= GRID_WIDTH or new[1] < 0 or new[1] >= GRID_HEIGHT:
            self.alive = False
            return

        # Collision with self
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.alive = False
            return

        self.positions.insert(0, new)
        if not self.growing:
            if len(self.positions) > self.length:
                self.positions.pop()
        else:
            self.growing = False

    def grow(self):
        self.length += 1
        self.score += 10
        self.growing = True

    def draw(self, surface):
        for i, p in enumerate(self.positions):
            r = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            color = COLOR_SNAKE_HEAD if i == 0 else COLOR_SNAKE_BODY
            
            # Draw body with slight rounding and padding for a polished look
            pygame.draw.rect(surface, color, r.inflate(-2, -2), border_radius=4)
            
            # Draw eyes on head
            if i == 0:
                eye_color = (0, 0, 0)
                eye_size = 3
                if self.direction == RIGHT:
                    pygame.draw.circle(surface, eye_color, (r.centerx + 5, r.centery - 5), eye_size)
                    pygame.draw.circle(surface, eye_color, (r.centerx + 5, r.centery + 5), eye_size)
                elif self.direction == LEFT:
                    pygame.draw.circle(surface, eye_color, (r.centerx - 5, r.centery - 5), eye_size)
                    pygame.draw.circle(surface, eye_color, (r.centerx - 5, r.centery + 5), eye_size)
                elif self.direction == UP:
                    pygame.draw.circle(surface, eye_color, (r.centerx - 5, r.centery - 5), eye_size)
                    pygame.draw.circle(surface, eye_color, (r.centerx + 5, r.centery - 5), eye_size)
                elif self.direction == DOWN:
                    pygame.draw.circle(surface, eye_color, (r.centerx - 5, r.centery + 5), eye_size)
                    pygame.draw.circle(surface, eye_color, (r.centerx + 5, r.centery + 5), eye_size)

    def handle_keys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.direction != DOWN:
                self.next_direction = UP
            elif event.key == pygame.K_DOWN and self.direction != UP:
                self.next_direction = DOWN
            elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                self.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                self.next_direction = RIGHT
