import random
import string
import math
import constants
from datetime import date



def random_password():
    pswd_str = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in
                       range(constants.PASSWORD_LENGTH))
    return pswd_str


def otp_generator():
    pswd_str = ''.join(random.choice(string.digits) for i in range(6))
    return int(pswd_str)


# round_up
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return round(math.ceil(n * multiplier) / multiplier)


def calculate_age(dob):
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


def remove_slug_in_role(role):
    user_role = role.replace("_", " ")
    return user_role.capitalize()
