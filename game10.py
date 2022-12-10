# importing necessary libraries 
import pygame 
from pygame.locals import * 
import random 

# initiating pygame modules 
pygame.init() 

# setting the window size 
width = 600
height = 600
screen = pygame.display.set_mode((width, height)) 

# setting window caption 
pygame.display.set_caption("Generative Art With Mouse Input") 

# defining colors using RGB 
red = (255, 0, 0) 
green = (0, 255, 0) 
blue = (0, 0, 255) 

# setting size for shapes 
size = 10

# loop for trapping key and mouse events 
while True : 
		
	# handling different events 
	for event in pygame.event.get() : 
		
		# if quit event is present 
		if event.type == pygame.QUIT : 
			pygame.quit()	 
			exit(0) 
		
		# if mouse is pressed 
		if event.type == MOUSEBUTTONDOWN : 
		
			# creating random numbers 
			a, b = random.randint(-1, 1), random.randint(-1, 1) 
			
			# obtaining mouse pressed position 
			x, y = pygame.mouse.get_pos() 
			
			# calculating new coordinates 
			x1 = x + (a * size) 
			y1 = y + (b * size) 
			
			# drawing line using draw.line with new coordinates 
			pygame.draw.line(screen, green, (x, y), (x1, 
									y1), size) 
			
	# updating display 
	pygame.display.update()