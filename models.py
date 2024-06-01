import re
from datetime import datetime

class User:
    current_id = 0
    def __init__(self, username, email, phone="") -> None:
        self.id = self.current_id
        if self.validate_username(username):
            self.username = username

        if self.validate_email(email):
            self.email = email

        if self.validate_phone(phone):
            self.phone = phone


        self.created_at = datetime.now()
        self.last_login_date = datetime.now()
        self.wallet = 0
        self.current_id += 1


    def validate_username(self, name):
        if len(name) > 100:
            raise ZeroDivisionError
        if re.match("^[A-Za-z0-9_-]*$", name) != None:
            return True
        return False
    
    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None
    
    def validate_phone(self, phone):
        pattern = r"^[0+0-9]"
        pass