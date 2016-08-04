from handlers.handler import Handler
from models.comment import Comment

class EditCommentHandler(Handler):

    def get(self):
        if self.authenticated():
            comment_id = self.request.get('comment_id')
            comment = Comment.get_by_id(int(comment_id))
            if comment.commenter.username == self.user.username:
                self.render("edit_comment.html",comment = comment)
            else:
                self.render_homepage("You can not edit others comment !")
        else:
            self.login_redirect()

    def post(self):
        comment_id = self.request.get('comment_id')
        comment_txt = self.request.get('comment')
        comment = Comment.get_by_id(int(comment_id))
        comment.comment = comment_txt
        comment.put()
        self.redirect('/blog/%s' % comment.post.key().id())
