from google.appengine.ext import db
from user import User

class Post(db.Model):
    title = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    likes = db.IntegerProperty()
    created = db.DateTimeProperty(auto_now_add = True)
    author = db.ReferenceProperty(User)

    @classmethod
    def by_author(self, user):
        return Post.all().filter("author =", user)
