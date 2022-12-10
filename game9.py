import pygame
from pygame.locals import *
import math
import random

# Initialize Pygame and the window
pygame.init()
scr_w, scr_h = 800, 600
screen = pygame.display.set_mode((scr_w, scr_h))
pygame.display.set_caption('Generative Art')

# Handle user input
done = False
clock = pygame.time.Clock()

# Colors
green = (0, 178, 0)
white = (255, 255, 255)

# Place a seed to start the generative art
pos_x, pos_y = scr_w/2, scr_h/2

# Generative Art
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =  True

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Calculate the vector of the mouse pointing at the starting point
            mouse_vec_x = mouse_x - pos_x
            mouse_vec_y = mouse_y - pos_y

            # Draw the vector between the starting point and the mouse
            pygame.draw.line(screen, green,
                             [pos_x, pos_y], [mouse_x, mouse_y],
                             2)
            
            # Calculate the angle between the inverse vector and the starting point
            angle = math.atan2(mouse_vec_y, mouse_vec_x)
            angle *= 180 / math.pi 

            # Use the angle to draw a geometric shape - in this case an Equilateral Triangle
            # Each triangle will be shifted by different amounts
            shift = random.uniform(-20, 20)
            side_len = shift + 40
            
            pygame.draw.polygon(screen, white, [[pos_x, pos_y], 
                                                [pos_x + side_len*math.cos(2*math.pi/3 + angle/180*math.pi), pos_y + side_len*math.sin(math.pi*2/3 + angle/180*math.pi)], 
                                                [pos_x + side_len*math.cos(4*math.pi/3 + angle/180*math.pi), pos_y + side_len*math.sin(4*math.pi/3 + angle/180*math.pi)]])

            # Set the position to the mouse x,y for the next iteration
            pos_x, pos_y = mouse_x, mouse_y

    pygame.display.update()
    clock.tick(60)
pygame.quit()