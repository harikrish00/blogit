import hmac
import random
import string
import hashlib
import os

SECRET = os.environ['BLOG_SECRET']

def make_salt():
    return ''.join(random.choice(string.letters) for x in range(5))

def hash_pwd(username, pw, salt=None):
    if not salt:
        salt = make_salt()
    hash_pw = hashlib.sha256(username + pw + salt).hexdigest()
    return "%s|%s" % (salt, hash_pw)

def make_secure_value(val):
       return '%s|%s' % (str(val), hmac.new(SECRET, val).hexdigest())

def validate_pw(username, password, hash_val):
    salt = hash_val.split('|')[0]
    return hash_pwd(username, password, salt) == hash_val

def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_value(val):
        return val
