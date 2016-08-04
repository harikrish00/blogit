import os
import webapp2
import jinja2
from google.appengine.ext import db
from models.user import User
from models.post import Post
from helpers.session_helper import *
import time

template_dir = os.path.join(os.path.dirname(__file__), "../templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class Handler(webapp2.RequestHandler):
    """Base handler class, inhertis from webapp2, from which all the other classes inherit from"""

    def write(self, *a, **kw):
        """Writes plain string to web page"""
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        """Returns the rendered string from template object"""
        params['user'] = self.user
        return render_str(template, **params)

    def render(self, template, **kw):
        """Renders frontend page with templates"""
        self.write(self.render_str(template, **kw))

    def render_homepage(self,alert_message):
        self.render("index.html",posts = Post.get_all_posts(), alert_message = alert_message)

    def read_secure_cookie(self, name):
        """Read the secure cookie from web request"""
        cookie = self.request.cookies.get(name)
        return cookie and check_secure_val(cookie)

    def initialize(self, *a, **kw):
        """Overrided initialize method to initialize user"""
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))

    def authenticated(self):
        """check if a user is autheticated by reading the cookie"""
        return self.read_secure_cookie('user_id')

    def login_redirect(self, auth_error = "You need to login to perform this action !"):
        """Perform login redirect if the user us not authenticated"""
        self.render("login.html", auth_error = auth_error)
