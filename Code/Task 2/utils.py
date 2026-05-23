import math
import numpy as np

# Rotate a 2D vector by a certain angle
def rotate(vector, angle):
	# Action required!
    x = vector[0] * math.cos(angle) - vector[1] * math.sin(angle)
    y = vector[0] * math.sin(angle) + vector[1] * math.cos(angle)
    return (x, y)

# Map a value from one range to another
def map(n, start1, stop1, start2, stop2):
    newval = (n - start1) / (stop1 - start1) * (stop2 - start2) + start2;

    if newval > stop2:
        return stop2
    elif newval < start2:
        return start2
    else:
        return newval
        return newval