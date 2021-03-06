import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.

# game loop
while 1:
    speed = int(input())  # the motorbike's speed.
    coord_x = int(input())  # the position on the road of the motorbike.
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if (coord_x == road - 1):
        print("JUMP")
    elif (coord_x > road - 1):
        print("SLOW")
    elif (speed == gap + 1):
        print("WAIT")
    elif (speed > gap + 1):
        print("SLOW")
    else:
        # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
        print("SPEED")
