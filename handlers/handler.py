import os
import webapp2
import jinja2
from google.appengine.ext import db
from models.user import User
from helpers.session_helper import *

template_dir = os.path.join(os.path.dirname(__file__), "../templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)
alert_message = ""

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        params['user'] = self.user
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def read_secure_cookie(self, name):
        cookie = self.request.cookies.get(name)
        return cookie and check_secure_val(cookie)

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))

    def authenticated(self):
        return self.read_secure_cookie('user_id')

    def login_redirect(self, auth_error = "You need to login to perform this action !"):
        self.render("login.html", auth_error = auth_error)
