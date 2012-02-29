from utils import debug_print
from webob import exc

import httplib2
import inspect
import json
import os.path
import settings
import sys

class MidonetClient(object):

    def __init__(self, base_url=None, token=None):
        self.h = httplib2.Http()
        if not base_url:
            self.base_url = settings.MIDONET_URL
        if not token:
            self.token = settings.AUTH_TOKEN

    def __call__(self, resource):

        path = resource.__class__.__name__.lower() + 's'
        resource.accept(self, path)
        return resource

    def _do_request(self, path, method, body='{}'):
        response, content = self.h.request(
            self.base_url + path, method, body, headers={
                                            "Content-Type": "application/json",
                                            "HTTP_X_AUTH_TOKEN": self.token} 
                                          )
        
#            frame =  inspect.stack()[2][0]
#            fi = inspect.getframeinfo(frame)
#            msg = "Call: " + os.path.basename(fi.filename)[:-2] + fi.function
        msg = "Request: " + method + " " + path
        debug_print(msg, response, content)
        
        if int(response['status']) > 300:
            raise exc.HTTPError(content)
        try:
            body = json.loads(content) if content else None
            return response, body
        except ValueError:
            return response, content
    
    def get(self, path):
        return self._do_request(path, 'GET')
    
    def put(self, path, body):
        return self._do_request(path, 'PUT', json.dumps(body))
    
    def post(self, path, body):
        return self._do_request(path, 'POST', json.dumps(body))
    
    def delete(self, path):
        return self._do_request(path, 'DELETE')
