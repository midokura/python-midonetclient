from utils import debug_print

import httplib2
import inspect
import json
import logging
import os.path
import settings
import sys

import exceptions
import tenants
import routers
import ports

class MidonetClient(object):

    t = tenants.Tenant()
    r = routers.Router()
    p = ports.Port()
    rp = ports.Port.RouterPort()
    bp = ports.Port.BridgePort()

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

    def tenants(self):
        self.t.accept(self, 'tenants')
        return self.t

    def routers(self):
        self.r.accept(self, 'routers')
        return self.r

    def ports(self):
        self.p.accept(self, 'ports')
        return self.p

    def router_ports(self):
        self.rp.accept(self, 'ports')
        return self.rp

    def bridge_ports(self):
        self.bp.accept(self, 'ports')
        return self.bp

    def _do_request(self, path, method, body='{}'):
        response, content = self.h.request(
            self.base_url + path, method, body, headers={
                                            "Content-Type": "application/json",
                                            "HTTP_X_AUTH_TOKEN": self.token} 
                                          )
        
#            frame =  inspect.stack()[2][0]
#            fi = inspect.getframeinfo(frame)
#            msg = "Call: " + os.path.basename(fi.filename)[:-2] + fi.function
        req = "Request: (%s on %s) " % (method, path)
        logging.error("Body: %r", body)
        debug_print(req, response, content)
        
        if int(response['status']) > 300:
#            raise exc.HTTPError(content)
            logging.error("%s got an error status %s", req, response['status'])
            e = exceptions.get_exception(response['status'])(content)
            logging.error("Raising an exeption: (%r): %r" %  (e, str(e)))
            raise e
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
