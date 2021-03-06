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
# import os
# import webapp2

# from google.appengine.api import users
# from google.appengine.ext.webapp import template

# def render_template(handler,templatename,templatevalues):
  # path = os.path.join(os.path.dirname(__file__), 'templates/' + templatename)
  # html = template.render(path, templatevalues)
  # handler.response.out.write(html)

# class MainHandler(webapp2.RequestHandler):
    # def get(self):
	  # user = users.get_current_user()
	  # if user:
        # #render_template(self, 'index.html', {}) 
		# #self.response.out.write('<html><body>yay you are logged in</body></html>')
		# greeting = ('Welcome, %, (<a href="%s">sign out</a>)' % (user.nickname(), users.create_logout_url('/')))
	  # else:
	    # #self.response.out.write('<html><body><a href="%s">Sign in or register.</a></body></html>' % users.create_login_url('/')) 
	    # greeting = ('<a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
    # self.response.out.write('<html><body>%s</body></html>' % greeting)
	
	
# app = webapp2.WSGIApplication([
    # ('/', MainHandler)
# ], debug=True)

import webapp2
from google.appengine.api import users

class MyHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))

        self.response.out.write("<html><body>%s</body></html>" % greeting)

app = webapp2.WSGIApplication([('/', MyHandler),], debug=True)
