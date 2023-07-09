import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Circles")

# Define circle parameters
circle_radius = 50
circle_color1 = (255, 0, 0)  # Red
circle_color2 = (0, 0, 255)  # Blue

# Set initial angle and rotation speed
angle1 = 0
angle2 = 0
rotation_speed1 = 0.02
rotation_speed2 = -0.03

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update circle angles
    angle1 += rotation_speed1
    angle2 += rotation_speed2

    # Clear the screen
    screen.fill((0, 0, 0))  # Black

    # Calculate circle positions
    center_x = width // 2
    center_y = height // 2
    x1 = center_x + int(150 * math.cos(angle1))
    y1 = center_y + int(150 * math.sin(angle1))
    x2 = center_x + int(200 * math.cos(angle2))
    y2 = center_y + int(200 * math.sin(angle2))

    # Draw circles
    pygame.draw.circle(screen, circle_color1, (x1, y1), circle_radius)
    pygame.draw.circle(screen, circle_color2, (x2, y2), circle_radius)

    # Update the display
    pygame.display.flip()

# Quit the program
pygame.quit()

