import asyncio
from utils.logger import logger
from pprint import pprint, pformat
import constants

logger.info(f"""
-== Starting {constants.APP_NAME}... 
Version: {constants.APP_VERSION}
""")

logger.info("-== Connecting to ShotGrid API...")
from utils import sg_utils
sg = sg_utils.get_sg_connection()
logger.info("Connected to ShotGrid API successfully!")
logger.info(" ")

logger.info("-== Running sync tasks...")
import tasks.sync_leave_requests
asyncio.run(tasks.sync_leave_requests.main())
