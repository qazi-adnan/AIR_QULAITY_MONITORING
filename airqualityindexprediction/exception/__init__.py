import logging
import os
import sys
from datetime import datetime

# Define the log directory explicitly
log_dir = r"D:\01 COLLEGE PROJECT\AIR_QULAITY_MONITORING\airqualityindexprediction\logs"

# Ensure the directory exists
os.makedirs(log_dir, exist_ok=True)

# Define the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}_exception.log"

# Full log file path
logs_path = os.path.join(log_dir, LOG_FILE)

# Configure logging for exceptions
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.ERROR,
)


def get_exception_details(error):
    """Extract detailed exception message."""
    exc_type, exc_value, exc_traceback = sys.exc_info()
    return f"Exception Type: {exc_type.__name__}, Message: {str(error)}, Line: {exc_traceback.tb_lineno}"


def log_exception(error):
    """Logs the exception details."""
    error_message = get_exception_details(error)
    logging.error(error_message)
    return error_message


if __name__ == "__main__":
    try:
        # Example: Trigger an exception
        x = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        print("An error occurred:", log_exception(e))  # Logs and prints error
