import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'server'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

remoteapi_CUSTOM_ENVIRONMENT_AUTHENTICATION = ('APPLICATION_ID', [ 'dev~united-learning' ])

# from graphene_gae.webapp2 import graphql_application
# from schema import schema

# graphql_application.config['graphql_schema'] = schema


# workaround for requests issue in GAE
# https://cloud.google.com/appengine/docs/python/issue-requests#issuing_an_http_request
import requests
import requests_toolbelt.adapters.appengine
requests_toolbelt.adapters.appengine.monkeypatch()
