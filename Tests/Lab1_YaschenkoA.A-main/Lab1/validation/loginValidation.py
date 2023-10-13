import re
from loguru import logger
from dbmanager import checkIfRegistered

def check_login_type(login: str) -> str:
    try:
        if login[0] == "+":

            return 1
        elif "@" in login:

            return 2
        else:

            return 3
    except Exception as e:
        logger.debug(f"{e} error happened during handling the operation in function check_login_type")

def check_if_login_is_valid(login: str) -> (str,str): #checking if login is valid
    login_type = check_login_type(login) # getting login type
    if checkIfRegistered(login=login):

        return "Failure", "User with this login already exists"
    elif len(login) == 0:
        
        return "Failure", "Login can not be empty"
    
    match login_type:
        case 1:
                pattern = r'\+\d-\d{3}-\d{3}-\d{4}' # if login type == phone login type, then checking if phone number is valid
                match = re.fullmatch(pattern,login)
                if match:

                    return "Success", ""
                else:

                    return "Failure", "Phone number is in incorrect format, must be (+x-xxx-xxx-xxxx)"
        case 2:
                pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' # if login type == email login type checking if email is valid
                match = re.fullmatch(pattern,login)
                if match:

                    return "Success", ""
                else:

                    return "Failure", "Email must be in a format of (xxx@xxx.xx)"
        case 3: 
            pattern = r'[^aA-zZ0-9_]' # pattern to search for banned symbols
            if len(login) <5 : 
                
                return "Failure", "Login must be at least 5 characters long"

            elif re.search(pattern,login):

                return "Failure", "Login can only contain latin characters, numbers from 0 to 9, and _ symbol"
            else:

                return "Success", ""
        case _:
            return "Failure", "Unknown mistake happened during validation login"