from utils import debug_print

import exceptions
import httplib2
import inspect
import json
import logging
import os.path
import settings
import sys

import chains
import ports
import routes
import bridges
import routers
import tenants
import vifs
import rules

class MidonetClient(object):

    tenant = tenants.Tenant()
    router = routers.Router()
    bridge = bridges.Bridge()
    port = ports.Port()
    rp = ports.Port.RouterPort()
    bp = ports.Port.BridgePort()
    route = routes.Route()
    vif = vifs.Vif()
    chain = chains.Chain()
    rule = rules.Rule()

    def __init__(self, base_uri=None, token=None):
        self.h = httplib2.Http()
        if not base_uri:
            self.base_uri = settings.MIDONET_URI
        if not token:
            self.token = settings.AUTH_TOKEN

        response, content = self.get(self.base_uri)

        self.version = content['version']
        self.vifs_uri = content['vifs']
        self.tenant_uri = content['tenant']
   

    def tenants(self):
        return self.tenant.accept(self, self.tenant_uri)

    def routers(self):
        return self.router.accept(self, self.base_uri + 'routers')

    def bridges(self):
        return self.bridge.accept(self, self.base_uri + 'bridges')

    def ports(self):
        return self.port.accept(self, self.base_uri + 'ports')

    def router_ports(self):
        return self.rp.accept(self, self.base_uri + 'ports')

    def bridge_ports(self):
        return self.bp.accept(self, self.base_uri + 'ports')

    def routes(self):
        return self.route.accept(self, self.base_uri + 'routes')

    def vifs(self):
        return self.vif.accept(self, self.vifs_uri)

    def chains(self):
        return self.chain.accept(self, self.base_uri + 'chains')

    def rules(self):
        return self.rule.accept(self, self.base_uri + 'rules')

    def _do_request(self, uri, method, body='{}'):
        response, content = self.h.request(
            uri, method, body, headers={
                                            "Content-Type": "application/json",
                                            "HTTP_X_AUTH_TOKEN": self.token} 
                                          )
        
#            frame =  inspect.stack()[2][0]
#            fi = inspect.getframeinfo(frame)
#            msg = "Call: " + os.path.basename(fi.filename)[:-2] + fi.function
        req = "Request: (%s on %s) " % (method, uri)
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
    
    def get(self, uri):
        return self._do_request(uri, 'GET')
    
    def put(self, uri, body):
        return self._do_request(uri, 'PUT', json.dumps(body))
    
    def post(self, uri, body):
        return self._do_request(uri, 'POST', json.dumps(body))
    
    def delete(self, uri):
        return self._do_request(uri, 'DELETE')
