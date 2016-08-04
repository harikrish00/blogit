from handlers.handler import Handler
from models.comment import Comment

class DeleteCommentHandler(Handler):
    """Handles the request when a user deletes a comment on a post"""

    def post(self):
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
