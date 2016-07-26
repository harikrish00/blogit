from handler import Handler

class LogoutHandler(Handler):
    def get(self):
        user_cookie = self.request.cookies.get("user_id")
        if user_cookie:
            self.response.headers.add_header('Set-Cookie','user_id=; Path=/')
            self.redirect('/blog/signup')
