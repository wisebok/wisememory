#!/usr/bin/env python

# Model : Memory

__author__ = 'bok@wisememory.com (Youngbok Yoon)'

from google.appengine.api import users
from google.appengine.ext import db

class Memory(db.Model) :
    A = db.StringProperty()
    B = db.StringProperty()

    @property
    def tags(self, ) :
        return Tag.gql("where memories = :1", self.key(), )

class Tag(db.Model):
    name = db.StringProperty()
    user = db.ReferenceProperty()

    def get_memories(self, ) :
        for k in self.memories :
            yield Memory.gql("where __key__ = :1", k).get()
