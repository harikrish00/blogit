
from handler import Handler
from sign_up_handler import *
from models.user import User
from google.appengine.ext import db

def valid_password(password, user_password):
    if password:
        if hash_str(password) == user_password:
            return True

def get_current_user(username):
    users = User.all()
    for user in users:
        if user.username == username:
            return user


class LoginHandler(Handler):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")

        user = get_current_user(username)

        if user:
            password = valid_password(password, user.password)

        if user and password:
            self.response.headers.add_header('Set-Cookie','user_id=%s; Path=/' % make_secure_value(str(user.key().id())))
            self.redirect("/blog/welcome")
        else:
            invalid_login = "Invalid Login !"
            self.render("login.html",
                            login_error = invalid_login,
                            username = username)
