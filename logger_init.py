import logging

logger = logging.getLogger("httpfs_logger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("access.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s  - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.disabled = False
