from handlers.handler import Handler
from models.post import Post

class LikeHandler(Handler):
    def post(self):
        if self.authenticated():
            post_id = self.request.get("like")
            post = Post.get_by_id(int(post_id))
            if post.likes:
                post.likes = post.likes + 1
            else:
                post.likes = 1
            post.put()
            self.redirect("/blog")
        else:
            self.login_redirect()
