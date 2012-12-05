# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
from router import Router
from bridge import Bridge
from port_group import PortGroup
from chain import Chain
from tunnel_zone import TunnelZone
from host import Host
import vendor_media_type

class Application(ResourceBase):

    media_type = vendor_media_type.APPLICATION_JSON

    def __init__(self, web, uri, dto):
        super(Application, self).__init__(web, uri, dto)

    def get_routers(self, query):
        headers = {'Content-Type':
                       vendor_media_type.APPLICATION_ROUTER_COLLECTION_JSON}
        return self.get_children(self.dto['routers'], query, headers, Router)

    def get_router(self, tenant_id, id_):
        return self._get_resource(Router, id_, self.dto['routers'],
                           {'tenant_id':tenant_id}, self.get_routers)

    def get_bridges(self, query):
        headers = {'Content-Type':
                   vendor_media_type.APPLICATION_BRIDGE_COLLECTION_JSON}
        return self.get_children(self.dto['bridges'], query, headers, Bridge)

    def get_bridge(self, tenant_id, id_):
        return self._get_resource(Bridge, id_, self.dto['bridges'],
                           {'tenant_id':tenant_id}, self.get_bridges)

    def get_port_groups(self, query):
        headers = {'Content-Type':
                       vendor_media_type.APPLICATION_PORTGROUP_COLLECTION_JSON}

        return self.get_children(self.dto['portGroups'], query, headers, PortGroup)

    def get_chains(self, query):
        headers = {'Content-Type':
                       vendor_media_type.APPLICATION_CHAIN_COLLECTION_JSON}
        return self.get_children(self.dto['chains'], query, headers, Chain)

    def get_chain(self, tenant_id, id_):
        return self._get_resource(Chain, id_, self.dto['chains'],
                           {'tenant_id': tenant_id}, self.get_chains)

    def get_tunnel_zones(self, query):
        headers = {
            'Content-Type':
                vendor_media_type.py.APPLICATION_TUNNEL_ZONE_COLLECTION_JSON}
        return self.get_children(self.dto['tunnelZones'], query, headers,
                                 TunnelZone)

    def get_hosts(self, query):
        headers = {'Content-Type':
                       vendor_media_type.APPLICATION_HOST_COLLECTION_JSON,
                   'Accept':
                       vendor_media_type.APPLICATION_HOST_COLLECTION_JSON}
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
        return TunnelZone(
            self.web_resource, self.dto['tunnelZones'], {'type':'gre'},
            vendor_media_type.APPLICATION_GRE_TUNNEL_ZONE_HOST_JSON,
            vendor_media_type.APPLICATION_GRE_TUNNEL_ZONE_HOST_COLLECTION_JSON)

    def add_capwap_tunnel_zone(self):
        return TunnelZone(
            self.web_resource, self.dto['tunnelZones'], {'type':'capwap'},
            vendor_media_type.APPLICATION_CAPWAP_TUNNEL_ZONE_HOST_JSON,
            vendor_media_type.\
                APPLICATION_CAPWAP_TUNNEL_ZONE_HOST_COLLECTION_JSON)

