import logging
import os
from datetime import datetime

# Define the log directory explicitly
log_dir = r"D:\01 COLLEGE PROJECT\AIR_QULAITY_MONITORING\airqualityindexprediction\logs"

# Ensure the directory exists
os.makedirs(log_dir, exist_ok=True)

# Define the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Full log file path
logs_path = os.path.join(log_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

logging.info("Logging is set up successfully.")
