from google.appengine.ext import db
from user import User

class Post(db.Model):
    title = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    author = db.ReferenceProperty(User,
                                required = True,
                                collection_name = "posts")

    @classmethod
    def by_author(self, user):
        return Post.all().filter("author =", user)
