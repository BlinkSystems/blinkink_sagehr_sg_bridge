import os

# Sync time interval in seconds
TIME_TO_WAIT = 60
if os.getenv("SAGE_LEAVE_REQUEST_SYNC_INTERVAL"):
    TIME_TO_WAIT = int(os.getenv("SAGE_LEAVE_REQUEST_SYNC_INTERVAL"))


import json
from utils.logger import logger
from utils import sage_utils, sg_utils
from pprint import pprint, pformat
import constants
import asyncio


def init_task():
    """
    Initialize the task, check if fields and information exists.
    :return:
    """
    logger.info("Initializing task...")

    SG_REQUIRED_FIELDS = {
        "sg_sagehr_leave_request_id":
            {
                "data_type": "text",
                "editable": False,
                "label": "SageHR Leave Request ID",
                "description": "The ID of the leave request in SageHR"
            }
    }

    sg = sg_utils.get_sg_connection()

    # Check if the fields exist in ShotGrid
    logger.info("Checking if required fields exist in ShotGrid...")
    for field_name, field_data in SG_REQUIRED_FIELDS.items():
        field = sg.schema_field_read("Booking", field_name)
        if not field:
            logger.warning(f"Field {field_name} not found in ShotGrid. Creating field...")
            sg.schema_field_create("Booking", field_name, field_data)
        else:
            logger.info(f"Field {field_name} found in ShotGrid.")
    logger.info("Required fields check complete.")

async def main():

    while True:

        logger.info(" ")
        logger.info("-== Getting SG connection...")
        sg = sg_utils.get_sg_connection()

        logger.info("-== Getting leave requests from SageHR...")
        leave_requests = sage_utils.get_sage_leave_requests()

        logger.info(f"Got {len(leave_requests)} leave requests from SageHR")
        for request in leave_requests:
            logger.debug(f"Leave Request:")
            logger.debug(pformat(request))

            if request["status_code"] == "approved":
                logger.info(f"Processing leave request: {request['id']}")
                # Process the leave request

                # get username
                user_id = request["employee_id"]
                user_data = sage_utils.get_sage_user(user_id)
                logger.debug(f"User Data: {pformat(user_data)}")

                # get user's email so we can match them to a ShotGrid user
                user_email = user_data.get("email", "")
                if not user_email:
                    logger.warning(f"Email not found for user {user_id}. Skipping leave request.")
                    continue

                # get ShotGrid user
                sg_user = sg_utils.get_sg_user_by_email(user_email)

                if not sg_user:
                    logger.warning(f"ShotGrid user not found for email {user_email}. Skipping leave request.")
                    continue

                # check if the leave request is already synced
                filters = [
                    ['sg_sagehr_leave_request_id', 'is', str(request['id'])]
                ]
                existing_booking = sg.find_one('Booking', filters)

                # Create or update holiday booking in ShotGrid
                data = {
                    "note": f"Leave request synced from SageHR. Leave Request ID: {request['id']}",
                    "user": sg_user,
                    "start_date": request["start_date"],
                    "end_date": request["end_date"],
                    "sg_sagehr_leave_request_id": str(request["id"]),
                    "vacation": True,
                    "sg_status_list": "cfrm",
                }
                if existing_booking:
                    logger.info(f"Updating existing booking: {existing_booking['id']}")
                    sg.update("Booking", existing_booking["id"], data)
                else:
                    logger.info("Creating new booking in SG...")
                    booking = sg.create("Booking", data)
                    logger.info(f"Created new booking: {booking['id']}")

        logger.info(f"Waiting for {TIME_TO_WAIT} seconds before next sync...")
        await asyncio.sleep(TIME_TO_WAIT)
