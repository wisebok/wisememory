# !/usr/bin/env python

# API Handler

__author__ = 'Youngbok Yoon <bok@wisememory.com>'

class APIHandler(webapp.RequestHandler):
  def get(self):
    action = self.request.get('api')
    arg_counter = 0;
    args = ()
    while True:
      arg = self.request.get('arg' + str(arg_counter))
      arg_counter += 1
      if arg:
        args += (simplejson.loads(arg),);
      else:
        break;
    result = getattr(self, action)(*args)
    self.response.out.write(simplejson.dumps((result)))
