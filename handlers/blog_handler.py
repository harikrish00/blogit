from handler import Handler
from models.post import Post

class BlogHandler(Handler):
    def get(self, post_id):
        if self.authenticated():
            post = Post.get_by_id(int(post_id))
            self.render("blog.html", post = post)
        else:
            self.login_redirect()
