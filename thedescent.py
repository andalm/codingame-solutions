import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while 1:
    space_x, space_y = [int(i) for i in input().split()]
    montain = h = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if (mountain_h > h):
            h = mountain_h
            montain = i
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).
    print(montain == space_x and "FIRE" or "HOLD")