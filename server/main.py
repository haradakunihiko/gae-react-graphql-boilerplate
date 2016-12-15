# -*- coding:utf-8 -*-
from webapp2 import Route, WSGIApplication

config = {
    'webapp2_extras.sessions': {
        'secret_key': 'my-app-cookie-key',
        'cookie_name': '_my-app',
    }
}

# accept HTTP PATCH method
WSGIApplication.allowed_methods = WSGIApplication.allowed_methods.union(('PATCH',))
app = WSGIApplication([
    Route(r'/graphql', handler='handler.graphql.GraphqlHandler'),
], debug=True, config=config)
