APP_NAME = "SageHR <-> ShotGrid Bridge"
APP_VERSION = "v1.0.0"

import os
from utils.logger import logger

logger.info(" ")
logger.info(f"-== Checking app requirements...")

SAGEHR_API_URL = os.getenv("SAGEHR_API_URL")
if not SAGEHR_API_URL:
    raise ValueError("Environment Variable SAGEHR_API_URL is not set!")

SAGEHR_API_SECRET = os.getenv("SAGEHR_API_KEY", "")
if not SAGEHR_API_SECRET:
    logger.warning("Environment Variable SAGEHR_API_KEY is not set!")
    SAGEHR_API_SECRET = ""
#     raise ValueError("Environment Variable SAGEHR_API_SECRET is not set!")

SG_SITE_URL = os.getenv("SG_SITE_URL")
if not SG_SITE_URL:
    raise ValueError("Environment Variable SG_SITE_URL is not set!")

SG_SCRIPT_NAME = os.getenv("SG_SCRIPT_NAME")
if not SG_SCRIPT_NAME:
    raise ValueError("Environment Variable SG_SCRIPT_NAME is not set!")

SG_SCRIPT_KEY = os.getenv("SG_SCRIPT_KEY")
if not SG_SCRIPT_KEY:
    raise ValueError("Environment Variable SG_SCRIPT_KEY is not set!")

logger.info("----------------------------------------------------")
