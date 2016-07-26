from handler import Handler
from sign_up_handler import *

class WelcomeHandler(Handler):
    def get(self):
        user_id = self.request.cookies.get("user_id")
        if user_id:
            # print "-->%s > %s" % (make_secure_value(user_id.split('|')[0]), user_id.split('|')[0])
            if make_secure_value(user_id.split('|')[0]) == user_id:
                username = User.get_by_id(int(user_id.split('|')[0])).username
                self.write("Thanks for signing up %s" % (username))
            else:
                self.redirect("/blog/signup")
