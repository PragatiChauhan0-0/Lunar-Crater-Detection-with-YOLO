import cv2
import os
import json
from tqdm import tqdm

# divides the processed strips into smaller tiles
INPUT = "processed/strips_png"
OUTPUT = "tiles"
META = "meta" # saves meta data for reconstruction

TILE_SIZE = 256 # size of each tile
STRIDE = 256

os.makedirs(OUTPUT, exist_ok=True)
os.makedirs(META, exist_ok=True)

metadata = []

for strip in tqdm(os.listdir(INPUT)):

    if not strip.endswith(".png"):
        continue

    img = cv2.imread(os.path.join(INPUT, strip))
    h, w = img.shape[:2]

    strip_name = strip.replace(".png","")

    for y in range(0, h, STRIDE):
        for x in range(0, w, STRIDE):

            tile = img[y:y+TILE_SIZE, x:x+TILE_SIZE]

            if tile.shape[0] < TILE_SIZE or tile.shape[1] < TILE_SIZE:
                continue

            tile_name = f"{strip_name}_{x}_{y}.png"

            cv2.imwrite(os.path.join(OUTPUT, tile_name), tile)

            metadata.append({
                "tile": tile_name,
                "strip": strip,
                "x": x,
                "y": y,
                "tile_size": TILE_SIZE
            })

with open(os.path.join(META, "tile_metadata.json"), "w") as f:
    json.dump(metadata, f, indent=2)