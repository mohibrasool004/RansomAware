import os
import random
from datetime import datetime

DECOY_DIR = os.path.join(os.getcwd(), 'decoys')

def update_decoy_file(filepath):
    # Open the file and update content slightly or rename the file
    with open(filepath, "a") as f:
        f.write("\nUpdate: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # Rename the file to simulate evolution
    new_name = os.path.join(DECOY_DIR, f"updated_{os.path.basename(filepath)}")
    os.rename(filepath, new_name)
    print(f"Decoy file updated and renamed: {new_name}")
    return new_name

def update_all_decoys():
    for file in os.listdir(DECOY_DIR):
        file_path = os.path.join(DECOY_DIR, file)
        if os.path.isfile(file_path):
            update_decoy_file(file_path)

if __name__ == "__main__":
    update_all_decoys()
