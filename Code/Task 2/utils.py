import math
import numpy as np

# Rotate a 2D vector by a certain angle
def rotate(vector, angle):
	# Action required!
    return vector

# Map a value from one range to another
def map(n, start1, stop1, start2, stop2):
    newval = (n - start1) / (stop1 - start1) * (stop2 - start2) + start2;

    if newval > stop2:
        return stop2
    elif newval < start2:
        return start2
    else:
        return newval