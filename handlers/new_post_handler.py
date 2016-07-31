from models.post import Post
from handler import Handler

class NewPostHandler(Handler):

    def check_authenticated(self):
        if not self.authenticated():
            self.login_redirect()
        else:
            return True

    def get(self):
        if self.check_authenticated():
            self.render("new.html")

    def post(self):
        title = self.request.get("subject")
        content = self.request.get("content")

        if self.check_authenticated():
            if title and content:
                a = Post(title = title, content = content, author = self.user)
                a.put()
                self.redirect("/blog/%s" % (a.key().id()))
            else:
                error = "Both title and art needed for submitting !"
                self.render("new.html",subject = title, content = content, error = error)
