# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Midokura PTE LTD.
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# @author: Tomoe Sugihara <tomoe@midokura.com>, Midokura
# @author: Ryu Ishimoto <ryu@midokura.com>, Midokura
# @author: Artem Dmytrenko <art@midokura.com>, Midokura

from midonetclient import vendor_media_type
from midonetclient.ad_route import AdRoute
from midonetclient.bgp import Bgp
from midonetclient.bridge import Bridge
from midonetclient.bridge_port import BridgePort
from midonetclient.chain import Chain
from midonetclient.host import Host
from midonetclient.port_group import PortGroup
from midonetclient.resource_base import ResourceBase
from midonetclient.route import Route
from midonetclient.router import Router
from midonetclient.router_port import RouterPort
from midonetclient.rule import Rule
from midonetclient.tenant import Tenant
from midonetclient.tunnel_zone import TunnelZone
from midonetclient.trace_condition import TraceCondition
from midonetclient.trace import Trace
from midonetclient.write_version import WriteVersion
from midonetclient.system_state import SystemState


class Application(ResourceBase):

    media_type = vendor_media_type.APPLICATION_JSON
    ID_TOKEN = '{id}'

    def __init__(self, uri, dto, auth):
        super(Application, self).__init__(uri, dto, auth)

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

    def get_tenant_template(self):
        return self.dto['tenantTemplate']

    def get_tunnel_zone_template(self):
        return self.dto['tunnelZoneTemplate']

    def get_trace_condition_template(self):
        return self.dto['traceConditionTemplate']

    def get_write_version_uri(self):
        return self.dto['writeVersion']

    def get_system_state_uri(self ):
        return self.dto['systemState']

    def get_tenants(self, query):
        headers = {'Accept':
                   vendor_media_type.APPLICATION_TENANT_COLLECTION_JSON}
        return self.get_children(self.dto['tenants'], query, headers, Tenant)

    def get_trace_template(self):
        return self.dto['traceTemplate']

    def get_routers(self, query):
        headers = {'Accept':
                   vendor_media_type.APPLICATION_ROUTER_COLLECTION_JSON}
        return self.get_children(self.dto['routers'], query, headers, Router)

    def get_bridges(self, query):
        headers = {'Accept':
                   vendor_media_type.APPLICATION_BRIDGE_COLLECTION_JSON}
        return self.get_children(self.dto['bridges'], query, headers, Bridge)

    def get_port_groups(self, query):
        headers = {'Accept':
                   vendor_media_type.APPLICATION_PORTGROUP_COLLECTION_JSON}

        return self.get_children(self.dto['portGroups'], query, headers,
                                 PortGroup)

    def get_chains(self, query):
        headers = {'Accept':
                   vendor_media_type.APPLICATION_CHAIN_COLLECTION_JSON}
        return self.get_children(self.dto['chains'], query, headers, Chain)

    def get_tunnel_zones(self, query):
        headers = {'Accept':
                   vendor_media_type.APPLICATION_TUNNEL_ZONE_COLLECTION_JSON}
        return self.get_children(self.dto['tunnelZones'], query, headers,
                                 TunnelZone)

    def get_tunnel_zone(self, id_):
        return self._get_resource_by_id(TunnelZone, self.dto['tunnelZones'],
                                        self.get_tunnel_zone_template(), id_)

    def get_hosts(self, query):
        headers = {'Accept':
                   vendor_media_type.APPLICATION_HOST_COLLECTION_JSON}
        return self.get_children(self.dto['hosts'], query, headers, Host)

    def delete_ad_route(self, id_):
        return self._delete_resource_by_id(self.get_ad_route_template(), id_)

    def get_ad_route(self, id_):
        return self._get_resource_by_id(AdRoute, self.dto['adRoutes'],
                                        self.get_ad_route_template(), id_)

    def delete_bgp(self, id_):
        return self._delete_resource_by_id(self.get_bgp_template(), id_)

    def get_bgp(self, id_):
        return self._get_resource_by_id(Bgp, None, self.get_bgp_template(),
                                        id_)

    def delete_bridge(self, id_):
        return self._delete_resource_by_id(self.get_bridge_template(), id_)

    def get_bridge(self, id_):
        return self._get_resource_by_id(Bridge, self.dto['bridges'],
                                        self.get_bridge_template(), id_)

    def delete_chain(self, id_):
        return self._delete_resource_by_id(self.get_chain_template(), id_)

    def get_chain(self, id_):
        return self._get_resource_by_id(Chain, self.dto['chains'],
                                        self.get_chain_template(), id_)

    def get_host(self, id_):
        return self._get_resource_by_id(Host, self.dto['hosts'],
                                        self.get_host_template(), id_)

    def delete_port_group(self, id_):
        return self._delete_resource_by_id(self.get_port_group_template(), id_)

    def get_port_group(self, id_):
        return self._get_resource_by_id(PortGroup, self.dto['portGroups'],
                                        self.get_port_group_template(), id_)

    def delete_port(self, id_):
        return self._delete_resource_by_id(self.get_port_template(), id_)

    def get_port(self, id_):
        return self._get_port_resource_by_id(None, self.get_port_template(),
                                             id_)

    def delete_route(self, id_):
        return self._delete_resource_by_id(self.get_route_template(), id_)

    def get_route(self, id_):
        return self._get_resource_by_id(Route, None, self.get_route_template(),
                                        id_)

    def delete_router(self, id_):
        return self._delete_resource_by_id(self.get_router_template(), id_)

    def get_router(self, id_):
        return self._get_resource_by_id(Router, self.dto['routers'],
                                        self.get_router_template(), id_)

    def delete_rule(self, id_):
        return self._delete_resource_by_id(self.get_rule_template(), id_)

    def get_rule(self, id_):
        return self._get_resource_by_id(Rule, None, self.get_rule_template(),
                                        id_)

    def get_tenant(self, id_):
        return self._get_resource_by_id(Tenant, self.dto['tenants'],
                                        self.get_tenant_template(), id_)

    def add_router(self):
        return Router(self.dto['routers'], {}, self.auth)

    def add_bridge(self):
        return Bridge(self.dto['bridges'], {}, self.auth)

    def add_port_group(self):
        return PortGroup(self.dto['portGroups'], {}, self.auth)

    def add_chain(self):
        return Chain(self.dto['chains'], {}, self.auth)

    def add_tunnel_zone(self):
        return TunnelZone(self.dto['tunnelZones'], {}, self.auth)

    def add_gre_tunnel_zone(self):
        return TunnelZone(
            self.dto['tunnelZones'], {'type': 'gre'}, self.auth,
            vendor_media_type.APPLICATION_GRE_TUNNEL_ZONE_HOST_JSON,
            vendor_media_type.APPLICATION_GRE_TUNNEL_ZONE_HOST_COLLECTION_JSON)

    def add_capwap_tunnel_zone(self):
        return TunnelZone(
            self.dto['tunnelZones'], {'type': 'capwap'}, self.auth,
            vendor_media_type.APPLICATION_CAPWAP_TUNNEL_ZONE_HOST_JSON,
            vendor_media_type.
            APPLICATION_CAPWAP_TUNNEL_ZONE_HOST_COLLECTION_JSON)

    # Trace condition operations
    def add_trace_condition(self):
        return TraceCondition(self.dto['traceConditions'], {}, self.auth)

    def get_trace_conditions(self, query):
        headers = {'Accept':
                   vendor_media_type.APPLICATION_CONDITION_COLLECTION_JSON}
        return self.get_children(self.dto['traceConditions'], query, headers,
                                 TraceCondition)

    def get_trace_condition(self, id_):
        return self._get_resource_by_id(TraceCondition,
                                        self.dto['traceConditions'],
                                        self.get_trace_condition_template(),
                                        id_)

    def delete_trace_condition(self, id_):
        return self._delete_resource_by_id(self.get_trace_condition_template(),
                                           id_)

    def get_trace_ids(self, query):
        headers = {'Accept':
                    vendor_media_type.APPLICATION_TRACE_COLLECTION_JSON}
        return self.get_children(self.dto['traces'], query, headers, Trace)

    def get_trace_messages(self, id_):
        return self._get_resource_by_id(Trace, None,
                                    self.get_trace_template(), id_)

    def delete_trace_messages(self, id_):
        return self._delete_resource_by_id(self.get_trace_template(), id_)

    def get_write_version(self):
        return self._get_resource(WriteVersion, None,
                                    self.get_write_version_uri())

    def get_system_state(self):
        return self._get_resource(SystemState, None,
                                    self.get_system_state_uri())

    def _create_uri_from_template(self, template, token, value):
        return template.replace(token, value)

    def _get_port_resource_by_id(self, create_uri, template, id_):
        uri = self._create_uri_from_template(template,
                                             self.ID_TOKEN,
                                             id_)
        res, dto = self.auth.do_request(
            uri, 'GET',
            headers={'Accept': vendor_media_type.APPLICATION_PORT_JSON})

        if dto['type'].endswith('Router'):
            return RouterPort(None, dto, self.auth)
        elif dto['type'].endswith('Bridge'):
            return BridgePort(None, dto, self.auth)

    def _get_resource(self, clazz, create_uri, uri):
        return clazz(create_uri, {'uri': uri}, self.auth).get(
            headers={'Content-Type': clazz.media_type,
                     'Accept': clazz.media_type})

    def _get_resource_by_id(self, clazz, create_uri,
                            template, id_):
        uri = self._create_uri_from_template(template,
                                             self.ID_TOKEN,
                                             id_)
        return self._get_resource(clazz, create_uri, uri)

    def _delete_resource_by_id(self, template, id_):
        uri = self._create_uri_from_template(template,
                                             self.ID_TOKEN,
                                             id_)
        self.auth.do_request(uri, 'DELETE')
