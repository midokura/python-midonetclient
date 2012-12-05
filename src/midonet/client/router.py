# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
from router_port import RouterPort
from bridge_port import BridgePort
from route import Route
import vendor_media_type
import port_type


class Router(ResourceBase):

    media_type = vendor_media_type.APPLICATION_ROUTER_JSON

    def __init__(self, web, uri, dto):
        super(Router, self).__init__(web, uri, dto)

    def get_name(self):
        return self.dto['name']

    def get_id(self):
        return self.dto['id']

    def get_tenant_id(self):
        return self.dto['tenantId']

    def get_inbound_filter_id(self):
        return self.dto['inboundFilterId']

    def get_outbound_filter_id(self):
        return self.dto['outboundFilterId']

    def name(self, name):
        self.dto['name'] = name
        return self

    def tenant_id(self, tenant_id):
        self.dto['tenantId'] = tenant_id
        return self

    def inbound_filter_id(self, id_) :
        self.dto['inboundFilterId'] = id_
        return self

    def outbound_filter_id(self, id_) :
        self.dto['outboundFilterId'] = id_
        return self

    def get_ports(self, query={}):
        headers = {'Content-Type':
                   vendor_media_type.APPLICATION_PORT_COLLECTION_JSON}

        return self.get_children(self.dto['ports'], query, headers, RouterPort)

    def get_routes(self, query={}):
        headers = {'Content-Type':
                       vendor_media_type.APPLICATION_ROUTE_JSON}
        return self.get_children(self.dto['routes'], query, headers, Route)


    def get_peer_ports(self, query={}):
        headers ={'Content-Type':
                      vendor_media_type.APPLICATION_PORT_COLLECTION_JSON}
        res, peer_ports =  self.web_resource.get(self.dto['peerPorts'], headers,
                                                 query)

        res = []
        for pp in peer_ports:
            if pp['type'] == port_type.LOGICAL_ROUTER:
                res.append(RouterPort(self.web_resource, self.dto['ports'], pp))
            elif pp['type'] == port_type.LOGICAL_BRIDGE:
                res.append(BridgePort(self.web_resource, self.dto['ports'], pp))
        return res

    def add_logical_port(self):
        return RouterPort(self.web_resource, self.dto['ports'],
                          {'type': port_type.LOGICAL_ROUTER})

    def add_materialized_port(self):
        return RouterPort(self.web_resource, self.dto['ports'],
                          {'type': port_type.MATERIALIZED_ROUTER})

    def add_route(self):
        return Route(self.web_resource, self.dto['routes'], {})
