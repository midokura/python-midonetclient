# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
from bgp import Bgp
import port_type
import vendor_media_type


class RouterPort(ResourceBase):

    media_type = vendor_media_type.APPLICATION_PORT_JSON

    def __init__(self, web, uri, dto):
        super(RouterPort, self).__init__(web, uri, dto)

    def get_id(self):
        return self.dto['id']

    def get_type(self):
        return self.dto['type']

    def get_device_id(self):
        return self.dto['deviceId']

    def get_inbound_filter_id(self):
        return self.dto['inboundFilterId']

    def get_outbound_filter_id(self):
        return self.dto['outboundFilterId']

    def get_network_address(self):
        return self.dto['networkAddress']

    def get_network_length(self):
        return self.dto['networkLength']

    def get_port_address(self):
        return self.dto['portAddress']

    def get_port_mac(self):
        return self.dto['portMac']

    def get_peer_id(self):
        return self.dto['peerId']

    def port_address(self, port_address):
        self.dto['portAddress'] = port_address
        return self

    def network_address(self, network_address):
        self.dto['networkAddress'] = network_address
        return self

    def network_length(self, network_length):
        self.dto['networkLength'] = network_length
        return self

    def local_network_address(self, local_network_address):
        assert self.get_type() == port_type.MATERIALIZED_ROUTER
        self.dto['localNetworkAddress'] = local_network_address
        return self

    def local_network_length(self, local_network_length):
        assert self.get_type() == port_type.MATERIALIZED_ROUTER
        self.dto['localNetworkLength'] = local_network_length
        return self

    def inbound_filter_id(self, id_) :
        self.dto['inboundFilterId'] = id_
        return self

    def outbound_filter_id(self, id_) :
        self.dto['outboundFilterId'] = id_
        return self

    def get_bgps(self):
        query = {}
        headers = {'Content-Type':
                       vendor_media_type.APPLICATION_BGP_COLLECTION_JSON}
        return self.get_children(self.dto['bgps'], query, headers, Bgp)

    #TODO
    def get_vpns(self):
        pass

    def add_bgp(self):
        return Bgp(self.web_resource, self.dto['bgps'], {})

    #TODO
    def add_vpn(self):
        pass

    def link(self, peer_uuid):
        self.dto['peerId'] = peer_uuid
        headers = {'Content-Type': self.media_type}
        self.web_resource.post(self.dto['link'], self.dto, headers=headers)
        return self.web_resource.get(self.dto['uri'], headers=headers)

    def unlink(self):
        self.dto['peerId'] = None
        headers = {'Content-Type': self.media_type}
        self.web_resource.post(self.dto['link'], self.dto, headers=headers)
        return self.web_resource.get(self.dto['uri'], headers=headers)
