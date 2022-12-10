import pygame
import random

# Define the colors we will use in RGB format
black = [ 0, 0, 0]
white = [255, 255, 255]
blue = [ 0, 0, 255]

# Initialize the game engine
pygame.init()

# Set the width and height of the screen [width,height]
size = [500, 500]
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("My Game")

# Create a clock object to help track time
clock = pygame.time.Clock()

# Loop until the user clicks the close button
done = False
 
while done == False:
    # Get the current mouse position
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    for event in pygame.event.get():
        # User did something
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Generate a random color
            r = random.randrange(0,255)
            g = random.randrange(0,255)
            b = random.randrange(0,255)
            color = [r, g, b]

            # Draw a circle at the mouse position
            pygame.draw.circle(screen, color, [x, y], 20, 0)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(20)
 
pygame.quit()