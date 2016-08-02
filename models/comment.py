from google.appengine.ext import db
from user import User
from post import Post

class Comment(db.Model):
    comment = db.TextProperty()
    commenter = db.ReferenceProperty(User, required = True, collection_name="comments")
    post = db.ReferenceProperty(Post, required = True, collection_name = "comments")
