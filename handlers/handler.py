import os
import webapp2
import jinja2
import hmac
import random
import string
import hashlib
from models.post import Post
from google.appengine.ext import db
from models.user import User

template_dir = os.path.join(os.path.dirname(__file__), "../templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)
SECRET = 'IAmVerySecret12!'

def make_salt():
    return ''.join(random.choice(string.letters) for x in range(5))

def hash_pwd(username, pw, salt=None):
    if not salt:
        salt = make_salt()
    hash_pw = hashlib.sha256(username + pw + salt).hexdigest()
    return "%s|%s" % (salt, hash_pw)

def make_secure_value(val):
       return '%s|%s' % (str(val), hmac.new(SECRET, val).hexdigest())

def validate_pw(username, password, hash_val):
    salt = hash_val.split('|')[0]
    return hash_pwd(username, password, salt) == hash_val

def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_value(val):
        return val

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
