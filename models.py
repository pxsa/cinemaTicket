import re
from datetime import datetime

class User:
    usernames = []
    emails = []
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
            raise Exception("unable to validate long username")
        elif re.match("^[A-Za-z0-9]*$", name) != None:
            if name not in self.usernames:
                self.usernames.append(name)
                return True
        return False
    
    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, email) is not None:
            if email not in self.emails:
                self.emails.append(email)
                return True
        return False
    
    def validate_phone(self, phone):
        # 09392972197
        # +989*********
        # ^(09\d{9}|\+989\d{9})$
        pattern = r"^(\+98|0)\d{10}$"
        return re.match(pattern, phone) is not None
    

    def validate_password(self, password):
        # check the length
        if len(password) < 8:
            return False
        
        # check the count of specific characters
        specific_chars = []
        for ch in password:
            if ch in ['@', '#', '&', '$']:
                specific_chars.append(ch)

        if len(specific_chars) < 2:
            return False
        
        # check only valid charachters
        pattern = r'^[a-zA-Z0-9@#$&]*$'
        return re.match(pattern, password) is not None

        