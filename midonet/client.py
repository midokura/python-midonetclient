from utils import debug_print

import exceptions
import httplib2
import inspect
import json
import logging
import os.path
import settings
import sys

import ports
import routes
import routers
import tenants
import vifs

class MidonetClient(object):

    t = tenants.Tenant()
    l3sw = routers.Router()
    p = ports.Port()
    rp = ports.Port.RouterPort()
    bp = ports.Port.BridgePort()
    r = routes.Route()
    v = vifs.Vif()

    def __init__(self, base_url=None, token=None):
        self.h = httplib2.Http()
        if not base_url:
            self.base_url = settings.MIDONET_URL
        if not token:
            self.token = settings.AUTH_TOKEN

    def tenants(self):
        return self.t.accept(self)

    def routers(self):
        return self.l3sw.accept(self)

    def ports(self):
        return self.p.accept(self)

    def router_ports(self):
        return self.rp.accept(self)

    def bridge_ports(self):
        return self.bp.accept(self)

    def routes(self):
        return self.r.accept(self)

    def vifs(self):
        return self.v.accept(self)

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
