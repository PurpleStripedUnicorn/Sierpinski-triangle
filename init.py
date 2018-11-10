
# IMPORT PACKAGES

from PIL import Image
import math
from random import *



# GLOBAL VARIABLES

iterations = 500000
field = { "x": 4000, "y": 4000 }
points = [
    { "x": 2000, "y": 100 },
    { "x": 100, "y": 3900 },
    { "x": 3900, "y": 3900 }
]
start = { "x": 200, "y": 200 }
background = (255, 255, 255)
fill = (0, 0, 0)



# PROGRAM

# generate grid for output result
output = [background] * (field["x"] * field["y"])

current = start
for i in range(0, iterations):

    # select random point to move towards
    r = randint(0, len(points) - 1)
    # get coords of point
    point = points[r]

    # move towards point
    current = {
        "x": int(round((current["x"] + point["x"]) * .5, 0)),
        "y": int(round((current["y"] + point["y"]) * .5, 0))
    }

    # draw point
    output[current["x"] + current["y"] * field["x"]] = fill

# generate image
img = Image.new('RGB', (field["x"], field["y"]), "white")
img.putdata(output)
img.save("img.png")
