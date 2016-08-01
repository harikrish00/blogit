from handler import Handler
from google.appengine.ext import db
from models.post import Post
from models.user import User
from models.like import Like

class BlogListHandler(Handler):
    def get(self):
        posts = db.GqlQuery("SELECT * FROM Post"
                        " ORDER BY created DESC")
        self.render("index.html", posts = posts)
