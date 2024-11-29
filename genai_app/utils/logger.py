import logging

# Configure logger
logger = logging.getLogger("GenAI")
logger.setLevel(logging.DEBUG)

# Console handler for real-time logs
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(console_format)

# File handler for detailed logs
file_handler = logging.FileHandler("output.log", mode="w")  # Overwrite file on each run
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
