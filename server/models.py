# -*- coding:utf-8 -*-
from google.appengine.ext import ndb


class User(ndb.Model):
    email = ndb.StringProperty()
    name = ndb.StringProperty()
    password = ndb.StringProperty()
    admin = ndb.BooleanProperty()
