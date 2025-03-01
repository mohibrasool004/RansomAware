import os
import random
import time

DECOY_DIR = os.path.join(os.getcwd(), 'decoys')

def simulate_ransomware_attack():
    decoy_files = [os.path.join(DECOY_DIR, f) for f in os.listdir(DECOY_DIR) if os.path.isfile(os.path.join(DECOY_DIR, f))]
    if not decoy_files:
        print("No decoy files found to attack.")
        return
    # Randomly pick a decoy file and simulate encryption/modification
    target = random.choice(decoy_files)
    with open(target, "w") as f:
        f.write("ENCRYPTED_CONTENT" + ''.join(random.choices("ABCDEF0123456789", k=50)))
    print(f"Simulated ransomware attack on: {target}")

if __name__ == "__main__":
    # Simulate an attack every 10 seconds (for testing purposes)
    while True:
        simulate_ransomware_attack()
        time.sleep(10)
