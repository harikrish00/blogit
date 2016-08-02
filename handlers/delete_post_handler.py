from handlers.handler import Handler
from handlers import blog_list_handler
from models.post import Post
import time

class DeletePostHandler(Handler):
    def post(self):
        post_id = self.request.get('post_id')
        post = Post.get_by_id(int(post_id))
        if self.authenticated():
            if post.author.username == self.user.username:
                post.delete()
                alert_message = "Your post have been deleted !"
                self.render_homepage(alert_message)
            else:
                alert_message = "You cant delete this !"
                self.render_homepage(alert_message)
        else:
            self.login_redirect()
