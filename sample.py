import os
import random
import shutil

# using filtered tiles
source = "tiles_selected"

# dividing into 3 parts for dataset
train_dir = "dataset/images/train"
val_dir = "dataset/images/val"
test_dir = "dataset/images/test"

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

files = os.listdir(source)
random.shuffle(files)

# ratio 180:50:30 for train:val:test
train = files[:180]
val = files[180:230]
test = files[230:260]

for f in train:
    shutil.copy(os.path.join(source,f), train_dir)

for f in val:
    shutil.copy(os.path.join(source,f), val_dir)

for f in test:
    shutil.copy(os.path.join(source,f), test_dir)

print("done")