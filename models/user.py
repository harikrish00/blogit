from google.appengine.ext import db
from helpers.session_helper import *

class User(db.Model):
    username = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    email = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add = True)
    loggedin_user = False

    @classmethod
    def by_id(cls, user_id):
        return User.get_by_id(user_id)

    @classmethod
    def by_name(cls, username):
        return User.all().filter("username =",username).get()

    @classmethod
    def login(cls, username, pw):
        user = cls.by_name(username)
        if user and validate_pw(username, pw, user.password):
            User.loggedin_user = True
            return user
