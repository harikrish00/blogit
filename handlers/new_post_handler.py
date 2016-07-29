from models.post import Post
from handler import Handler

class NewPostHandler(Handler):
    def get(self):
        if self.authenticated():
            self.render("new.html")
        else:
            self.redirect("/blog/login")
            alert_message = "Please login to access this feature"

    def post(self):
        title = self.request.get("subject")
        content = self.request.get("content")

        if title and content:
            a = Post(title = title, content = content)
            a.put()
            self.redirect("/blog/%s" % (a.key().id()))
        else:
            error = "Both title and art needed for submitting !"
            self.render("new.html",subject = title, content = content, error = error)
