import pygame
import random

# Initialize the pygame 
pygame.init()

# Initialize the screen
size = (800, 600)
screen = pygame.display.set_mode(size)

# Title and Icon
pygame.display.set_caption("Mouse Interactive Generative Art")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Variables
running = True

# Main Loop
while running:

    # Set the screen background
    screen.fill((255,255,255))

    # Generative art algorithm
    for i in range(10):
        # Generate random colors
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)

        # Generate random positions
        x = random.randint(0, 800)
        y = random.randint(0, 600)

        # Generate random sizes
        width = random.randint(1, 20)
        height = random.randint(1, 20)

        # Draw the rectangles
        pygame.draw.rect(screen, (red, green, blue), (x, y, width, height))

    # Get the mouse position
    mouseX, mouseY = pygame.mouse.get_pos()

    # Generate a circle at the mouse position
    pygame.draw.circle(screen, (255, 0, 0), (mouseX, mouseY), 10)

    # Update the display
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit the game
pygame.quit()