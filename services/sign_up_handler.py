from handler import Handler
from models.user import User
from helpers.validate_helper import ValidateHelper
import hmac

helper = ValidateHelper()
SECRET = 'IAmVerySecret12!'

def make_salt():
    return ''.join(random.choice(string.letters) for x in range(5))

def hash_str(string_to_hash, salt = None):
    hash_pw = hmac.new(str(string_to_hash), SECRET).hexdigest()
    return hash_pw

def make_secure_value(s):
       return "%s|%s" % (s,hash_str(s))

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

        username = helper.valid_name(user_username)
        password = helper.valid_password(user_password)
        verify_password = None
        email = None

        if user_email:
            email = helper.valid_email(user_email)
            if not email:
                invalid_email = "That's not a valid email."

        if not username:
            username_error = "That's not a valid username."
        elif (helper.user_exists(username=user_username)):
            username = None
            username_error = "User already exists !"

        if password:
            verify_password = helper.valid_verify_password(user_password, user_verify_password)
            if not verify_password:
                verify_password_error = "Your passwords didn't match."
        else:
            invalid_password = "That wasn't a valid password."

        if username and password and verify_password and not invalid_email:
            password_hash = hash_str(user_password)
            user = User(username = user_username, password = password_hash, email = user_email)
            user.put()
            self.response.headers.add_header('Set-Cookie','user_id=%s' % make_secure_value(str(user.key().id())))
            self.redirect("/blog/welcome")
        else:
            self.render("signup.html",
            username_error = username_error,
            username = user_username,
            invalid_password = invalid_password,
            verify_password_error = verify_password_error,
            invalid_email = invalid_email,
            email = user_email)
