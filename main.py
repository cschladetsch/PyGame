import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Basic Pygame Window")

# Set up square properties
square_size = 50
square_color = (255, 255, 255)  # White
square_x, square_y = width // 2 - square_size // 2, height // 2 - square_size // 2  # Center the square
square_speed = 5

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move square with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and square_x > 0:  # Prevent moving out of bounds
        square_x -= square_speed
    if keys[pygame.K_RIGHT] and square_x < width - square_size:  # Prevent moving out of bounds
        square_x += square_speed
    if keys[pygame.K_UP] and square_y > 0:  # Prevent moving out of bounds
        square_y -= square_speed
    if keys[pygame.K_DOWN] and square_y < height - square_size:  # Prevent moving out of bounds
        square_y += square_speed

    # Fill screen with black color
    screen.fill((0, 0, 0))

    # Draw square
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

    # Update display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()
sys.exit()

