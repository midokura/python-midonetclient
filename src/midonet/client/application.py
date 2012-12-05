# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
from router import Router
from bridge import Bridge
from port_group import PortGroup
from chain import Chain
from tunnel_zone import TunnelZone
from host import Host


class Application(ResourceBase):

    media_type = 'application/vnd.com.midokura.midolman.mgmt.Application+json'

    def __init__(self, web, uri, dto):
        super(Application, self).__init__(web, uri, dto)

    def get_routers(self, query):
        headers = {'Content-Type': 'application/vnd.com.midokura.midolman.mgmt.collection.Router+json'}
        return self.get_children(self.dto['routers'], query, headers, Router)

    def get_router(self, tenant_id, id_):
        return self._get_resource(Router, id_, self.dto['routers'],
                           {'tenant_id':tenant_id}, self.get_routers)

    def get_bridges(self, query):
        headers = {'Content-Type': 'application/vnd.com.midokura.midolman.mgmt.collection.Bridge+json'}
        return self.get_children(self.dto['bridges'], query, headers, Bridge)

    def get_bridge(self, tenant_id, id_):
        return self._get_resource(Bridge, id_, self.dto['bridges'],
                           {'tenant_id':tenant_id}, self.get_bridges)

    def get_port_groups(self, query):
        headers = {'Content-Type': 'application/vnd.com.midokura.midolman.mgmt.collection.PortGroup+json'}
        return self.get_children(self.dto['portGroups'], query, headers, PortGroup)

    def get_chains(self, query):
        headers = {'Content-Type': 'application/vnd.com.midokura.midolman.mgmt.collection.Chain+json'}
        return self.get_children(self.dto['chains'], query, headers, Chain)

    def get_chain(self, tenant_id, id_):
        return self._get_resource(Chain, id_, self.dto['chains'],
                           {'tenant_id': tenant_id}, self.get_chains)

    def get_tunnel_zones(self, query):
        headers = {'Content-Type': 'application/vnd.com.midokura.midolman.mgmt.collection.TunnelZone+json'}
        return self.get_children(self.dto['tunnelZones'], query, headers, TunnelZone)

    def get_hosts(self, query):
        headers = {'Content-Type': 'application/vnd.com.midokura.midolman.mgmt.collection.Host+json',
                   'Accept': 'application/vnd.com.midokura.midolman.mgmt.collection.Host+json'}
        return self.get_children(self.dto['hosts'], query, headers, Host)

    def get_host(self, id_):
        return self._get_resource(Host, id_, self.dto['hosts'], {},
                                  self.get_hosts)

    def add_router(self):
        return Router(self.web_resource, self.dto['routers'], {})

    def add_bridge(self):
        return Bridge(self.web_resource, self.dto['bridges'], {})

    def add_port_group(self):
        return PortGroup(self.web_resource, self.dto['portGroups'], {})

    def add_chain(self):
        return Chain(self.web_resource, self.dto['chains'], {})

    def add_gre_tunnel_zone(self):
        return TunnelZone(self.web_resource, self.dto['tunnelZones'], {'type':'gre'},
                          'application/vnd.com.midokura.midolman.mgmt.GreTunnelZoneHost+json',
                          'application/vnd.com.midokura.midolman.mgmt.collection.GreTunnelZoneHost+json')

    def add_capwap_tunnel_zone(self):
        return TunnelZone(self.web_resource, self.dto['tunnelZones'], {'type':'capwap'},
                          'application/vnd.com.midokura.midolman.mgmt.CapwapTunnelZoneHost+json',
                          'application/vnd.com.midokura.midolman.mgmt.collection.CapwapTunnelZoneHost+json')