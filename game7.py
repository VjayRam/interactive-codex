import random
from tkinter import *

# Create the tkinter canvas
master = Tk()
canvas = Canvas(master, width=500, height=500)
canvas.pack()

# Define variables to track mouse position
mouse_x = 0
mouse_y = 0

# Define a function to be called when the mouse moves
def motion(event):
	global mouse_x, mouse_y
	mouse_x = event.x
	mouse_y = event.y

	# Generate a random circle at the mouse position
	draw_circle(mouse_x, mouse_y)

# Add a function to draw a circle based on geometric principles
def draw_circle(x, y):
	# Generate a random color
	random_color = "#%06x" % random.randint(0, 0xFFFFFF)
	

	# Generate a random radius
	radius = random.randint(1, 25)

	canvas.create_oval(x-radius, y-radius, x+radius, y+radius,
						fill=random_color, outline='')

# Track mouse movement
canvas.bind('<Motion>', motion)

# Start the main loop
master.mainloop()