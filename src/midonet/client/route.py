# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase

class Route(ResourceBase):

    media_type = 'application/vnd.com.midokura.midolman.mgmt.Route+json'

    def __init__(self, web, uri, dto):
        super(Route, self).__init__(web, uri, dto)

    def get_attributes(self):
        return self.dto['attributes']

    def get_dst_network_addr(self):
        return self.dto['dstNetworkAddr']

    def get_dst_network_length(self):
        return self.dto['dstNetworkLength']

    def get_src_network_addr(self):
        return self.dto['srcNetworkAddr']

    def get_src_network_length(self):
        return self.dto['srcNetworkLength']

    def get_id(self):
        return self.dto['id']

    def get_next_hop_gateway(self):
        return self.dto['nextHopGateway']

    def get_next_hop_port(self):
        return self.dto['nextHopPort']

    def get_router_id(self):
        return self.dto['routerId']

    def get_type(self):
        return self.dto['type']

    def get_weight(self):
        return self.dto['weight']

    def attributes(self, attributes):
        self.dto['attributes'] = attributes
        return self

    def dst_network_addr(self, addr):
        self.dto['dstNetworkAddr'] = addr
        return self

    def dst_network_length(self, len_):
        self.dto['dstNetworkLength'] = len_
        return self

    def src_network_addr(self, addr):
        self.dto['srcNetworkAddr'] = addr
        return self

    def src_network_length(self, len_):
        self.dto['srcNetworkLength'] = len_
        return self

    def next_hop_gateway(self, gateway):
        self.dto['nextHopGateway'] = gateway
        return self

    def next_hop_port(self, id_):
        self.dto['nextHopPort'] = id_
        return self

    def type(self, type_):
        self.dto['type'] = type_
        return self

    def weight(self, weight):
        self.dto['weight'] = weight
        return self

