import os
import torchaudio
import shutils
import glob

def remove_not_flac(path):
    try:
        torchaudio.load(path)
    except RuntimeError:
        os.remove(path)
        print(f"Removed {path}")

flacs = glob.glob('datasets/voices/*/*.flac')
for flac in flacs:
    remove_not_flac(flac)
