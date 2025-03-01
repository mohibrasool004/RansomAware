import os
import random
import string
from datetime import datetime

# Define the directory for decoy files
DECOY_DIR = os.path.join(os.getcwd(), 'decoys')
os.makedirs(DECOY_DIR, exist_ok=True)

def random_filename(extension=".txt"):
    # Generate a random filename that seems realistic (e.g., "financial_report_2023.txt")
    prefixes = ["financial_report", "client_data", "project_notes", "confidential"]
    prefix = random.choice(prefixes)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}{extension}"

def create_decoy_file():
    filename = random_filename()
    file_path = os.path.join(DECOY_DIR, filename)
    # Content can be a mix of random text and decoy information
    content = "This document is classified.\nDo not distribute.\n" + ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    with open(file_path, "w") as f:
        f.write(content)
    print(f"Decoy file created: {file_path}")
    return file_path

if __name__ == "__main__":
    # Create a few decoy files initially
    for _ in range(5):
        create_decoy_file()
