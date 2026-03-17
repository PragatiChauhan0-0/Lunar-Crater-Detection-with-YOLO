import cv2
import os
import numpy as np

# takes all tiles and removes the ones with very low texture
INPUT = "tiles"
OUTPUT = "tiles_selected"

os.makedirs(OUTPUT, exist_ok=True)

kept = 0

for f in os.listdir(INPUT):

    path = os.path.join(INPUT, f)
    img = cv2.imread(path, 0)

    texture = np.std(img)

    if texture > 12:   # threshold for lunar terrain
        cv2.imwrite(os.path.join(OUTPUT,f), img)
        kept += 1

print("tiles kept:", kept)