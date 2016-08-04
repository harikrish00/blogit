from handlers.handler import Handler
from models.comment import Comment
from models.post import Post

class CommentHandler(Handler):
    """Handles the request when a user comments on a post"""

    def post(self):
        """Recieves comment message from user and stores in database"""
        if self.authenticated():
            post_id = self.request.get('post_id')
            post = Post.get_by_id(int(post_id))
            comment_txt = self.request.get('comments')
            comment = Comment(comment = comment_txt, commenter = self.user, post = post)
            comment.put()
            self.redirect('/blog/%s' % (post_id))
        else:
            self.login_redirect()

    def delete(self):
        comment_id = self.request.get('comment_id')
        comment = Comment.get_by_id(int(comment_id))
        if self.authenticated():
            if comment.commenter.username == self.user.username:
                comment.delete()
            else:
                self.render_homepage("You cant delete others comment")
            self.redirect('/blog/%s' % comment.post.key().id())
        else:
            self.login_redirect()
