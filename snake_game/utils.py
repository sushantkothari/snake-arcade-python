import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
COLOR_BG = (15, 15, 25)
COLOR_GRID = (30, 30, 45)
COLOR_SNAKE_HEAD = (50, 255, 50)
COLOR_SNAKE_BODY = (0, 200, 0)
COLOR_FOOD = (255, 50, 50)
COLOR_POWERUP = (255, 255, 50)
COLOR_TEXT = (230, 230, 230)
COLOR_PARTICLE = (200, 200, 200)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def draw_text(surface, text, size, color, x, y, center=True):
    font = pygame.font.SysFont("Arial", size, bold=True)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)
