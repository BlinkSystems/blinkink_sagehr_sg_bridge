import constants
import shotgun_api3


def get_sg_connection():
    sg = shotgun_api3.Shotgun(
        constants.SG_SITE_URL,
        script_name=constants.SG_SCRIPT_NAME,
        api_key=constants.SG_SCRIPT_KEY
    )
    return sg


def get_sg_user_by_email(email):
    sg = get_sg_connection()
    filters = [
        ['email', 'is', email]
    ]
    fields = ['id', 'email']
    user = sg.find_one('HumanUser', filters, fields)
    return user