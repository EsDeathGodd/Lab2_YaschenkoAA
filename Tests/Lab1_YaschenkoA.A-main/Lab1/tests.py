import unittest
from laba import registerUser
from validation.loginValidation import check_if_login_is_valid,check_login_type
from validation.passwordValidation import validate_password


class TestIfValidLogin(unittest.TestCase):

    def test_login(self):
        #valid inputs
        self.assertEqual(check_if_login_is_valid("login@mail.ru"),("Success",""))
        self.assertEqual(check_if_login_is_valid("+7-999-999-9999"),("Success",""))
        self.assertEqual(check_if_login_is_valid("5simvolov"),("Success",""))
        # invalid inputs
        self.assertEqual(check_if_login_is_valid("edg1337"),("Failure","User with this login already exists"))
        self.assertEqual(check_if_login_is_valid("+7-999-999-999"),("Failure","Phone number is in incorrect format, must be (+x-xxx-xxx-xxxx)"))
        self.assertEqual(check_if_login_is_valid("edg@mailru"),("Failure", "Email must be in a format of (xxx@xxx.xx)"))
        self.assertEqual(check_if_login_is_valid("aaa"),("Failure", "Login must be at least 5 characters long"))
        self.assertEqual(check_if_login_is_valid("somelogin***"),("Failure", "Login can only contain latin characters, numbers from 0 to 9, and _ symbol"))
        self.assertEqual(check_if_login_is_valid(""),("Failure", "Login can not be empty")) # must be a string index out of range error

class TestIfValidPassword(unittest.TestCase):

    def test_pass(self):
        #invalid
        self.assertEqual(validate_password("jeka","jeka"),("Password must be at least 7 characters long"))
        self.assertEqual(validate_password("jeka","jeka2"),("Passwords does not match"))
        self.assertEqual(validate_password("ааааааааааааааа","ааааааааааааааа"),("Password must contain at least 1 special symbol"))
        self.assertEqual(validate_password("латиницавпароле+","латиницавпароле+"),("Password must contain at least 1 uppercase letter"))
        self.assertEqual(validate_password("12345678","12345678"),("Password must contain at least 1 uppercase letter"))
        self.assertEqual(validate_password("coolpasswordxd1","coolpasswordxd1"),("Password can not contain any latin characters"))
        self.assertEqual(validate_password("Пожалуйстапомогите+","Пожалуйстапомогите+"),("Password must contain at least 1 number"))
        self.assertEqual(validate_password("ПАРОЛЬКАПСОМ+1","ПАРОЛЬКАПСОМ+1"),("Password must contain at least 1 lowercasse letter"))
        #valid
        self.assertEqual(validate_password("Подходящийпароль1+1","Подходящийпароль1+1"),("All good"))
        self.assertEqual(validate_password("Какойтопароль+2","Какойтопароль+2"),("All good"))
        self.assertEqual(validate_password("Последнийпарольнатест))2","Последнийпарольнатест))2"),("All good"))

class TestLoginType(unittest.TestCase):

    def test_login_type(self):
        #valid
        self.assertEqual(check_login_type("login@mail.ru"),(2))
        self.assertEqual(check_login_type("+7-999-999-9999"),(1))
        self.assertEqual(check_login_type("shlyapa"),(3))
