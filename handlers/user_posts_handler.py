from handler import Handler
from google.appengine.ext import db
from models.post import Post
from models.user import User

class UserPostsHandler(Handler):
    def get(self):
        # posts = db.GqlQuery("SELECT * FROM Post where author='%s'"
        #                 " ORDER BY created DESC" % (self.user.key().id()))
        # print "-->",self.user.key().id(),posts
        posts = Post.by_author(self.user)
        self.render("index.html", posts = posts)
