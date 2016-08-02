from handlers.handler import Handler
from models.post import Post
from models.like import Like

class LikeHandler(Handler):
    """Handles the request to like a post from a user """

    def post(self):
        """The post request is made when someone clicks on like button"""
        if self.authenticated():
            post_id = self.request.get("like")
            post = Post.get_by_id(int(post_id))
            # creator of the post can not like his/her own posts
            if not post.author.username == self.user.username:
                likes = post.likes.get()
                if likes:
                    # user can not like a post more than once
                    if not likes.voter.username == self.user.username:
                        like_new = Like(post = post, voter = self.user)
                        like_new.put()
                else:
                    like_new = Like(post = post, voter = self.user)
                    like_new.put()
            self.redirect("/blog")
        else:
            #if the user is not authenticated perform login page redirect            
            self.login_redirect()
