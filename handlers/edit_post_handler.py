from handlers.handler import Handler
from models.post import Post

class EditPostHandler(Handler):

    def get(self):
        if self.authenticated():
            post_id = self.request.get('post_id')
            post = Post.get_by_id(int(post_id))
            if post.author.username == self.user.username:
                self.render("edit.html",post = post)
            else:
                self.redirect('/')

    def post(self):
        post_id = self.request.get('post_id')
        title = self.request.get('subject')
        content = self.request.get('content')
        post = Post.get_by_id(int(post_id))
        post.title = title
        post.content = content
        post.put()
        self.redirect('/')
