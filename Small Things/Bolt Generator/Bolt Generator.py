import random as r
import time
t = 0

'''
The start position (x value) should always be set to where the bolt starts in the middle of the terminal window.
If there's an extra line between each bolt piece then you've made the starting position too large OR the bolt wandered too far to the right and looped back around.
It is recommended to zoom out as much as you can to minimize extra lines from occuring.
'''

# NOTE: Customize these numbers before starting the program!
x = 50        # START POSITION
y = 700       # LENGTH OF BOLT

while t < y:
    # Reset moves (m)
    m = 0
    
    # Decide left or right
    direction = r.randint(0, 1)
    
    # Decide amount of times moving in direction
    moves = r.randint(2, 10)
    
    # Move
    while m < moves:
        print("  " * x + "-~+#{}#+~-")
        if direction == 0: # Left
            x -= 1
            m += 1
            t += 1
        elif direction == 1: # Right
            x += 1
            m += 1
            t += 1
    time.sleep(0.02)