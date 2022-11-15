import os
import shutils
import glob

folders = glob.glob('datasets/voices/*')
for folder in folders:
    if len(os.listdir(folder)) == 0:
        os.rmdir(folder)
        print(f"Removed {folder}")

