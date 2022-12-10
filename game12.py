import tkinter as tk
import random

# Create a tkinter canvas
canvas = tk.Canvas(width=800, height=600) 
canvas.pack() 
  
# Create empty list
polygon_list = [] 
  
def mouseClick(event): 
  
    # Append mouse position to list
    polygon_list.append((event.x, event.y)) 
    print(polygon_list) 
  
    # Draw the polygon
    canvas.create_polygon(polygon_list, fill="", outline="black") 
  

# Create mouse click event
canvas.bind("<Button-1>", mouseClick) 


# Randomly generate polygons when mouse is double clicked
def doubleClick(event): 
    canvas.delete("all") 
  
    # Generate random end points
    point1 = (random.randrange(100, 700), random.randrange(100, 500)) 
    point2 = (random.randrange(100, 700), random.randrange(100, 500)) 
    point3 = (random.randrange(100, 700), random.randrange(100, 500)) 
    point4 = (random.randrange(100, 700), random.randrange(100, 500)) 
  
    # Generate random shape
    draw_polygon = canvas.create_polygon((point1, point2, point3, point4), 
                                         fill="", outline="black") 
  
    # Bind a mouse move event
    canvas.bind("<B1-Motion>", move_polygon) 
  

# Move generated shape using mouse
def move_polygon(event): 
    # Calculate the vector of movement
    dx = event.x - event.x_root 
    dy = event.y - event.y_root 
  
    # Move shape
    canvas.move(draw_polygon, dx, dy) 
  

# Bind double click event
canvas.bind("<Double-Button-1>", doubleClick) 

tk.mainloop()