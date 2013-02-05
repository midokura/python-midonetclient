# Copyright 2012 Midokura Japan KK

from ad_route import AdRoute
from bgp import Bgp
from bridge import Bridge
from bridge_port import BridgePort
from chain import Chain
from host import Host
from port_group import PortGroup
from resource_base import ResourceBase
from route import Route
from router import Router
from router_port import RouterPort
from rule import Rule
from tunnel_zone import TunnelZone
import vendor_media_type

class Application(ResourceBase):

    media_type = vendor_media_type.APPLICATION_JSON
    ID_TOKEN = '{id}'

    def __init__(self, web, uri, dto):
        super(Application, self).__init__(web, uri, dto)

    def get_ad_route_template(self):
        return self.dto['adRouteTemplate']

    def get_bgp_template(self):
        return self.dto['bgpTemplate']

    def get_bridge_template(self):
        return self.dto['bridgeTemplate']

    def get_chain_template(self):
        return self.dto['chainTemplate']

    def get_host_template(self):
        return self.dto['hostTemplate']

    def get_port_group_template(self):
        return self.dto['portGroupTemplate']

    def get_port_template(self):
        return self.dto['portTemplate']

    def get_route_template(self):
        return self.dto['routeTemplate']

    def get_router_template(self):
        return self.dto['routerTemplate']

    def get_rule_template(self):
        return self.dto['ruleTemplate']

    def get_routers(self, query):
        headers = {'Content-Type':
                       vendor_media_type.APPLICATION_ROUTER_COLLECTION_JSON}
        return self.get_children(self.dto['routers'], query, headers, Router)

    def get_bridges(self, query):
        headers = {'Content-Type':
                   vendor_media_type.APPLICATION_BRIDGE_COLLECTION_JSON}
        return self.get_children(self.dto['bridges'], query, headers, Bridge)

    def get_port_groups(self, query):
        headers = {'Content-Type':
                       vendor_media_type.APPLICATION_PORTGROUP_COLLECTION_JSON}

        return self.get_children(self.dto['portGroups'], query, headers,
                                 PortGroup)

    def get_chains(self, query):
        headers = {'Content-Type':
                       vendor_media_type.APPLICATION_CHAIN_COLLECTION_JSON}
        return self.get_children(self.dto['chains'], query, headers, Chain)

    def get_tunnel_zones(self, query):
        headers = {
            'Content-Type':
                vendor_media_type.APPLICATION_TUNNEL_ZONE_COLLECTION_JSON}
        return self.get_children(self.dto['tunnelZones'], query, headers,
                                 TunnelZone)

    def get_hosts(self, query):
        headers = {'Content-Type':
                       vendor_media_type.APPLICATION_HOST_COLLECTION_JSON,
                   'Accept':
                       vendor_media_type.APPLICATION_HOST_COLLECTION_JSON}
        return self.get_children(self.dto['hosts'], query, headers, Host)

    def get_ad_route(self, id_):
        return self._get_resource_by_id(AdRoute, self.dto['adRoutes'],
                                        self.get_ad_route_template(), id_)

    def get_bgp(self, id_):
        return self._get_resource_by_id(Bgp, self.dto['bgps'],
                                        self.get_bgp_template(), id_)

    def get_bridge(self, id_):
        return self._get_resource_by_id(Bridge, self.dto['bridges'],
                                        self.get_bridge_template(), id_)

    def get_chain(self, id_):
        return self._get_resource_by_id(Chain, self.dto['chains'],
                                        self.get_chain_template(), id_)

    def get_host(self, id_):
        return self._get_resource_by_id(Host, self.dto['hosts'],
                                        self.get_host_template(), id_)

    def get_port_group(self, id_):
        return self._get_resource_by_id(PortGroup, self.dto['portGroups'],
                                        self.get_port_group_template(), id_)

    def get_port(self, id_):
        return self._get_resource_by_id('Port', None,
                                        self.get_port_template(), id_)

    def get_route(self, id_):
        return self._get_resource_by_id(Route, None, self.get_route_template(),
                                        id_)

    def get_router(self, id_):
        return self._get_resource_by_id(Router, self.dto['routers'],
                                        self.get_router_template(), id_)

    def get_rule(self, id_):
        return self._get_resource_by_id(Rule, None, self.get_rule_template(),
                                        id_)

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

    def _create_uri_from_template(self, template, token, value):
        return template.replace(token, value)

    def _get_resource_by_id(self, clazz, create_uri,
                            template, id_):
        uri = self._create_uri_from_template(template,
                                             self.ID_TOKEN,
                                             id_)
        if clazz == 'Port' : # nasty hack to determine the type of port
            res, dto = self.web_resource.get(uri)
            if dto['type'].endswith('Router'):
                return RouterPort(self.web_resource, None, dto)
            elif dto['type'].endswith('Bridge'):
                return BridgePort(self.web_resource, None, dto)
        else:
            return clazz(self.web_resource, create_uri, {'uri': uri}).get(
                {'Content-Type': clazz.media_type, 'Accept': clazz.media_type})
