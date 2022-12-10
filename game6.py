import pygame
import math
 
# Initialize the game engine
pygame.init()
 
# Create the screen
screen_width = 600
screen_height = 800
window = pygame.display.set_mode([screen_width, screen_height])
 
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
 
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Calculate the angle between the mouse position and the center of the screen.
            angle = math.atan2(mouse_pos[1]-screen_height/2, mouse_pos[0] - screen_width/2)
            # Draw a white circle with a black outline at the mouse position
            pygame.draw.circle(window, white, mouse_pos, 20)
            pygame.draw.circle(window, black, mouse_pos, 20, 2)
            
            # Create a list of points for a polygon
            polygon_points = []
            x = mouse_pos[0]
            y = mouse_pos[1]
            radius = 20
            for i in range(3):
                # Apply the geometric principles using the angle calculated above to generate the polygon points
                x += math.cos(angle + (i * 2 * math.pi) / 3) * radius
                y += math.sin(angle + (i * 2 * math.pi) / 3) * radius
                polygon_points.append( (x, y) )
 
            # Draw the polygon using the points list
            pygame.draw.polygon(window, white, polygon_points, 0)
            pygame.draw.polygon(window, black, polygon_points, 1)
 
    pygame.display.flip()
 
# Close window
pygame.quit()