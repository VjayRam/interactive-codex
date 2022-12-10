import pygame
from pygame.locals import *
import random

# setup display surface
pygame.init()
surface_size = (800,800)
main_surface = pygame.display.set_mode(surface_size)
my_clock = pygame.time.Clock()

# setup colors
BLACK = (0,0,0)
GRAY = (127,127,127)
WHITE = (255,255,255)
RED = (255,0,0)
violet = (150,0,255)
BLUE = (0,0,255)
 
# draw on the main surface
def draw_circle(pos):
    x = pos[0]
    y = pos[1]
    pygame.draw.circle(main_surface, BLUE, (x,y), 10, 0)
 
def draw_rectangle(pos):
    x = pos[0]
    y = pos[1]
    pygame.draw.rect(main_surface, WHITE, [x, y, 10, 10], 0)

def random_generate():
    random_x = random.randint(0, 800)
    random_y = random.randint(0, 800)
    random_shape = random.choice([draw_circle, draw_rectangle])
    random_shape((random_x, random_y))

# game loop
while True:
    my_clock.tick(60)
 
    # handle pygame events
    ev = pygame.event.poll()
    if ev.type == QUIT:
        # exit the game loop
        break
 
    # add background
    main_surface.fill(GRAY)
 
    # draw on the main surface
    pos_x, pos_y = pygame.mouse.get_pos()
    draw_rectangle([pos_x, pos_y])
    random_generate()
    
    # update screen
    pygame.display.flip()
 
pygame.quit()