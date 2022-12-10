import cv2
import random
import numpy as np

#Positions
x,y = 0, 0 

#Colors
red,green, blue = 0,0,0

# Pythagoras Theorem 
a,b,c = 0,0,0

def draw(event , x,y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        
        cv2.rectangle(img, (x-3,y-3), (x+3, y+3), (red,green,blue), -1)
        
        a = np.sqrt((x*x)+(y*y))
        b = np.sqrt((img.shape[0] - x)*(img.shape[0] - x)+(y*y))
        c = np.sqrt((img.shape[0] - x)*(img.shape[0] - x)+(img.shape[1] - y)*(img.shape[1] - y))
       
        cv2.line(img, (0,y),(x,0), (red,green,blue),5)
        cv2.line(img, (x,0),(img.shape[0],y), (red,green,blue),5)
        cv2.line(img, (img.shape[0],y),(0,img.shape[1]), (red,green,blue),5)
        print(a,b,c)
 
    
#Creating a black image
img = np.zeros(shape=(512,512,3), dtype=np.uint8)

# Defining the window 
cv2.namedWindow(winname = 'Geometric Art')

# Binding the mouseButtonDown event with our draw function 
cv2.setMouseCallback('Geometric Art', draw)

while True:
    
    cv2.imshow('Geometric Art',img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()