import math
import numpy as np

# Rotate a 2D vector by a certain angle
def rotate(vector, angle):
    # Action required!
    # i grab the x and y from the vector so i can work with them separately
    x = vector[0]
    y = vector[1]

    # i apply the rotation matrix to spin the point around the origin by the given angle
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)

    # i return the new rotated point so the ship draws itself facing the right direction
    return (new_x, new_y)

# Map a value from one range to another
def map(n, start1, stop1, start2, stop2):
    newval = (n - start1) / (stop1 - start1) * (stop2 - start2) + start2;

    if newval > stop2:
        return stop2
    elif newval < start2:
        return start2
    else:
        return newval