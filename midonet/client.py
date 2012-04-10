from utils import debug_print

import exc
import httplib2
import inspect
import json
import logging
import os.path
import sys

import chains
import ports
import routes
import bridges
import routers
import tenants
import vifs
import rules

LOG = logging.getLogger('midonet.client')

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

    def __init__(self, midonet_uri='http://localhost:8080/midolmanj-mgmt', 
                 keystone_tokens_endpoint=None, token=None, username=None, 
                 password=None, tenant_name=None, no_ks=False):
        self.h = httplib2.Http()
        self.token = None
        self.midonet_uri = midonet_uri
        if (not no_ks) and (not token) and keystone_tokens_endpoint:
            # Generate token from keystone
            body = {"auth": {"tenantName": tenant_name, 
                    "passwordCredentials":{"username": username, "password": password}}}
            response, content = self.post(keystone_tokens_endpoint, body)
            self.token = content['access']['token']['id']

        # Get resource URIs
        response, content = self.get(self.midonet_uri)
        self.version = content['version']
        self.vifs_uri = content['vifs']
        self.tenant_uri = content['tenant']
   

    def tenants(self):
        return self.tenant.accept(self, self.tenant_uri)

    def routers(self):
        return self.router.accept(self)

    def bridges(self):
        return self.bridge.accept(self)

    def router_ports(self):
        return self.rp.accept(self)

    def bridge_ports(self):
        return self.bp.accept(self, self.midonet_uri + 'ports')

    def routes(self):
        return self.route.accept(self)

    def vifs(self):
        return self.vif.accept(self, self.vifs_uri)

    def chains(self):
        return self.chain.accept(self, self.midonet_uri + 'chains')

    def rules(self):
        return self.rule.accept(self, self.midonet_uri + 'rules')

    def _do_request(self, uri, method, body='{}'):
        headers = {}
        headers["Content-Type"] = "application/json"
        if self.token:
            headers["X-Auth-Token"] = self.token
        response, content = self.h.request(uri, method, body, headers=headers)
        
#            frame =  inspect.stack()[2][0]
#            fi = inspect.getframeinfo(frame)
#            msg = "Call: " + os.path.basename(fi.filename)[:-2] + fi.function
        req = "Request: (%s on %s) " % (method, uri)
        LOG.error("Body: %r", body)
        debug_print(req, response, content)
        
        if int(response['status']) > 300:
#            raise exc.HTTPError(content)
            LOG.error("%s got an error status %s", req, response['status'])
            e = exc.get_exception(response['status'])(content)
            LOG.error("Raising an exeption: (%r): %r" %  (e, str(e)))
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
