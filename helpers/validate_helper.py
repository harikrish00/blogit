import re

#Username can not contain spaces, or any special characters
USER_RE = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')

#Email should be in a proper format name@company.domain
EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

#Password should be minimum 3 letters upto 20 letters
PASSWORD_RE = re.compile(r'^.{3,20}$')

def valid_email(email):
    """Checks if email id entered is valid"""
    return EMAIL_RE.match(email)

def valid_name(name):
    """Checks if username enteres is valid"""
    return USER_RE.match(name)

def valid_password(password):
    """Checks if password entered is valid and matches the regular expression"""
    return PASSWORD_RE.match(password)

def valid_verify_password(password, verify_password):
    """Checks if password and verify password are same """
    if password == verify_password:
        return True
