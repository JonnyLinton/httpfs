import logging
import os

logger = logging.getLogger("httpfs_logger")
logger.setLevel(logging.DEBUG)
# Send output of logger to access.log
file_handler = logging.FileHandler(os.getcwd() + "/access.log")
# Also send output to console
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s  - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.disabled = False
