import pygame
import random
 
WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR = (0,0,0)

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mouse Interactive Generative Art")
screen.fill(BACKGROUND_COLOR)

#draws a line between the two points
def draw_line(screen, start_x, start_y, end_x, end_y, color):
    pygame.draw.line(screen, color, [start_x, start_y], [end_x, end_y], 3)

#draws a rectangle with random start and end x and y coordinates    
def draw_rectangle(screen, start_x, start_y, end_x, end_y, color):
    pygame.draw.rect(screen, color, [start_x, start_y, end_x, end_y], 0)

#draws an ellipse with random start and end x and y coordinates    
def draw_ellipse(screen, start_x, start_y, end_x, end_y, color):
    pygame.draw.ellipse(screen, color, [start_x, start_y, end_x, end_y], 0)
 
mouse_x = 0
mouse_y = 0

running = True
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Get the current mouse position.
    mouse_x, mouse_y = pygame.mouse.get_pos()
 
    # Create random colors.
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)

    # Generates a random geometric shape using different geometric principles and mouse movement.
    draw_line(screen, mouse_x, mouse_y, mouse_x + random.randint(-10, 10), mouse_y + random.randint(-10, 10), color)
    draw_rectangle(screen, mouse_x, mouse_y, mouse_x + random.randint(-25, 25), mouse_y + random.randint(-25, 25), color)
    draw_ellipse(screen, mouse_x, mouse_y, mouse_x + random.randint(-10, 10), mouse_y + random.randint(-10, 10), color)
    
    # Refresh the display with the new shapes.
    pygame.display.flip()
 
pygame.quit()