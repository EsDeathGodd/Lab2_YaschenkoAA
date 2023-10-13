import re


def validate_password(password: str, passcopy: str) -> str: # searches if contains cyryllic letters, and other stuff stated below
    if password != passcopy:

        return "Passwords does not match"

    elif len(password) == 0:

        return "Password is empty"
    elif len(password) < 7:
        
        return "Password must be at least 7 characters long"
    else:
        patternLatins=r'[aA-zZ]' # if has latin letters
        patternSpecialSymbols=r'[_#$%^&*()!_+-=\[\]{};\':"\\|,.<>/?]' # if has spec symbol
        patternUppercase=r'[А-Я]' # if has uppercase letter
        patternNumbers=r'[0-9]' # if has number
        patternLowercase=r'[а-я]' # if has lowercase letter
        pattern = r'[^аА-яЯЁ0-9_#$%^&*()!_+-=\[\]{};\':"\\|,.<>/?]' # if matches all conditions
        if re.search(patternLatins, password):
            
            return "Password can not contain any latin characters"
        elif not re.search(patternSpecialSymbols, password):

            return "Password must contain at least 1 special symbol"
        elif not re.search(patternUppercase, password):

            return "Password must contain at least 1 uppercase letter"
        elif not re.search(patternNumbers, password):

            return "Password must contain at least 1 number"
        elif not re.search(patternLowercase, password):

            return "Password must contain at least 1 lowercasse letter"
        elif re.search(pattern, password): # pattern catches all the cyryllic letters, special symbols and numbers from 0 to 9

            return "Password can contain only cyryllic letters, special symbols, numbers from 0 to 9"
        else:

            return "All good"
