import re

USER_RE = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
PASSWORD_RE = re.compile(r'^.{3,20}$')

def valid_email(email):
    return EMAIL_RE.match(email)

def valid_name(name):
    return USER_RE.match(name)

def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_verify_password(password, verify_password):
    if password == verify_password:
        return True
