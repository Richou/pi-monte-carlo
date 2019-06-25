from __future__ import division
import random
import math

inCircle = 0
currentOcc = 0
rayon = 1

while True:
    currentOcc += 1
    x = random.uniform(0, rayon)
    y = random.uniform(0, rayon)
    distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    if distance <= rayon :
        inCircle += 1
    pi = (inCircle / currentOcc) * 4
    print pi