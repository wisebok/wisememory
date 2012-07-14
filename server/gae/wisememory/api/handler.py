# !/usr/bin/env python

# API Handler

__author__ = 'Youngbok Yoon <bok@wisememory.com>'

from google.appengine.ext import webapp
from api import API
import simplejson

class APIHandler(webapp.RequestHandler):
    def __init__(self):
        webapp.RequestHandler.__init__(self)
        self.methods = API()
    
    def get(self):
        action = self.request.get('api')
        if action:
            if action[0] == '_':
                self.error(403) # access denied
                return
            else:
                func = getattr(self.methods, action, None)
        if not func:
            self.error(404) # file not found
            return

        args = ()
        while True:
            key = 'arg%d' % len(args)
            val = self.request.get(key)
            if val:
                args += (simplejson.loads(val),)
            else:
                break
        result = func(*args)
        self.response.out.write(simplejson.dumps(result))

