import pygame
import random

# Initializing PyGame
pygame.init()

# Setting up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Setting up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Setting up the circle parameters
circle_x_pos = window_width // 2
circle_y_pos = window_height // 2
circle_radius = 50

# Initializing the game loop
running = True
while running:
    # Filling the background
    window.fill(black)

    # Generate a random color
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw the circle
    pygame.draw.circle(window, random_color, (circle_x_pos, circle_y_pos), circle_radius)

    # Get mouse position
    mouse_x_pos, mouse_y_pos = pygame.mouse.get_pos()

    # Check if the mouse is hovering over the circle
    if ((mouse_x_pos - circle_x_pos)**2 + (mouse_y_pos - circle_y_pos)**2)**0.5 <= circle_radius:
        # Change the circle's color to white
        pygame.draw.circle(window, white, (circle_x_pos, circle_y_pos), circle_radius)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the window
    pygame.display.update()

# Quit PyGame
pygame.quit()