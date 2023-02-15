import pygame
import random

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
black = [ 0, 0, 0]
white = [255, 255, 255]
blue = [ 0, 0, 255]

# Set the width and height of the screen [width,height]
size = [1000, 1000]
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("My Game")

# Create a clock object to help track time
clock = pygame.time.Clock()

# Loop until the user clicks the close button
done = False
def colordraw(color,x,y):
    pygame.draw.circle(screen, color, [x, y], 10, 0)

def sym_four(color,x,y):
    colordraw(color,x,y)
    colordraw(color,1000-x,1000-y)
    colordraw(color,y,1000-x)
    colordraw(color,1000-y,x)

while done == False:
    # Get the current mouse position
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    left_click, _, _ = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        # User did something
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Generate a random color
            r = 0
            g = random.randrange(0,255)
            b = random.randrange(0,255)
            color = [r, g, b]

            # Draw a circle at the mouse position
        if left_click:
            r = 0
            g = random.randrange(0,255)
            b = random.randrange(0,255)
            color = [r, g, b]
            sym_four(color,x,y)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 120 frames per second
    clock.tick(120)
 
pygame.quit()