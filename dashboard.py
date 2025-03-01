from flask import Flask, render_template, jsonify
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Paths to your blockchain log and decoy files folder
CHAIN_FILE = os.path.join(os.path.dirname(__file__), 'chain.json')
DECOY_DIR = os.path.join(os.path.dirname(__file__), 'decoys')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/logs')
def get_logs():
    if os.path.exists(CHAIN_FILE):
        with open(CHAIN_FILE, 'r') as f:
            chain = json.load(f)
        return jsonify(chain)
    else:
        return jsonify([])

@app.route('/api/decoys')
def get_decoys():
    if os.path.exists(DECOY_DIR):
        files = os.listdir(DECOY_DIR)
        return jsonify(files)
    else:
        return jsonify([])

@app.route('/api/simulate', methods=['POST'])
def simulate_attack():
    # For simulation purposes, return a simulated event object.
    simulated_event = {
        "index": 9999,
        "timestamp": 9999999999,  # Dummy timestamp
        "event_data": {
            "action": "SIMULATED_ATTACK",
            "file": "simulated_ransomware_attack.txt"
        }
    }
    return jsonify(simulated_event)

if __name__ == '__main__':
    # Run dashboard on port 5001 to avoid conflicts
    app.run(debug=True, port=5001)
