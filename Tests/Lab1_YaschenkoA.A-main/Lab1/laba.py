from loguru import logger
from dbmanager import *
import bcrypt
from validation.loginValidation import check_if_login_is_valid
from validation.passwordValidation import validate_password



logger.add("loguru.log") # logger


def registerUser(login: str, password: str, repeatPassword: str) -> (str, str): 
    encodedPassword = password.encode("utf-8")  # encoding 2 passwords
    encodedRepeatPassword = repeatPassword.encode("utf-8") 
    salt = bcrypt.gensalt() # generating salt for salt encoding algho
    hashed_password = bcrypt.hashpw(encodedPassword, salt)
    hashed_repeatPassword = bcrypt.hashpw(encodedRepeatPassword, salt) # now hashing
    
    if check_if_login_is_valid(login)[0] == "Success" and validate_password(password,repeatPassword) == "All good":
        if bcrypt.checkpw(encodedPassword, hashed_repeatPassword): # logging if everything is good
            logger.info(f"Login: {login}")
            logger.info(f"Encoded password: {encodedPassword}")
            logger.info(f"Encoded repeated password: {encodedRepeatPassword} Password matches!\n The user above was successfully registered!")
            

        return "Success", ""
    elif check_if_login_is_valid(login)[0] == "Failure": # logging if login is invalid
        logger.debug(f"Login: {login}")
        logger.debug(f"Encoded password: {encodedPassword}")
        logger.debug(f"Encoded repeated password: {encodedRepeatPassword}")
        logger.debug(f"\n{check_if_login_is_valid(login)}")

        return "Failure", f"{check_if_login_is_valid(login)}"
    else: # else logging if password is invalid
        logger.debug(f"Login: {login}")
        logger.debug(f"Encoded password: {encodedPassword}")
        logger.debug(f"Encoded repeated password: {encodedRepeatPassword}")
        logger.debug(f"\n{validate_password(password,repeatPassword)}")

        return "Failure", f"{validate_password(password,repeatPassword)}"
    


    
    




