from handler import Handler
from google.appengine.ext import db
from models.post import Post
from models.user import User

class UserPostsHandler(Handler):
    """To fetch user specific posts which maps to 'My Posts' link on the blog"""

    def get(self):
        posts = Post.by_author(self.user)
        self.render("index.html", posts = posts)
