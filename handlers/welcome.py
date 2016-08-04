from handler import Handler
from models.user import User
from helpers.session_helper import *

class WelcomeHandler(Handler):
    """Redirects user to welcome page after the sign up with our blog"""

    def get(self):
        user_id = self.request.cookies.get("user_id")
        if user_id and make_secure_value(user_id.split('|')[0]) == user_id:
            username = User.get_by_id(int(user_id.split('|')[0])).username
            self.render("welcome.html",name = username)
        else:
            self.redirect("/blog/signup")
