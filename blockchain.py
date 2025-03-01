import hashlib
import json
from time import time
import os

class Blockchain:
    def __init__(self, chain_file='chain.json'):
        self.chain_file = chain_file
        self.chain = []
        self.load_chain()
    
    def load_chain(self):
        if os.path.exists(self.chain_file):
            with open(self.chain_file, 'r') as f:
                self.chain = json.load(f)
        else:
            # Create the genesis block
            self.new_block(previous_hash="1", proof=100)
    
    def new_block(self, proof, previous_hash=None, event_data=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'event_data': event_data,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.chain.append(block)
        self.save_chain()
        return block
    
    def save_chain(self):
        with open(self.chain_file, 'w') as f:
            json.dump(self.chain, f, indent=4)
    
    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def last_block(self):
        return self.chain[-1]
    
    def add_event(self, event_data):
        # Very basic proof-of-work for demonstration (not secure for production!)
        last_proof = self.last_block()['proof']
        proof = self.proof_of_work(last_proof)
        previous_hash = self.hash(self.last_block())
        block = self.new_block(proof, previous_hash, event_data)
        return block
    
    def proof_of_work(self, last_proof):
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof
    
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

if __name__ == "__main__":
    blockchain = Blockchain()
    # Example of logging an event
    event = {"action": "MODIFIED", "file": "decoy_file.txt"}
    block = blockchain.add_event(event)
    print("Block added:", block)
