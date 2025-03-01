import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
from blockchain import Blockchain
blockchain = Blockchain()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class DecoyEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.event_times = []  # store timestamps of events

    def record_event(self):
        current_time = time.time()
        self.event_times.append(current_time)
        # Remove events older than one minute
        self.event_times = [t for t in self.event_times if current_time - t < 60]
        if len(self.event_times) > 3:  # threshold
            print("Warning: Unusual activity detected!")
            # Optionally log this event to blockchain as well
            self.log_event("ANOMALOUS_ACTIVITY", "Multiple rapid file events detected")

    def on_modified(self, event):
        if not event.is_directory:
            logging.info(f"Modified: {event.src_path}")
            self.record_event()
            self.log_event("MODIFIED", event.src_path)
    
    def on_created(self, event):
        if not event.is_directory:
            logging.info(f"Created: {event.src_path}")
            self.record_event()
            self.log_event("CREATED", event.src_path)
    
    def on_deleted(self, event):
        if not event.is_directory:
            logging.info(f"Deleted: {event.src_path}")
            self.record_event()
            self.log_event("DELETED", event.src_path)

    def log_event(self, action, filepath):  # Added 'self'
        event_data = {"action": action, "file": filepath}
        blockchain.add_event(event_data)
        print(f"Logged event: {event_data}")
    

if __name__ == "__main__":
    path = "./decoys"
    event_handler = DecoyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
