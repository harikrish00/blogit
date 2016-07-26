import re
from models.user import User

class ValidateHelper():
    USER_RE = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
    EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
    PASSWORD_RE = re.compile(r'^.{3,20}$')

    def valid_email(self, email):
        return ValidateHelper.EMAIL_RE.match(email)

    def valid_name(self, name):
        return ValidateHelper.USER_RE.match(name)

    def valid_password(self, password):
        return ValidateHelper.PASSWORD_RE.match(password)

    def valid_verify_password(self, password, verify_password):
        if password == verify_password:
            return True

    def user_exists(self, username):
        users = User.all()
        for user in users:
            if user.username == username:
                return True
