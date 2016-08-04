#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
from handlers import blog
from handlers import blog_list
from handlers import new_post
from handlers import sign_up
from handlers import welcome
from handlers import login
from handlers import logout
from handlers import user_posts
from handlers import like_post
from handlers import comment_post
from handlers import edit_post
from handlers import delete_post
from handlers import delete_comment
from handlers import edit_comment

app = webapp2.WSGIApplication([
    (r'/', blog_list.BlogListHandler),
    (r'/blog', blog_list.BlogListHandler),
    (r'/blog/(\d+)', blog.BlogHandler),
    (r'/blog/newpost', new_post.NewPostHandler),
    (r'/blog/myposts', user_posts.UserPostsHandler),
    (r'/blog/signup', sign_up.SignUpHandler),
    (r'/blog/welcome', welcome.WelcomeHandler),
    (r'/blog/login', login.LoginHandler),
    (r'/blog/logout', logout.LogoutHandler),
    (r'/blog/likepost', like_post.LikeHandler),
    (r'/blog/editpost', edit_post.EditPostHandler),
    (r'/blog/deletepost', delete_post.DeletePostHandler),
    (r'/blog/commentpost', comment_post.CommentHandler),
    (r'/blog/deletecomment', delete_comment.DeleteCommentHandler),
    (r'/blog/editcomment', edit_comment.EditCommentHandler)
    ], debug=True)
