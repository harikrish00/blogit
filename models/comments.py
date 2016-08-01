from google.appengine.ext import db
from user import User

class Comments(db.Model):
    comments = db.IntegerProperty()
    commenter = db.ReferenceProperty(User)
    post = db.ReferenceProperty(Post)
