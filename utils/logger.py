import os
import logging
logger = logging.getLogger(__name__)

# set the logger level if the user sets the environment variable LOG_LEVEL
log_level = os.getenv("LOG_LEVEL", "INFO")
if log_level == "DEBUG":
    logger.setLevel(logging.DEBUG)
elif log_level == "INFO":
    logger.setLevel(logging.INFO)
elif log_level == "WARNING":
    logger.setLevel(logging.WARNING)
elif log_level == "ERROR":
    logger.setLevel(logging.ERROR)

logger.addHandler(logging.StreamHandler())
logger.name = "Bridge"

# set the logger format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.handlers[0].setFormatter(formatter)
