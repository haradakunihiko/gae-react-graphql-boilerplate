# -*- coding:utf-8 -*-
import webapp2
from schema import schema
import json


class GraphqlHandler(webapp2.RequestHandler):

    def post(self):
        data = json.loads(self.request.body)
        if 'query' in data:
            self._process(data['query'])

    def get(self):
        query = self.request.get('query')
        self._process(query)

    def _process(self, query):
        result = schema.execute(query)
        if len(result.errors) > 0:
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(json.dumps([error.message for error in result.errors]))
        else:
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(json.dumps(result.data))
