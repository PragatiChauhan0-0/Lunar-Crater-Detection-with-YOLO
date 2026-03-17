import cv2
import numpy as np
import os
from tqdm import tqdm

# takes raw strips and processed them
INPUT = "processed/raw"
OUTPUT = "processed/strips_png"

os.makedirs(OUTPUT, exist_ok=True)

for file in tqdm(os.listdir(INPUT)):
    if not file.endswith(".png"):
        continue

    path = os.path.join(INPUT, file)

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) # convert to grayscale

    # Normalize intensity
    img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX) # scale to full 0-255 range

    # Histogram equalization
    img_eq = cv2.equalizeHist(img_norm) # enhance contrast by equalizing histogram

    out_path = os.path.join(OUTPUT, file)
    cv2.imwrite(out_path, img_eq)