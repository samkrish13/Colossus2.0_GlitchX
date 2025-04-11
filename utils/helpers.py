import logging
import os

LOG_FILE = "data/logs/analysis.log"

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

def log_event(event_msg):
    logging.info(event_msg)
