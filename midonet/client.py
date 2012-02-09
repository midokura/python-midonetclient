import httplib2
import json
import openstackx.api.exceptions as api_exceptions


class MidonetClient:
    def __init__(self, request):
        self.h = httplib2.Http()
        self.token = request.user.token

    def _do_request(self, url, method, body='{}'):
        response, content = self.h.request(url, method, body, headers={
                                            "Content-Type": "application/json",
                                            "HTTP_X_AUTH_TOKEN": self.token} 
                                          )
        
        if int(response['status']) > 300:
            raise api_exceptions.ApiException(content)
        
        try:
            body = json.loads(content) if content else None
            return response, body
        except ValueError:
            return response, content
    
    def get(self, url):
        return self._do_request(url, 'GET')
    
    def put(self, url, body):
        return self._do_request(url, 'PUT', json.dumps(body))
    
    def post(self, url, body):
        return self._do_request(url, 'POST', json.dumps(body))
    
    def delete(self, url):
        return self._do_request(url, 'DELETE')
