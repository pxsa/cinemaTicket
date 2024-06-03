import unittest
import sys
sys.path.append("../")
from models import User

class UserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User("ali", "ali@gmail.com", "123$@#salam", "")
    
    def test_validate_username(self):
        # test unique username
        self.assertEqual(self.user.validate_username("ali"), False)

        #  test length of username
        long_name = "1" * 101
        self.assertRaises(Exception, self.user.validate_username, long_name)

        # test letters and number
        bad_name = "%hadi*()"
        self.assertEqual(False, self.user.validate_username(bad_name))

    
    def test_validate_email(self):
        # unique email only
        email = "akbar@gmail.com"
        self.assertEqual(True, self.user.validate_email(email))
        self.assertEqual(False, self.user.validate_email(email))

        # invalide email
        invalid_email = "salam_khobi"
        self.assertEqual(False, self.user.validate_email(invalid_email))

    
    def test_validate_phone(self):
        valid_phone1 = "09391111111"
        valid_phone2 = "+989222222222"
        invalid_phone = "093933333"
        invalid_phone2 = "09392jk97219"

        # correct numbers
        self.assertEqual(True, self.user.validate_phone(valid_phone1))
        self.assertEqual(True, self.user.validate_phone(valid_phone2))

        # invalid length
        self.assertEqual(False, self.user.validate_phone(invalid_phone))

        # invalid character
        self.assertEqual(False, self.user.validate_phone(invalid_phone2))
        

    def test_validate_password(self):

        #  examine the length of password
        password = "1" * 8  + "@#"
        self.assertEqual(True, self.user.validate_password(password))
        password = "1" * 6
        self.assertEqual(False, self.user.validate_password(password))

        # at least contains 2 of these characters [$, &, #, @]
        password = "@salam&salam"
        self.assertEqual(True, self.user.validate_password(password))
        password = "@salamklsalam"
        self.assertEqual(False, self.user.validate_password(password))

        # check allowed characters
        password = "fsjdflk&#@$jdkjgdf@@@-dfd"
        self.assertEqual(False, self.user.validate_password(password))
