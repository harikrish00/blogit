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
from services.blog_handler import BlogHandler
from services.blog_list_handler import BlogListHandler
from services.new_post_handler import NewPostHandler
from services.sign_up_handler import SignUpHandler
from services.welcome_handler import WelcomeHandler
from services.login_handler import LoginHandler
from services.logout_handler import LogoutHandler

app = webapp2.WSGIApplication([
    (r'/blog', BlogListHandler),
    (r'/blog/(\d+)', BlogHandler),
    (r'/blog/newpost', NewPostHandler),
    (r'/blog/signup', SignUpHandler),
    (r'/blog/welcome', WelcomeHandler),
    (r'/blog/login', LoginHandler),
    (r'/blog/logout', LogoutHandler)
    ], debug=True)
