from handler import Handler
from google.appengine.ext import db
from models.post import Post
from models.user import User
from models.like import Like

class BlogListHandler(Handler):
    """Lists all the posts on the home page, handles request to render index page
    with all the posts """
    def get(self):
        posts = Post.get_all_posts()
        if posts:
            self.render("index.html", posts = posts)
