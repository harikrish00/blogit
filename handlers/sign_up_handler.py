from handler import Handler
from models.user import User
from helpers.validate_helper import *
from helpers.session_helper import *

class SignUpHandler(Handler):
    def get(self):
        self.render("signup.html")

    def post(self):
        # Error messages
        username_error = invalid_email = invalid_password = verify_password_error = None

        user_username = self.request.get("username")
        user_password = self.request.get("password")
        user_verify_password = self.request.get("verify")
        user_email = self.request.get("email")

        params = dict(username = user_username,
                    email = user_email)

        username = valid_name(user_username)
        password = valid_password(user_password)
        verify_password = None
        email = None

        if user_email:
            email = valid_email(user_email)
            if not email:
                params['invalid_email'] = "That's not a valid email."

        if not username:
            params['username_error'] = "That's not a valid username."
        elif (User.by_name(user_username)):
            username = None
            params['username_error'] = "User already exists !"

        if password:
            verify_password = valid_verify_password(user_password, user_verify_password)
            if not verify_password:
                params['verify_password_error'] = "Your passwords didn't match."
        else:
            params['invalid_password'] = "That wasn't a valid password."

        if username and password and verify_password and not invalid_email:
            password_hash = hash_pwd(user_username, user_password)
            user = User(username = user_username, password = password_hash, email = user_email)
            user.put()
            self.response.headers.add_header('Set-Cookie','user_id=%s; Path=/' % make_secure_value(str(user.key().id())))
            self.redirect("/blog/welcome")
        else:
            self.render("signup.html", **params)
