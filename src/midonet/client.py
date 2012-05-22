from utils import debug_print

import exc
import httplib2
import inspect
import json
import logging
import os.path
import sys
from datetime import datetime
from datetime import timedelta

import chains
import ports
import routes
import bridges
import routers
import tenants
import vifs
import rules
import dhcps
import dhcp_hosts

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
    dhcp = dhcps.Dhcp()
    dhcp_host = dhcp_hosts.DhcpHost()


    def __init__(self, midonet_uri='http://localhost:8080/midolmanj-mgmt',
                 token=None, ks_uri='http://localhost:5000/v2.0',
                 username=None, password=None, tenant_id=None, no_ks=False):
        self.h = httplib2.Http()
        self.token = token
        self.midonet_uri = midonet_uri
        self.username = username
        self.password = password
        self.tenant_id = tenant_id
        self.ks_uri = ks_uri
        self.no_ks = no_ks
        self.token_expires = None
        if token:
            self.token = token
        if not no_ks:
            # Generate a scoped token from keystone
            self.token, self.token_expires = self._gen_ks_token(
                self.username, self.password, self.tenant_id)

        # Get resource URIs
        response, content = self.get(self.midonet_uri)
        self.version = content['version']
        self.vifs_uri = content['vifs']
        self.tenant_uri = content['tenant']

    def _gen_ks_token(self, username, password, tenant_id):
        from keystoneclient.v2_0 import client as keystone_client
        ks_conn = keystone_client.Client(endpoint=self.ks_uri)
        token = ks_conn.tokens.authenticate(
            username=username, password=password, tenant_id=tenant_id)
        return token.id, datetime.strptime(token.expires, '%Y-%m-%dT%H:%M:%SZ')

    def tenants(self):
        return self.tenant.accept(self, self.tenant_uri)

    def routers(self):
        return self.router.accept(self)

    def bridges(self):
        return self.bridge.accept(self)

    def router_ports(self):
        return self.rp.accept(self)

    def bridge_ports(self):
        return self.bp.accept(self)

    def routes(self):
        return self.route.accept(self)

    def vifs(self):
        return self.vif.accept(self, self.vifs_uri)

    def chains(self):
        return self.chain.accept(self)

    def rules(self):
        return self.rule.accept(self)

    def dhcps(self):
        return self.dhcp.accept(self)

    def dhcp_hosts(self):
        return self.dhcp_host.accept(self)

    def _do_request(self, uri, method, body='{}'):
        headers = {}
        headers["Content-Type"] = "application/json"
        if self.token:
            # Renew token one hour before the expiration
            if (not self.no_ks) and \
                    self.token_expires - datetime.now() < \
                    timedelta(seconds=60*60):
                self.token, self.token_expires = self._gen_ks_token(
                    self.username, self.password, self.tenant_id)

            headers["X-Auth-Token"] = self.token
        response, content = self.h.request(uri, method, body, headers=headers)

#            frame =  inspect.stack()[2][0]
#            fi = inspect.getframeinfo(frame)
#            msg = "Call: " + os.path.basename(fi.filename)[:-2] + fi.function
        req = "Req: (%s on %s) " % (method, uri)
        debug_print(req, body, response, content)

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
