from handler import Handler
from models.post import Post

class BlogHandler(Handler):
    """Blog post permalink handler class, handles the request to get a single post"""
    def get(self, post_id):
        """handles Get request for a single post id"""
        if self.authenticated():
            #get the post which is requested with post_id
            post = Post.get_by_id(int(post_id))
            if post:
                # if the post is found then redirect to the post
                self.render("blog.html", post = post)
            else:
                # if the post is not found redirect to home page
                self.render_homepage('Post is not found !')
        else:
            #if the user is not authenticated perform login page redirect
            self.login_redirect()
