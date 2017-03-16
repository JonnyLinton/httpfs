import logging
import os

logger = logging.getLogger("httpfs_logger")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.getcwd() + "/access.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s  - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.disabled = False
