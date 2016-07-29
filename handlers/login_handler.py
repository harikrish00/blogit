from handler import Handler
from models.user import User
from helpers.session_helper import *

class LoginHandler(Handler):
    def get(self):
        if not self.authenticated():
            self.render('login.html')
        else:
            self.redirect('/blog')

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")

        user = User.login(username, password)

        if user:
            self.response.headers.add_header('Set-Cookie','user_id=%s; Path=/' % make_secure_value(str(user.key().id())))
            self.redirect("/blog/welcome")
        else:
            invalid_login = "Invalid Login !"
            self.render("login.html",
                            login_error = invalid_login,
                            username = username)
