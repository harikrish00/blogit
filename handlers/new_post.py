from models.post import Post
from handler import Handler

class NewPostHandler(Handler):
    """ Handles creating a new blog post along with author name"""
    def get(self):
        """Renders the form for new post"""
        if self.authenticated():
            # Check if user is authenticated to render form for new post
            self.render("new.html")
        else:
            # if the user is not autheticated it redirects to login page
            self.login_redirect()

    def post(self):
        """Handles post request to store the blog post information into database"""
        title = self.request.get("subject")
        content = self.request.get("content")

        if self.authenticated():
            if title and content:
                a = Post(title = title, content = content, author = self.user)
                a.put()
                self.redirect("/blog/%s" % (a.key().id()))
            else:
                error = "Both title and art needed for submitting !"
                self.render("new.html",subject = title, content = content, error = error)
        else:
            # if the user is not autheticated it redirects to login page
            self.login_redirect()
