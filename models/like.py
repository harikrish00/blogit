from google.appengine.ext import db
from user import User
from post import Post

class Like(db.Model):
    post = db.ReferenceProperty(Post, required=True, collection_name='likes')
    voter = db.ReferenceProperty(User, required=True, collection_name='likes')
