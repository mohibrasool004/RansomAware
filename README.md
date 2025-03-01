RansomAware: Blockchain-Backed, Behavior-Based Ransomware Detection with Decoy Traps
Overview
RansomAware is an innovative cybersecurity tool designed to detect ransomware attacks at their early stages. It uses a decoy-based approach to lure attackers away from real data, while a custom blockchain-immutable logging system records all file events for forensic analysis. An integrated, interactive dashboard offers real-time monitoring, alerts, and reporting features, making it a robust, proactive solution for mitigating ransomware threats.

Features
Decoy File Deployment: Generates and deploys realistic decoy files in sensitive directories to mislead attackers.
Real-Time File Monitoring: Continuously monitors file system events (creation, modification, deletion) using the Watchdog library.
Blockchain-Based Logging: Records file events in an immutable blockchain ledger to ensure tamper-proof evidence.
Behavioral Anomaly Detection: Detects abnormal activity patterns (e.g., rapid file modifications) indicative of ransomware behavior.
Interactive Dashboard:
Event Logs: Displays real-time logs with options for sharing and PDF report generation.
Intrusion Alerts: Provides dynamic alerts with blinking notifications and an emergency lockdown button.
Live Intruder Tracking: Fetches IP and geolocation details using the ipinfo.io API.
Event Frequency Chart: Visualizes event data using Chart.js.
File Interaction Simulator & Decoy Control Panel: Demonstrates and monitors decoy file interactions.
Smart Notification System: Simulated integration for sending alert notifications (e.g., via email or Telegram).
Tech Stack
Backend: Python, Flask
Monitoring: Watchdog library
Blockchain: Custom Python blockchain implementation
Frontend: HTML, Bootswatch Darkly, Chart.js, jsPDF
External API: ipinfo.io for live intruder tracking
Others: JavaScript, jQuery
Installation
Clone the Repository:

bash
Copy
Edit
git clone <repository_url>
cd RansomAware
Setup Virtual Environment (Optional but Recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy
Edit
pip install flask watchdog
Configure API Token:

Sign up at ipinfo.io for an API token.
In index.html, replace <YOUR_TOKEN_HERE> with your actual token.
Usage
Run the Core Application:

Start the file monitoring and blockchain logging modules:

bash
Copy
Edit
python backend/monitor.py
Run the Dashboard:

Launch the Flask dashboard server (e.g., on port 5001):

bash
Copy
Edit
python dashboard.py
Access the Dashboard:

Open your web browser and go to http://localhost:5001 to view real-time logs, alerts, charts, and to interact with simulation features.

Project Structure
php
Copy
Edit
RansomAware/
├── backend/
│   ├── monitor.py          # File monitoring & logging module
│   ├── blockchain.py       # Custom blockchain implementation
│   ├── decoy_generator.py  # Decoy file generation module
│   └── anomaly_detection.py  # Anomaly detection module
├── dashboard.py            # Flask dashboard server
├── templates/
│   └── index.html          # Dashboard frontend
├── static/
│   ├── css/                # Custom styles (if any)
│   └── js/                 # Custom scripts (if any)
├── chain.json              # Blockchain ledger file
└── README.md
How It Works
Decoy File Generation:
Realistic decoy files are generated and placed in strategic locations to act as bait for ransomware.

Real-Time Monitoring:
The Watchdog library monitors file events continuously, capturing any unauthorized or rapid file changes.

Blockchain Logging:
All detected events are hashed and recorded in a blockchain ledger, ensuring the integrity of forensic data.

Anomaly Detection:
A threshold-based algorithm identifies abnormal activity patterns and triggers alerts.

Interactive Dashboard:
The dashboard visualizes real-time logs, intrusion alerts, and event frequencies. It also includes functionalities like live intruder tracking, emergency lockdown, report sharing, and PDF report generation.