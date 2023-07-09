import pygame
import math

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60
RADIUS = 100
ANGLE = 0
SPEED = 2

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing
    screen.fill((0, 0, 0))  # Fill the screen with black
    # Calculate circle position
    x = WIDTH // 2 + RADIUS * math.cos(math.radians(ANGLE))
    y = HEIGHT // 2 + RADIUS * math.sin(math.radians(ANGLE))
    # Draw the circle
    pygame.draw.circle(screen, (0, 0, 255), (int(x), int(y)), 50)
    # Rotate the angle
    ANGLE = (ANGLE + SPEED) % 360

    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Cap the frame rate

pygame.quit()

