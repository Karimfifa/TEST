import pyautogui as py
import time as t

# Coordinates of the pixel to check
x = 1063 
y = 488

# Sleep to allow time to move the mouse to the desired location
t.sleep(4)

while True:
    # Get the RGB color value of the pixel at the specified coordinates
    px = py.pixel(x, y)
    print(px)
    
    # Convert the RGB tuple to a string for comparison
    px_str = ','.join(map(str, px))
    
    # Check if the pixel color matches the desired color
    if px_str == "83,83,83":
        print("Found it!")
        py.press('space')
    else:
        print('No enemy')
