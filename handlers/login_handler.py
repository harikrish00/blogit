from handler import Handler
from models.user import User
from helpers.session_helper import *

class LoginHandler(Handler):
    """ Handles login request to the blog page"""
    def get(self):
        if not self.authenticated():
            # if the user is not autheticated it redirects to login page
            self.render('login.html')
        else:
            # if the user is autheticated it redirects to home page
            self.redirect('/blog')

    def post(self):
        """ Authenticates and logs in the user"""
        username = self.request.get("username")
        password = self.request.get("password")

        # User class method login to autheticate the user
        user = User.login(username, password)

        if user:
            # if successfull login, then store cookie
            self.response.headers.add_header('Set-Cookie','user_id=%s; Path=/' % make_secure_value(str(user.key().id())))
            self.redirect("/blog/welcome")
        else:
            # if unsuccessfull login, then provide error message and redirect to login page
            invalid_login = "Invalid Login !"
            self.render("login.html",
                            login_error = invalid_login,
                            username = username)
