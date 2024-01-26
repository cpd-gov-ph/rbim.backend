import constants
import re

class PasswordValidation:

    @staticmethod
    def validate_characters_of_password(password : str):
        if (password.isalpha() == True) or (password.isnumeric() == True):
            raise Exception("Password should contain alphanumeric values")
        return None

    @staticmethod
    def validate_length_of_password(password : str):
        if len(password) < constants.PASSWORD_LENGTH:                                                                         
            raise Exception(constants.PASSWORD_LENGTH_INVALID_ERROR_MSG.format(constants.PASSWORD_LENGTH))
        return None

class EmailValidation:
    @staticmethod
    def validate_email(email : str):
        regex = re.compile('[_!#$%^&*()<>?/\|}{~:]') 
        if ("@" not in email or regex.search(email) != None) and email != "":  
            raise Exception(constants.INVALID_EMAIL_ERROR_MSG)
        return None

class PageValidation:
    @staticmethod
    def validate_page(data : dict):
        mandatory_fields = ['page','page_size']
        for i in mandatory_fields:
            if i not in data.keys():
                raise Exception(constants.KEYS_REQUIRED_ERROR_MSG.format(i))
            elif data[i] == "" or data[i] == None:
                raise Exception("please enter your {} to proceed".format(i))
        return None

    @staticmethod
    def validate_page_with_status(data : dict):
        mandatory_fields = ['page','page_size', 'status']
        for i in mandatory_fields:
            if i not in data.keys():
                raise Exception(constants.KEYS_REQUIRED_ERROR_MSG.format(i))
            elif data[i] == "" or data[i] == None:
                raise Exception("please enter your {} to proceed".format(i))
        return None