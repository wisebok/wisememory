#!/usr/bin/env python

# Model : user

__author__ = 'bok@wisememory.com (Youngbok Yoon)'

from google.appengine.api import users
from google.appengine.ext import db

class UserPrefs(db.Model):
    userid = db.StringProperty()
