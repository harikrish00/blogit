from handler import Handler
from google.appengine.ext import db
from models.post import Post

class BlogListHandler(Handler):
    def get(self):
        posts = db.GqlQuery("SELECT * FROM Post"
                        " ORDER BY created DESC")
        self.render("index.html", posts = posts)

    def post(self):
        post_id = self.request.get("like")
        post = Post.get_by_id(int(post_id))
        if post.likes:
            post.likes = post.likes + 1
        else:
            post.likes = 1
        post.put()
        print "====>",post.likes
        self.redirect("/blog")
