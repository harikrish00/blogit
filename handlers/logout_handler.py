from handler import Handler
from models.user import User

class LogoutHandler(Handler):
    def get(self):
        user_cookie = self.request.cookies.get("user_id")
        if user_cookie:
            self.response.headers.add_header('Set-Cookie','user_id=; Path=/')
            User.loggedin_user = False
            self.redirect('/blog/signup')
