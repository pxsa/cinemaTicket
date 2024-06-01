import unittest
import sys
sys.path.append("../")
from models import User

class UserTest(unittest.TestCase):
    def test_validate_username(self):
        u = User("ali", "ali@gmail.com")
        self.assertEqual(u.validate_username("ali"), True)

        #  test length of username
        long_name = "1" * 101
        self.assertRaises(ZeroDivisionError, u.validate_username, long_name)

        # test letters and number
        bad_name = "%hadi*()"
        self.assertEqual(False, u.validate_username(bad_name))